#Group
# Mihr Azyel M. Santos, Kalel Gabriel F. Dizon, Pollux C. Rivera

#List of valid characters for password
valid_characters = ["a","b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m","o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "A", "B", "C", "D", "E", "F", "G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","0","1","2","3","4","5","6","7","8","9"]
#User enters password
password = input("Enter your username: ")
#Counts the amount of letters
letter = len(password)
#Checks the conditions here
if 11 <= letter <= 4 or password[letter - 1] not in valid_characters:
    print("Invalid username")
else:
    print("Valid username")