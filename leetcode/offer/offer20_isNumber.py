# 表示数字的字符串

# 有限状态自动机解决
class Solution:
    def isNumber(self, s:str) -> bool:
        states = [
            {' ':0, 's':1, 'd':2 , '.':4},  # 0. start with 'blank'
            {'d':2, '.':4},                 # 1. 'sign' before 'e'
            {'d':2, '.':3, 'e':5, ' ':8},   # 2. 'digit' before 'dot'
            {'d':3, 'e':5, ' ':8},          # 3. 'digit' after 'dot'
            {'d':3},                        # 4. 'blank' before 'dot' and 'digit' after 'dot'
            {'s':6, 'd':7},                 # 5. 'e'
            {'d':7},                        # 6. 'sign' after 'e'
            {'d':7, ' ':8},                 # 7. 'digit' after 'e'
            {' ':8}                         # 8. end with 'blank'
        ]

        p = 0                               # start with state 0
        for c in s:
            if '0' <= c <= '9': 
                t = 'd'
            elif c in '+-':
                t = 's'
            elif c in 'eE':
                t = 'e'
            elif c in '. ':
                t = c
            else:
                t = '?'
            if t not in states[p]:
                return False
            p = states[p][t]

        return p in (2,3, 7, 8)

# 常规思路，逐位遍历，并做好是否遇见小数点、eE的标记
# class Solution {
#     public boolean isNumber(String s) {
#         if(s == null || s.length() == 0) return false; // s为空对象或 s长度为0(空字符串)时, 不能表示数值
#         boolean isNum = false, isDot = false, ise_or_E = false; // 标记是否遇到数位、小数点、‘e’或'E'
#         char[] str = s.trim().toCharArray();  // 删除字符串头尾的空格，转为字符数组，方便遍历判断每个字符
#         for(int i=0; i<str.length; i++) {
#             if(str[i] >= '0' && str[i] <= '9') isNum = true; // 判断当前字符是否为 0~9 的数位
#             else if(str[i] == '.') { // 遇到小数点
#                 if(isDot || ise_or_E) return false; // 小数点之前可以没有整数，但是不能重复出现小数点、或出现‘e’、'E'
#                 isDot = true; // 标记已经遇到小数点
#             }
#             else if(str[i] == 'e' || str[i] == 'E') { // 遇到‘e’或'E'
#                 if(!isNum || ise_or_E) return false; // ‘e’或'E'前面必须有整数，且前面不能重复出现‘e’或'E'
#                 ise_or_E = true; // 标记已经遇到‘e’或'E'
#                 isNum = false; // 重置isNum，因为‘e’或'E'之后也必须接上整数，防止出现 123e或者123e+的非法情况
#             }
#             else if(str[i] == '-' ||str[i] == '+') { 
#                 if(i!=0 && str[i-1] != 'e' && str[i-1] != 'E') return false; // 正负号只可能出现在第一个位置，或者出现在‘e’或'E'的后面一个位置
#             }
#             else return false; // 其它情况均为不合法字符
#         }
#         return isNum;
#     }
# }


if __name__ == '__main__':
       obj = Solution()
       print(obj.isNumber('1 '))


