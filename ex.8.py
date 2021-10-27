from RobotArm import RobotArm

robotArm = RobotArm('exercise 8')
# Jouw python instructies zet je 

robotArm.moveRight()
for total in range (7):
    for movement in range (8):
            robotArm.grab()
            robotArm.moveRight()
    robotArm.drop()
    for movement in range (8):
        robotArm.moveLeft()
    robotArm.wait()



    
    
        
       
      
   

# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()