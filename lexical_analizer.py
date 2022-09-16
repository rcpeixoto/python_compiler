

from symbol_table import symbolTable
from tokens import tokens
import string


class lexicalAnalyzer:

    def __init__(self, filePath):
        self.file = filePath
        self.symbolTable = symbolTable()
        self.tokens = tokens()
        self.states = ['initial_state', 'identifier', 'digit',
                       'float_digit', 'ponctuation_symbol', 'dash', 'logical_operator']
        self.currentState = self.states[0]

        self.letters = list(string.ascii_letters)
        self.digits = list(string.digits)
        self.ponctuation = list(string.punctuation)

    def parse(self):
        f = open(self.file)
        lines = f.readlines()
        for line in lines:
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
                        self.tokens.createtoken(
                            'NRO', self.symbolTable.insertSymbol(symbol))
                        symbol = ''
                        # Read Letter starts Identifier reading
                        self.currentState = self.states[1]
                        symbol = symbol + line[i]

                # Reads a digit
                elif line[i] in self.digits:
                    # if the digit read is in initial_state, then it must be a number
                    if self.currentState is self.states[0]:
                        self.currentState = self.states[2]
                        symbol = symbol + line[i]

                    # if not, it can be anything TEMPORALY
                    else:
                        symbol = symbol + line[i]

                elif line[i].isspace():
                    if self.currentState is self.states[2] or self.currentState is self.states[3]:
                        self.tokens.createtoken(
                            'NRO', self.symbolTable.insertSymbol(symbol))
                        symbol = ''
                    elif self.currentState is self.states[5]:
                        symbol = symbol + line[i]
                    elif self.currentState is self.states[1]:
                        if self.symbolTable.verifyReservedWord(symbol):
                            self.tokens.createtoken(
                                'PRE', self.symbolTable.insertSymbol(symbol))
                        else:
                            self.tokens.createtoken(
                                'IDE', self.symbolTable.insertSymbol(symbol))
                        symbol = ''
                    elif self.currentState is self.states[6]:
                        self.tokens.createToken('LOG', self.symbolTable.insertSymbol(symbol))
                        symbol = ''
                        # Reads a symbol after identifier
                    self.currentState = self.states[0]

                elif line[i] == '\n' or line[i] == '\t':
                    if self.currentState is self.states[1]:
                        if self.symbolTable.verifyReservedWord(symbol):
                            self.tokens.createtoken(
                                'PRE', self.symbolTable.insertSymbol(symbol))
                        else:
                            self.tokens.createtoken(
                                'IDE', self.symbolTable.insertSymbol(symbol))
                    elif self.currentState is self.states[2] or self.currentState is self.states[3]:
                        self.tokens.createtoken(
                            'NRO', self.symbolTable.insertSymbol(symbol))
                    elif self.currentState is self.states[6]:
                        self.tokens.createToken('LOG', self.symbolTable.insertSymbol(symbol))
                        symbol = ''
                    self.currentState = self.states[0]

                # Reads a ponctuation symbol
                elif line[i] in self.ponctuation:
                    # Reading a Identifier, then finds a ponctuation symbol which is not "_"
                    # Finish reading and save token
                    if self.currentState == self.states[1] and line[i] != '_':
                        # Verifies whether the token represents a Reserved word
                        if self.symbolTable.verifyReservedWord(symbol):
                            self.tokens.createtoken(
                                'PRE', self.symbolTable.insertSymbol(symbol))
                        else:
                            self.tokens.createtoken(
                                'IDE', self.symbolTable.insertSymbol(symbol))
                        symbol = ''
                        # Reads a symbol after identifier
                        self.currentState = self.states[4]
                        symbol = symbol + line[i]

                    # Reading a float digit, then finds a ponctuation symbol
                    # Saves token
                    elif self.currentState == self.states[3]:
                        self.tokens.createtoken(
                            'NRO', self.symbolTable.insertSymbol(symbol))
                        symbol = ''
                        # Reads a symbol after identifier
                        self.currentState = self.states[4]
                        symbol = symbol + line[i]

                    # Starts reading of a negative digit
                    elif line[i] == '-':
                        if self.currentState == self.states[0]:
                            self.currentState = self.states[5]
                            symbol = symbol + line[i]

                    # Starts reading of a '.'
                    elif line[i] == '.':
                        # if the reading is current in a digit, the '.' is seen as a float point divisor
                        if self.currentState == self.states[2]:
                            self.currentState = self.states[3]
                            symbol = symbol + line[i]

                    # starts reading of a '_'
                    elif line[i] == '_':
                        # If the reading is current in a identifier, the '_' is seen as part of the identifier
                        if self.currentState == self.states[1]:
                            symbol = symbol + line[i]

                elif line[i] is "!" or line[i] is "&" or line[i] is "|": 
                    if self.currentState == self.states[0]:
                        self.currentState = self.states[6]
                        symbol = symbol + line[i]
                    if self.currentState == self.states[6] and ((line[i] is "&" and symbol == "&") or (line[i] is "|" and symbol == "|")):
                        symbol = symbol + line[i]
        f.close()
        
    def printar(self):
        print(self.ponctuation)
    
    def printtokens(self):
        f = open(self.file + '-saida.txt', 'w')
        tokens = self.tokens.getAlltokens()
        for token in tokens:
            f.write(
                token[0] + ' ' + self.symbolTable.getSymbol(token[1], token[0]) + '\n')
        f.close()

if __name__ == '__main__':
    lexicalAnalyzer = lexicalAnalyzer("C:\Python27")
    lexicalAnalyzer.printar()