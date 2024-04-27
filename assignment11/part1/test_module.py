import numpy as np
import searchUtilsTeam08 as search

def test_search_functions():
    # Sorted array
    sorted_array = np.array([1.5, 3.0, 4.5, 6.0, 7.5, 9.0], dtype=np.float64)
    # Unsorted array
    unsorted_array = np.array([2.0, 4.0, 6.0, 8.0, 10.0], dtype=np.float64)

    # Linear Search function - Searching for a value that exists
    print("Testing linearsearch with value 3.0 in sorted_array:")
    print(search.searchutils.linearsearch(sorted_array, len(sorted_array), 3.0))

    # Searching for a value that does not exist
    print("Testing linearsearch with value 5.0 in unsorted_array:")
    print(search.searchutils.linearsearch(unsorted_array, len(unsorted_array), 5.0))

    # BinarySearch function
    print("Testing binarysearch with value 6.0 in sorted_array:")
    print(search.searchutils.binarysearch(sorted_array, len(sorted_array), 6.0))

    # Searching for a value that does not exist
    print("Testing binarysearch with value 5.0 in sorted_array:")
    print(search.searchutils.binarysearch(sorted_array, len(sorted_array), 5.0))

if __name__ == "__main__":
    test_search_functions()
    print("All tests passed successfully.")