from PortMap import *
from MissionBase import *
from Actions import *
from BasicDriveActions import *
from Estimation import *
from AdvancedActions import *
import autotime
#5 west
#2 north
#facing north
#blue home
#attachment down
#tray loaded
class CraneMission(MissionBase):
    def routine(self): 
        driveBase.settings(turn_rate=90),
        self.runAction(SeriesAction(
            DriveStraightAction(415),
            DriveTurnAction(-45),
            DriveStraightAction(250),
            DriveTurnAction(-45),
            DriveStraightAction(630)))
        driveBase.settings(turn_rate=45)
        self.runAction(SeriesAction(
            DriveTurnAction(90),
            DriveStraightAction(170),
            DriveStraightAction(-50),
            SpinMotor(300, 145),
            DriveStraightAction(-80),
            DriveTurnAction(-180),
            DriveStraightAction(110),
            SpinMotor(180,1460),
            DriveStraightAccurate(-60),
            DriveTurnAction(-90),
            DriveStraightAction(-200),
            DriveTurnAction(90),
            DriveStraightAction(-70),
            DriveStraightAction(50),  #  \ Edit these values to change where the
            DriveTurnAction(-90),     #  | robot ends up at the stage.
            DriveStraightAction(790), #  /
            #-----
            ExitAction(), #This is a hacky way of doing this, but ExitAction
                          #stops the program when its start method is called.
            ParallelAction(
                SpinMotor(230,-1460),
                SeriesAction(
                DriveStraightAction(-66),
                DriveTurnAction(-90),
                DriveStraightAction(700))),
            SpinMotor(430,1230),
            #-----
            #Kaitlynn: Based on your mom's text, it sounds like you may have
            #already started, but hopefully these comments are still helpful.
            #You may be able to use some of the following. If you decide to do
            #so, you'll probably have to remove most of what's between the
            #-----s, and definitely the ExitAction. You may still want the
            #travel in a ParallelAction with a SpinMotor, but you might be able
            #to just turn the motor by the delta of the heights instead of going
            #all the way down and up again.
            DriveStraightAction(65),
            DriveTurnAction(-110),
            DriveStraightAction(20),
            DriveTurnAction(-90),
            DriveStraightAction(-180),
            DriveTurnAction(-95),
            DriveStraightAction(195),
            DriveStraightAction(110),
            DriveTurnAction(180),
            SpinMotor(430,-1230),
            DriveStraightAction(115),
            DriveTurnAction(-75)
            ))

if __name__ == "__main__": #run on file run but not import
    CraneMission()
    CraneMission = CraneMission()
    CraneMission.run()
