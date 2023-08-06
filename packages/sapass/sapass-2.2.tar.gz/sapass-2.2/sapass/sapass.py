import random

passType = {'mix',
            'alphabet',
            'number',
            }


class generator():
    def __init__(self):
        pass

    @classmethod
    def get_new_pass(cls, length=None, passType='mix', includeSymbol=None, includeUppercaseCharacters=None):
        if passType.__eq__('mix'):
            alphabet = "abcdefghijklmnopqrstuvwxyz"
            if includeUppercaseCharacters:
                alphabet += "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
            if includeSymbol:
                alphabet += "@#$%!^&*()_+-/|"
        elif passType.__eq__('alphabet'):
            alphabet = "abcdefghijklmnopqrstuvwxyz"
            if includeUppercaseCharacters:
                alphabet += "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        elif passType.__eq__('number'):
            alphabet = "0123456789"

        pw_length = length or 8
        mypw = ""
        for i in range(pw_length):
            next_index = random.randrange(len(alphabet))
            mypw = mypw + alphabet[next_index]

        # replace 1 or 2 characters with a number
        for i in range(random.randrange(1, 3)):
            replace_index = random.randrange(len(mypw) // 2)
            mypw = mypw[0:replace_index] + str(random.randrange(10)) + mypw[replace_index + 1:]

        # replace 1 or 2 letters with an uppercase letter
        for i in range(random.randrange(1, 3)):
            replace_index = random.randrange(len(mypw) // 2, len(mypw))
            mypw = mypw[0:replace_index] + mypw[replace_index].upper() + mypw[replace_index + 1:]

        return mypw

# pa = passgenerator().generate(length=15, includeSymbol=True, includeUppercaseCharacters=True)
