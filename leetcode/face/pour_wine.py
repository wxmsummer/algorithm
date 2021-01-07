from collections import deque

def pour_wine(nums):
    # 初始状态
    init_state = (0, 0, nums[2])
    task = deque()
    task.append(init_state)
    visited = set()
    volumns = (nums[0], nums[1], nums[2])
    count = 1
    while task:
        count += 1
        size = len(task)
        for i in range(size):
            state = task.popleft()
            if state not in visited:
                visited.add(state)

            state = list(state)

            for idx in range(3):
                for jdx in range(3):
                    if idx == jdx:
                        continue
                    if state[idx] > 0 and state[jdx] < volumns[jdx]:
                        new_state = state.copy()
                        new_state[idx] = max(0, state[idx] - volumns[jdx] + state[jdx])
                        new_state[jdx] = min(volumns[jdx], state[idx] + state[jdx])
                        new_state = tuple(new_state)
                        if new_state not in visited:
                            task.append(new_state)
                        if new_state[2] == nums[2] / 2:
                            return count
    return -1


if __name__ == "__main__":
    print(pour_wine([3, 5, 8]))
