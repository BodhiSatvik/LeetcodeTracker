class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        resultList = []
        tempList = []

        def recursiveFunction(index):
            if index >= len(nums):                      # if index is out of range
                resultList.append(tempList.copy())      # copy, since we're gonna make more changes to the list 
                return  
            
            # In decision tree, decision to add i to the list
            tempList.append(nums[index])
            recursiveFunction(index + 1)

            # In decision tree, decision to not add i to the list
            tempList.pop()
            recursiveFunction(index + 1)

        recursiveFunction(0)
        return resultList