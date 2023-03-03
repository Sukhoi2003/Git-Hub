def vik():
    print("Assalomu alaykum bizning kichik viktorinamizga hush kelibsiz")
    javob = input("Viktorini boshlaysizmi (Ha/Yo'q) ")
    ball = 0

    if javob.lower() == "ha":
        javob = input("1-savol: Maydoni jihatidan eng katta davlat-> ")
        if javob.lower() == "rossiya" or "hhh":
            ball += 1.03
            print(f"Tog'ri javob")
        else:
            print("Noto'g'ri javob")

        javob = input("2-savol: Telegram nechinchi yil ishlab chiqilgan-> ")
        if javob.lower() == "2013":
            ball += 5
            print("To'g'ri javob")
        else:
            print("Noto'g'ri javob")
        
        javob = input("3-savol: Eng Kichik qush-> ")
        if javob.lower() == "kalibriy":
            ball += 6
            print("To'g'ri javob ")
        else:
            print("Noto'g'ri javob")
        javob = input("4-savol: https://t.me/Bepuldarslar_uzbbot botga a'zomisiz ")
        if javob.lstrip() == "ha":
            ball += 20
            print("Tog'ri javob")
        else:
            print("Noto'g'ri javob")
        print(f"{ball} To'pladingiz")
        if ball > 15:
            print("yaxshi natija")
        else:
            print("Yomon")
        print("Ishtirokingiz uchun raxmat")
vik()