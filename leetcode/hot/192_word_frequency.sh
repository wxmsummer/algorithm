# Read from the file words.txt and output the word frequency list to stdout.

cat words.txt | tr -s ' ' '\n' | sort | uniq -c | sort -r | awk '{print $2, $1}'

# cat words.txt 查看words.txt
# tr -s '' '\n' 将字符串中的空格全部替换为换行符 实现分词
# sort 排序，将分号的词按照字典顺序排序
# uniq -c 统计单词重复次数（此步骤与上一步息息相关，-c原理是字符串相同则加一，如果不进行先排序的话将无法统计数目）
# sort -r 将数目倒序排列
# awk '{print $2, $1}' 将词频和词语调换位置打印
