# 单词接龙

from collections import deque

class Solution:
    # 广度优先搜索
    def ladderLength(self, beginWord: str, endWord: str, wordList: list) -> int:
        
        # 注意这里一定要转换为set，否则会超时
        word_set = set(wordList)

        if endWord not in word_set:
            return 0

        queue = deque()
        queue.append(beginWord)

        length = len(beginWord)
        count = 1
        
        # 用于标识是否已访问
        visited = set(beginWord)
        while queue:
            size = len(queue)
            for i in range(size):
                word = list(queue.popleft())

                # 对每个单词，修改其中的一个字母，判断该单词是否在word_set中
                # 如果在，则加入queue，然后标记已访问
                for j in range(length):
                    tmp = word[j]

                    for k in range(26):
                        word[j] = chr(ord('a') + k)
                        new_word = ''.join(word)
                        if new_word in word_set:
                            if new_word == endWord:
                                return count+1
                            if new_word not in visited:
                                queue.append(new_word)
                                visited.add(new_word)
                    word[j] = tmp
            # 每一层遍历，count+1
            count += 1
        return 0
        
if __name__ == '__main__':
    obj = Solution()
    print(obj.ladderLength('hit', 'cog', ["hot","dot","cog"]))
    # print(obj.ladderLength('hit', 'cog', ["hot","dot","dog","lot","log","cog"]))
    # print(obj.ladderLength("qa","sq",["si","go","se","cm","so","ph","mt","db","mb","sb","kr","ln","tm","le","av","sm","ar","ci","ca","br","ti","ba","to","ra","fa","yo","ow","sn","ya","cr","po","fe","ho","ma","re","or","rn","au","ur","rh","sr","tc","lt","lo","as","fr","nb","yb","if","pb","ge","th","pm","rb","sh","co","ga","li","ha","hz","no","bi","di","hi","qa","pi","os","uh","wm","an","me","mo","na","la","st","er","sc","ne","mn","mi","am","ex","pt","io","be","fm","ta","tb","ni","mr","pa","he","lr","sq","ye"]))
    # print(obj.ladderLength("qa","sq",["si","cm","so","ph","mt","db","mb","sb","kr","ti","ba","to","ra","fa","yo","ow","sn","ya","cr","po","fe","ho","ma","re","or","rn","au","ur"]))


# # 深度优先会超时
# class Solution:
#     def ladderLength(self, beginWord: str, endWord: str, wordList: list) -> int:
        
#         def recur(tmp, count):
#             # 判断tmp是否等于endWord，如果相等，返回count
#             if tmp == endWord:
#                 res.append(count)

#             # 遍历当前字典，找到一个和tmp相差1个字符的单词

#             for i in range(len(wordList)):
#                 if wordList[i] != '#' and helper(wordList[i], tmp):
#                     count += 1
#                     visited = wordList[i]
#                     wordList[i] = '#'
#                     recur(visited, count)
#                     count -= 1
#                     wordList[i] = visited
#                     # 标记该单词已访问
#                     # 把该单词作为新单词，递归
#                     # 恢复该单词 

#         def helper(a, b):
#             count = 0
#             for i in range(len(a)):
#                 if a[i] != b[i]:
#                     count += 1
#             return count == 1

#         res = []
#         recur(beginWord, 1)
#         if not res:
#             return 0
#         return min(res)