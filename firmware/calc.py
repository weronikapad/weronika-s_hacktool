
import math


def run(show, get_input):
    show("in order to use functions like sqrt(x) type math before \n possible functions: math.(sin/cos/tan)(x); math.sqrt(x); math.log(x, base); pow(x, y)")
    
    while True:
        
        eq = get_input()
        if eq == "esc":
            return
        
        try:
            result = eval(eq)
            show(eq + " =" + result)
        except:
            show(eq + "error")