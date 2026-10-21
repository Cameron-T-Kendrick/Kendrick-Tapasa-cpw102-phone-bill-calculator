# -base tolerance 
# -
# -input GB used
# -input Base Plan Cost
# -
# -int calc of Gb over to buckaroos
# -
# -if gb <= 5 then is moderate
# -if gb > 5  then is HIGH
# -
# -Output Status on usage "You are within your data limit" OR "You are (number) GB over your limit"
# -Output Total Bill

base_tolerance = 10

def is_under(gb):
    return gb <= 0

def convert(gb):
    gb = gb - base_tolerance  
    return gb


def main():
    user_gb = float(input("Enter GB used: "))
    user_base_plan = float(input("Enter Base Plane cost: "))

    gb = convert(user_gb)
    base = user_base_plan

    bucks = gb * 2 + base

    
    if is_under(gb):
        print("You are within your data limit.")
        print(f"Total Bill: ${base}") 
    elif gb <=5:
        print(f"You are {gb} GB over your limit")
        print("Moderate Extra GB Usage")
        print(f"Total Bill: ${bucks}")
    elif gb > 5:
        print(f"You are {gb} GB over your limit")
        print("High Extra GB Usage")
        print(f"Total Bill: ${bucks}")

main()





  
