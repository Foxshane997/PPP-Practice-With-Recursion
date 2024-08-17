# Name KWARGS Function

def name_args   (**kwargs):
    for key, value in kwargs.items():
        print(f"{key} : {value}");

name_args(name="Ali", age=30, city="california");