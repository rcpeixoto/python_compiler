
import symbol_table as symbolTable
import tolkens as tolkens
import string

class lexicalAnalyzer:

    def __init__(self, filePath):
        self.file = filePath
        self.symbolTable = symbolTable()
        self.tolkens = tolkens()
        self.states = ['initial_state','identifier']
        self.currentState = 'initial_state'

        self.letters = list(string.ascii_letters)
        self.digits = list(string.digits)
        self.ponctuation = list(string.punctuation)

    def parse(self):
        f = open(self.file)
        lines = f.readlines()
        for line in lines:
            #Creates Symbol List for the line to be read
            symbol = ''
            for char in line:
                if char in self.letters and self.currentState is self.states[0]:
                    self.currentState = self.states[1]
                    symbol = symbol + char
                elif char in self.digits or char is '-':
                    if self.currentState is self.states[1]:
                        symbol = symbol + char
                elif char is '_':
                    if self.currentState is self.states[1]:
                        symbol = symbol + char
                elif char in self.ponctuation:
                    if self.currentState is self.states[1]:
                        if self.symbolTable.verifyReservedWord(symbol):
                            self.tolkens.createTolken(symbol)
                        else:
                            index = self.symbolTable.insertSymbol(symbol)
                            self.tolkens.createTolken(symbol, index)
                        symbol = ''
        f.close()

 