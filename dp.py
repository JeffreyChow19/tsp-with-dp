import math
import json
import numpy as np
import time
from itertools import permutations
from math import inf

'''
Calculate the Euclidean Distance between two coordinates
@param coord1 : first coordinate
@param coord2 : second coordinate
'''
def distance(coord1, coord2):
    '''Calculate the Euclidean distance between two coordinates.'''
    x1, y1 = coord1
    x2, y2 = coord2
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

'''
Create a weighted adjacency matrix from list of points
@param points : list of points
'''
def weighted_adjacency_matrix(points):
    n = len(points)
    adj_matrix = np.zeros((n,n))

    for i in range(n):
        for j in range(n):
            if i != j:
                x1,y1 = points[i]
                x2,y2 = points[j]
                dist = ((x1-x2)**2 + (y1-y2)**2)**0.5
                adj_matrix[i,j] = dist

    return adj_matrix

'''
Find optimum solution for Travelling Salesman Problem using Dynamic Programming
@param i : source
@param S : set of destinations 
'''
def tsp_with_dp(i, S):
    ''' Base : if S has only 1 item left, return distance from it to the ending point '''
    if (len(S) == 1):
        j = S.pop()
        return ([i, j, 0],  adj_mtrx[i][j] + adj_mtrx[j][0])
 
    # Set default value for the result
    result = ([], 10**9)

    # Iterate through all item in S
    for j in S:

        ''' Recursion '''
        recursion = tsp_with_dp(j, S-{j})

        # Insert source to the result array
        recursion[0].insert(0,i)

        # Create new tuple for the result and add distance from source(i) to current destination (j)
        recursion_result = (recursion[0], recursion[1] + adj_mtrx[i,j])
    
        # Take result only if minimum, compared by the distance
        result = min(result, recursion_result, key=lambda x: x[1])

    return result

'''
Find optimum solution for Travelling Salesman Problem using Brute Force
@param weighted_adjacency_matrix : weighted adjacency matrix
@param start_index : start and end location index
'''
def tsp_with_bf(weighted_adjacency_matrix, start_index):
    n = len(weighted_adjacency_matrix)
    min_path = inf
    min_perm = None
    vertex = [i for i in range(n) if i != start_index]
    for perm in permutations(vertex):
        current_path = weighted_adjacency_matrix[start_index][perm[0]]
        for i in range(n - 2):
            current_path += weighted_adjacency_matrix[perm[i]][perm[i + 1]]
        current_path += weighted_adjacency_matrix[perm[-1]][start_index]
        if current_path < min_path:
            min_path = current_path
            min_perm = perm
    return ([start_index] + list(min_perm) + [start_index], min_path)

def print_result(tuple_of_solution, execution_time, type):
    print("\n======================================================")
    print(f"Using {type} algorithm")
    print(f"Execution time : {execution_time:.4f} seconds\n")

    print("\nRoute to travel : ")
    for places in tuple_of_solution[0]:
        print(f"{data[places]['code']}{' - ' if places != 0 else ''}{data[places]['name']} in {data[places]['area']}")

    print(f"\nApproximate distance to travel : {tuple_of_solution[1]:.2f} meters")
    print("Assume : 1 pixel in map equals to 1 meter")
    print("======================================================")

# Extract the JSON file
with open("uss.json") as f:
    data = json.load(f)

# Create tuple of coordinates from the JSON data
coords = [tuple(location["coordinate"]) for location in data]

# Create weighted adjacency matrix for each points in data
adj_mtrx = weighted_adjacency_matrix(coords)

# Create set of coordinates index to evaluate
set_of_coordinates = set(range(1, len(coords)))

# Find solution using Dynamic Programming
dp_start = time.time()

tsp_with_dp_result = tsp_with_dp(0,set_of_coordinates)

dp_end = time.time()
dp_execution_time = dp_end - dp_start

# Find solution using Brute Force
bf_start = time.time()

tsp_with_bf_result = tsp_with_bf(adj_mtrx, 0)

bf_end = time.time()
bf_execution_time = bf_end - bf_start

# Print results
print_result(tsp_with_dp_result, dp_execution_time, "Dynamic Programming")
print_result(tsp_with_bf_result, bf_execution_time, "Brute Force")



