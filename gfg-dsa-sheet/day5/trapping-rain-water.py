class Solution:
    def trapping_rain_water(self, arr):
        leftHighest = []
        rightHighest = []
        maxTillNow = -1
        trappedWaterBlocks = 0

        for i in range(len(arr)):
            maxTillNow = max(maxTillNow, arr[i])
            leftHighest.append(max(maxTillNow, arr[i]))

        maxTillNow = -1

        for i in reversed(range(len(arr))):
            maxTillNow = max(maxTillNow, arr[i])
            rightHighest.append(max(maxTillNow, arr[i]))

        for i in range(len(arr)):
            trappedWaterBlocks += min(leftHighest[i], rightHighest[i]) - arr[i]

        return trappedWaterBlocks


arr = [3,0,0,2,0,4]
obj = Solution()
no_of_blocks_of_water = obj.trapping_rain_water(arr)
print(no_of_blocks_of_water)


# here we need to find the number of units rain water can be trapped by the given array of blocks.
# so the main concept here is to get the highest left block till now vs highest right block till now.
# get the minimum number between left highest and right highest and subtract the current index value from that.
# so first we need to iterate the array two times to make the left highest and right highest arrays.
# after that we need to iterate and compare and subtract.


# here time complexity of the solution will be - O(n) and space complexity will be - O(n).
# as we are iterating, the time is directly dependent upon the size of the array. So the time complexity will be O(n).
# as we are using variables to store data which is directly dependent on the size of the array, the space complexity will be O(n).

# Video Link - https://www.youtube.com/watch?v=UZG3-vZlFM4
