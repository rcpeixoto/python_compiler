class tokens:

    def __init__(self):
        self.token = []

    def createtoken(self, value, line, index=''):
        entry = [value, index, line]
        self.token.append(entry)

    def removetoken(self, token):
        self.token.remove(token)

    def getAlltoken(self):
        return self.token

    def lasttoken(self):
        return (self.token[len(self.token)-1])
