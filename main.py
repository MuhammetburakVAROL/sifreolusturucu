import secrets
sifre_liste = []
def sifreolusturucu():
    print(f"Hoşgeldiniz;")
    print(50 * '*')

    while True:
        karar = input("Programı sonlandırmak için X'i,\n 8 haneli bir şifre oluşturmak için s'yi,\n 7 haneli bir şifre oluşturmak için y'yi,\n 6 haneli bir şifre oluşturmak için a'yı, tuşlayınız: ")
        if karar == "X":
            print(f"Program sonlandırıldı. Şifreniz oluşturuldu \nYeni Şifreniz = {sifre} \nKaydedilen Şifreler : {sifre_liste}")
            break
        if karar == "s":
            sifre = secrets.token_urlsafe(6)
            sifre_liste.append(sifre)
        if karar == "y":
            sifre = secrets.token_urlsafe(5)
            sifre_liste.append(sifre)
        if karar == "a":
            sifre = secrets.token_urlsafe(4)
            sifre_liste.append(sifre)


sifreolusturucu()