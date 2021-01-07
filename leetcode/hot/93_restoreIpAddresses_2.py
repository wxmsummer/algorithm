# 复原ip地址

class Solution:
    def restoreIpAddresses(self, s: str) -> list:
        def backTrack(start, tmp):
            # 如果刚好分割为4段，则加入解集
            if len(tmp) == 4 and start == len(s):
                res.append('.'.join(tmp))
            # 如果分割为4段之后还没分割完，则剪枝，后面不用分了
            if len(tmp) == 4 and start < len(s):
                return
            # i为段长度，取1到3
            for i in range(1, 4):
                # 如果当前段长加上start超过字符串长，则剪枝
                if start + i > len(s):
                    return
                # 如果段长不为1，且段起始为0，则剪枝
                if i != 1 and s[start] == '0':
                    return
                # 段值不能大于255
                seg = s[start:start+i]
                if int(seg) > 255:
                    return
                tmp.append(seg)
                # 开启下一层的递归
                backTrack(start+i, tmp)
                tmp.pop()

        res = []
        backTrack(0, [])
        return res 

if __name__ == '__main__':
    obj = Solution()
    print(obj.restoreIpAddresses('101023'))