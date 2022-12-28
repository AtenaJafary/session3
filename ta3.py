import math

def moadele_daraje2() :
    a=int(input("please enter a:"))
    b=int(input("please enter b: "))
    c= int(input("please enter c:"))
    delta=(b**2)-(4*a*c)
    if delta==0 :
      x=(-b/2*a)
      print("moadele_daraje2 yek javab dare: ", x )
    elif delta>0 :
      x1=(-b+ math.sqrt(delta)/a*2)
      x2=(-b-math.sqrt(delta)/a*2)
      print("javab haye moadele_daraje2: ", x1,"va", x2)
    elif delta<0 :
        print("moadele_daraje2 javab nadarad ")

moadele_daraje2()