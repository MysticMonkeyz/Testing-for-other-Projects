def changecase(func): #feed returns of a function into the function
  def myinner(): #creates a function myinnner in the function
    return int(func()) - 1 #converts returns of the function into and integer and minus' 1 and returns that value from myinner function
  return int(myinner) #returns the returns from myinner (defaults to a string without int specified)

@changecase #calls for function
def myfunction(): #function to feed into changecase
  return 5 #the value being fed as it is the return

print(myfunction())

#Prints 4
