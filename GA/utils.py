def convert_to_tuple(list):
    return tuple(list)

def checkNumber(val):
    if isinstance(val, (int, float)):
        # number only
        return True;
    else:
        raise Exception("Sorry, you have entered wrong index!")