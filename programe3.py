from collections import deque

# Function to compute the Greatest Common Divisor (GCD) of two numbers
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

# Function to check if the target amount is measurable
def is_solvable(x, y, d):
    return d <= max(x, y) and d % gcd(x, y) == 0

# Function to solve the Water Jug Problem using BFS
def water_jug_problem(x, y, d):
    if not is_solvable(x, y, d):
        return "No solution possible"
    
    # Queue for BFS, storing (jug1, jug2) states
    queue = deque([(0, 0)])  # Start with both jugs empty
    visited = set()  # To keep track of visited states
    visited.add((0, 0))
    
    # List of possible states from current state
    while queue:
        jug1, jug2 = queue.popleft()

        # If we reach the target amount in either jug, return the solution
        if jug1 == d or jug2 == d:
            return f"Solution found: Jug1 = {jug1}, Jug2 = {jug2}"

        # List of possible states: fill, empty, or pour
        possible_states = [
            (x, jug2),  # Fill jug1
            (jug1, y),  # Fill jug2
            (0, jug2),  # Empty jug1
            (jug1, 0),  # Empty jug2
            (jug1 - min(jug1, y - jug2), jug2 + min(jug1, y - jug2)),  # Pour jug1 into jug2
            (jug1 + min(jug2, x - jug1), jug2 - min(jug2, x - jug1))   # Pour jug2 into jug1
        ]

        # Explore each possible state and add to queue if not visited
        for state in possible_states:
            if state not in visited:
                visited.add(state)
                queue.append(state)

    return "No solution found"

# Example usage
if __name__ == "__main__":
    x = 4  # Capacity of Jug 1
    y = 3  # Capacity of Jug 2
    d = 2  # Desired amount of water

    result = water_jug_problem(x, y, d)
    print(result)
