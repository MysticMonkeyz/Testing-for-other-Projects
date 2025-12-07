def changecase(func): #feed returns of a function into the function
  def myinner(): #creates a function myinnner in the function
    dog, cat = func() #unpacking function returns
    return int(dog) - 1, int(cat) - 1 #converts returns of the function into and integer and minus' 1 and returns that value from myinner function
  return myinner 

@changecase #calls for function
def myfunction(): #function to feed into changecase
  return (5, 4) #the value being fed as it is the return

print(myfunction())

#Prints 4, 3
