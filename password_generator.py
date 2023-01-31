import random

char1 = ["A","B","C","D","E","F","G","H","I","J","k","L","M","N","0","P","Q","R","S","T","U","V","W","X","Y","Z"]
char2 = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
char3 = ["1","2","3","4","5","6","7","8","9","0"]
char4 = ["!","£","$","%","^","&","*"]

    
    


upper = int(input("amount of upper case letters: "))
lower = int(input("amount of lower case letters: "))
spec = int(input("amount of special characters: "))
num = int(input("amount of numbers: "))
   

new_password = ""
for i in range(upper):
    new_password+=random.choice(char1)
for x in range(lower):
    new_password+=random.choice(char2)
for y in range(spec):
    new_password+=random.choice(char3)
for z in range(num):
        new_password+=random.choice(char4)
        
pass_word = list(new_password)
shuffle = random.shuffle(pass_word)
new_pass = "".join(pass_word)

print(new_pass)
