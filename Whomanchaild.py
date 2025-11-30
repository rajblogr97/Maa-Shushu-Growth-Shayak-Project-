



import datetime
import time
for i in range(5):
        print ("🔱🌹🌹Welcome To ❤ Maa Shishu Shayak System🌹🌹🔱")
        time.sleep(0.2)
        print ("=====🌄======🌹How Can Help you🌹======🌄=========")
        time.sleep(0.2)
        print ("🔷️🔷️🔷️🔷️🔷🔶️Whomen Chaild Develapment🔷️🔷️🔷️🔷️🔷️🔷️🔶️")
        time.sleep(0.2)
name = input("Wel🌹come Enter Your name :=")
presentHour= datetime.datetime.now().hour
if 5 <= presentHour <=11:
        print ("🌹🌹🌄Good Morning🌄🌹🌹",name)
elif 11<= presentHour <=17:
        print ("😊😊😊Good Afternoon😊😊😊",name)
elif 17<= presentHour <=20:
        print ("🌈🌈🌈Good Evening🌈🌈🌈",name)
else:
        print ("😴😴😴Good Night😴😴😴",name)


def classify_child_growth(age_months, sex, height_cm, weight_kg):
    """
    Bahut simple approx rules:
    - 0-6 months: 3-8 kg, 50-68 cm
    - 6-24 months: 7-12 kg, 65-88 cm
    - 2-6 years: 10-22 kg, 80-118 cm
    Real life me WHO tables chahiye, yeh sirf demo educational logic hai.
    """

    if age_months <= 6:
        min_w, max_w = 3.0, 8.0
        min_h, max_h = 50.0, 68.0
    elif age_months <= 24:
        min_w, max_w = 7.0, 12.0
        min_h, max_h = 65.0, 88.0
    else:
        # 2-6 saal ~ 24-72 months
        min_w, max_w = 10.0, 22.0
        min_h, max_h = 80.0, 118.0

    # Weight status
    if weight_kg < min_w:
        w_status = "weight thoda KAM lag raha hai."
    elif weight_kg > max_w:
        w_status = "weight THODA ZYADA lag raha hai."
    else:
        w_status = "weight age ke hisab se THEEK lag raha hai."

    # Height status
    if height_cm < min_h:
        h_status = "height thodi KAM lag rahi hai."
    elif height_cm > max_h:
        h_status = "height AGE se zyada hai (ye bhi normal ho sakta hai)."
    else:
        h_status = "height age ke hisab se THEEK lag rahi hai."

    message = (f"Bacche ka approx range: weight {min_w}-{max_w} kg, "f"height {min_h}-{max_h} cm."f"A>
        "Yeh sirf ek educational tool hai, final salah ke liye "
        "hamesha doctor/anganwadi/ANM se milen.")

    # Overall status choose karo
    if "KAM" in w_status or "KAM" in h_status:
        overall = "Growth THODI KAM ho sakti hai."
    elif "ZYADA" in w_status:
        overall = "Growth THODI ZYADA ho sakti hai."
    else:
        overall = "Growth LAGBHAG NORMAL lag rahi hai."

    return overall, message


def classify_pregnancy_growth(height_cm, pre_preg_weight_kg, current_weight_kg, week):
    """
    Simple pregnancy helper:
    - BMI calculate karta hai
    - Trimester nikalta hai
    - Weight gain ka approx idea deta hai
    Real practice me WHO/IOM charts chahiye, yeh sirf demo hai.
    """
    height_m = height_cm / 100
    bmi = pre_preg_weight_kg / (height_m ** 2)

    if week <= 13:
        trimester = 1
    elif week <= 27:
        trimester = 2
    else:
        trimester = 3

    gained = current_weight_kg - pre_preg_weight_kg

    # Rough BMI category
    if bmi < 18.5:
        bmi_cat = "underweight"
        rec_min, rec_max = 12, 18   # full pregnancy ke dauran approx
    elif bmi < 25:
        bmi_cat = "normal"
        rec_min, rec_max = 11, 16
    elif bmi < 30:
        bmi_cat = "overweight"
        rec_min, rec_max = 7, 11
    else:
        bmi_cat = "obese"
        rec_min, rec_max = 5, 9

    # Trimester ke hisab se approx fraction (bahut rough)
    if trimester == 1:
        frac = 0.2
    elif trimester == 2:
        frac = 0.6
    else:
        frac = 1.0

    t_min = rec_min * frac
    t_max = rec_max * frac

    if gained < t_min:
        status = "Aapka weight gain thoda KAM lag raha hai."
    elif gained > t_max:
        status = "Aapka weight gain thoda ZYADA lag raha hai."
    else:
        status = "Aapka weight gain is stage par LAGBHAG THEEK lag raha hai."

    message = (f"Aapka BMI lagbhag: {bmi:.1f} ({bmi_cat})." f"Pregnancy week: {week} (trimester {trim>
        "Yeh sirf educational tool hai. Kisi bhi doubt me gynecologist/ANM se zaroor milen.")

    return status, message


def get_lactation_info():
    """
    Lactating women ke liye basic information (hard-coded text).
    """
    info_lines = [
        "• Janm ke baad pehle 6 mahine sirf maa ka doodh (exclusive breastfeeding) ki salah di jati h>
        "• Har 2-3 ghante me bacche ko feed karna chahiye, raat me bhi.",
        "• Baccha thik feed le raha hai ya nahi: din me 6-8 baar geela diaper, weight dheere-dheere b>
        "• Danger signs: bilkul susu na karna, bahut kam roona, bahut sust rehna, tez bukhar, saans l>
        "Aise cases me turant najdi ki hospital/ANM/doctor se milen. Yeh tool sirf jankari ke liye ha>
    ]
    return "".join(info_lines)


def run_growth_helper():
    """
    Main menu: yahi 'agent system' ka entry point hai.
    """
    print ("=======🔶️🔷️=======🌹🌹Welcom🌹🌹====🔷️🔶️=====")
    print ("❤❤❤❤❤Maa Shishu🚻🚻🚻 Growth Sahayak❤=======)")
    print ("===================🌹🌹🌹====================")

    while True:
        print ("Aap kaun hain? (Choose option number)")
        print ("1 - Pregnant woman (garbhavati)")
        print ("2 - Child 0-6 years")
        print ("3 - Lactating woman (stanpan karne wali)")
        print ("4 - Exit")
        choice = input("Option: ").strip()

        if choice == "2":
            try:
                age = int(input("Bacche ki umra (months me): "))
                sex = input("Ladka (M) / Ladki (F): ").strip().upper()
                ht = float(input("Height (cm): "))
                wt = float(input("Weight (kg): "))
                overall, msg = classify_child_growth(age, sex, ht, wt)
                print ("--- Child Growth Result ---")
                print (overall)
                print (msg)
                print ("---------------------------")
            except Exception as e:
                print ("Input me error aa gaya, dobara koshish karein.")
                elif choice == "1":
            try:
                h = float(input("Aapki height (cm): "))
                pre = float(input("Pregnancy se pehle weight (kg): "))
                cur = float(input("Abhi ka weight (kg): "))
                wk = int(input("Pregnancy week: "))
                status, msg = classify_pregnancy_growth(h, pre, cur, wk)
                print ("--- Pregnancy Growth Result ---")
                print (status)
                print (msg)
                print ("--------------------------------")
            except Exception as e:
                print ("Input me error aa gaya, dobara koshish karein.")

        elif choice == "3":
            print ("--- Lactation Information ---")
            print (get_lactation_info())
            print ("-----------------------------")

        elif choice == "4":
            print ("Dhanyavaad! Swasth rahen, doctor ki salah jaroor lein.")
            break

        else:
            print ("Galat option. 1, 2, 3 ya 4 choose karein.")


# Program start
if __name__ == "__main__":
    run_growth_helper()

                
  
