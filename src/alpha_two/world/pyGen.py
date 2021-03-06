#! /usr/bin/env python
from subprocess import Popen, PIPE
import subprocess
import sys
import random

#Usage Instructions
if (len(sys.argv)!=3):
    print ("Usage:  python pyGen.py <number of sheep>  <Field number (1-4)>")
    sys.exit()
numSheep = int(sys.argv[1])
numGrass = 10
fieldNumber = int(sys.argv[2])

#Reading myworld.world file
ins = open( "myworld.world", "r" )
array = []
for line in ins:
    array.append(line)
ins.close()

commandArray =  []
sheepNum = 26

#Creating sheep in random places around that chosen field
for i in range(0,numSheep):
    command =  []
    if (fieldNumber == 1):
        x = random.randint(2,28)
        y = random.randint(2,28)
    elif (fieldNumber == 2):
        x = random.randint(2,28)
        y = -(random.randint(2,28))
    elif (fieldNumber == 3):
        x = -(random.randint(2,28))
        y = -(random.randint(2,28))
    elif (fieldNumber == 4):
        x = -(random.randint(2,28))
        y = random.randint(2,28)
    angle  = random.randint(1,359)
    line = "myRobot( pose [" +str(x)+" "+str(y) + " 0 "+str(angle)+" ] name \"r"+str(i)+"\" color \"white\" )"

    array.append(line)
    line = "mySheepsPoop( pose [" +str(x)+" "+str(y) + " 0.1 "+str(angle)+" ] name \"poop"+str(i)+"\" color \"brown\" )"
    array.append(line)
    #command.append("source ../../../devel/setup.bash\n")
    command.append("rosrun alpha_two R1 "+str(sheepNum)+"  "+str(x)+" "+str(y)+" " +str(angle)+"\n")    

    subprocess.Popen("rosrun alpha_two R1 "+str(sheepNum)+"  "+str(x)+" "+str(y)+" " +str(angle),shell=True,stdout = PIPE)
    sheepNum = sheepNum + 2   
  
grassNum = 26 + numSheep*2  

#Creating grass in field 1
for i in range(0,numGrass):
    x = random.randint(1,29)
    y = random.randint(1,29)
    line = "myGrass( pose [" +str(x)+" "+ str(y) + " 0 0 ] name \"g"+str(i)+"\" color \"green\" )"
    array.append(line)
    subprocess.Popen("rosrun alpha_two grass "+str(grassNum)+"  "+str(x)+" "+str(y),shell=True,stdout = PIPE)
    grassNum = grassNum + 1

#Creating grass in field 2
for i in range(0,numGrass):
    x = random.randint(1,29)
    y = -(random.randint(1,29))
    line = "myGrass( pose [" +str(x)+" "+ str(y) + " 0 0 ] name \"g"+str(i+numGrass)+"\" color \"green\" )"
    array.append(line)
    subprocess.Popen("rosrun alpha_two grass "+str(grassNum)+"  "+str(x)+" "+str(y),shell=True,stdout = PIPE)
    grassNum = grassNum + 1

#Creating grass in field 3
for i in range(0,numGrass):
    x = -(random.randint(1,29))
    y = -(random.randint(1,29))
    line = "myGrass( pose [" +str(x)+" "+ str(y) + " 0 0 ] name \"g"+str(i+numGrass*2)+"\" color \"green\" )"
    array.append(line)
    subprocess.Popen("rosrun alpha_two grass "+str(grassNum)+"  "+str(x)+" "+str(y),shell=True,stdout = PIPE)
    grassNum = grassNum + 1

#Creating grass in field 4
for i in range(0,numGrass):
    x = -(random.randint(1,29))
    y = random.randint(1,29)
    line = "myGrass( pose [" +str(x)+" "+ str(y) + " 0 0 ] name \"g"+str(i+numGrass*3)+"\" color \"green\" )"
    array.append(line)
    subprocess.Popen("rosrun alpha_two grass "+str(grassNum)+"  "+str(x)+" "+str(y),shell=True,stdout = PIPE)
    grassNum = grassNum + 1

#Opening new file to write 
ins = open( "newmyworldpython.world", "w" )

#Writing to file
for line in array:
  ins.write("%s\n" % line)
ins.close()


#Running farm controller script
p1 = Popen("rosrun alpha_two farm",shell=True,stdout=PIPE)

#Running cloud controller
p2 = Popen("rosrun alpha_two cloud",shell=True,stdout=PIPE)

#Running stageros to start simulation
p=Popen("rosrun stage stageros newmyworldpython.world",shell=True,stdout=PIPE) 



    


