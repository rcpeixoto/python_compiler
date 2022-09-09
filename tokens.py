class tokens:

    def __init__(self):
        self.token = []

    def createToken(self, value, index=''):
        entry = (value, index)
        self.token.append(entry)

    def removeToken(self, token):
        self.token.remove(token)

    def getAllTokens(self):
        return self.token
