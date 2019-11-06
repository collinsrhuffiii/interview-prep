'''
There are two sorted arrays nums1 and nums2 of size m and n respectively.

Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).

Example 1:
nums1 = [1, 3]
nums2 = [2]

The median is 2.0
Example 2:
nums1 = [1, 2]
nums2 = [3, 4]

The median is (2 + 3)/2 = 2.5
'''

class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        MAX_INT = 2**63 -1
        MIN_INT = -MAX_INT -1
        n1 = len(nums1)
        n2 = len(nums2)
        if n1 < n2:
            nums1, n1, nums2, n2 = nums2, n2, nums1, n1
        low = 0
        high = n2 * 2
        while(low <= high):
            mid2 = (low+high)//2
            mid1 = n1+n2 - mid2
            l1 = MIN_INT if mid1 == 0 else nums1[(mid1-1)//2]
            l2 = MIN_INT if mid2 == 0 else nums2[(mid2-1)//2]
            r1 = MAX_INT if mid1 == n1*2 else nums1[mid1//2]
            r2 = MAX_INT if mid2 == n2*2 else nums2[mid2//2]
            if l1 > r2: 
                low = mid2+1
            elif l2 > r1: 
                high = mid2-1
            else:
                return (max(l1,l2)+ min(r1, r2))/2
         
sol = Solution()
arr1 = [1,2,3]
arr2 = [4,5]
print(f'{arr1}, {arr2}, {sol.findMedianSortedArrays(arr1, arr2)}')

arr1 = [4,5]
arr2 = [1,2,3]
print(f'{arr1}, {arr2}, {sol.findMedianSortedArrays(arr1, arr2)}')

arr1 = [1,2,3]
arr2 = [4,5,6]
print(f'{arr1}, {arr2}, {sol.findMedianSortedArrays(arr1, arr2)}')

arr1 = []
arr2 = []
print(f'{arr1}, {arr2}, {sol.findMedianSortedArrays(arr1, arr2)}')

arr1 = [1,2,3]
arr2 = [4,5,6,7]
print(f'{arr1}, {arr2}, {sol.findMedianSortedArrays(arr1, arr2)}')

arr1 = [1,2,5]
arr2 = [3,4,6]
print(f'{arr1}, {arr2}, {sol.findMedianSortedArrays(arr1, arr2)}')
