class Solution:
    def partitionLabels(self, S: str) -> list:
        last = [0] * 26
        for i in range (len(S)):
            last[ord(S[i]) - ord('a')] = i
        
        left, right = 0, 0
        result = []
        for i in range (len(S)):
            right = max(right, last[ord(S[i]) - ord('a')])
            if i == right:
                result.append(right - left + 1)
                left = i + 1
        return result

if __name__ == '__main__':
    obj = Solution()
    print(obj.partitionLabels("ababcbacadefegdehijhklij"))