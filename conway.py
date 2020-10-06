import random, time, copy
WIDTH = 60
HEIGHT = 20

# List of list for the cells 
nextCells = []
for x in range(WIDTH):
  column = [] # creates a new column 
  for y in range(HEIGHT):
    if random.randint(0, 1) == 0:
      column.append('#') #Adds living cell
    else:
      column.append(' ') #Add dead cell
  nextCells.append(column) #list of column list 

#Main program Loop 
while True:
  print('\n\n\n\n\n') #Seperate each with new lines
  currentCells = copy.deepcopy(nextCells)
  for y in range(HEIGHT):
    for x in range(WIDTH):
      print(currentCells[x][y], end='')
    print()
#Calculate next steps cells based on current cells 
for x in range(WIDTH):
  for y in range(HEIGHT):
    #get coordinates 
    #'% WIDTH' ensures is always between width 0 - 1
    leftCoord = (x - 1) % WIDTH
    rightCoord = (x + 1) % WIDTH
    aboveCoord = (y - 1) % HEIGHT
    belowCoord = (y + 1) % HEIGHT

    #Count number of living neighbors
    numNeighbors = 0
    if currentCells[leftCoord][aboveCoord] == '#':
      numNeighbors += 1
    if currentCells[x][aboveCoord] == '#':
      numNeighbors += 1
    if currentCells[rightCoord][aboveCoord] == '#':
      numNeighbors += 1
    if currentCells[leftCoord][y] == '#':
      numNeighbors += 1
    if currentCells[rightCoord][y] == '#':
      numNeighbors += 1
    if currentCells[leftCoord][belowCoord] == '#':
      numNeighbors += 1
    if currentCells[x][belowCoord] == '#':
      numNeighbors += 1
    if currentCells[rightCoord][belowCoord] == '#':
      numNeighbors += 1
    
    #Set cell based on Conway's Life rules:
    if currentCells[x][y] == '#' and (numNeighbors == 2 or numNeighbors == 3):
      #Living cells with 2 or 3 neighbors stay alive:
      nextCells[x][y] = '#'
    elif currentCells[x][y] == ' ' and numNeighbors == 3:
      #Dead cells with 3 neighbors become alive:
      nextCells[x][y] = '#'
    else:
      nextCells[x][y] = ' '
      
  time.sleep(1) #Add 1 second delay to reduce flickering

    
