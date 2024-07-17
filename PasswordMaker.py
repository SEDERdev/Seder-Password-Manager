import random
import os
import csv
import tkinter as tk
from tkinter import *

current_directory = os.path.dirname(os.path.abspath(__file__))

file_path = os.path.join(current_directory, 'Passwords.csv')

GUI = tk.Tk()

Password = ""
Username = ""
Application = ""
PasswordWorks = "No"
PasswordIsRandomlyGenerated = False
PasswordCharacters = IntVar()
PasswordCharacters.set(12)
PositiveCheckResponses = ['Y', 'y', 'Yes', 'yes']
NegativeCheckResponses = ['N', 'n', 'No', 'no']
UppercaseLetters    = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
LowercaseLetters    = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
Digits              = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
SpecialCharacters   = ['!', '@', '#', '$', '%', '^', '*', '(', ')', '-', '_', '+', '=', '{', '}', '[', ']', '|', '~', ',', '.', '?']
Characters = UppercaseLetters +  LowercaseLetters + Digits + SpecialCharacters

def MainMenu():

    def ManageAccounts(Row):
        
        def InfoSeen():

            AccountInfoButton.pack_forget()
            FullAppInfo.pack_forget()
            UsernameLabel.pack_forget()
            UsernamePack.pack_forget()
            PasswordLabel.pack_forget()
            PasswordPack.pack_forget()

            MainMenu()

        MMAddNewAccount.pack_forget()
        ApplicationLabel.pack_forget()
        AccountsLabel.pack_forget()

        FullAppInfo = Label(GUI, text=f"Application: {Row [0]} ")
        FullAppInfo.pack()

        UsernameLabel = Label(GUI, text="Username:")
        UsernameLabel.pack()
        UsernamePack = Text(GUI, height=1, width=25, borderwidth=1, font=("Helvetica", 16))
        UsernamePack.insert(tk.END, Row [1])
        UsernamePack.tag_configure("center", justify='center')
        UsernamePack.tag_add("center", 1.0, "end")
        UsernamePack.pack()

        PasswordLabel = Label(GUI, text="Password:")
        PasswordLabel.pack()
        PasswordPack = Text(GUI, height=1, width=25, borderwidth=1, font=("Helvetica", 16))
        PasswordPack.insert(tk.END, Row[2])  # Assuming 'Row[1]' contains the password
        PasswordPack.tag_configure("center", justify='center')
        PasswordPack.tag_add("center", 1.0, "end")
        PasswordPack.pack()


        for Buttons in AccountButtons:

            Buttons.pack_forget()

        AccountInfoButton = Button(GUI, text="OK", command=InfoSeen)
        AccountInfoButton.pack()
        
    
    def AddNewAccount():

        MMAddNewAccount.pack_forget()
        AccountsLabel.pack_forget()

        if 'NoAccounts' in globals() and NoAccounts.winfo_ismapped():
            
            NoAccounts.pack_forget()

        for Buttons in AccountButtons:

            Buttons.pack_forget()

        EntryPage()

    AccountButtons = []

    MMAddNewAccount = Button(GUI, text="Add New Account", command=AddNewAccount)
    MMAddNewAccount.pack()
    AccountsLabel = Label(GUI, text="Your Accounts:")
    AccountsLabel.pack()

    try:

        with open(file_path, 'r' , newline='') as ReadCVSHandle:
            
            ReadCVSFile = list(csv.reader(ReadCVSHandle))

            if not ReadCVSFile:

                global NoAccounts
                NoAccounts = Label(GUI, text="You have no saved accounts yet!")
                NoAccounts.pack()


            for RowNumber, Row in enumerate(ReadCVSFile):

                ApplicationFromCSV = Row[0]
                ApplicationLabel = Button(GUI, text=ApplicationFromCSV, width=25, command=lambda r=Row: ManageAccounts(r))
                ApplicationLabel.pack()
                AccountButtons.append(ApplicationLabel)
    
    except:
        
        NoAccounts = Label(GUI, text="You have no saved accounts yet!")
        NoAccounts.pack()


def EntryPage():

    global Username
    global Application
    global AllClearNotClearTrue
    AllClearNotClearTrue = False

    def AllClear():

        global AllClearNotClearTrue
        global Application
        global Username
        global Password

        if ApplicationEntry.get() and UsernameEntry.get() and PassCheckVar.get() == True:

            Application = ApplicationEntry.get()
            Username = UsernameEntry.get()

            AppLabel.pack_forget()
            ApplicationEntry.pack_forget()
            UserLabel.pack_forget()
            UsernameEntry.pack_forget()
            CheckLabel.pack_forget()
            CharacterCheck.pack_forget()
            DataEntryCompleteButton.pack_forget()
            AllClearNotClear.pack_forget()
            PasswordLabel.pack_forget()
            PasswordEntry.pack_forget()
            PasswordCheckbox.pack_forget()

            GeneratePassword()
        
        elif ApplicationEntry.get() and UsernameEntry.get() and PasswordEntry.get():

            Application = ApplicationEntry.get()
            Username = UsernameEntry.get()
            Password =PasswordEntry.get()

            AppLabel.pack_forget()
            ApplicationEntry.pack_forget()
            UserLabel.pack_forget()
            UsernameEntry.pack_forget()
            CheckLabel.pack_forget()
            CharacterCheck.pack_forget()
            DataEntryCompleteButton.pack_forget()
            AllClearNotClear.pack_forget()
            PasswordLabel.pack_forget()
            PasswordEntry.pack_forget()
            PasswordCheckbox.pack_forget()

            PasswordPage()
        
        elif AllClearNotClearTrue != True:
            AllClearNotClear.pack()
            AllClearNotClearTrue = True

    def GenerateOrEnterPasswordSwitch():

        global AllClearNotClearTrue

        if PassCheckVar.get() == True:
            
            CheckLabel.pack()
            CharacterCheck.pack()
            PasswordLabel.pack_forget()
            PasswordEntry.pack_forget()
            DataEntryCompleteButton.pack_forget()
            DataEntryCompleteButton.pack()

            if AllClearNotClearTrue == True:

                AllClearNotClear.pack_forget()
                AllClearNotClear.pack()
        
        elif PassCheckVar.get() == False:

            CheckLabel.pack_forget()
            CharacterCheck.pack_forget()
            PasswordLabel.pack()
            PasswordEntry.pack()
            DataEntryCompleteButton.pack_forget()
            DataEntryCompleteButton.pack()

            if AllClearNotClearTrue == True:

                AllClearNotClear.pack_forget()
                AllClearNotClear.pack()


    AppLabel = Label(GUI, text="Aplication Name:")
    AppLabel.pack()
    ApplicationEntry = Entry(GUI, width=50, textvariable=Application)
    ApplicationEntry.pack()
    UserLabel = Label(GUI, text="Username:")
    UserLabel.pack()
    UsernameEntry = Entry(GUI, width=50, textvariable=Username)
    UsernameEntry.pack()
    PassCheckVar = BooleanVar(value=True)
    PasswordCheckbox =  Checkbutton(GUI, text="Gererate Secure Password?", variable=PassCheckVar, command=GenerateOrEnterPasswordSwitch)
    PasswordCheckbox.pack()
    PasswordLabel = Label(GUI, text="Password:")
    PasswordEntry = Entry(GUI, width=50, textvariable=Password)
    CheckLabel = Label(GUI, text="Password Length:")
    CheckLabel.pack()
    CharacterCheck = Spinbox(GUI, from_=8, to=24, textvariable=PasswordCharacters)
    CharacterCheck.pack()
    DataEntryCompleteButton = Button(GUI, text="OK", command=AllClear)
    DataEntryCompleteButton.pack()
    AllClearNotClear = Label(GUI, text="Please fill in the above information!")


def GeneratePassword():

    global Password
    global PasswordIsRandomlyGenerated
    ThereIsUppercaseLetter = False
    ThereIsLowercaseLetters = False
    ThereIsDigits = False
    ThereIsSpecialCharacters = False
    AllCharactersIncluded = False

    while AllCharactersIncluded == False:

        Password = ""

        for i in range(PasswordCharacters.get()):

            Password += random.choice(Characters)

            if Password[i] in UppercaseLetters:
                ThereIsUppercaseLetter = True
            if Password[i] in LowercaseLetters:
                ThereIsLowercaseLetters = True
            if Password[i] in Digits:
                ThereIsDigits = True
            if Password[i] in SpecialCharacters:
                ThereIsSpecialCharacters = True
            
        if ThereIsUppercaseLetter == ThereIsLowercaseLetters == ThereIsDigits == ThereIsSpecialCharacters == True:
            AllCharactersIncluded = True
            PasswordIsRandomlyGenerated = True
            PasswordPage()

def PasswordPage():

    def NotClear():
        PasswordLabel.pack_forget()
        UndesiredPassword.pack_forget()
        SavePassword.pack_forget()
        PasswordPack.pack_forget()

        UndesiredPasswordFollowUp()


    def AllClear():

        PasswordLabel.pack_forget()
        UndesiredPassword.pack_forget()
        SavePassword.pack_forget()
        PasswordPack.pack_forget()

        CSVSave()
    
    if PasswordIsRandomlyGenerated == True:

        PasswordLabelText = f"Your randomly generated password is:"


    elif PasswordIsRandomlyGenerated == False:

        PasswordLabelText = f"Your password is: "

    PasswordLabel = Label(GUI, text=PasswordLabelText)
    PasswordLabel.pack()
    PasswordPack = Text(GUI, height=1, width=25, borderwidth=1, font=("Helvetica", 16))
    PasswordPack.insert(tk.END, Password, )
    PasswordPack.tag_configure("center", justify='center')
    PasswordPack.tag_add("center", 1.0, "end")
    PasswordPack.pack()
    UndesiredPassword = Button(GUI, text="Gererate A Different Password", command=NotClear)
    UndesiredPassword.pack()
    SavePassword = Button(GUI, text="Save This Password", command=AllClear)
    SavePassword.pack()


def UndesiredPasswordFollowUp():

    def AllClear():

        CharacterCheck.pack_forget()
        DataEntryCompleteButton.pack_forget()

        GeneratePassword()
    
    CheckLabel = Label(GUI, text="Password Length:")
    CheckLabel.pack()
    CharacterCheck = Spinbox(GUI, from_=8, to=24, textvariable=PasswordCharacters)
    CharacterCheck.pack()
    DataEntryCompleteButton = Button(GUI, text="OK", command=AllClear) 
    DataEntryCompleteButton.pack()

def CSVSave():

    global Application
    global Username

    def AllClear():

        InfoSavedButton.pack_forget()
        InfoSavedLabel.pack_forget()

        MainMenu()

    with open(file_path, 'a', newline='') as WriteCVSHandle:

        WriteCVSFile = csv.writer(WriteCVSHandle)
        WriteCVSFile.writerow([Application, Username, Password])
        InfoSavedLabel = Label(GUI, text="Your information is saved!")
        InfoSavedLabel.pack()
        InfoSavedButton = Button(GUI, text="OK", command=AllClear)
        InfoSavedButton.pack()

MainMenu()

GUI.mainloop()

#Create a way to only access that file with a master password
#Ammend the GUI
#Encrypt the CSV file