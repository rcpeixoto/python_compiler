class symbolTable:

    def __init__(self):
        self.symbols = []
        self.reserverWords = {
            "var": "var",
            "const": "const",
            "struct": "struct",
            "extends": "extends",
            "procedure": "procedure",
            "function": "function",
            "start": "start",
            "return": "return",
            "if": "if",
            "else": "else",
            "then": "then",
            "while": "while",
            "read": "read",
            "print": "print",
            "int": "int",
            "real": "real",
            "boolean": "boolean",
            "string": "string",
            "true": "true",
            "false": "false",
        }

    def getSymbol(self, index, type):
        if type is 'PRE':
            return (self.reserverWords[index])
        else:
            return (self.symbols[index])

    def insertSymbol(self, symbol):
        if symbol in self.reserverWords.keys():
            return self.reserverWords[symbol]
        elif (self.symbols.count(symbol) > 0):
            return self.symbols.index(symbol)
        else:
            self.symbols.append(symbol)
            return self.symbols.index(symbol)

    def verifyReservedWord(self, symbol):
        return symbol in self.reserverWords.keys()
