class Bottles:

    def verse (self, value):
        response = "\n" + str(value)
        response += " bottles of beer on the wall, "
        response += str(value)
        response += " bottles of beer.\nTake one down and pass it around, "
        response += str(value - 1)
        if value > 2:
            response += " bottles of beer on the wall.\n"
        else:
            response += " bottle of beer on the wall.\n"
        return response
