class Solution:
    def smallestNumber(self, n: int) -> int:
        power = 1
        while True:
            biner = 2**power - 1
            if biner >= n:
                return biner
            power += 1


# Test:
while True:
    try:
        input_number = int(input('Enter a number for the lower limit: '))
        break
    except ValueError:
        print('Just input a number')
        continue
check_biner = Solution()
print(check_biner.smallestNumber(input_number))

'''
  input = 5 -> 7
  input = 10 -> 15
  input = 3 -> 3
'''