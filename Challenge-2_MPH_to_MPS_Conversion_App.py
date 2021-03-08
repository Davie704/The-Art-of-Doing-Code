#Basic Data Types Challenge 2: MPH to MPS Conversion App

print("\nWelcome to the MPH to MPS Conversion App")

#Gather user input
mph = float(input("\nWhat is your speed in miles per hour: "))

#Convert to MPS
mps = mph*0.4474
mps = round(mps, 3)

print("Your speed in meters per second is " + str(mps) + ".")
