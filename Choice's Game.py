print("Welcome To the Choice Game")
print(" \nYou Have Choose Your Path By the Choice's Given And Find the Prize \n It is a story type plz enjoy Plz On your CAPS Lock   ")
S=input("\nEnter 'S' To start The Game ")
if S =="S" :
    print("\nStory:- So You Are told About A Hidden Prize from the Local Bar you Sit,\n You Decide to Find it , but there Is Only One Prize.\n")
    a=input("Your at the Path With Two Route (L/R) Which one Will Your Choice:")
    if a == "L" :
        lb=input("\nAs You walk the Path You See Beautiful Sky and Birds Cripping as you walk, you  Found A River . \n Now You have Two opitons Swim(S)/Wait(W) :")
        if lb == "S":
            print("\nYou try To Swim The River, You Try ever hard and sudden A Big wave Washes You away , you Loose ")
        elif lb == "W" :
            print(" \nYou Wait and After some Time A boat arrive, You hop on the Boat and cross the river and Reach The Other Side")
            lbc=input("\nAfter Walking in The forest you arrive near a Castle. Now you have Two Option Enter(E)/Wait(W):")
            if lbc == "W":
                print("\nYou wait Outside Of the castle and slowly Time fades And Now It Is night time and warewolf attacks And You die ")
            elif lbc == "E":
                print("\nyou Enter the Castle And You find The Castle Very stunning and beautiful ")
                lbcd=input("\nAfter Exploring You Accross Two option you can Upstairs(U)/Downstairs(D):")
                if lbcd == "U":
                    print("\nyou Decide To go upstairs and sudden fall into a Trap and you Loose ")
                elif lbcd == "D":
                    print(" \nYou go downstairs into a basement and You find a Box : ")
                    lbcde=input("\nNow you Two option open(O)/Don't(D)")
                    if lbcde == "D" :
                        print("\nYou Don't open the box as the time files you Exit the Castle and you find A group Of Bandit which kidnaps You\n Now Have to Work For them For Rest of your life")
                    elif lbcde == "O":
                        print(" \nYayyyyy you found the prize which is gold coin for which you can live life without Working ")
                    else :
                        print("invalid input")
                else:
                    print("invalid input")
            else:
                print("invalid input")
        else:
            print("invalid input")
    elif a == "R":
        print("\nYou walk the path and you arrive at a River ")
        rb = input("\nNow You have Two option Swim(S)/Wait(W) :")
        if rb == "W":
            print("\nAs you Wait The Time fades, now it is Night Time and Rain starts you feel the Cold And Suddenly Bandit's Attack And you Losse Your life ")
        elif rb == "S":
            print("\nYou Decide To swim The River And You Swim like A pro and reach The other Side ")
            rbc = input("\nAs You walk The path into the forest you wander, What the Prize Will be and You see a big castle, Now You have two option Wait(W)/Enetr(E) ")
            if rbc == "W":
                print("\nYou Wait Outside And Find For A other Route But As You find The Time Files And Night falls you are attacked By The Warewolf you lost you life ")
            elif rbc == "E":
                print("\nYou Enter the Castle And See A beautiful Interior And is amazed ")
                rbcd = input("\nYou Dawn upon Two Opiton Eihter go upstairs(U)/downstairs(D):")
                if rbcd == "D":
                    print("\nYou Go Down From the stairs And Fall into A Trap And Gets locked in Room and loose your life ")
                elif rbcd == "U":
                    rbcde = input("You Go up Stairs And Find two Doors RedDoor(R)/BlueDoor(B): \nS"
                                  "SWhich one Will you Enter:")
                    if rbcde == "B":
                        print("\nAs You Enter The BlueDoor you See No Floor And You Fall From The Height And Died ")
                    elif rbcde == "R":
                        print("\nAs You enter the door You See A Box ")
                        rbcdef = input("Would Open the Box Or Not (O/N) ")
                        if rbcdef == "N":
                            print("\nYou don't trust the Box And Not open But As time fade you night falls and you loose hope you exit the castle and get attack by th warewolf and died ")
                        elif rbcdef == "O":
                            print("\nYou open The Box And A Big teeth Bear Attacks\n You fall Upon Your Feet As You try to Run But wasn't able to run\n As You try To save your life You touch a sharp gold object\n")
                            rbcdefg = input("Would You trust the object or not (Y/N)")
                            if rbcdefg == "N":
                                print("\nYou Loose Your life And The Bear Eats you Alive ")
                            elif rbcdefg == "Y":
                                print("\nYou pick The Object And Swing it and Kill the Bear\n After The Time Files You take A Rest And See It The Mythical Sword \n . ")
                                print("\nYayyy you found the secret weapon but it is not the prize  , thanx for playing")
                            else:
                                print("invalid input")
                        else:
                            print("invalid input")
                    else:
                        print("invalid input")
                else:
                    print("invalid input")
            else:
                print("invalid input")
        else:
            print("invalid input")
    else:
        print("invalid input")
else:
    print("Invaild ")