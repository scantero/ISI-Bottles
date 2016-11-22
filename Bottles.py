class Bottles:

    def verse (self, value):
        response = "\n" + str(value)
        if value > 1:
            response += " bottles of beer on the wall, "
            response += str(value)
            response += " bottles of beer.\nTake one down and pass it around, "
            response += str(value - 1)
            if value > 2:
                response += " bottles of beer on the wall.\n"
            elif value == 2:
                response += " bottle of beer on the wall.\n"
        else:
            response += " bottle of beer on the wall, "
            response += str(value)
            response += " bottle of beer.\nTake it down and pass it around, "
            response += "no more bottles of beer on the wall."
        return response
