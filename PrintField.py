#!python

def printField (fieldSize, fieldType):
  field=""
  for j in range(0,fieldSize):
    for i in range(0,fieldSize):
      field=field+fieldType
    field=field+"\n"
  print (field)

def main():
  # parameters
  fieldSize = 3
  fieldType = "N"
  numberOfFields = 5
  # call function to print the field
  # printField(fieldSize, fieldType)
  printGameBoard(fieldSize, fieldType, numberOfFields)
  
def printGameBoard(fieldSize, fieldType, numberOfFields):
  gameboard=""
  #write the first line of gameboard
  for k in range(0,fieldSize):
    for m in range(0,fieldSize):
      for i in range(0,numberOfFields):
        for j in range(0,fieldSize):
          gameboard=gameboard+fieldType
        gameboard=gameboard+"|"
      gameboard=gameboard+"\n"
    #print dashes after line is finished
    print ("-" * (fieldSize * numberOfFields + numberOfFields))      
  print (gameboard)

  
if __name__ == '__main__':
  main()