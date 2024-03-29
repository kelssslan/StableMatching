
import random
from timeit import default_timer as timer

# Options for Hospitals to choose (k x n matrix)
HOptions = []

#Options for Students to choose
SOptions = [] 


#List of preferences based on the options generated
HIndex = []
SIndex = []

# 2D matrix of all the preferences in their corresponding order (k X n matrix)
HList = [] 
SList = []


def generateList(n,k):
  
  #randomizing n non repeating numbers from the range (0, n-1) for k times
  for i in range(k):
    HOptions.append(random.sample(range(n), n))
    SOptions.append(random.sample(range(n), n))
  
  #randomize n numbers
  for j in range (n):
    v1 = random.randint(0,k-1)
    v2 = random.randint(0,k-1)
    
    
    HList.append(HOptions[v1])
    SList.append(SOptions[v2])

    HIndex.append(v1)
    SIndex.append(v2)


  return

def displayList(n,k):
  print()

  print("Hospital Options")
  for i in range(len(HOptions)):
    print(HOptions[i])
  
  print()

  print("Student Options")
  for j in range(len(SOptions)):
    print(SOptions[j])

  print()

  print ("Hospital Preferences")
  print(HList)
  
  print()

  print ("Student Preferences")
  print(SList)
  print()

  return

# current - current individual that is proposed to
# originalC - original candidate
# newC - new candidate to consider

def preferredCandidate(current,originalC,newC, candidateList):
  oldIndex = candidateList[current].index(originalC)
  newIndex = candidateList[current].index(newC)

  if (newIndex < oldIndex ):
    return True
  else:
    return False

def GaleShapely(n,k, finderList, candidateList):


  #finderList -> finder (proposing )'s list of preferences (Hospital)
  #candidateList -> candidate (being proposed to)'s list of perferences (student)

  #each index corresponds to the hospital/student 
  # if -1 is present then that means the hospital has not been matched
  # example (0,1,-1) H0 is matched with S0, H1 is matched with S1, H2 has not found a match yet

  fMatching = [-1] * n 
  cMatching = [-1] * n
  count = 0;

  while -1 in fMatching:

    # i represents the current Hospital that is proposing 
    # j represents the current student that is being proposed

    for i in range (len(finderList)):

      if (fMatching[i] != -1):
        continue

      for j in range (len(finderList[0])):

       
        temp = finderList[i][j] #gives student

        if temp not in fMatching:
       
          fMatching[i] = temp
          cMatching[temp] = i 
          break
          

        elif (preferredCandidate(temp, cMatching[temp],i, candidateList)):
      
          fMatching[i] = temp
          old = cMatching[temp]
          cMatching[temp] = i

          fMatching[old] = -1

          break
          

        else:
          continue
  return fMatching  

def printResults():
  # hospitals propose to students

  print("Matching for hospitals as priority is")
  results1 = GaleShapely(n,k, HList, SList)

  for i in range(len(results1)):
    print("Hospital ", i,"is matched with Student", results1[i] )

  print()
  

  #students propose to hospitals
  print("Matching for students as priority is")
  results2 = GaleShapely(n,k, SList, HList)

  for i in range(len(results2)):
    print("Student ", i,"is matched with Hospital", results2[i] )

  print()
  

  
temp = str(input())
consoleInput = temp.split()


#check if the user input is 1 or 2 numerical values

if (len(consoleInput) > 1):  # 2 inputs
   n = int(consoleInput[0]);
   k = int(consoleInput[1]);

else:  # 1 input
  n = int(consoleInput[0]);
  k = n

generateList(n,k)
displayList(n,k)
printResults()



