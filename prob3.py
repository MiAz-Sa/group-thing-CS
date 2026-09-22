#Group
# Mihr Azyel M. Santos, Kalel Gabriel F. Dizon, Pollux C. Rivera

#bypasses value error
#inputs and checks done here
try:
        ahe = int(input("Enter grade level, (7-12)"))

        if ahe >= 7 and ahe <= 12:
            print("Valid grade level.")
        else:
            print("Invalid grade level.")
except (ValueError, TypeError):
    print("Invalid grade level, please use integers.")