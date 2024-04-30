print("Beden kitle indexi hesaplayıcı")
boy=float(input("Lütfen boy uzunluğunuzu (m) giriniz:"))
kilo=int(input("Lütfen ağırlığınızı (kg) giriniz:"))
boy_kilo_indexi=kilo/boy**2
print ("Senin bki:")
print(boy_kilo_indexi)
if (boy_kilo_indexi<=1.80):
    print("Zayıfsın be hocam")
elif(boy_kilo_indexi<=25.0):
    print("Aferim iyi böyle")
elif(boy_kilo_indexi<=30.0):
    print("Balık etli Berkay")
elif(boy_kilo_indexi<=35.0):
    print("Şişko patata ")
elif(boy_kilo_indexi<=40.0):
    print("Obezito mu depozito mu ne")
elif(boy_kilo_indexi>=40.0):
    print("Obez XXX Plus")