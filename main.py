print "Hello! This is a unit converter."

while True:
    kilometers = int ( raw_input ("Tell us the number you want to convert.") )
    miles = kilometers * 0.621371
    print("%s kilometers is %s miles." % (kilometers, miles))

    choice = raw_input ( "Would you like to do another conversion (y/n):" )
    if choice != "y":
        print "Thank you for using our services."
        break