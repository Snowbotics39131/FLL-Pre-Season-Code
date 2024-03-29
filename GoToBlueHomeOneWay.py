from PortMap import *
from BasicDriveActions import *
from AdvancedActions import *
from MissionBase import *
class GoToBlueHome(MissionBase):
    def routine(self):
        self.runAction(DriveCurveAction(250, 90))
        self.runAction(DriveStraightAction(445))
        self.runAction(DriveTurnAction(20))
        try:
            motorBack.run_angle(200, 180)
        except:
            hub.speaker.beep()
        self.runAction(DriveCurveAction(100, -20))
        driveBase.straight(260)
        driveBase.turn(30)
        driveBase.straight(200)
        driveBase.turn(-75)
        driveBase.straight(120)
        driveBase.turn(90)
        driveBase.curve(600, -45)
if __name__=='__main__':
    motorBack.angle() #check if this throws an error so it won't later
    GoToBlueHome().run()
