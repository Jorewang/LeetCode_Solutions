class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        len1 = len(nums1)
        len2 = len(nums2)
        length = len1 + len2
        count = (length + 1)//2
        i = j = 0
        while count > 1:
            if i < len1 and j < len2:
                if nums1[i] > nums2[j]:
                    j += 1
                else:
                    i += 1
            elif i < len1:
                i += 1
            else:
                j += 1
            count -= 1
        if i < len1 and j < len2:
            if nums1[i] > nums2[j]:
                value1 = nums2[j]
                j += 1
            else:
                value1 = nums1[i]
                i += 1
            if length % 2 == 0:
                if i < len1 and j < len2:
                    if nums1[i] > nums2[j]:
                        value2 = nums2[j]
                    else:
                        value2 = nums1[i]
                    return (value1 + value2)/2
                elif i < len1:
                    value2 = nums1[i]
                    return (value1 + value2)/2
                else:
                    value2 = nums2[j]
                    return (value1 + value2)/2
            else:
                return value1

        elif i < len1:
            if length % 2 == 0:
                return (nums1[i] + nums1[i+1])/2
            else:
                return nums1[i]
        else:
            if length % 2 == 0:
                return (nums2[j] + nums2[j+1])/2
            else:
                return nums2[j]


if __name__ == '__main__':
    c = Solution()
    nums1 = [1, 3, 4, 9]
    nums2 = [2]
    print(c.findMedianSortedArrays(nums1, nums2))
