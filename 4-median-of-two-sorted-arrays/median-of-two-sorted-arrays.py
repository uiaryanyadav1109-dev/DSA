
class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        m, n = len(nums1), len(nums2)

        if m > n:
            nums1, nums2 = nums2, nums1
            m, n = n, m

        total = m + n

        def kth(k):
            low = max(0, k - n)
            high = min(k, m)

            while low <= high:
                i = (low + high) // 2
                j = k - i

                left1 = nums1[i - 1] if i > 0 else float('-inf')
                right1 = nums1[i] if i < m else float('inf')
                left2 = nums2[j - 1] if j > 0 else float('-inf')
                right2 = nums2[j] if j < n else float('inf')

                if left1 > right2:
                    high = i - 1
                elif left2 > right1:
                    low = i + 1
                else:
                    return max(left1, left2)

        if total % 2:
            return float(kth(total // 2 + 1))

        return (kth(total // 2) + kth(total // 2 + 1)) / 2.0
