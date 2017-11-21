#5) Write a program that accepts a sequence of lines as input and prints the lines after making all characters in the sentence capitalized.
class Capitalized:
    def insert_the_string(self):
        first = raw_input('Enter the First String\n')
        self.upper_the_string(first)
    def upper_the_string(self,first):
        first = first.upper()
        print 'The first string are-',first
n = Capitalized()
n.insert_the_string()