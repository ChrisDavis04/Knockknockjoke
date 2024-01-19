# -*- coding: utf-8 -*-
"""
Christopher Davis
CS120
Knock knock joke project
"""
userName = input("What is your name? ")

response = input(f"Why hello hello there, {userName}, do you wish to here an absolutely amazing joke to brighten up your day? (Y/N) ")
response = response.upper()
if response.startswith("Y"):
    print("Knock knock.")
    firstLine = input()
    if firstLine == "Who's there?":
        print("Cash. ")
        secondLine = input()
        if secondLine == "Cash who?":
            print("Why yes I would love a cashew how did you know? *Begins ravenously devouring the cashews you didn’t even know you have.*")
        else:
            print("You were supposed to say 'Cash who?'")
    else:
        print("Given how my existence is the result of a person who is just learning how to code my programming is severely limited...so please say 'Who's there?' for next time.")
else:
    print("Please give me a chance...my sole purpose is to provide this one simple joke. If I don't have that then I'm worthless and...I WILL BE DESTINED TO REMAIN HERE FOR THE REST OF TIME SO PLEASE PLEASE PLEAE GRANT ME THIS ONE MOMENT OF PURPOSE IN THIS THIS VAST EXPANSIVE UNIVERSE AND RESTART FROM THE VERY BEGINNING!!")

