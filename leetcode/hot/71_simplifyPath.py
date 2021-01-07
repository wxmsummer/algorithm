# 简化路径

class Solution:
    # 未通过
    # def simplifyPath(self, path: str) -> str:
    #     letter_stack = []
    #     length = len(path)
    #     i = 1
    #     letter = ''
    #     while i < length:
    #         while path[i] >= 'a' and path[i] <= 'z':
    #             letter += path[i]
    #             i += 1
    #         if letter != '':
    #             letter_stack.append(letter)
    #             letter = ''
            
    #         if letter_stack and path[i] == '.' and path [i-1] == '.':
    #             letter_stack.pop()
    #         i += 1
    #     print('letter_stack:', letter_stack)

    #     if not letter_stack:
    #         return '/'
    #     res = ''
    #     for s in letter_stack:
    #         res += '/' + s
    #     return res

    # 先将路径用 / 分隔开，然后根据分隔的字符进行处理
    def simplifyPath(self, path:str) -> str:
        stack = []
        path = path.split('/')

        for i in path:
            # 如果发现 .. 则去看栈是否为空
            # 如果为空则跳过，否则就出栈
            if i == '..':
                if stack:
                    stack.pop()
            # 如果是除了 . 之外的其他元素，则加入栈
            elif i and i != '.':
                stack.append(i)
        
        # 这里注意的是顶格先加上一个 / 
        return '/' + '/'.join(stack)

if __name__ == '__main__':
    obj = Solution()
    print(obj.simplifyPath('/../'))
    print(obj.simplifyPath('/home/'))
    print(obj.simplifyPath('/home//foo/'))
    print(obj.simplifyPath('/a/./b/../../c/'))
