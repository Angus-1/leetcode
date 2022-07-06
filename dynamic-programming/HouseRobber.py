class Solution:       
    def rob(self, nums: List[int]) -> int:
        last, curr = 0, 0
        for i in nums:
            last, curr = curr, max(last + i, curr)
        return curr
      
     def rob2(self, nums: List[int]) -> int:  #another way to approach
        rob = [None] * (len(nums) + 1)
        # Base case: 0 rooms and 1 room
        rob[0] = 0
        rob[1] = nums[0]
        # Solving sub questions and store the sub solutions: more than 1 rooms
        for i in range(2, len(nums) + 1):
            # For any given number at index n: compare dp[n-2] + number and dp[n-1]
            rob[i] = max(rob[i-2] + nums[i-1], rob[i-1])
        # Return the larget amount of money been stolen from the dp results
        return rob[len(nums)]
