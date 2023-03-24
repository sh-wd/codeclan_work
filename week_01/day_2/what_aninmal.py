# SET animal = INPUT "what animal are you?"
# IF animal is "chicken"
#   THEN PRINT "This is my favourite animal"
# ELSE IF animal is "dog"
#   THEN PRINT "I love dogs"
# ELSE
#   THEN PRINT "Sadly not my favourite"
# END

animal = input("What animal are you?")

if animal == "chicken":
    print("This is my favourite animal!")
elif animal == "dog":
    print("I love dogs!")
else:
    print("Sadly not my favourite animal")

result = "pass" if animal == "chicken" else "fail"