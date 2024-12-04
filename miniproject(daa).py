# Function to check if it is safe to place a component at (row, col) on the grid

def is_safe(board, row, col, N):

    """

    Check if it's safe to place a component at position (row, col).

    Ensures no two components are in the same row, column, or diagonal.

    """

    # Check column conflict

    for i in range(row):

        if board[i] == col or board[i] - i == col - row or board[i] + i == col + row:

            return False

    return True

 

# Backtracking function to solve the circuit placement problem

def place_components_util(board, row, N, solutions):

    """

    Tries to place components one by one on the grid using backtracking.

    """

    # If all components are placed, save the current solution

    if row == N:

        solution = []

        for i in range(N):

            row_result = ['.'] * N

            row_result[board[i]] = 'C'  # 'C' represents a component

            solution.append(' '.join(row_result))

        solutions.append(solution)

        return

   

    # Try placing a component in each column of the current row

    for col in range(N):

        if is_safe(board, row, col, N):

            board[row] = col  # Place component at (row, col)

            place_components_util(board, row + 1, N, solutions)  # Recurse to place next component

            board[row] = -1  # Backtrack: Remove component

 

# Function to solve the circuit placement problem

def circuit_design_verification(N):

    """

    Simulate circuit placement and verify using the N-Queens backtracking approach.

    N represents the number of components to place.

    """

    if N < 1:

        print("Please enter a positive integer for N.")

        return

   

    # Initialize the board (all positions set to -1 indicating no component placed)

    board = [-1] * N

    solutions = []

   

    place_components_util(board, 0, N, solutions)

   

    # Print all the valid solutions

    if solutions:

        print(f"Valid Circuit Placements for N = {N}:")

        print_solutions(solutions)

    else:

        print(f"No valid placement exists for {N} components.")

 

# Helper function to print all valid placements

def print_solutions(solutions):

    """

    Prints all valid circuit placements.

    """

    solution_number = 1

    for solution in solutions:

        print(f"Placement {solution_number}:")

        for row in solution:

            print(row)

        print()

        solution_number += 1

 

# Example usage of the circuit design and verification

try:

    N = int(input("Enter the number of components (N) to place in the circuit: "))

    circuit_design_verification(N)

except ValueError:

    print("Please enter a valid integer.")