# 🗑️ Remove Element - My Solution 🚀

Hi! 👋 This file documents how I solved the **"Remove Element"** coding challenge.

This challenge is quite interesting because it requires us to modify the array _in-place_ (directly within the array itself) without using any additional arrays.

## 🧐 About the Challenge

The core of this problem is that we are given an integer array `nums` and a target value `val`. The task is to remove all occurrences of `val` inside `nums`.

**Key Requirements:**

- 🛠️ Must be done **in-place**. O(1) extra space.
    
- 🔄 The order of the remaining elements may be changed.
    
- 🔢 We must return the number of elements (`k`) that remain (those that are not `val`).
    

### 🎯 Case Examples

**Example 1:**

> Input: `nums = [3,2,2,3]`, `val = 3`
> 
> My Output: `k = 2`, and the array becomes `[2,2,_,_]`
> 
> _(Number 3 successfully removed! 🎉)_

**Example 2:**

> Input: `nums = [0,1,2,2,3,0,4,2]`, `val = 2`
> 
> My Output: `k = 5`, and the array becomes `[0,1,4,0,3,_,_,_]`
> 
> _(All number 2s are gone! 😎)_

## 💡 My Approach: "Two Pointers" Technique

To solve this efficiently, I used the **Two Pointers** approach.

I imagine this array as having two parts: a "clean" part (without `val`) at the front, and the remaining "unchecked" part.

### 🧠 Code Logic:

1. I set up a pointer `k` starting at index `0`. This pointer is responsible for marking the last position of "safe" elements (not `val`).
    
2. I _loop_ through the entire array using an iterator pointer `i`.
    
3. Whenever I find a number that is **NOT** the target (`nums[i] != val`), I "save" it by moving it to position `k`.
    
4. After moving it, I advance the `k` pointer by one step.
    
5. If I find the target number (`val`), I simply ignore it and continue to the next iteration.
    

In the end, the value of `k` will indicate how many "safe" numbers I successfully collected at the front of the array.

## 💻 My Code Solution

Here is the complete implementation in Python:

```
class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        k = 0  # Pointer for "safe" elements 🛡️

        # Iterate through the entire array 🏃‍♂️
        for i in range(len(nums)):
            # If current element is NOT the target to remove...
            if nums[i] != val:
                # ...move it to the safe 'k' position ✅
                nums[k] = nums[i]
                # Advance safe pointer for next slot ➡️
                k += 1
            
        # Return the count of remaining elements 🎉
        return k
```