a=int(input("what will be the temperature today?"))
if a<12:
    print("wear a jacket")
    if a<10:
        print("wear a scarf")
        if a<8:
            print("wear a hat")
            if a<6:
                print("wear a pair of gloves")
elif a>25:
    print("wear a sunglasses")
else:
   print("You do not need to wear any special things")
b=int(input("what will be the probability of rain (from 0-100)?"))
if b>50:
    print("bring an umberella")
