def get_age(yr):
    age=2018-yr
    if age < 18:
        print("you are a minor")
    elif age > 18 and age < 36:
        print("you are a youth")
    elif age > 36:
        print("you are an elder")

if __name__ == '__main__':
    x = int(input("enter year of birth: "))
    get_age(x)