from symbol_table import symbolTable
from tokens import tokens
import string

class lexicalAnalyzer:

    def __init__(self, filePath):
        self.file = filePath
        self.symbolTable = symbolTable()
        self.token = tokens()
        self.states = ['initial_state', 'identifier', 'digit', 'float_digit',
                       'ponctuation_symbol', 'negative_num', 'artih_-', 'artith_+',
                       'logical_operator', 'delimiter', 'relational_1', 'relational_2', 'digit_space',]
        self.currentState = self.states[0]
        self.letters = list(string.ascii_letters)
        self.digits = list(string.digits)
        self.ponctuation = list(string.punctuation)
        self.arithmetic = list("+-/*")
        self.logical = list("|&!")
        self.delimiters = list(";,()[]{}.")
        self.relational = list("<>=!")

    def parse(self):
        f = open(self.file)
        lines = f.readlines()
        j = 0
        for line in lines:
            j = j + 1
            # Creates Symbol List for the line to be read
            symbol = ''
            line = line + '\n'
            for i in range(0, len(line) - 1):

                if line[i] in self.letters:

                    # Starts reading a identifier, begining with a letter
                    if self.currentState is self.states[0] or self.currentState is self.states[1]:
                        self.currentState = self.states[1]
                        symbol = symbol + line[i]

                    # Reading digit then finds a letter
                    # Finish reading and saves token
                    elif self.currentState is self.states[2] or self.currentState is self.states[3]:
                        # ERROR
                        a = 1
                    elif self.currentState is self.states[6]:
                        self.token.createTolken(
                            'ART', j, self.symbolTable.insertSymbol(symbol.strip()))
                        symbol = ''
                        self.currentState = self.states[1]
                        symbol = symbol + line[i]

                # Reads a digit
                elif line[i] in self.digits:
                    # if the digit read is in initial_state, then it must be a number
                    if self.currentState is self.states[0] or self.currentState is self.states[5]:
                        self.currentState = self.states[2]
                        symbol = symbol + line[i]
                    elif self.currentState is self.states[6]:
                        self.currentState = self.states[2]
                        symbol = symbol + line[i]
                    # if not, it can be anything TEMPORALY
                    else:
                        symbol = symbol + line[i]

                elif line[i].isspace():
                    if self.currentState is self.states[2] or self.currentState is self.states[3]:
                        if symbol[0] is '-' and self.token.lastTolken()[0] is 'NRO' and self.token.lastTolken()[2] == j:
                            symbol_1 = symbol[0]
                            symbol_2 = symbol[1:]
                            self.token.createTolken(
                                'ART', j, self.symbolTable.insertSymbol(symbol_1))
                            self.token.createTolken(
                                'NRO', j, self.symbolTable.insertSymbol(symbol_2))
                        else:
                            self.token.createTolken(
                                'NRO', j, self.symbolTable.insertSymbol(symbol))
                        symbol = ''
                        self.currentState = self.states[0]
                    elif self.currentState is self.states[1]:
                        if self.symbolTable.verifyReservedWord(symbol):
                            self.token.createTolken(
                                'PRE', j, self.symbolTable.insertSymbol(symbol))
                        else:
                            self.token.createTolken(
                                'IDE', j, self.symbolTable.insertSymbol(symbol))
                        symbol = ''
                        self.currentState = self.states[0]
                        # Reads a symbol after identifier
                    elif self.currentState is self.states[7]:
                        self.token.createTolken(
                            'ART', j, self.symbolTable.insertSymbol(symbol))
                        symbol = ''
                    elif self.currentState is self.states[8]:
                        self.tokens.createToken(
                            'LOG', self.symbolTable.insertSymbol(symbol))
                        symbol = ''
                    elif self.currentState is self.states[9]:
                        self.tokens.createToken(
                            'DEL', self.symbolTable.insertSymbol(symbol))
                        symbol = ''
                        self.currentState = self.states[0]

                elif line[i] is '\n' or line[i] is '\t':
                    if self.currentState is self.states[1]:
                        if self.symbolTable.verifyReservedWord(symbol):
                            self.token.createTolken(
                                'PRE', j, self.symbolTable.insertSymbol(symbol))
                        else:
                            self.token.createTolken(
                                'IDE', j, self.symbolTable.insertSymbol(symbol))
                    elif self.currentState is self.states[2] or self.currentState is self.states[3]:
                        if symbol[0] is '-' and self.token.lastTolken()[0] is 'NRO' or self.token.lasttoken()[2] is j:
                            symbol_1 = symbol[0]
                            symbol_2 = symbol[1:]
                            self.token.createTolken(
                                'ART', j, self.symbolTable.insertSymbol(symbol_1))
                            self.token.createTolken(
                                'NRO', j, self.symbolTable.insertSymbol(symbol_2))
                    elif self.currentState is self.states[8]:
                        self.tokens.createToken(
                            'LOG', self.symbolTable.insertSymbol(symbol))
                        symbol = ''
                    elif self.currentState is self.states[9]:
                        self.tokens.createToken(
                            'DEL', self.symbolTable.insertSymbol(symbol))
                        symbol = ''
                    self.currentState = self.states[0]

                # Reads a ponctuation symbol
                elif line[i] in self.ponctuation:

                    if (self.currentState is self.states[2] or self.currentState is self.states[3]) and line[i] is not '.':
                        if symbol[0] is '-' and self.token.lastTolken()[0] is 'NRO' or self.token.lasttoken()[2] is j:
                            symbol_1 = symbol[0]
                            symbol_2 = symbol[1:]
                            self.token.createTolken(
                                'ART', j, self.symbolTable.insertSymbol(symbol_1))
                            self.token.createTolken(
                                'NRO', j, self.symbolTable.insertSymbol(symbol_2))
                        else:
                            self.token.createTolken(
                                'NRO', j, self.symbolTable.insertSymbol(symbol))
                        symbol = ''
                        self.currentState = self.states[0]

                    # Reading a Identifier, then finds a ponctuation symbol which is not "_"
                    # Finish reading and save tolken
                    if self.currentState is self.states[1] and line[i] is not '_':
                        # Verifies whether the tolken represents a Reserved word
                        if self.symbolTable.verifyReservedWord(symbol):
                            self.token.createTolken(
                                'PRE', j, self.symbolTable.insertSymbol(symbol))
                        else:
                            self.token.createTolken(
                                'IDE', j, self.symbolTable.insertSymbol(symbol))
                        symbol = ''
                        # Reads a symbol after identifier
                        self.currentState = self.states[0]

                    # Starts reading of a '.'
                    if line[i] is '.':
                        # if the reading is current in a digit, the '.' is seen as a float point divisor
                        if self.currentState is self.states[2]:
                            self.currentState = self.states[3]
                            symbol = symbol + line[i]

                    # starts reading of a '_'
                    elif line[i] is '_':
                        # If the reading is current in a identifier, the '_' is seen as part of the identifier
                        if self.currentState is self.states[1]:
                            symbol = symbol + line[i]

                    elif line[i] in self.arithmetic:
                        if self.currentState is self.states[0] and line[i] is '+':
                            self.currentState = self.states[7]
                            symbol = symbol + line[i]
                        elif self.currentState is self.states[0] and line[i] is '-':
                            self.currentState = self.states[6]
                            symbol = symbol + line[i]
                        elif (self.currentState is self.states[6] and line[i] is '+') or (self.currentState is self.states[7] and line[i] is '-'):
                            self.token.createTolken(
                                'ART', j, self.symbolTable.insertSymbol(symbol.strip()))
                            symbol = line[i]
                            self.token.createTolken(
                                'ART', j, self.symbolTable.insertSymbol(symbol.strip()))
                            symbol = ''
                            self.currentState = self.states[0]
                        elif (self.currentState is self.states[6] and line[i] is '-') or (self.currentState is self.states[7] and line[i] is '+'):

                            symbol = symbol + line[i]
                            self.token.createTolken(
                                'ART', j, self.symbolTable.insertSymbol(symbol.strip()))
                            symbol = ''
                            self.currentState = self.states[0]

                        else:
                            if symbol.strip() is '-':
                                self.token.createTolken(
                                    'ART', j, self.symbolTable.insertSymbol(symbol.strip()))
                            symbol = line[i]
                            self.token.createTolken(
                                'ART', j, self.symbolTable.insertSymbol(symbol.strip()))
                            symbol = ''
                            self.currentState = self.states[0]

                    elif line[i] in self.relational:
                        if self.currentState is self.states[0]:
                            self.currentState = self.states[10]
                            symbol = symbol + line[i]

                    elif line[i] in self.logical:
                        if self.currentState is self.states[0]:
                            self.currentState = self.states[8]
                            symbol = symbol + line[i]
                        if self.currentState is self.states[8] and ((line[i] is "&" and symbol is "&") or (line[i] is "|" and symbol is "|")):
                            symbol = symbol + line[i]

                    elif line[i] in self.delimiters:
                        if self.currentState is self.states[0]:
                            self.currentState = self.states[9]
                            symbol = symbol + line[i]
        f.close()

    def printar(self):
        print(self.ponctuation)

    def printtokens(self):
        f = open(self.file + '-saida.txt', 'w')
        token = self.token.getAlltoken()
        for tolken in token:
            f.write(str(tolken[2]) + ' ' + tolken[0] + ' ' +
                    self.symbolTable.getSymbol(tolken[1], tolken[0]) + '\n')
        f.close()


if __name__ == '__main__':
    lexicalAnalyzer = lexicalAnalyzer("./file/entrada.txt")
    lexicalAnalyzer.printar()
