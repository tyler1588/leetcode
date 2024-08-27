class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = {}
        buckets = [[] for _ in range(len(nums) + 1)]
        
        for n in nums:
            counts[n] = 1 + counts.get(n, 0)
        
        for val, count in counts.items():
            buckets[count].append(val)

        result = []
        for i in range(len(buckets) - 1, -1, -1):
            while len(buckets[i]) > 0 and k > 0:
                result.append(buckets[i].pop())
                k -= 1

        return result

# Bucket sort
# The indices are the counts
# The values are nested lists containing the elements that have that frequency