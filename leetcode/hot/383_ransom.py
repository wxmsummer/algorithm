ransomNote = input()
magazine = input()
list_1 = list(ransomNote)
list_2 = list(magazine)
for i in range(len(list_1)):
    print(list_1)
    print(list_2)
    if list_1[0] not in list_2:
        print(0)
        break
    else:
        list_2.remove(list_1[0])
        del list_1[0]
        continue
print(1)

# return not collections.Counter(ransomNote) - collections.Counter(magazine)