

class symbolTable:

    def __init__(self):
        self.symbols = []
        self.specialWords = []
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



    def getSymbol(self, index):
        return (self.symbols[index])[0]

    def insertSymbol(self, symbol):
        self.symbols.append([symbol])
        return len(self.symbols) - 1

    def verifyReservedWord(self, symbol):
        return (self.symbols.count(symbol) > 0)
