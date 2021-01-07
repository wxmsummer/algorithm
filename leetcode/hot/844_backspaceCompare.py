class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        return self.back(S) == self.back(T)

    def back(self, S: str) -> list:
        list_s = []
        for s in S:
            if s != '#':
                list_s.append(s)
            else :
                if list_s:
                    list_s.pop()
                else:
                    continue
        return list_s