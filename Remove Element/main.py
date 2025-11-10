from src.solution import Solution
from data import test1
from data import test2

remove_element = Solution()

print('\n--- 📋Test 1 ---')
print(f'nums = {test1.nums}')
print(f'val = {test1.val}')
answer = remove_element.removeElement(test1.nums,test1.val)
print(f'answer = {answer}')

print('\n--- 📋Test 1 ---')
print(f'nums = {test2.nums}')
print(f'val = {test2.val}')
answer = remove_element.removeElement(test2.nums,test2.val)
print(f'answer = {answer}')