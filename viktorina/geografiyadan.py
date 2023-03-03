def geog():
    ball = 0
    javob = input("Marhamat \n1-savol: Avstraliyada yashovchi mutlaqo suv ichmaydigan sut emizuvchi hayvon? 6 ball \n>>> ").capitalize()
    if javob == "Koala":
        print("To'g'ri")
        ball += 1
    else:
        print("Noto'g'ri")
    javob = input("Qaysi mamlakatning madhiyasi 158 ta usulda yangrashi mumkin? 5 ball\n>>> ").capitalize()
    if javob == "Gretsiya":
        print("Tog'ri")
        ball += 5
    else:
        print("Noto'g'ri")
    javob = input("3-savol: AQSH ning 31-prezindenti? 10 ball\n>>>").capitalize()
    if javob == "Herbert Hooven" or javob == "Hooven Herber":
        print("To'g'ri")
        ball += 10
    else:
        print("Noto'g'ri")
    javob = input("4-savol: Dunyodagi qaysi dengiz eng iliq dengiz deb tan olingan? 4ball\n>>>").capitalize()
    if javob == "Qizil dengiz" or javob == "Qizil":
        print("To'g'ri")
        ball += 4
    else:
        print("Noto'g'ri")
    javob = input("5-savol: Qaysi mamlakatda tovuq go`shti eng ko`p iste`mol qilinadi? 6 ball\n>>>").capitalize()
    if javob == "AQSH" or javob == "Amerika" or javob == "Aqsh":
        print("To'g'ri")
        ball += 6
    else:
        print("Noto'g'ri")

    print(f"{ball} ball to'pladingiz")
    if ball == 26:
        print("Siz maksimal ball to'pladingiz!!!")
geog()




