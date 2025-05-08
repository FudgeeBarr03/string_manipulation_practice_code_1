#Ask for user full name not in pascal case
fullname = input("enter your full name not in pascal case: ")

#convert user input into correct pascal case
print(''.join(word.capitalize() for word in fullname.split()))