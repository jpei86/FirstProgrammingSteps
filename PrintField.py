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
  numberOfFields = 6
  # call function to print the field
  # printField(fieldSize, fieldType)
  printGameBoard(fieldSize, fieldType, numberOfFields)
  
def printGameBoard(fieldSize, fieldType, numberOfFields):

  # create the separator between lines
  dashes = ("-" * (fieldSize * numberOfFields + numberOfFields + 1))
  
  # reserve variable and already add the first line
  gameboard=dashes+"\n"
  
  # loop to write all fields (rows)
  for i in range(0,numberOfFields):
    # write all lines for one field
    for j in range(0,fieldSize):
      # at the beginning of the line add separator
      gameboard = gameboard + "|"
      # loop to write all fields (columns)
      for k in range(0,numberOfFields):
        # inner loop writing one column
        for l in range(0,fieldSize):
          gameboard=gameboard+fieldType
        # after writing the column add a separator
        gameboard=gameboard+"|"
      # after writing the line add a newline
      gameboard=gameboard+"\n"
    # after field is added, add a separator
    gameboard = gameboard + dashes + "\n"
  gameboard = gameboard[:62] + "1" + gameboard[62 + 1:]
  print (gameboard)

  
if __name__ == '__main__':
  main()