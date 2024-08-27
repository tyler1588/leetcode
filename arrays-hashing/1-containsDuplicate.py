class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dups = set()
        for n in nums:
            if n in dups:
                return True
            dups.add(n)
        return False


# Naive
# Nested for loop O(n^2)
# Iterate over each element
# Check if the element is present a second time in the array

# Efficient
# Create a hash table
# Add each element to the hash table
# If the element is already in the has table return false
# Runs in Theta(n)
         