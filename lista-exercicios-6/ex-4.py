
def votação(a,b):
    t = float(a) + float(b)
    x = t * 0.7 
    if a >= x:
        return True
    else:
        return False

a = votação(10,4)
print(a)
