print("Title of program: MCQ revision program")
print()

counter = 0
score = 0
total_num_of_qn = 5


counter +=1
tracker = 0

while tracker !=1:
  
  print("Q"+str(counter)+") "+ "What is the chemical formula of Helium?")
  print("   a) He")
  print("   b) H")
  print("   c) El")
  print("   d) Helium")
  answer = input("Your answer: ")
  answer = answer.lower()
  if answer == "a":
    output = "Yes, that's right!"
    score -=1
  elif answer == "b":
    output = "Wrong. Refer to your periodic table again."
    score -=1
  elif answer == "c":
    output = "Wrong. Refer to your periodic table again."
    tracker =1
    score +=1
  elif answer == "d":
    output = "Wrong. Refer to your periodic table again."
    score -=1
  else:
    output = "Please choose a, b, c or d only."
  
  print()
  print(output)
  print()
  print("Your current score: " + str(round((score/total_num_of_qn*100),1)) + "%"  )
  print()
  print()
  


counter +=1
tracker = 0

while tracker !=1:
  
  print("Q"+str(counter)+") "+ "The chemical formula H2 represents")
  print("   a) one hydrogen molecule")
  print("   b) two hydrogen atoms")
  print("   c) one hydrogen atom")
  print("   d) two hydrogen molecules")
  answer = input("Your answer: ")
  answer = answer.lower()
  if answer == "a":
    output = "Yes, that's right!"
    tracker =1
    score +=1
  elif answer == "b":
    output = "Wrong. If so, then it will be written as H and H - two hydrogen atoms."
    score -=1
  elif answer == "c":
    output = "Wrong. Clearly the number 2 in the formulae must mean something?"
    score -=1
    
  elif answer == "d":
    output = "Wrong. What's the difference between a molecule and an atom?"
    score -=1
  else:
    output = "Please choose a, b, c or d only."

  print()
  print(output)
  print()
  print("Your current score: " + str(round((score/total_num_of_qn*100),1)) + "%"  )
  print()
  print()
  
  

counter +=1
tracker = 0

while tracker !=1:
  
  print("Q"+str(counter)+") "+ "Which represents the electronic configuration of a non-metal?")
  print("   a) 2,1")
  print("   b) 2,8,3")
  print("   c) 2,8,8,2")
  print("   d) 2,7")
  answer = input("Your answer: ")
  answer = answer.lower()
  if answer == "a":
    output = "Wrong. Think again - how many electron shells are filled, and which group is this in?"
    score -=1
  elif answer == "b":
    output = "Wrong.  Think again - how many electron shells are filled, and which group is this in?"
    score -=1
  elif answer == "c":
    output = "Wrong.  Think again - how many electron shells are filled, and which group is this in?"
    score -=1
    
  elif answer == "d":
    output = "Yes, that's right!"
    tracker =1
    score +=1
  else:
    output = "Please choose a, b, c or d only."

  

  print()
  print(output.lower())
  print()
  print("Your current score: " + str(round((score/total_num_of_qn*100),1)) + "%"  )
  print()
  print()
  
  while tracker !=1:
  
  print("Q"+str(counter)+") "+ "What is an example of osmosis?")
  print("   a) The spreading of the smell of perfume from the other side of the room.")
  print("   b) The absorbtion of water into the small intestines.")
  print("   c) The absorption of water from the soil by root hair cells.")
  print("   d) The spreading of a drop of ink after placed in water.")
  answer = input("Your answer: ")
  answer = answer.lower()
  if answer == "a":
    output = "Wrong. Osmosis reqiuires a membrane and can only take place with water molecules."
    score -=1
  elif answer == "b":
    output = "Wrong. Osmosis reqiuires a membrane and can only take place with water molecules."
    score -=1
  elif answer == "c":
    output = "Yes, that's right!"
    tracker =1
    score +=1
  elif answer == "d":
    output = "Wrong. Osmosis reqiuires a membrane and can only take place with water molecules."
    score -=1
  else:
    output = "Please choose a, b, c or d only."
  
  print()
  print(output)
  print()
  print("Your current score: " + str(round((score/total_num_of_qn*100),1)) + "%"  )
  print()
  print()
  
  while tracker !=1:
  
  print("Q"+str(counter)+") "+ "What is not present in a bacteria?")
  print("   a) Cell Wall")
  print("   b) Cytoplasm")
  print("   c) Nucleus")
  print("   d) Flagellum")
  answer = input("Your answer: ")
  answer = answer.lower()
  if answer == "a":
    output = "Wrong. The cell wall proptects the cell against osmosic stress and provides structural support."
    score -=1
  elif answer == "b":
    output = "Wrong. The cytoplasm protects the part of a cell and is very important."
    score -=1
  elif answer == "c":
    output = "Yes, that's right! The bacteria cell does not have a nucleus but DNA instead."
    tracker =1
    score +=1
  elif answer == "d":
    output = "Wrong. The bacteria cell needs a flagellum to move around."
    score -=1
  else:
    output = "Please choose a, b, c or d only."
  
  print()
  print(output)
  print()
  print("Your current score: " + str(round((score/total_num_of_qn*100),1)) + "%"  )
  print()
  print()
  
print("End of quiz!")
