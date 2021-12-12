print("this " + str(50))
print(f"this {50}")  # version since 3.6
print(f"this {20 * 24 * 60} minutes")  # f=format
print(f"this {25 * 24 * 60 * 60} seconds")
to_second = 24 * 60 * 60
to_minutes = 24 * 60
name_of_unit = "seconds"
name_of_unit1 = "minutes"


def days_to_units(num_of_days, message):
    print(f"this {num_of_days * to_minutes} {name_of_unit1}")
    print(f"this {num_of_days * to_second} {name_of_unit}")
    print(message)


# doesn't work because you have to call the fct


days_to_units(20, "good")


def days_to_unitss(num_of_days):
    # if num_of_days > 0:
    return f"this {num_of_days * to_minutes} {name_of_unit1}"


""" elif num_of_days == 0:
 return "this is a 0"
 else:
 return "negative num babaaaaaay" """


def ifff():
    try:  # (with if) user_input.isdigit(): with this fnct we don't filter out - it only accepts + integer+0
           # number = int(i)  # nrodoha i 3la 5ter boucle for snn kenit user_input 3adya
        number = int(days_unit_dict["days"])
        if number > 0:  # nested if else
            my_var = days_to_unitss(number)
            print(my_var)
        elif number == 0:
            print("dis a 0")
        else:   # we have to bring back - validation with except (no .isdigit fnct)
            print("dis -")
    except ValueError:  # write only (except) to cover all types of error
        print("not a number you fucked up")


# while True:  # True always majus in python
user_input = ""  # lezem initialisation snn y9olik mehech definie lvariable
"""while user_input != "exit":
    user_input = input("enter days fraise\n")  # \n for tarja3 listar
    print(type(user_input.split(", ")))  # titsaref fil les espaces bich lprint tji behya
    print(user_input.split(", "))
    #for i in user_input.split():  # t7ot espace bin les valeurs snn tiktib separateur li t7ib 3lih fi wist fct split
     #ifff()"""


"""while user_input != "exit":
     user_input = input("enter days fraise\n")
     listofdaysset = (user_input.split(", "))
     print(listofdaysset)
     print(set(listofdaysset))
     print(type(listofdaysset))
     print(type(set(listofdaysset)))

     for i in set(listofdaysset):
        ifff() """

while user_input != "exit":
        user_input = input("heet days and unit\n")
        days_unit = (user_input.split(":"))
        print(days_unit)
        days_unit_dict = {"days": days_unit[0], "unit": days_unit[1]}
        print(days_unit_dict)
        ifff()
