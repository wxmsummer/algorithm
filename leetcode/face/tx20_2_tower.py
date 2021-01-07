
class Solution():
    def tower(self, num_list):
        length = len(num_list)
        stack, count_list = [], [1]*length
        for i in range(length):
            count_list[i] += len(stack)
            while(stack and num_list[i] > stack[len(stack)-1]):
                stack.pop()
            stack.append(num_list[i])
            print('stack:', stack, 'count_list:', count_list)

        stack = []
        for i in range(length-1, -1, -1):
            count_list[i] += len(stack)
            while(stack and num_list[i] > stack[len(stack)-1]):
                stack.pop()
            stack.append(num_list[i])
            print('stack:', stack, 'count_list:', count_list)

        return count_list

if __name__ == '__main__':
    obj = Solution()
    obj.tower([5, 3, 8, 3, 2, 5])
