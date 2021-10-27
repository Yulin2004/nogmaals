from RobotArm import RobotArm

robotArm = RobotArm('exercise 9')
# Jouw python instructies zet je vanaf
robotArm.speed = 3
for i in range (4):
    for i in range (4):
        robotArm.grab()
        [robotArm.moveRight() for movement in range (5)]
        robotArm.drop()
        [robotArm.moveLeft() for movement in range (4)]
    [robotArm.moveLeft() for x in range (4)]
robotArm.wait()

