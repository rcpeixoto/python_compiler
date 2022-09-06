class tolkens:

    def __init__(self):
        self.tolken = []


    def createTolken(self, value, index=''):
        entry = (value, index)
        self.tolken.append(entry)
    
    def removeTolken(self, tolken):
        self.tolken.remove(tolken)

    