class Solution:
    def addition_without_arithmetic_operator(self, a, b):
        sum  = 0
        while b != 0:
            carry = a & b
            a = a ^ b
            b = carry << 1

        return a

# Driver code
obj = Solution()
a = 5
b = 3
res = obj.addition_without_arithmetic_operator(a, b)
print(res) 


# here we need to add two integers without using arithmetic operation.
# so to do that we need to use the binary operators.
# in binary, when we add, we place 1 if the digits on a particular position are 1 and 0 and place 0 if the digits are same on particular position.
# to achieve that, we will use XOR operator. We will store the sum into the first number.
# but in that case we skip one thing. If both are 1, we place 0 and we carry forward the one to the next position.
# to do that, we need to evaluate the carry through AND operator where if both are 1, there will be 1.
# after getting the carry value, we will perform one left shift with the carry and insert into the second number.
# we will store the carry part before performing the XOR part. Because after XOR, a becomes different and carry value becomes wrong.
# so the carry value will act as the second variable and will continue to add until it gets 0.

# here time complexity of the solution will be - O( max( no of bits in a, no of bits in b ) ) and space complexity will be - O(1).
# as we are iterating until b gets 0, it literally iterates till the number of maximum bit between a and b.
# as we are using variables to store values which are not directly dependent on the size of the array, the space complexity will be O(1).

