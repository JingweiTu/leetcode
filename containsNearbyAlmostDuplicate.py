class Solution(object):
    def containsNearbyAlmostDuplicate(self, nums, k, t):
        """
        :type nums: List[int]
        :type k: int
        :type t: int
        :rtype: bool
        """
        # Bucket sort. Each bucket has size of t. For each number, the possible
        # candidate can only be in the same bucket or the two buckets besides.
        # Keep as many as k buckets to ensure that the difference is at most k.
        buckets = {}
        for i, v in enumerate(nums):
            if t < 0 or k < 0:
                return False
                
            # t == 0 is a special case where we only have to check the bucket
            # that v is in.
            if t > 0:
                bucketNum, offset = (v / t, 1) 
            else: 
                bucketNum, offset = (v, 0)
            for idx in xrange(bucketNum - offset, bucketNum + offset + 1):
                if idx in buckets and abs(buckets[idx] - nums[i]) <= t:
                    return True
    
            buckets[bucketNum] = nums[i]
            if len(buckets) > k:
                # Remove the bucket which is too far away. Beware of zero t.
                del buckets[nums[i - k] / t if t else nums[i - k]]
    
        return False