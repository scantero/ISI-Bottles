class Bottles:

    def verse (self, value):
        if value > 1:
            response = "\n" + str(value)
            response += " bottles of beer on the wall, "
            response += str(value)
            response += " bottles of beer.\nTake one down and pass it around, "
            response += str(value - 1)
            if value > 2:
                response += " bottles of beer on the wall.\n"
            elif value == 2:
                response += " bottle of beer on the wall.\n"
        elif value == 1:
            response = "\n1 bottle of beer on the wall, 1 bottle of beer.\n"
            response += "Take it down and pass it around, no more bottles of beer on the wall.\n"
        else: #value 0
            response = "\nNo more bottles of beer on the wall, no more bottles of beer.\n"
            response += "Go to the store and buy some more, 99 bottles of beer on the wall.\n"
        return response

    def verses(self, value1, value2):
        response = ""
        lis = range(value2, value1+1)
        for i in reversed(lis):
            response += self.verse(i)
        return response
