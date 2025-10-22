# 1) დაწერე ფუნქცია სახელად `add_numbers`, რომელსაც გადაეცემა ორი რიცხვი.
# ფუნქციამ უნდა დააბრუნოს ამ ორი რიცხვის ჯამი.

# 2) დაწერე ფუნქცია სახელად `average`, რომელსაც გადაეცემა სამი რიცხვი.
# დააბრუნე ამ სამი რიცხვის საშუალო არითმეტიკული.

# 3) დაწერე ფუნქცია სახელად `max_number`, რომელსაც გადაეცემა ორი რიცხვი.
# დააბრუნე უდიდესი რიცხვი.

# 4) დაწერე ფუნქცია სახელად `even_or_odd`, რომელსაც გადაეცემა ერთი რიცხვი.
# თუ რიცხვი ლუწია, დააბრუნე `"ლუწი"`, თუ კენტია — `"კენტი"`.

# 5) დაწერე ფუნქცია სახელად `sum_list`, რომელსაც გადაეცემა სია რიცხვებით.
# ფუნქციამ უნდა დააბრუნოს სიაში არსებული რიცხვების ჯამი.

# 6) დაწერე ფუნქცია სახელად `filter_even`, რომელსაც გადაეცემა სია რიცხვებით.
# დააბრუნე ახალი სია, რომელშიც მხოლოდ ლუწი რიცხვები იქნება.

# 7) დაწერე ფუნქცია სახელად `word_length`, რომელსაც გადაეცემა ერთი სიტყვა (სტრინგი).
# დააბრუნე ამ სიტყვის სიგრძე (რამდენი ასოა მასში).

# 8) დაწერე ფუნქცია სახელად `longest_word`, რომელსაც გადაეცემა სია სიტყვებით.
# დააბრუნე ყველაზე გრძელი სიტყვა ამ სიიდან.

# 9) დაწერე ფუნქცია სახელად `square`, რომელსაც გადაეცემა ერთი რიცხვი.
# დააბრუნე ამ რიცხვის კვადრატი.

# Task 1
def add_numers(num1, num2):
    sum=num1+num2
    return sum

# Task 2
def average(num1,num2,num3):
    average=(num1+num2+num3)/3
    return average

# Task 3
def max_number(num1,num2):
    if num1>num2:
        return num1
    elif num2>num1:
        return num2
    else:
        return "tolia"
    
# Task 4
def even_or_odd(num):
    if num%2==0:
        return "even"
    else :
        return "odd"
    
# Task 5
def sum_list(list):
    i=0
    jami=0
    while i<len(list):
        jami+=list[i]
        i+=1
    return jami

# Task 6
def filter_even(sia):
    i=0
    list=[]
    while i<len(sia):
        if sia[i]%2==0:
            list.insert(0, sia[i])
        i+=1
    return list

# Task 7
def word_length(string):
    return len(string)

# Task 8
def longest_word(strings):
    i=0
    longest_word=strings[i]
    while i<len(strings):
        if len(longest_word) < len(strings[i+1]):
            longest_word=strings[i+1]
        i+=1
    return longest_word

# Task 9
def square(gverdi):
    return gverdi*gverdi