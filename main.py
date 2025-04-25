import os
import random
import json

dir = "C:/"
blanks = 5
bullet = 1


def deletef():
    files = os.listdir(dir)

    if files:
        random_file = random.choice(files)
        fpath = os.path.join(dir, random_file)

    #daa of deleted paths
    data = {
        "deleted": {fpath}
    }

    #makes a json file
    with open("data.json", "w") as file:
        json.dump(data, file, indent=4)

    os.remove(fpath)

def shoot():
    live = False
    choice = random.randint(1, 6)
    if choice < 6:
        print("U got lucky this time")
        return False
    elif choice == 6:
        deletef()
        return True

print("Welcome to PC Roullete")
print("You'll be given a deletevolver with 1 bullet")
print("You can shoot or reload")
print("If u get shot a random file will be deleted FOREVER")
ans = input("start to start")

while True:
    if ans == "start":
        print(f"U have { blanks } blanks left")
        ans1 = input("Shoot or reload?")
        if ans1 == "shoot" or "Shoot":
            result = shoot()
            if result == False:
                blanks -= 1
                print(f"U survived, u have { blanks } blanks left")
            elif result == True:
                print("You died")