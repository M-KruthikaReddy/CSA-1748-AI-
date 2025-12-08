from typing import List, Tuple
from collections import deque


def is_valid_state(state: Tuple[int, int, int, int, int, int]) -> bool:
    """
    Check if a state is valid according to the problem constraints.
    """
    m1, c1, b, m2, c2, _ = state

    if m1 < 0 or c1 < 0 or m2 < 0 or c2 < 0:
        return False

    
    if (m1 > 0 and m1 < c1) or (m2 > 0 and m2 < c2):
        return False

    return True


def get_successors(state: Tuple[int, int, int, int, int, int]) -> List[Tuple[int, int, int, int, int, int]]:
    """
    Generate all valid successor states.
    """
    m1, c1, b, m2, c2, d = state
    successors = []

   
    moves = [(1, 0), (0, 1), (1, 1), (2, 0), (0, 2)]

    if d == 1:  
        for i, j in moves:
            new_state = (m1 - i, c1 - j, 0, m2 + i, c2 + j, 0)
            if is_valid_state(new_state):
                successors.append(new_state)
    else:  
        for i, j in moves:
            new_state = (m1 + i, c1 + j, 1, m2 - i, c2 - j, 1)
            if is_valid_state(new_state):
                successors.append(new_state)

    return successors


def breadth_first_search() -> List[Tuple[int, int, int, int, int, int]]:
    """
    Solve problem using BFS.
    """
    initial_state = (3, 3, 1, 0, 0, 1)
    goal_state = (0, 0, 0, 3, 3, 0)

    visited = set()
    queue = deque([(initial_state, [])])

    while queue:
        state, path = queue.popleft()

        if state == goal_state:
            return path + [state]

        if state in visited:
            continue

        visited.add(state)

        for successor in get_successors(state):
            if successor not in visited:
                queue.append((successor, path + [state]))

    return []


if __name__ == "__main__":
    solution = breadth_first_search()
    print("Solution:")
    for state in solution:
        print(state)
