# class Solution:
#     # @param {integer[]} nums1
#     # @param {integer[]} nums2
#     # @return {float}
#     def findMedianSortedArrays(self, nums1, nums2):
#         self.nums1 = nums1
#         self.nums2 = nums2
#         if not nums1:
#             return nums2[len(nums2)/2] if len(nums2) % 2 == 1 else float(nums2[len(nums2)/2-1] + nums2[len(nums2)/2])/2
#         if not nums2:
#             return nums1[len(nums1)/2] if len(nums1) % 2 == 1 else float(nums1[len(nums1)/2-1] + nums1[len(nums1)/2])/2
#         if (len(nums1) + len(nums2)) % 2:
#             return self.find_ele(0, len(nums1) - 1, 0, len(nums2) - 1, (len(nums1) + len(nums2) - 1)/2)
#         else:
#             return (self.find_ele(0, len(nums1) - 1, 0, len(nums2) - 1, (len(nums1) + len(nums2) - 1)/2) +
#                 self.find_ele(0, len(nums1) - 1, 0, len(nums2) - 1, (len(nums1) + len(nums2) - 1)/2 + 1)) / 2.0
#
#     def find_ele(self, start1, end1, start2, end2, k):
#         total_len = end1 - start1 + end2 - start2 + 1
#         m1 = int((float(k) / total_len) * (end1 - start1) + start1)
#         m2 = int((float(k) / total_len) * (end2 - start2) + start2)
#         #if k <= 3:
#         #    return sorted(self.nums1[start1:end1 + 1] + self.nums2[start2: end2 + 1])[k]
#         try:
#             if self.nums1
#         if self.nums1[m1] == self.nums2[m2]:
#             return self.nums1[m1]
#         elif self.nums1[m1] > self.nums2[m2]:
#             return self.find_ele(start1, m1-1, m2+1, end2, k - (m2 - start2)- 1)
#         else:
#             return self.find_ele(m1+1, end1, start2, m2-1, k - (m1 - start1)-1)


class Solution:
    # @param {integer[]} nums1
    # @param {integer[]} nums2
    # @return {float}
    def findMedianSortedArrays(self, nums1, nums2):
        self.nums1 = nums1
        self.nums2 = nums2
        if not nums1:
            return nums2[len(nums2)/2] if len(nums2) % 2 == 1 else float(nums2[len(nums2)/2-1] + nums2[len(nums2)/2])/2
        if not nums2:
            return nums1[len(nums1)/2] if len(nums1) % 2 == 1 else float(nums1[len(nums1)/2-1] + nums1[len(nums1)/2])/2
        if (len(nums1) + len(nums2)) % 2:
            return self.recur(0, len(nums1), 0, len(nums2), (len(nums1)+ len(nums2))/2+1)
        else:
            return float(self.recur(0, len(nums1), 0, len(nums2), (len(nums1)+ len(nums2))/2) +
                         self.recur(0, len(nums1), 0, len(nums2), (len(nums1)+ len(nums2))/2+1))/2

    def recur(self, start1, l1, start2, l2, k):
        if l1 == 0:
            return self.nums2[k-1]
        if l2 == 0:
            return self.nums1[k-1]
        if l1/2 + l2/2 + 1 > k:
            if self.nums1[l1/2] > self.nums2[l2/2]:
                return self.recur(start1, l1/2, start2, l2, k)
            else:
                return self.recur(start1, l1, start2, l2/2, k)
        else:
            if self.nums1[l1/2] > self.nums2[l2/2]:
                return self.recur(start1, l1, start2 + l2/2 + 1, l2/2-1, k - l2/2 - 1)
            else:
                return self.recur(start1 + l1/2 + 1, l1/2-1, start2, l2, k - l1/2 -1)

print Solution().findMedianSortedArrays([2,3,4,5,6,7,8], [1,2,3,4])