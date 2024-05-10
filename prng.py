import random
import time

print("prng.py is running...")


while True:

    with open("number-service.txt", "r") as infile:
        request = infile.read()

    if request == "request":
        number = str(random.randint(1, 20))

        with open("number-service.txt","w") as outfile:
                outfile.write(number)

    time.sleep(1)


    
