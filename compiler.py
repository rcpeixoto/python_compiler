from lexical_analizer import lexicalAnalyzer
import sys

def start():
    if(len(sys.argv)  != 2):
        return
    else:
        lexical = lexicalAnalyzer(sys.argv[1])
        lexical.parse()
        lexical.printTolkens()

if __name__ == '__main__':
    start()