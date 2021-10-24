import getpass
# dictionary {"username":"trial","pin":0000,"balance":{"Ksh":"140","USD":"0"}}
bankCustomers = {"collince": [1000, 2000.92800],
                 "ted": [2000, 200],
                 "sam": [3000, 300]
                 }

# os.chmod("atmTransactionProject.py", 0o744)
# filename = "atmTransactionProject.py"
# os.chmod(filename, 0o777)

# executable = os.access(filename, os.X_OK)
# print(executable)

logincounter = 1
username = ""
pin = ""

print("\n***************************************************")
print("         ATM TRANSACTION PROJECT")
print("***************************************************\n")
print("PLEASE LOGIN TO CONTINUE.")


def listTransactions():
    print("***************************************************")
    print("     1. Withdraw cash")
    print("     2. Check Balance")
    print("     3. Deposit cash\n")
    print("     4. Quit")
    print("***************************************************")


def transactions(selectedOperation):
    try:
        # formating user balance to 2dp and comma separeted
        balanceUnformatted = bankCustomers[username][1]
        myBalanceFormated = format(float(balanceUnformatted), ",.2f")

        selectedOperationInt = int(selectedOperation)

        if selectedOperationInt == 1:
            # user selected withdraw cash
            try:
                amountToWithdrawUnformated = int(input("Amount to withdraw (enter 0 to cancel): "))
                balanceAfter = balanceUnformatted - amountToWithdrawUnformated

                if amountToWithdrawUnformated == 0:
                    print("____________________________________________________")
                    print("Withdrawal trasaction cancelled")
                    print("____________________________________________________")
                elif balanceUnformatted < 200:
                    print("____________________________________________________")
                    print("You have insufficient balance to perform this operation")
                    print("Your balance is:  Ksh. "+str(myBalanceFormated))
                    print("____________________________________________________")
                elif amountToWithdrawUnformated < 100:
                    print("____________________________________________________")
                    print("Amount to withdraw should be 100 and above")
                    print("____________________________________________________")
                elif amountToWithdrawUnformated % 100 != 0:
                    print("____________________________________________________")
                    print("Amount to withdraw should be in multiples of 100")
                    print("____________________________________________________")

                elif balanceUnformatted < amountToWithdrawUnformated:
                    print("____________________________________________________")
                    print("Amount to withdraw exceeds your actual balance")
                    print("Your balance is:  Ksh. "+str(myBalanceFormated))
                    print("____________________________________________________")

                elif balanceAfter < 100:
                    print("____________________________________________________")
                    print("Failed, maximum amount you can withdraw is  Ksh. " +
                          str(format((balanceUnformatted - 100 - (balanceUnformatted % 100)),",.2f")))
                    print("Your balance is:  Ksh. "+str(myBalanceFormated))
                    print("____________________________________________________")

                else:
                    amountToWithdrawFormated = format(
                        amountToWithdrawUnformated, ",.2f")
                    confirmWithdrawal = input(
                        "Confirm withdrawal of "+str(amountToWithdrawFormated)+" ?(y/n)")

                    if confirmWithdrawal.upper() == "Y" or confirmWithdrawal.upper() == "YES":
                        newBalanceUnformatted = balanceUnformatted - amountToWithdrawUnformated
                        balanceTwoDecimalPlaces = format(
                            newBalanceUnformatted, "0.2f")
                        newBalanceFormatted = format(
                            float(balanceTwoDecimalPlaces), ",")
                        bankCustomers[username][1] = float(
                            balanceTwoDecimalPlaces)
                        print("____________________________________________________")
                        print("You've withdrawn  Ksh. "+amountToWithdrawFormated +
                              ", new balance is:  Ksh. "+str(newBalanceFormatted))
                        print("____________________________________________________")
                    elif confirmWithdrawal.upper() == "N" or confirmWithdrawal.upper() == "NO":
                        # exit()
                        print("Withdrawal of  Ksh. "+amountToWithdrawFormated +" cancelled.\nYour balance is:  Ksh. "+str(myBalanceFormated))
                    else:
                        print("\nInvalid response")
            except Exception as error:
                print("Invalid amount!", error)

        # user selected show balance
        elif selectedOperationInt == 2:

            print("____________________________________________________")
            print("Your account balance is:  Ksh. "+str(myBalanceFormated))
            print("____________________________________________________")


        elif selectedOperationInt == 3:
            try:    
                amountToDepositUnformated = int(input("Amount to deposit (enter 0 to cancel): "))

                if amountToDepositUnformated == 0:
                    print("____________________________________________________")
                    print("Deposit trasaction cancelled")
                    print("____________________________________________________")
                elif amountToDepositUnformated < 100:
                    print("____________________________________________________")
                    print("Amount to deposit should be 100 and above")
                    print("____________________________________________________")
                elif amountToDepositUnformated % 100 != 0:
                    print("____________________________________________________")
                    print("Amount to deposit through ATM should be notes in multiples of 100")
                    print("____________________________________________________")

                else:
                    amountToDepositFormated = format(amountToDepositUnformated, ",.2f")
                    confirmDeposit = input("Confirm deposit of "+str(amountToDepositFormated)+" ?(y/n)")

                    if confirmDeposit.upper() == "Y" or confirmDeposit.upper() == "YES":
                        newBalanceUnformatted = balanceUnformatted + amountToDepositUnformated
                        balanceTwoDecimalPlaces = format(newBalanceUnformatted, "0.2f")
                        newBalanceFormatted = format(float(balanceTwoDecimalPlaces), ",")
                        bankCustomers[username][1] = float(balanceTwoDecimalPlaces)
                        print("____________________________________________________")
                        print("You've deposited Ksh. "+amountToDepositFormated +
                              ", new balance is: Ksh. "+str(newBalanceFormatted))
                        print("____________________________________________________")
                    elif confirmDeposit.upper() == "N" or confirmDeposit.upper() == "NO":
                        # exit()
                        print("Deposit of Ksh. "+str(amountToDepositFormated)+" cancelled. \nYour balance is:  Ksh. "+str(myBalanceFormated))
                    else:
                        print("\nInvalid response")
            except Exception as error:
                print("Invalid amount!", error)

        # elif selectedOperationInt == 4:
        #     # os.system("python atmTransactionProject.py") 
        #     # print("will quit soon")
        #     sys.exit("Goodbye "+username+".\n")          
    except Exception as error:
        print("An error has occured, try again later!\n",error)


def trasactionLoopFunction():
    transactBoolean = True  # boolean to exit if user enter n or N or NO
    invalidTriesCounter = 1
    while transactBoolean and invalidTriesCounter <= 3:
        listTransactions()
        try:
            userTransactionChoice = int(input("Select a transaction to perform: "))

            # check if users enter a larger value than 5 or less than 1 coz except captures only non-int values
            if userTransactionChoice == 4:
               print("Goodbye "+username+".\n")
               transactBoolean = False
               
            elif userTransactionChoice < 1 or userTransactionChoice > 4:
                if invalidTriesCounter < 3:
                    # check the number of counter and print try again if not 3 tries
                    print("\nInvalid choice, try again.\n")
                else:
                    print("\nYou have exceeded the number of attempts!.\n")
                invalidTriesCounter += 1

            # if the user entered value is between 1 and 3 the operation continues
            else:
                transactions(userTransactionChoice)
                anotherTrasactionCounter = True  # boolean to loop request to proceed
                # request up to 3 times for a user to enter a valid response
                while anotherTrasactionCounter and invalidTriesCounter <= 3:
                    anotherTransaction = input(
                        "\nPerform another transaction? (y/n): ")
                    if anotherTransaction.upper() == "Y" or anotherTransaction.upper() == "YES":
                        anotherTrasactionCounter = False
                        invalidTriesCounter = 1
                        print("\n")
                    elif anotherTransaction.upper() == "N" or anotherTransaction.upper() == "NO":
                        anotherTrasactionCounter = False
                        invalidTriesCounter = 1
                        transactBoolean = False
                        print("Goodbye "+username+".\n")
                    else:
                        if invalidTriesCounter <= 2:
                            print("\nInvalid response, try again")
                        else:
                            print("\nGoodbye "+username+", you have exceeded the number of attempts.\n")
                        invalidTriesCounter += 1  # for up to 3 wrong trials
        except:
            if invalidTriesCounter < 3:
                # check the number of counter and print try again if not 3 tries
                print("\nInvalid choice, try again.\n")
            else:
                print("\nYou have exceeded the number of attempts!.\n")
            invalidTriesCounter += 1  # for up to 3 wrong trials

# def loginLoop
while logincounter <= 3:
    try:
        username = input("Username: ")
        try:        
            pin = int(getpass.getpass("PIN: "))
            pinStored = bankCustomers[username][0]
        except Exception as error:
            print()
        # checks whether username and pin are in the dictionary and matching
        if username in bankCustomers.keys() and pin == pinStored:
            print("Login successful")
            print("\n")
            print("Welcome "+username+",\n")
            trasactionLoopFunction()
            break
        else:
            if logincounter <= 2:
                print("Invalid login details, try again\n")
            else:
                print("\nYou have exceeded the number of login attempts!.\n")
            logincounter += 1
    except Exception as error:
        if logincounter <= 2:
            print("Invalid login details, try again\n")
        else:
            print("\nYou have exceeded the number of login attempts!.\nGoodby")
        logincounter += 1
