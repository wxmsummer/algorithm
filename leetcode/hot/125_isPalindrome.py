class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        i, j = 0, len(s) - 1
        
        while i < j:
            while i < j and not (s[i].islower() or s[i].isdigit()):
                i += 1
            while i < j and not (s[j].islower() or s[j].isdigit()):
                j -= 1
            print('i, j:', s[i], s[j])
            if s[i] != s[j]:
                return False

            i += 1
            j -= 1
            

        return True


if __name__ == '__main__':
    obj = Solution()
    print(obj.isPalindrome('A man, a plan, a canal: Panama'))
    print(obj.isPalindrome('0P'))
