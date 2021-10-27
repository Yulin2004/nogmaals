from RobotArm import RobotArm

robotArm = RobotArm('exercise 11')
robotArm.speed = 3

[robotArm.moveRight() for movement in range (8)]                        # begin helemaal aan de rechter kant!!!!!
for movement in range (9):                                              # anders leg je misschien een wit blok op een ander wit blok
    robotArm.grab()                                                     # en dan kan het onderste witte blok niet verplaatst worden
    color = robotArm.scan()
    if color == 'white':
        robotArm.moveRight()
        robotArm.drop()
        [robotArm.moveLeft() for movement in range (2)]
    else:
        robotArm.drop()
        robotArm.moveLeft()

robotArm.wait()
from RobotArm import RobotArm
