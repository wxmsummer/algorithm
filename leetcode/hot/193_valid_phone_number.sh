# Read from the file file.txt and output all valid phone numbers to stdout.
grep -P '^([0-9]{3}-|\([0-9]{3}\) )[0-9]{3}-[0-9]{4}$' file.txt

# ^ 表示匹配开始位置
# [0-9] 匹配0~9的数字
# {3} 表示出现三次
# | 或者 从两者中选取一个匹配
# \ 用于转义表达
# $ 匹配表达式结束位置