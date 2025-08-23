# Task 2
# არგუმენტი არის მნიშვნელობა, რომელსაც ფუნქციას გადავცემთ input-ის სახით. მაგალითად print ფუნქციაში რასაც ჩავწერთ ეს არის არგუმენტი. 

# Task 3 
# range ფუნქცია გამოიყენება რიცხვითი მიმდევრობის შესაქმნელად. 
# range ფუნქციას სამი მნიშვნელობა შეგვიძლია გადავცეთ: range(start, end, step)
# თუ მარტო ერთი მნიშვნელობა უწერია ფრჩხილებში, იგულისხმება, რომ ის არის დასასრულის მნიშვნელობა, დასაწყისს ავტომატურად 0, ნაბიჯს კი 1 ენიჭება. 
# თუ ორი უწერია- ესენია დასაწყისი და დასასრული. მესამეს ავტომატურად 1 ენიჭება. 


# Task 4
jami=0
for i in range (50,101):
    jami+=i
print(jami)

# Task 5
namravli=1
for i in range(100,200):
    namravli*=i
print(namravli)

# Task 6
# for მაშინ გამოიყენება, როდესაც ზუსტად ვიცით კოდი რამდენჯერ გვინდა განმეორდეს, 
# while მაშინ გამოიყენება, როდესაც გვინდა კოდი იქამდე განმეორდეს, სანამ რაიმე კონკრეტული პირობა შესრულდება.

# Task 7 
i=1
while i<11:
    print(i)
    i+=1

# Task 8
chafikrebuli_ricxvi=7
ricxvi=int(input("shemoitanet ricxvi 1-10-is chatvlit"))
while chafikrebuli_ricxvi!=ricxvi:
    print("wrong number")
    ricxvi=int(input("shemoitanet ricxvi 1-10-is chatvlit"))

print("You win")

