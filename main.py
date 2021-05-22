import time

def again():
    is_again = input("Is there anything else i can do for you? y/n")
    if is_again.upper()=="Y":
        main()
    else:
        exit()

def exit():
    print("Thanks for using me!")
    quit()

def main():
    print("Weight converter. Choose what you want to convert.")
    time.sleep(1)
    while True:
        print("1.KG to LBS")
        unit = input("2.LBS to KG ")
        if not (unit == "1" or unit == "2"):
            print("Pick 1 or 2")
        else:
            break

    while True:
        try:
            weight = float(input("Weight: "))
            break
        except:
            print("Incorrect weight")
    if unit == "2":
        conv = weight * 0.45
        conv = round(conv, 1)
        print(f"Your weight is {conv} KG")
        time.sleep(2)
        is_want = input("Do you want me to calculate your bmi? y/n")
        if is_want.upper() == "Y":
            weightkg = conv
            bmi_calc(weightkg)
        else:
            exit()
    elif unit == "1":
        conv = weight / 0.45
        conv = round(conv, 1)
        print(f"Your weight is {conv} LBS")
        time.sleep(2)
        is_want = input("Do you want me to calculate your bmi? y/n")
        if is_want.upper() == "Y":
            weightkg = conv * 0.45
            bmi_calc(weightkg)
        else:
           exit()

def bmi_calc(weightkg):
   while True:
       try:
          height = float(input("Enter your height in meters(x.xx): "))
          break
       except:
           print("Incorrect height")
   bmi = weightkg / height ** 2
   bmi = round(bmi, 1)
   print(f"Your bmi is: {bmi}")
   time.sleep(1)
   again()

main()








