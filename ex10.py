from pygame.constants import GL_FRAMEBUFFER_SRGB_CAPABLE
from RobotArm import RobotArm

robotArm = RobotArm('exercise 10')
# Jouw python instructies zet je vanaf
from RobotArm import RobotArm
robotArm = RobotArm('exercise 10')             
moveR = 9
moveL = 8
for movement in range (5):
    robotArm.grab()
    [robotArm.moveRight() for movement in range (moveR)]
    robotArm.drop() 
    [robotArm.moveLeft() for movement in range (moveL)]
    moveR = moveR -2
    moveL = moveL -2
robotArm.wait()

   
        
    

     
  


robotArm.wait()
