# put your python code here
def multiply(a, b=1, *args):
    a *= b
    for i in args:
        a *= i
    return a