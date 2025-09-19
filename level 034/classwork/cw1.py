# def greet():
#     name=input("daweret tkveni saxeli")
#     print("Hello world!")
#     print("Hello "+ name)

# greet()

# 1) შექმენით len ფუნქციის კლონი. Custom ფუნქციების დახმარებით.
# ანუ უნდა შექმნათ ფუნქცია, რომელსაც გადაეცემა ერთი არგუმენტი, ეს იქნება სია ან string-ი. თქვენი დავალებაა 
# გადაცემული სიის/string-ის სიგრძე ანუ ელემენტთა რაოდენობა დააბრუნოთ.

# შეგიძლიათ შექმნათ ცვლადი, რომელსაც თავიდან გაუტოლებთ 0-ს. შემდეგ for ციკლით გადაუაროთ მიღებულ ელემენტს 
# და დაითვალოთ რამდენი ელემენტია მასში ამ ცვლადის ყოველი იტერაციისას ერთით გაზრდით

# 2) შექმენით find ფუნქციის(string ფუნქციის) კლონი

# 3) შექმენით range ფუნქციის კლონი

# Task 1
def kloni1(argumenti):
    number=0
    for i in argumenti:
        number+=1
    print(number)

kloni1("world")

# Task 2
def kloni2(word, sadziebo):
    # word= world  # sadziebo=o
    word_sigrdze=len(word)
    sadziebo_sigrdze=len(sadziebo)

    #  for i in word:
        
    #     if i==sadziebo:
    #          print()


