import random
import string
import mysql.connector
import csv

con = mysql.connector.connect(host="locaLhost",
                              user="root",
                              password="Mr.Shau@2004",
                              database= "shaus")

cur = con.cursor()

print("1. Create an account")
print("2. Login")
print("3. Update Password \n")

choice= str(input("Enter your choice:"))
if choice == "1":
    print("Sign Up")
    usern= str(input("Username:"))
    cur.execute("select Username from userdata")
    usdata= str(cur.fetchall())
    if usern in usdata:
        print("Username exists")
    elif usern not in usdata:
        pwd = str(input("Password:"))
        userid = str(''.join(random.choices(string.ascii_uppercase + string.digits, k=7)))
        cpwd = str(input("Confirm password:"))
        if cpwd == pwd:
            cur.execute("use shaus")
            try:
                query = "insert into userdata values('{}', '{}', '{}')".format(usern, pwd, userid)
                cur.execute(query)
                con.commit()
                print("Account made successfully")
            except Exception as e:
                print("Password Exists!")

        else:
            print("Confirmation wrong")

elif choice == "2":
    print("Sign In")
    nuser= input("Enter your username:")
    cur.execute("select Username from userdata where Username = '{}'".format(nuser))
    bus= str(cur.fetchall())
    if nuser in bus:
        npass = input("Enter your password:")
        cur.execute("use shaus")
        mainq= "select Pass from userdata where Username = '{}'".format(nuser)
        cur.execute(mainq)
        conf= str(cur.fetchall())
        if npass in conf:
            print("Logged In")
            print("You can now play games\n1. Coinflip\n2. Snake, Water, Gun")
            checkc = int(input("Enter your choice:"))

            if checkc == 2:
                l1 = ["s", "w", "g"]

                print('Welcome to snake water gun game !\nLet us see who wins')
                print("==========")
                print("s : snake\nw : water\ng : gun")
                print("==========")
                print("INSTRUCTIONS:\nThere will be ten rounds in this game and the"
                      " results will be declared after the game ends")

                csscore = 0
                myscore = 0

                var1 = 0
                while (var1 <= 10):
                    computer = random.choice(l1)
                    me = input("Enter your choice:")
                    if me == computer:
                        print("Draw")
                        csscore += 1
                        myscore += 1
                    elif me == "s" and computer == "w":
                        print("You won this round")
                        myscore += 1
                    elif me == "s" and computer == "g":
                        print("Computer won this round")
                        csscore += 1
                    elif me == "w" and computer == "g":
                        print("You won this round")
                        myscore += 1
                    elif me == "w" and computer == "s":
                        print("Computer won this round")
                        csscore += 1
                    elif me == "g" and computer == "s":
                        print("You won this round")
                        myscore += 1
                    elif me == "g" and computer == "w":
                        print("Computer won this round")
                    else:
                        print("Check your response")
                        break
                    var1 += 1
                print("=================================================")

                var2 = []
                if myscore > csscore:
                    print("You won the game")
                    var2 = "won"
                elif myscore < csscore:
                    print("You lost the game")
                    var2 = "lost"
                else:
                    print("The game was drawn")
                    var2 = "drawn"

                print(f"Your score:{myscore}  Computer's score:{csscore}")
                print("=================================================")

                grec = str(f"{nuser} {var2} from the computer with {myscore - csscore} points")

                with open("game records.csv", "w") as f:
                    filewriter = csv.writer(f, delimiter=' ', quotechar = "")
                    filewriter.writerow(grec)

            elif checkc == 1:

                chance = 0
                ms = 0
                cos = 0
                while chance <= 10:
                    l = ["heads", "tales"]
                    hc = input("Enter your call:")
                    if hc == l[1]:
                        cc = l[0]
                    elif hc == l[0]:
                        cc = l[1]

                    coinflip = random.choice(l)

                    if coinflip == hc:
                        print("You won")
                        ms += 1
                    elif coinflip == cc:
                        print("Computer won")
                        cos += 1

                    chance += 1

                print(f"Your score:{ms} Computer score:{cos}")

        else:
            print("Incorrect Password!")
    else:
        print("Username does not exist!")

elif choice == "3":
    cusn= input("Enter Username:")
    cur.execute("use shaus")
    cur.execute("select Username from userdata where Username = '{}'".format(cusn))
    cond= str(cur.fetchall())
    if cusn in cond:
        cpass= input("Enter Passsword:")
        cur.execute("Use shaus")
        cur.execute("Select Pass from userdata where Username ='{}'".format(cusn))
        passdata= str(cur.fetchall())
        if cpass in passdata:
            npass= input("Enter new password:")
            conpass= input("Confirm the new password:")
            if npass == conpass:
                cur.execute("use shaus")
                cur.execute("update userdata set Pass = '{}' where Username = '{}'".format(npass,cusn))
                con.commit()
                print("Updated successfully")
            else:
                print("try again! check your response")
        else:
            print("Incorrect password")
    else:
        print("Incorrect Username")

else:
    print("Check your response")