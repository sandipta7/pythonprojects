import random
    
secret_number = random.randint(1,100)

while True:
    guess = int(input("Enter any number (1,100): "))

    difference = abs(guess - secret_number)

    if guess == secret_number:
       print("🎉 You got it! That's the exact number. You Nailed IT!!!")
       break

    elif difference <= 3:
        if guess > secret_number:
            print("🔥 Slightly too high, almost there!\n")
        else:
            print("🔥 Slightly too low, almost there!\n")
    elif difference <= 10:
        if guess > secret_number:
            print("☀️  A bit too high, but you're in the right neighborhood!\n")
        else:
            print("☀️  A bit too low, but you're in the right neighborhood!\n")
    else:
        if guess > secret_number:
            print("❄️ Cold... Way too High!!!\n")
        else:
            print("❄️ Cold... Way too Low!!!\n")