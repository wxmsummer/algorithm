from collections import defaultdict

class Solution:
    def circleWord(self , wordList):
        dic = defaultdict(list)
        length = len(wordList)
        i = 0
        while i < length:
            word = wordList[i]
            if word == '#':
                i += 1
                continue
            double_word = word + word
            for j in range(i, length):
                if wordList[j] in double_word:
                    dic[word].append(wordList[j])
                    wordList[j] = '#'
        print('dic:', dic)
        res = []
        for val in dic.values():
            res.append(val)
        return res

if __name__ == '__main__':
    obj = Solution()
    print(obj.circleWord(["picture", "turepic", "icturep", "word", "ordw"]))
    print(obj.circleWord(['cat', 'atc', 'tca', 'peer', 'eerp']))
