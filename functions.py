
# import random
import random

def isNotEmpty(value=""):
  if(value!=None and value!=""):
    return True
  else:
    False



def generateUnid(lent=4):
  newval=""
  list1=("a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","A","B","C","D","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z",1,2,3,4,5,6,7,8,9,0)
  for i in range(lent):
    newval+=f"{random.choice(list1)}"
  return newval




# print(generateUnid(8))