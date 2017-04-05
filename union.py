A = [1, 12, 42, 70, 36, -4, 43, 15, 36, -2]
B = [5, 15, 44, 72, 36, 2, 69, 24, 36, -1]
N = 10

# Using the python sorted function which is an implementation of timsort.
# Arguments: 
#     A -> Array of ints which corresponds to lower bounds of an interval
#     B -> Array of ints which corresponds to upper bounds of an interval
#     N -> Number of items in the array that is 0 offset
# Returns:
#     int count -> count of disjointed intervals
def pythonic_solution(A, B, N):
    # We will be keeping track of counts by counting only when we find a new disjointed interval
    count = 0
    i = 0
    # Reference interval, will change everytime we find a new disjointed interval
    # Python tuples are immutable so we can't reassign thats why we keep seperate lower/upper bounds
    ref_lower = None
    ref_upper = None
    
    # Turn A and B arrays into tuple objects for easier sorting without keeping track of indices
    C = list(zip(A,B))
    C = sorted(C, key=lambda x: x[0])

    while i < N:
        # On first item set the lower and upper bounds of our first interval and this is our first disjointed set
        if i == 0:
            ref_lower = C[i][0]
            ref_upper = C[i][1]
            count += 1 
            i += 1
            print("current iteration i -> {} : ({}, {})".format(i, ref_lower, ref_upper))
            continue

        # If this lower bound is less than or equal to the referenced upper bound it is a union interval no count change       
        if C[i][0] <= ref_upper:
            # Check if the upper bound is actually smaller than the reference if it is don't change it
            if ref_upper < C[i][1]:
                ref_upper = C[i][1]
            i += 1
            print("current iteration i -> {} : ({}, {})".format(i, ref_lower, ref_upper))
            continue
        # Otherwise the new interval is a newly disjointed one, increase count and change the references
        else:
            count += 1
            ref_lower = C[i][0]
            ref_upper = C[i][1]
            i += 1
            print("current iteration i -> {} : ({}, {})".format(i, ref_lower, ref_upper))

    # return our disjointed counts
    return count

if __name__ == "__main__":
    print(pythonic_solution(A, B, N))   