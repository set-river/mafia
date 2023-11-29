# калькулятор, принимающий 2 числа от юзера и принимающий выбор действия

n1 = int(input("первое число: "))
n2 = int(input("второе число: "))
oper = input("Введите знак для выбора действия (+/-/:/*): ")
def summ(n1,n2):
    return n1 + n2
def minys(n1,n2):
    return n1 - n2
def delit(n1,n2):
    return n1 / n2
def ymnojaet(n1,n2):
    return n1 * n2
def calc(n1, n2, oper):
    if oper == "+":
        print(summ(n1,n2))
    if oper == "-":
        print(minys(n1,n2))
    if oper == ":":
        print(delit(n1,n2))
    if oper == "*":
        print(ymnojaet(n1,n2))

calc(n1, n2, oper)
