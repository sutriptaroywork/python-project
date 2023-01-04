class Solution:
    def stock_span(self, arr):
        span_arr = []
        my_stack = []

        for i in range(len(arr)):
            span = 1
            while my_stack and my_stack[-1]["value"] <= arr[i]:
                span += my_stack[-1]["span"]
                my_stack.pop()

            val_span = {
                "value": arr[i],
                "span": span
            }

            my_stack.append(val_span)
            span_arr.append(span)

        return span_arr


arr = [100, 80, 60, 70, 60, 75, 85]

obj = Solution()
stock_span_array = obj.stock_span(arr)
print(stock_span_array)


# here we need to find the number of consecutive days where the stock price were lower than the current.
# so basically we need to check that how many consecutive indexes have lesser number than the current index.
# here minimum 1 will be there as the current index is also countable.
# now we will use stack to do this in optimal time.
# on every iteration, the stack will be pushed the current element with it's span number.
# now how to get the span number ? Well... we will check the last item is lesser than or not on every insertion.
# until we are getting last item bigger than the current value, we will continuously removing the last item of the stack and adding the span value of those values.
# once we get the bigger last element than the current value, we will insert it with the sum of spans and will insert the sum of spans into a separate array.
# the array, where we are storing the span, will be our output array and will be returned.


# here time complexity of the solution will be - O(n) and space complexity will be - O(n).
# as we are iterating, the time is directly dependent upon the size of the array. So the time complexity will be O(n).
# as we are storing span data for every array items, space is directly dependent on the size of the array. So the space complexity will be O(n).

# Video Link - https://www.youtube.com/watch?v=XlD5VsOZsyA
