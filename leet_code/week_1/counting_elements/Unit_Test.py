import unittest
import counting_elements as CE


class Test(unittest.TestCase):
    arr = []
    solution = CE.Solution()

    def test_0_input(self):
        """
        Any method that starts with test_ will cosist of test case
        """

        print("\nstart input test\n")

        with open('input.txt', 'r') as file:
            input_list = file.readlines()

            for i in range(len(input_list)):
                self.arr = list(map(int, input_list[i].strip().split(',')))
                # get the length of arr obtained from the function
                length = self.solution.set_arr(self.arr)

                # check if the obtained user id is null or not
                # length <= 1  will fail the test
                self.assertGreater(length, -1)

                for value in self.arr:

                    # will fail if value in arr is greater than 1000
                    self.assertGreater(1000, value)

                    # will fail if value in arr is greater than 1000
                    self.assertGreater(value, 0)

                print("arr length =", length)
                print(self.arr)
                self.test_1_countElements()


def test_1_countElements(self):
    print("\nstart countElement Test\n")
    # getting the count of element from function

    result = self.solution.countElements()
    # Will fail if result has value less than 0
    self.assertGreater(result, -1)
    print("countElements = ", result)
    print("\nFinished countElement Test\n")
    print("\nFinished set_arr test\n")


if __name__ == '__main__':
    # begin unittest.main()
    unittest.main()
