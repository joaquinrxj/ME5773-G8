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
    time_int=[]
    err=[]

    # Loop over all tasks to send the quadrature
    available_workers = list(range(1, size))
    num_gauss=20
    for i in range(1,20+1):
        x = [0.0] * i
        w = [0.0] * i
        x1, x2 = -1.0, 1.0
        gauss.gauleg(x1,x2,x,w,i)
        quadrature=np.array([x,w])
        # Dynamically allocate tasks to available workers
        worker_rank = available_workers[(i - 1) % len(available_workers)]
        comm.send(quadrature,dest=worker_rank)

        print(f"Master sent quadrature to process {i}")
        

    while len(integral) < num_gauss:
        status = MPI.Status()
        partial, times = comm.recv(source=MPI.ANY_SOURCE, status=status)
        source = status.Get_source()
        integral.append(partial)
        print(f"Master received value {partial} from process {source}")
        
        # Compute Error and Time
        err.append(abs((partial - 0.735758882342885) / 0.735758882342885 * 100))
        time_int.append(times)

    # Print results table

    with open('part2.txt', 'w') as f:
        f.write("Quadrature no.\tIntegration Result\tPercent error %\tRun time (s)\n")
        for i in range(1,len(integral)):
            f.write(f"{i}\t\t\t\t{integral[i-1]:<15.16}\t\t\t\t{err[i-1]:<15.16}%\t\t\t\t{time_int[i-1]:<15.16}\n")

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
        x=quadrature[0,:]
        w=quadrature[1,:]
        # Placeholder computation, replace with actual integration code
        sum = 0.0
        for i in range(0,len(x)):
            sum = sum + w[i]*gauss.f(x[i])
        end_i = time.perf_counter()
        comm.send((sum,end_i-start_i), dest=0)
    # Signal completion to master
    comm.send(None, dest=0)


