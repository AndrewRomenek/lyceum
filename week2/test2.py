#Числа и знаки
x = input("Число1\n")

y = input("Число2\n")

z = input("Число3")

oper = input("Знак\n")

oper_2 = input("Знак №2 \n")


#Решение
if x != int or y != int or z !=int:
    Solve_1 = "Чёт это на цифры не похоже"
else:   
    if oper == "+":
        if oper_2 == "+":
            Solve_1 = x + y + z
        elif oper_2 == "-":
            Solve_1 = x + y - z
        elif oper_2 == "*":
            Solve_1 = x + y*z
        elif oper_2 == "/":
            Solve_1 = x + y/z
        else: 
            Solve_1 = "ЭЭЭууэ слыш вуася ты это давай знак вводи да"
    elif oper == "-":
        if oper_2 == "+":
            Solve_1 = x - y + z
        elif oper_2 == "-":
            Solve_1 = x - y - z
        elif oper_2 == "*":
            Solve_1 = x - y*z
        elif oper_2 == "/":
            Solve_1 = x - y/z
        else: 
            Solve_1 = "ЭЭЭууэ слыш вуася ты это давай знак вводи да"
    elif oper == "*":
        if oper_2 == "+":
            Solve_1 = x*y + z
        elif oper_2 == "-":
            Solve_1 = x*y - z
        elif oper_2 == "*":
            Solve_1 = x*y*z
        elif oper_2 == "/":
            Solve_1 = x*y/z
        else: 
            Solve_1 = "ЭЭЭууэ слыш вуася ты это давай знак вводи да"
    elif oper == "/":
        if oper_2 == "+":
            Solve_1 = x/y + z
        elif oper_2 == "-":
            Solve_1 = x/y - z
        elif oper_2 == "*":
            Solve_1 = x/y*z
        elif oper_2 == "/":
            Solve_1 = x/y/z
        else: 
            Solve_1 = "ЭЭЭууэ слыш вуася ты это давай знак вводи да"
    else:
        Solve_1 = "ЭЭЭууэ слыш Вася ты это давай знак вводи да"

#Господи, какое же оно не красивое, там вроде функция while для такого есть или нет?

print(str(Solve_1))
  




