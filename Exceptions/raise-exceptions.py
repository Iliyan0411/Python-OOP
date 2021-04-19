
class EvenList(list):
    def append(self, integer):
        if not isinstance(integer, int):
            raise TypeError("Only integers can be added!\n")

        if integer % 2:
            raise ValueError("Only even integers can be added!\n")

        super().append(integer)


#########################

def funny_devision(num):
    '''This function returns text message if you try to devide by zero. But if the argument is
    another invalid value it returns exception message.'''
    try:
        return 100 / num
    except ZeroDivisionError:
        return "Hey, you can't devide by zero."

############################

def funny_devision2(num):
    '''This function handles ZeroDivisionError and TypeError exceptions and returns specific
    exceptions message if occurs ValueError(when argument is equal to 13).'''

    try:
        if num == 13:
            raise ValueError("13 is unlucky number")
        return 100 / num
    except ZeroDivisionError:
        return "You can't devide by zero."
    except TypeError:
        return "You must enter a number as argument."
    except ValueError as ve:
        return ve.args

############################

# else and finally blocks
import random

def f():
    some_exceptions = [ValueError, TypeError, ZeroDivisionError, None]
    choice = random.choice(some_exceptions)

    try:
        print("raising: {}".format(choice))
        if choice:
            raise choice("An error")
    except ValueError:
        print ("ValueError caught")
    except TypeError:
        print("TypeError caught")
    except Exception as ex:
        print("Caught other error type: %s" % (ex.__class__.__name__))
    else:
        print("There is not caught exceptions")
    finally:
        print("Exceptions cleaned")
