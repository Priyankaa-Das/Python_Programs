class NamePrinter:
    def __init__(self, name):
        self.name = name

    def print(self):
        for char in self.name[:5]:
            print(char, end=" ")

nameobj = NamePrinter("Priyanka")
nameobj.print()