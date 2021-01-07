# 加油站
class Solution:
    # 暴力法，直接从每个位置开始，考虑从该位置开始是否能环游
    def canCompleteCircuit(self, gas: list, cost: list) -> int:
        length = len(gas)
        for i in range(length):
            cur_gas = 0
            idx = i
            count = 0
            print('i:', i)
            # count 用于记录环游步数
            while count < length:
                print('idx:', idx)
                # 如果大于length，就回环
                if idx >= length:
                    idx = idx % length
                cur_gas += gas[idx]
                cur_gas -= cost[idx]
                idx += 1
                # 如果当前位置开始环游，发现油不够，就考虑从下一个位置开始
                if cur_gas < 0:
                    break
                count += 1
            # 如果发现能环游，返回该位置
            if count == length:
                return idx
        # 如果走遍了所有位置，都无法环游，则返回-1
        return -1

if __name__ == '__main__':
    obj = Solution()
    print(obj.canCompleteCircuit([1,2,3,4,5], [3,4,5,1,2]))
    print(obj.canCompleteCircuit([2,3,4], [3,4,3]))