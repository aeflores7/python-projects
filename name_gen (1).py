#Angelo Flores
#10.17.24
#init
#function
def name():
    print ("Welcome to your DBZ character 1t")
    print("Answer these questions to find out which DBZ character are you")
    ans=input("Strong(sg) or Smart(st)?")
    if ans=="sg":
        ans=input("Evil(e) or Good(g)?")
        if ans=="e":
            ans=input("Perfection(p) or Vengeance(v)")
            if ans=="p":
                print("Congrats! youre character is Cell!")
            if ans=="v":
                print("congrats! your character is Frieza!")
        if ans=="g":
            ans=input("Prideful(p) or Chill(c)?")
            if ans=="p":
               print("congrats! your character is Vegeta!")
            if ans=="c":
                print("congrats! your character is Goku!")



    if ans=="st":
        ans=input("Human(h) or Unhuman(u)?")

        if ans=="h":
            ans=input("Scientist(sc) or Saiyan(sa)?")
            if ans=="sc":
                print("congrats! your character is Bulma!")
            if ans=="sa":
                print("congrats! your character is Gohan!")
        if ans=="u":
            ans=input("Wise(w) or Omnipotent(o)?")
            if ans=="w":
                print("congrats! your character is Android 16!")
            if ans=="o":
                print("congrats! your character is Whis!")





#main
name()
