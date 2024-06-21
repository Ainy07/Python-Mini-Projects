H = float(input('Enter your height in meters: '))
W = float(input('Enter your weight in kg: '))
BMI = W / (H * H)
print('Your Body Mass Index is: ', BMI)

if BMI > 0:
    if BMI <= 16:
        print('You are severely underweight :(')
    elif BMI <= 18.5:
        print('You are underweight :(')
    elif BMI <= 25:
        print('Hooray! You are healthy :)')
    elif BMI <= 30:
        print('Oops! You are overweight :(')
    else:
        print('You are suffering from obesity.')
else:
    print("Kindly enter valid details")
