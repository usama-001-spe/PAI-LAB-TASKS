from collections import deque

def water_jug_solution(jug1_cap, jug2_cap, target):
    queue = deque()
    queue.append((0, 0, []))  
    visited = set()
    
    while queue:
        jug1, jug2, steps = queue.popleft()
        
 
        if jug1 == target or jug2 == target:
            print("\nSolution Found! Steps:")
            for i, step in enumerate(steps, 1):
                print(f"Step {i}: Jug1={step[0]}L, Jug2={step[1]}L")
            print(f"Final State: Jug1={jug1}L, Jug2={jug2}L")
            return True
        
        if (jug1, jug2) in visited:
            continue
        visited.add((jug1, jug2))
        
        next_steps = []
        
        # 1. Fill Jug1 to capacity
        next_steps.append((jug1_cap, jug2))
        # 2. Fill Jug2 to capacity
        next_steps.append((jug1, jug2_cap))
        # 3. Empty Jug1
        next_steps.append((0, jug2))
        # 4. Empty Jug2
        next_steps.append((jug1, 0))
        
        # 5. Pour from Jug1 to Jug2
        transfer = min(jug1, jug2_cap - jug2)
        next_steps.append((jug1 - transfer, jug2 + transfer))
        
        # 6. Pour from Jug2 to Jug1
        transfer = min(jug2, jug1_cap - jug1)
        next_steps.append((jug1 + transfer, jug2 - transfer))
        
        # Add new states to queue
        for new_j1, new_j2 in next_steps:
            if (new_j1, new_j2) not in visited:
                new_steps = steps + [(jug1, jug2)]
                queue.append((new_j1, new_j2, new_steps))
    
    print("No solution found")
    return False

jug1_size = 4
jug2_size = 3
target_water = 2
water_jug_solution(jug1_size, jug2_size, target_water)