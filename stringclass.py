#2) Define a class which has at least two methods one to get a string from console input and another to print the string in upper case.
class Stringclass:
    def insert_the_string(self):
        first = raw_input('Enter the First String\n')
        second = raw_input('Enter Second th Second String\n')
        self.upper(first,second)
    def upper_the_string(self,first,second):
        first = first.upper()
        print 'The first string are-',first
        second = second.upper()
        print 'The second String are -',second
n= Stringclass()
n.insert()


