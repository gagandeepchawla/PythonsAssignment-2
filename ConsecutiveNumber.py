# Write a python program to find the maximum consecutive sum of integers in a list
class ConsecutiveNumber:
    def __init__(self,number):
        self.number = number
        self.consective(number)
    def consective(self,range):
        list = []
        dict = {}
        while range:
            number = int(raw_input('Enter the Number'))
            # print   reasutl
            list.append(number)
            range = range - 1
        print list
        temp = 0
        for i in list:
            number = i
            temp2 = temp + number
            dict[temp2] = [str(temp) + ' ,' + str(number)]
            temp = number
        print 'The Maximum Number Consective Number',max(dict.items())
range = int(raw_input('Enter Range'))
get = ConsecutiveNumber(range)
