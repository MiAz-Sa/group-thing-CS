#Group
# Mihr Azyel M. Santos, Kalel Gabriel F. Dizon, Pollux C. Rivera

#bypasses value error
#inputs and checks done here
try:
        ahe = int(input("Enter age, (12-18)"))

        if ahe >= 12 and ahe <= 18:
            print("You are of age.")
        else:
            print("You are not of age... (12-18)")
except (ValueError, TypeError):
    print("Invalid age, please use integer number")