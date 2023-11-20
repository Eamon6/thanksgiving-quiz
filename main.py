print("Thanksgiving quiz!")
ready = input("Are you ready? ")

if ready == "yes":
    print("Great!")
elif ready == "no":
    print("Too bad!")
print("For each multiple choice question, answer with the letter of your answer. For each true or false question, write 't' or 'f'")
q1 = input("""Question 1: Where did the first Thanksgiving take place?
a) Plymouth, Massachusetts
b) Philadelphia, Pennsylvania
c) Jamestown, Virginia
d) Albany, New York 
""")

if q1 != "a":
    print("Incorrect! the correct answer is a!")
else:
    print("Correct!")

q2 = input("""Question 2: True or false -- only male turkeys gobble.""")
if q2 != "t":
    print("Incorrect!")
else:
    print("Correct!")

q3= input("""Question 3: What percentage of Americans  eat turkey on Thanksgiving?
a) 95%
b) 88%
c) 78%
d) 60%
""")
if q3 != "b":
    print("Incorrect! the correct answer is b!")
else:
    print("Correct!")

q4 = input("""Question 4: How many turkeys do Americans prepare each Thanksgiving?
a) 30 million 
b) 58 million
c) 100 million
d) 46 million
""")
if q4 != "d":
    print("Incorrect! the correct answer is d!")
else:
    print("Correct!")

q5 = input("""Question 5: When did 'A Charlie Brown Thanksgiving' premier?
a) 1956 
b) 1973
c) 1970
d) 1966
""")
if q5 != "b":
    print("Incorrect! the correct answer is b!")
else:
    print("Correct!")

q6 = input("""Question 6: True or false -- Former President Calvin Coolidge once recieved a raccoon on Thanksgiving as a gift.""")
if q6 != "t":
    print("Incorrect!")
else:
    print("Correct!")


q7 = input("""Question 7: True or false -- Turkeys are debated to be the most intelligent bird.""")
if q7 != "f":
    print("Incorrect!")
else:
    print("Correct!")

print("Thank you for playing this Thanksgiving quiz!")