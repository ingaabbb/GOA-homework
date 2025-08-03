# 1) დაწერეთ 2-2 მაგალითი შედარების ოპერატორებზე(>, <, <=, >=, ==, !=)

# 2) დაწერეთ მაგალითები შედარების ოპერატორებზე.

# 3) სანამ ამ კოდს გაუშვებდეთ, კარგად იფიქრეთ ამის პასუხზე(პასუხი იქნება ერთ-ერთი, ორი Boolean მნიშვნელობებიდან True/False)

# print(True and False or 5 > 10 and 100 / 5 > 10 and "Python" == "Python" or 2 * 3 < 5 or 6 + 7 - 9 < 20 and True and 5 > 5.0 or 10 - 10 < 100)

# Task 1
print(5 > 10)  #false
print(23 > 15) #true
print(15 < 25)  #true
print(12 < 90)  #false
print(25 >= 25)  #true
print(35 >= 40) #false
print(30 <= 30)  #true
print(53 <= 55) #true
print(5 == 4)  #false
print(10 == 10) #True
print( 3 != 9)  #true
print(44 != 44)  #False

# Task 2 
num1=5
num2=10
print(num1 > num2)
print(num1 < num2)
print(2*num1 == num2)

print(True and False or 5 > 10 and 100 / 5 > 10 and "Python" == "Python" or 2 * 3 < 5 or 6 + 7 - 9 < 20 and True and 5 > 5.0 or 10 - 10 < 100)
 #        False      or  False and    True      and    True              or  False    or     True       and True and False   or True  
 #               False         and    True      and    True              or  False    or     True       and True and False   or True 
 # ასე თუ გავაგრძელებთ პასუხი გამოვა True 
 