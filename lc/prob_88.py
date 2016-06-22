class Solution:
    # @param {integer[]} nums1
    # @param {integer} m
    # @param {integer[]} nums2
    # @param {integer} n
    # @return {void} Do not return anything, modify nums1 in-place instead.
    def merge(self, nums1, m, nums2, n):
        for i in xrange(len(nums1) - 1, m-1, -1):
            del nums1[i]
        for i in xrange(len(nums2) - 1, n-1, -1):
            del nums2[i]
        for idx2 in xrange(len(nums2)):
            for idx in xrange(len(nums1)):
                if nums1[idx] > nums2[idx2]:
                    nums1.insert(idx, nums2[idx2])
                    break
            else:
                nums1.append(nums2[idx2])

Solution().merge([0], 0, [1], 1)