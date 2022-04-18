
#longest word in file

def longest_words(filename):
    with open(filename, 'r') as infile:
        words = infile.read().split(' ')
    max_len = len(max(words, key=len))
    return [word for word in words if len(word) == max_len]

print(longest_words('a.txt'))


#calculator error handling

class FormulaError(Exception):
    def __init__(self, msg):
        self.msg=msg


def calculat():
    expr = input("Enter the expression: ")
    keep_going= True
    if expr == "quit":
        exit()
    while keep_going:
        strArg = expr.split(" ")
        try:
            if (len(strArg) < 3):
                raise (FormulaError("Invalid expression"))
            if strArg[1] != '+' and strArg[1] != '-':
                raise (FormulaError("Invalid operation"))

            a = float(strArg[0])
            b = float(strArg[2])

            if strArg[1] == '+':
                print(int(strArg[0]) + int(strArg[2]))
            if strArg[1] == '-':
                print(int(strArg[0]) - int(strArg[2]))

        except FormulaError as error:
            print("Error occured: ", error.msg)
        except ValueError as error:
            print("Error occured: ", error.msg)
        finally:
            calculat()

calculat()


