def center_spread(s, size, left, right):
    l = left
    r = right
    while l >= 0 and r < size and s[l] == s[r]:
            l -= 1
            r += 1
    return s[l+1:r], r-l-1

def max_palindrome():
    s= input()
    size = len(s)
    if size == 0:
        print('the string is empty')
        return ''
    max_length = 1
    longest_palindrome = s[0]
    for i in range(size):
        (odd_palindrome, odd_len) = center_spread(s, size, i, i)
        (even_palindrome, even_len) = center_spread(s, size, i, i+1)
        cur_max_sub = odd_palindrome if odd_len >= even_len else even_palindrome
        if len(cur_max_sub) > max_length:
            max_length = len(cur_max_sub)
            longest_palindrome = cur_max_sub
    print(longest_palindrome)
    return longest_palindrome

if __name__ == '__main__':
    max_palindrome()