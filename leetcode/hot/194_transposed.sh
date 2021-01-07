# Read from the file file.txt and print its transposed content to stdout.
awk '{
    for (i=1;i<=NF;i++){
        if (NR==1){
            res[i]=$i
        }
        else {
            res[i]=res[i]" "$i
        }
    }
}END{
    for(j=1;j<=NF;j++){
        print res[j]
    }
}' file.txt

# awk 是一行一行地处理文本文件，其运行流程是：
# 1.先运行BEGIN后的{Action} 相当于表头
# 2.再运行{Action}中的文件处理主体命令
# 3.最后运行END后的{Action}中的命令

# NF 是当前行的filed字段数；NR是正在处理的当前行数
# 使用res数组存储转置字符串
# 转置的方法：先将第一行作为转置后的第一列，然后从第二行开始，依次将字段追加到对应行的末尾

# 如 1 2
#    a b
#    3 4

# 先放置第一列
# 1
# 2

# 然后将其余行中的字符添加到数组行后

# 1 a
# 2 b

# 1 a 3
# 2 b 4