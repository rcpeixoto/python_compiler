class symbolTable:

    def __init__(self):
        self.symbols = []
        self.specialWords = []
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
        self.specialWords.append("var")
        self.specialWords.append("const")
        self.specialWords.append("struct")
        self.specialWords.append("extends")
        self.specialWords.append("procedure")
        self.specialWords.append("function")
        self.specialWords.append("start")
        self.specialWords.append("return")
        self.specialWords.append("if")
        self.specialWords.append("else")
        self.specialWords.append("then")
        self.specialWords.append("while")
        self.specialWords.append("read")
        self.specialWords.append("print")
        self.specialWords.append("int")
        self.specialWords.append("real")
        self.specialWords.append("boolean")
        self.specialWords.append("string")
        self.specialWords.append("true")
        self.specialWords.append("false")

    def getSymbol(self, index, type):
        if type is 'PRE':
            return (self.specialWords[index])
        else:
            return (self.symbols[index])

    def insertSymbol(self, symbol):
        if (self.specialWords.count(symbol) > 0):
            return self.specialWords.index(symbol)
        elif (self.symbols.count(symbol) > 0):
            return self.symbols.index(symbol)
        else:
            self.symbols.append(symbol)
            return self.symbols.index(symbol)

    def verifyReservedWord(self, symbol):
        return (self.specialWords.count(symbol) > 0)
