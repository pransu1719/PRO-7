import math

def factorial(n):
    return mathfactorial(n)

def compound_interest(p,r,t):
    amount = p*((1+r/100)**t)
    return round(amount,2)

def trig_values(angle):
    a= math.radians(angle)
    return{
        "sin": round(math.sin(a), 4),
        "cos": round(math.cos(a), 4),
        "tan": round(math.tan(a), 4),
          }
def area_circle(r):
    return round(math.pi*r*r*r, 2)

def area_rectangle(l, w):
    return round(l*w, 2)
