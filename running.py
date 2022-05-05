temp = float(input("What is the temperature outside? "))

if temp > 70:
    print("It's too hot outside. Better find something else for today.")
elif temp < 0:
    print("It's too cold. Stay inside!")
else:
    print("The temperature seems ok...")

    weather = input("What are the current weather conditions (rain, snow, meteor, sun)? ")

    # This changes the weather variable to permanently store the lowercase version
    weather = weather.lower()

    if weather == "sun":
        print("Enjoy your run")
    elif weather == "snow":
        print("Stay inside!")
    else:
        print("Sounds a little sketchy")

# This doesn't permanently change the variables value
#if weather.lower() == "sun":


# We haven't talked about this, but this checks to see if it's in the list of choices...
# if weather in ["sun", "sunny", "bright"]:
