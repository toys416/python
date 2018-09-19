
def twosum(nums, target):
    """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
    for i in range(0, len(nums)):
        for j in range(i+1,len(nums)):
            a = nums[i]
            b = nums[j]
            if a+b == target:
                return[i , j]

rct = twosum([2,7,11,15],17)
print rct
