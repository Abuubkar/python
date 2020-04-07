#36ms
# class Solution:
#     def isHappy(self, n: int) -> bool:
        
#         output = dict()
#         while True:
#             happy_numbers = [int(digit)**2 for digit in str(n)]
#             sum_ = sum(happy_numbers)
            
            
#             if n == 1 :
#                 return True
            
#             if sum_ == n:
#                 return False
#             n = sum_
#             if n not in output:
#                 output[n] = 0
#             else:
#                 output[n]+=1
#             if output[n] > 1:
#                 return False


class Solution: # 36ms
    def isHappy(self, n: int) -> bool:

        output = []
        while True:
            happy_numbers = [int(digit)**2 for digit in str(n)]
            sum_ = sum(happy_numbers)

            print(sum_)
            if n == 1:
                return True

            if sum_ == n:
                return False
            n = sum_
            if n in output:
                return False

            output.append(n)


print(Solution.isHappy(2))
