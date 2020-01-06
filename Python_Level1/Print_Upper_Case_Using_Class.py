class String():
    def __init__(self):
        self.string = ""

    def get_String(self):
        self.string=input("Enter the input string : ")

    def print_String(self):
        print(self.string.upper())

S = String()
S.get_String()
S.print_String()
