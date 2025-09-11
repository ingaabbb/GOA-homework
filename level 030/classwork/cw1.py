# .upper() - გადაჰყავს string-ის მაღალ რეგისტრში
# .lower() - გადაჰყავს string-ის დაბალ რეგისტრში
# .capitalize() - string-ის პირველი სიმბოლო გადაჰყავს მაღალ რეგისტრში, ხოლო დანარჩენი დაბალში
# .title() - string-ში ყოველი სიტყვის პირველი სიმბოლო გადაჰყავს მაღალ რეგისტრში, ხოლო დანარჩენი დაბალში
# .find() - string-ში ეძებს პირველ არგუმენად გადაცემულ ელემენტს და აბრუნებს მის ინდექსს, თუ გადაცემული ელემენტი string-ში არ აღმოჩნდა, აბრუნებს -1-ს.

word="hApPy biRthDay "
print(word.upper()) #HAPPY BIRTHDAY 
print(word.lower()) #happy birthday 
print(word.capitalize()) #Happy birthday 
print(word.title()) #Happy Birthday
print(word.find("P")) #
