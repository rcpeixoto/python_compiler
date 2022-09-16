class tolkens:

    def __init__(self):
        self.tolken = []


    def createTolken(self, value, line, index=''):
        entry = [value, index, line]
        self.tolken.append(entry)
    
    def removeTolken(self, tolken):
        self.tolken.remove(tolken)

    def getAllTolkens(self):
        return self.tolken

    def lastTolken(self):
        return (self.tolken[len(self.tolken)-1])
    