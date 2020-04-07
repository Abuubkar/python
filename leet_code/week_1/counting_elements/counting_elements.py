"""
Authors
---------
Primary: Abubakar Khawaja

Description: 
----------
Given an integer array arr, count element x such that 
x + 1 is also in arr.
If there're duplicates in arr, counts them also.

"""

# Imports
from collections import defaultdict


class Solution:
    arr = []

    def set_arr(self, arr: [int]):
        self.arr = arr.copy()
        return len(self.arr)

    def countElements(self):
        """
        This function takes array of integers and sorts them in descending order.
        And initializes dictionary based on element of array to zero if encountered first time,
        and then checks if parent key exists in dictionary if so increments by one,
        in the dictionary having key as its element
        and prints sum of values in dictionary.
        """

        # Step 1: Defining dictionary with default value type of int
        dic = defaultdict(int)

        # Step 2: Traversing list in sorted(Descending) manner
        for element in sorted(self.arr, reverse=True):

            # Step 3: Initializing dictionary with element of array as key
            #         When encountered First time
            if element not in dic:
                dic[element] = 0

            # Step 4: Checking if element+1 key is present in dictionary
            #         If so then adding 1 to element 1 dictionary
            if element+1 in dic:
                dic[element] += 1

        # Step 5: adding all the values in dictionary to get total count of
        #         values present
        # print (sum(dic.values()))
        return (sum(dic.values()))

# Providing call to count element with array of integer as parameter
#solution = Solution()
#solution.set_arr([1, 3, 2, 3, 5, 0])
# solution.countElements()
