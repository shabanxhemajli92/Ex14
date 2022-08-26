print("Let's find nemo ")
stupid_fish="I am finding Nemo "
stupid_fish1="I found Nemo at  "
stupid_fish2="I found Nemo at "
word = "Nemo"
find_theindex=stupid_fish.find(word)
find_theindex1=stupid_fish1.find(word)
find_theindex2=stupid_fish2.find(word)
print("(1) I found nemo at" , "(2)Nemo is me" , "(3) I found nemo at")
choice = input("choose: ")
if choice == "1":
    print(stupid_fish + str(find_theindex))
elif choice == "2":
    print(stupid_fish1 + str(find_theindex1))
elif choice == "3":
    print(stupid_fish2 + str(find_theindex2))
else:
    print("I can't find Nemo :(")