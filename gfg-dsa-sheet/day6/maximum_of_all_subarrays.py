import collections

class Solution:
    def maximum_of_all_sub_arrays(self, arr, k):
        maximum_arr = []
        myDeque = collections.deque([])

        for i in range(len(arr)):
            if myDeque and myDeque[0] == i - k :
                myDeque.popleft()

            while myDeque and arr[myDeque[-1]] < arr[i]:
                myDeque.pop()

            myDeque.append(i)

            if i >= k - 1:
                maximum_arr.append(arr[myDeque[0]])

        return maximum_arr


# arr = [1, 2, 3, 1, 4, 5, 2, 3, 6]
# arr = [1909, 1209, 1758, 1221, 1588, 1422 1946 1506 1030 1413 1168 1900 1591 1762 1655 1410 1359 1624 1537 1548 1483 1595 1041 1602 1350 1291 1836 1374 1020 1596 1021 1348 1199 1668 1484 1281 1734 1053 1999 1418 1938 1900 1788 1127 1467 1728 1893 1648 1483 1807 1421 1310 1617 1813 1514 1309 1616 1935 1451 1600 1249 1519 1556 1798 1303 1224 1008 1844 1609 1989 1702 1195 1485 1093 1343 1523 1587 1314 1503 1448 1200 1458 1618 1580 1796 1798 1281 1589 1798 1009 1157 1472 1622 1538 1292 1038 1179 1190 1657 1958 1191 1815 1888 1156 1511 1202 1634 1272 1055 1328 1646 1362 1886 1875 1433 1869 1142 1844 1416 1881 1998 1322 1651 1021 1699 1557 1476 1892 1389 1075 1712 1600 1510 1003 1869 1861 1688 1401 1789 1255 1423 1002 1585 1182 1285 1088 1426 1617 1757 1832 1932 1169 1154 1721 1189 1976 1329 1368 1692 1425 1555 1434 1549 1441 1512 1145 1060 1718 1753 1139 1423 1279 1996 1687 1529 1549 1437 1866 1949 1193 1195 1297 1416]
arr = [1909, 1209, 1758, 1221, 1588, 1422, 1946, 1999, 1506, 1030, 1413, 1168, 1900, 1591, 1762, 1655, 1410, 1359, 1624, 1537]
# k = 3
k = 12
obj = Solution()
maximum_array = obj.maximum_of_all_sub_arrays(arr, k)
print(maximum_array)


# here we need to find the maximum number from each sub set.
# number of elements in a sub set is passing into a variable named "k".
# here we are implementing a method named "nge" or "next greater element".
# to do that we are using deque. Now what is a deque ? Well a deque is a queue where we can add and remove items from both the front and end.
# in a normal queue we can only add element at the end and remove from the front, but deque has the ability to do both from both the end.
# to do this problem in optimal time, we need this.
# so here on every iteration, we are removing items from the front which is equal to i - k, as we only want to check within i and i - k + 1 elements.
# after that we are removing all the elements from back one by one on which the value is greater than the current index value.
# then we enter the current index.
# and at the end we check if the index is greater than equal to the k - 1 th index, insert the 0th element in the deque into a separate array to get the maximum.


# here time complexity of the solution will be - O(n) and space complexity will be - O(k).
# as we are iterating, the time is directly dependent upon the size of the array. So the time complexity will be O(n).
# as we are using variables to store data which is directly dependent on the size of the "k", the space complexity will be O(k). ( Note : Maximum k number of elements we needed at a time in the deque )

# Video Link - https://www.youtube.com/watch?v=CZQGRp93K4k
