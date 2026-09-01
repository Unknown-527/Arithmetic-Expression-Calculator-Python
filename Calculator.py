def main():
    expressionl=[]
    a=input("Enter expression, seperate the numbers and operators by spaces: ")
    for i in a.split():
        try:
            expressionl.append(float(i))
        except:
            expressionl.append(i)
    ch=input("Enter A for BODMAS or B for PEMDAS: ")
    try:
        if ch.lower()=="a":
            bodmas(expressionl)
        elif ch.lower()=="b":
            pemdas(expressionl)
        else:
            print("Wrong Choice")
    except:
            print("Error, you did something ")
        
def bodmas(n):
    n=of(n)
    n=div(n)
    n=pro(n)
    n=addit(n)
    n=subit(n)
    print("Result: ",float(n))

def pemdas(n):
    n=exp(n)
    n=pro(n)
    n=div(n)
    n=addit(n)
    n=subit(n)
    print("Result: ",float(n))
            
def div(n):
    print("div")
    while "/" in n:
            a=n[n.index("/")-1]/n[n.index("/")+1]
            n.insert(n.index("/")-1,a)
            n.pop(n.index("/")-1)
            n.pop(n.index("/")+1)
            n.pop(n.index("/"))
            print (n)
    return n
def pro(n):
    print("pro")
    while "*" in n:
            a=n[n.index("*")-1]*n[n.index("*")+1]
            n.insert(n.index("*")-1,a)
            n.pop(n.index("*")-1)
            n.pop(n.index("*")+1)
            n.pop(n.index("*"))
            print (n)
    return n

def addit(n):
    print("addit")
    while "+" in n:
            a=n[n.index("+")-1]+n[n.index("+")+1]
            n.insert(n.index("+")-1,a)
            n.pop(n.index("+")-1)
            n.pop(n.index("+")+1)
            n.pop(n.index("+"))
            print (n)
    return n

def subit(n):
    print("subit")
    while "-" in n:
            a=n[n.index("-")-1]-n[n.index("-")+1]
            n.insert(n.index("-")-1,a)
            n.pop(n.index("-")-1)
            n.pop(n.index("-")+1)
            n.pop(n.index("-"))
            print (n)
    return n

def of(n):
    print("of")
    while "of" in n:
        a=n[n.index("of")-1]*n[n.index("of")+1]
        n.insert(n.index("of")-1,a)
        n.pop(n.index("of")-1)
        n.pop(n.index("of")+1)
        n.pop(n.index("of"))
        print (n)
    return n

def exp(n):
    print("exponent")
    while "^" in n:
        a=n[n.index("^")-1]**n[n.index("^")+1]
        n.insert(n.index("^")-1,a)
        n.pop(n.index("^")-1)
        n.pop(n.index("^")+1)
        n.pop(n.index("^"))
        print (n)
    return n

main()
