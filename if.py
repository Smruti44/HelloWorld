is_hot = True
is_cold = True

if is_hot:
    print("It's a hot day")
    print("Drink plenty of water")

elif is_cold:
    print("It's a cold day")
    print("Wear warm clothes")

else:
    print("It's a lovely day")

print("Enjoy your day")

//////////////////////////////////////


price = 1000000
has_good_credit = False

if has_good_credit:
    down_payment = 0.1 * price

else:
    down_payment = 0.2 * price

print(f"Down payment: ${down_payment}")

///////////////////////////////////////

has_good_credit = True
has_criminal_record = True

if has_good_credit and not has_criminal_record:
    print("Eligible for loan")

else:
    print("Not Eligible for loan")

////////////////////////////////////////

name = input("Type your name here ")

if len(name) < 3:
    print("Name must be of 3 characters")

elif len(name) > 50:
    print("Name max can be of 50 characters")

else:
    print("Name looks good!")

//////////////////////////////////////////

weight = int(input('weight: '))
unit = input('(L)bs or (K)g: ')

if unit.upper() == "L":
    converted = weight * 0.45
    print(f"You are {converted} kilos")

else:
    converted = weight / 0.45
    print(f"You are {converted} pounds")

//////////////////////////////////////////

