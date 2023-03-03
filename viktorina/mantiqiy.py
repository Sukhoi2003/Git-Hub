ball = 0
javob = input("Marhamat\n1-savol: Undan qanchalik ko'p olaversangiz, u shunchalik kattalashib boraveradi. U nima? 6 ball\n>>> ").capitalize()
if javob == "Chuqur":
    print("To'g'ri")
    ball += 6
else:
    print("Noto'g'ri")

javob = input("2-savol: Kichkina, kulranggina, filga o'xshaydi. 3 ball\n>>> ").capitalize()
if javob == "Filning bolasi" or javob == "Filcha":
    print("To'g'ri")
    ball += 3
else:
    print("Noto'g'ri")

javob = input("3-savol: Nok osilib turibdi, lekin uni yeb bo'lmaydi. Lampochka emas. 15 ball\n>>> ").capitalize()
if javob == "Birovning noki" or javob == "Begonaning noki":
    print("To'g'ri")
    ball += 15
else:
    print("Noto'g'ri")

javob = input("4-savol: Qaysi yegulikni pishirishda qancha tuz solsa ham, u sho'r bo'lib ketmaydi? 8 ball\n>>> ").capitalize()
if javob == "Qaynatilgan tuxum":
    print("To'g'ri")
    ball += 8
else:
    print("Noto'g'ri")

javob = input("5-savol: Kim o'tirgan holda yuradi? 5 ball\n>>> ").capitalize()
if javob == "Shaxmatchi":
    print("To'g'ri")
    ball += 5
else:
    print("Noto'g'ri")
    ball -= 5  

javob = input("5-savol: Men suvman va suv yuzasida suzib yuripman. Men kimman? 2 ball\n>>> ").capitalize()
if javob == "Muz":
    print("To'g'ri")
    ball += 2
else:
    print("Noto'g'ri")
    ball -= 10