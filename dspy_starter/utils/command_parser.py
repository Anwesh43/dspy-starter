import sys


class CommandParser:
    def __init__(self):
        self.arguments = sys.argv

    def isEnoughArgs(self):
        return len(self.arguments) > 1

    def getSentence(self):
        return " ".join(self.arguments[1:])
