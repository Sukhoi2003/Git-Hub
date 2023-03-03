def victo():

    t = True
    while t:
        print("Boshlaysizmi Ha 1/Yo'q 0")
        n = int(input(">> "))
        if n == 1:
            x=input("Ey kimsan: ")
            if x == "Tursunxonman":
                print("Tog'ri")
            else:
                print("Bash")
            if input('yana o\'ynaysizmi? [1/0]:'):
                continue
            else: break
        else:
            print("Bye")
            break
        

victo()
