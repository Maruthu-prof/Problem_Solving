from collections import deque
from typing import List

class Solution:
    def minMoves(self, classroom: List[str], energy: int) -> int:
        m, n = len(classroom), len(classroom[0])
        litter_positions = []
        start_r, start_c = -1, -1
        
        # Locate the starting position and all litter locations
        for r in range(m):
            for c in range(n):
                if classroom[r][c] == 'S':
                    start_r, start_c = r, c
                elif classroom[r][c] == 'L':
                    litter_positions.append((r, c))
                    
        num_litters = len(litter_positions)
        litter_map = {pos: i for i, pos in enumerate(litter_positions)}
        target_mask = (1 << num_litters) - 1
        
        # If there is no litter to collect, we are already done
        if target_mask == 0:
            return 0
            
        # queue stores: (row, col, litter_mask, current_energy, steps)
        queue = deque([(start_r, start_c, 0, energy, 0)])
        
        # visited map tracks: (row, col, litter_mask) -> max_remaining_energy
        visited = {(start_r, start_c, 0): energy}
        
        while queue:
            r, c, mask, curr_e, steps = queue.popleft()
            
            # If a better path reached this exact substate with more energy, skip
            if visited.get((r, c, mask), -1) > curr_e:
                continue
                
            # Explore all 4 adjacent directions
            for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nr, nc = r + dr, c + dc
                
                # Check grid boundaries and avoid obstacles
                if 0 <= nr < m and 0 <= nc < n and classroom[nr][nc] != 'X':
                    next_e = curr_e - 1
                    
                    # Invalid move if we run out of energy before landing
                    if next_e < 0:
                        continue
                    
                    next_mask = mask
                    # Collect litter if present at the next cell
                    if classroom[nr][nc] == 'L':
                        litter_idx = litter_map[(nr, nc)]
                        next_mask |= (1 << litter_idx)
                        
                    # Recharge to maximum energy capacity if landing on a reset area
                    if classroom[nr][nc] == 'R':
                        next_e = energy
                        
                    # Goal check: Return the total moves immediately upon collecting all litter
                    if next_mask == target_mask:
                        return steps + 1
                        
                    # Only add to queue if it offers a strictly better energy level for this state
                    if next_e > visited.get((nr, nc, next_mask), -1):
                        visited[(nr, nc, next_mask)] = next_e
                        queue.append((nr, nc, next_mask, next_e, steps + 1))
                        
        return -1

        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna