# Given 2 ints, a and b, return their sum. However, sums in the range 10..19 inclusive, are forbidden, so in that case just return 20.
class TwoNumberSum:
    def sum_the_number(self,number1, number2):
        add = number1 + number2
        return add
    def check_the_number(self,number1, number2):
        check = self.sum_the_number(number1, number2)
        if check in range(10, 19):
            print 20
        else:
            print check
    def insert_number(self):
        first = int(raw_input("Enter the First Number\n"))
        second = int(raw_input("Enter the second Number\n"))
        self.check_the_number(first, second)
number = TwoNumberSum()
number.insert_number()
