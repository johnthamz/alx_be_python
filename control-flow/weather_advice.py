# Weather Recommendation Program
#Python script that ask the user about the current weather conditions and provide clothing

# Ask the user for the current weather condition
weather = input("What's the weather like today? (sunny/rainy/cold):")

# Use conditional statements to give clothing advice
if weather == "sunny":
    print("Wear a t-shirt and sunglassses.")
elif weather == "rainy":
    print("Don't forget your umbrella and raincoat.")
elif weather == "cold":
    print("Make sure to wear a warm coat and a scarf.")
else:
    print("Sorry, I don't have recommondations for this weather.")