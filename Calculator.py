def main():
    expressionl=[]
    a=input("Enter expression, seperate the numbers and operators by spaces: ")
    for i in a.split():
        try:
            expressionl.append(int(i))
        except:
            expressionl.append(i)
    ch=input("Enter A for BODMAS or B for PEMDAS: ")
    if ch.lower()=="a":
        bodmas(expressionl)
def bodmas(n):
    for i in range(len(n)-1):
        if n[i]=="/":
            a=div(n)
        elif n[i]=="*":
            a=pro(n)
        elif n[i]=="+":
            a=addit(n)
        elif n[i]=="-":
            a=subit(n)
def div(n):
    print("div")
def pro(n):
    print("pro")
def addit(n):
    print("addit")
def subit(n):
    print("subit")
main()
