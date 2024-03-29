from mpi4py import MPI
import time
import gauleg as gauss
import numpy as np

# Start timer
start = time.perf_counter()

# Start the MPI process
comm = MPI.COMM_WORLD

# Determine total number of tasks
size = comm.Get_size()

# Determine id of "this" task
rank = comm.Get_rank()

# --- Master ---
if rank == 0:
    print(f"Total Numer of Workers = {size}")
    print(size)

    integral = []  # running total of the integral
    time_int = []
    err = []

    # Number of integration points
    num_integration_points = 20

    # Initialize counters for tasks sent and completed
    tasks_sent = 0
    tasks_completed = 0

    # Loop over all tasks to send the quadrature
    while tasks_sent < num_integration_points:
        # Receive result from any worker
        status = MPI.Status()
        partial, times = comm.recv(source=MPI.ANY_SOURCE, status=status)
        source = status.Get_source()
        integral.append(partial)
        print(f"Master received value {partial} from process {source}")

        # Compute Error and Time
        err.append(abs((partial - 0.735758882342885) / 0.735758882342885 * 100))
        time_int.append(times)

        # Increment tasks_completed counter
        tasks_completed += 1

        # If there are more tasks to send, send one
        if tasks_sent < num_integration_points:
            x = [0.0] * (tasks_sent + 1)
            w = [0.0] * (tasks_sent + 1)
            x1, x2 = -1.0, 1.0
            gauss.gauleg(x1, x2, x, w, tasks_sent + 1)
            quadrature = np.array([x, w])
            # Send quadrature to the worker
            comm.send(quadrature, dest=source)

            print(f"Master sent quadrature to process {source}")
            
            # Increment tasks_sent counter
            tasks_sent += 1

    # Print results table
    with open('part2.txt', 'w') as f:
        f.write("Quadrature no.\tIntegration Result\tPercent error %\tRun time (s)\n")
        for i in range(num_integration_points):
            f.write(f"{i + 1}\t\t{integral[i]:<15}\t\t{err[i]:<15}%\t\t{time_int[i]:<15}\n")

    # Integral complete
    finish = time.perf_counter()
    print(f'Finish in {round(finish - start, 3)} seconds')

# --- Worker ---
else:
    # Print notification including process id
    print(f"Process {rank} starts")
    start_i = time.perf_counter()
    while True:
        quadrature = comm.recv(source=0)
        if quadrature is None:
            break
        x = quadrature[0, :]
        w = quadrature[1, :]
        # Placeholder computation, replace with actual integration code
        sum = 0.0
        for i in range(len(x)):
            sum += w[i] * gauss.f(x[i])
        end_i = time.perf_counter()
        comm.send((sum, end_i - start_i), dest=0)
    # Signal completion to master
    comm.send(None, dest=0)
