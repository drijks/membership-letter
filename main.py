# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


letter = "(Insert Member Name), This is a note to confirm that your account (insert #) has been cancelled with an effective date of today (insert date). We greatly appreciate the time you have spent with us and we are sad to see you go. We hope that you continue chasing your health and fitness goals and are ready to help you again when you want to return! Yours in Health"

print()
selection = input("cxl=1, Frz no AF=2, Frz AF=3, Indefinite Freeze=4\n")
membername = input("Name \n")
acctnmbr = input("Account #\n")
todaysdate = input("Date\n")
if selection == "1":
    print("cxl")
    letter = str(membername + ", This is a note to confirm that your account " + acctnmbr + " has been cancelled with an effective date of today " + todaysdate + ". We greatly appreciate the time you have spent with us and we are sad to see you go. We hope that you continue chasing your health and fitness goals and are ready to help you again when you want to return! Yours in Health")
elif selection == "2":
    print("Frz no AF")
    letter = str(membername + ", This is a note to confirm that your account " + acctnmbr + " has been cancelled with an effective date of today " + todaysdate + ". We greatly appreciate the time you have spent with us and we are sad to see you go. We hope that you continue chasing your health and fitness goals and are ready to help you again when you want to return! Yours in Health")
elif selection == "3":
    print("Frz AF")
    letter = str(membername + ", This is a note to confirm that your account " + acctnmbr + " has been cancelled with an effective date of today " + todaysdate + ". We greatly appreciate the time you have spent with us and we are sad to see you go. We hope that you continue chasing your health and fitness goals and are ready to help you again when you want to return! Yours in Health")
elif selection == "4":
    print("Indefinite Freeze")
    letter = str(membername + ", This is a note to confirm that your account " + acctnmbr + " has been cancelled with an effective date of today " + todaysdate + ". We greatly appreciate the time you have spent with us and we are sad to see you go. We hope that you continue chasing your health and fitness goals and are ready to help you again when you want to return! Yours in Health")
else:
    print("you fucked up")

print(letter)
