#Given a number n, return True if n is in the range 1..10, inclusive. Unless outside_mode is True, in which case return True if the number is less or equal to 1, or greater or equal to 10.
class Number:
    def insert(self):
        status = int(raw_input('choose status 1 for True and 2 for False \n'))
        second = int(raw_input('Enter Number\n'))
        if status == 1:
            status_bol = True
        if status ==2:
            status_bol = False
        self.check(status_bol,second)
    def check(self,number1,number2):
        if number1 == False:
            if number2 in range(1,10):
                print 'True'
            else:
                print 'False'
        else:
            if number2 in range(1, 10):
                print 'True'
            else:
                print 'False'
n = Number()
n.insert()