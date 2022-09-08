
from curses.ascii import isspace
from symbol_table import symbolTable
from tolkens import tolkens
import string

class lexicalAnalyzer:

    def __init__(self, filePath):
        self.file = filePath
        self.symbolTable = symbolTable()
        self.tolkens = tolkens()
        self.states = ['initial_state','identifier', 'digit', 'float_digit', 'ponctuation_symbol', 'dash']
        self.currentState = self.states[0]
        
        self.letters = list(string.ascii_letters)
        self.digits = list(string.digits)
        self.ponctuation = list(string.punctuation)

    def parse(self):
        f = open(self.file)
        lines = f.readlines()
        for line in lines:
            #Creates Symbol List for the line to be read
            symbol = ''
            line = line + '\n'
            for i in range(0, len(line) - 1):
                if line[i] in self.letters:
                    #Starts reading a identifier, begining with a letter
                    if self.currentState is self.states[0] or self.currentState is self.states[1]:
                        self.currentState = self.states[1]
                        symbol = symbol + line[i]

                    #Reading digit then finds a letter
                    #Finish reading and saves tolken
                    elif self.currentState is self.states[2] or self.currentState is self.states[3]:
                        self.tolkens.createTolken('NRO', self.symbolTable.insertSymbol(symbol))
                        symbol = ''
                        #Read Letter starts Identifier reading
                        self.currentState = self.states[1]
                        symbol = symbol + line[i]



                #Reads a digit
                elif line[i] in self.digits:
                    #if the digit read is in initial_state, then it must be a number
                    if self.currentState is self.states[0]:
                        self.currentState = self.states[2]
                        symbol = symbol + line[i]

                    #if not, it can be anything TEMPORALY
                    else:
                        symbol= symbol + line[i]


                elif line[i].isspace():
                    if self.currentState is self.states[2] or self.currentState is self.states[3]:
                        self.tolkens.createTolken('NRO', self.symbolTable.insertSymbol(symbol))
                        symbol = ''
                    elif self.currentState is self.states[5]:
                        symbol = symbol + line[i]
                    elif self.currentState is self.states[1]:
                        if self.symbolTable.verifyReservedWord(symbol):
                            self.tolkens.createTolken('PRE', self.symbolTable.insertSymbol(symbol))
                        else:
                            self.tolkens.createTolken('IDE', self.symbolTable.insertSymbol(symbol))
                        symbol = ''
                        #Reads a symbol after identifier
                    self.currentState = self.states[0]

                elif line[i] is '\n' or line[i] is '\t':
                    if self.currentState is self.states[1]:
                        if self.symbolTable.verifyReservedWord(symbol):
                            self.tolkens.createTolken('PRE', self.symbolTable.insertSymbol(symbol))
                        else:
                            self.tolkens.createTolken('IDE', self.symbolTable.insertSymbol(symbol))
                    elif self.currentState is self.states[2] or self.currentState is self.states[3]:
                        self.tolkens.createTolken('NRO', self.symbolTable.insertSymbol(symbol))
                    self.currentState = self.states[0]


                        
                #Reads a ponctuation symbol
                elif line[i] in self.ponctuation:
                    #Reading a Identifier, then finds a ponctuation symbol which is not "_"
                    #Finish reading and save tolken
                    if self.currentState is self.states[1] and line[i] is not '_':
                        #Verifies whether the tolken represents a Reserved word
                        if self.symbolTable.verifyReservedWord(symbol):
                            self.tolkens.createTolken('PRE', self.symbolTable.insertSymbol(symbol))
                        else:
                            self.tolkens.createTolken('IDE', self.symbolTable.insertSymbol(symbol))
                        symbol = ''
                        #Reads a symbol after identifier
                        self.currentState = self.states[4]
                        symbol = symbol + line[i]

                    #Reading a float digit, then finds a ponctuation symbol
                    #Saves tolken
                    elif self.currentState is self.states[3]:
                        self.tolkens.createTolken('NRO', self.symbolTable.insertSymbol(symbol))
                        symbol = ''
                        #Reads a symbol after identifier
                        self.currentState = self.states[4]
                        symbol = symbol + line[i]

                    #Starts reading of a negative digit
                    elif line[i] is '-':
                        if self.currentState is self.states[0]:
                            self.currentState = self.states[5]
                            symbol = symbol + line[i]

                    #Starts reading of a '.'
                    elif line[i] is '.':
                        #if the reading is current in a digit, the '.' is seen as a float point divisor
                        if self.currentState is self.states[2]:
                            self.currentState = self.states[3]
                            symbol = symbol + line[i]

                    #starts reading of a '_'
                    elif line[i] is '_':
                        #If the reading is current in a identifier, the '_' is seen as part of the identifier
                        if self.currentState is self.states[1]:
                            symbol = symbol + line[i]

        f.close()

    def printTolkens(self):
        f = open(self.file + '-saida.txt', 'w')
        tolkens = self.tolkens.getAllTolkens()
        for tolken in tolkens:
            f.write(tolken[0] + ' ' + self.symbolTable.getSymbol(tolken[1], tolken[0]) + '\n')
        f.close()
