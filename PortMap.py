try:
    from pybricks.hubs import *
    from pybricks.parameters import *
    from pybricks.pupdevices import *
    from pybricks.robotics import *
    from pybricks.tools import *
except ModuleNotFoundError:
    pass
class Device:
    def __init__(self, **kwargs):
        if 'is_robot' in kwargs.keys():
            self.is_robot=kwargs['is_robot']
        else:
            self.is_robot=True
        if 'hub_type' in kwargs.keys():
            self.hub_type=kwargs['hub_type']
        elif self.is_robot:
            raise TypeError('must specify a hub type')
        else:
            self.hub_type='cpython'
        if 'supports_drive_base' in kwargs.keys():
            self.supports_drive_base=kwargs['supports_drive_base']
        else:
            self.supports_drive_base=False
        if 'motor_config' in kwargs.keys():
            self.motor_config=kwargs['motor_config']
        else:
            self.motor_config=[]
        if 'color_sensor_config' in kwargs.keys():
            self.color_sensor_config=kwargs['color_sensor_config']
        else:
            self.color_sensor_config=[]
    def __str__(self):
        output='portmap.Device('
        first_arg=True
        if self.is_robot!=True:
            if not first_arg:
                output+=', '
            first_arg=False
            output+=f'is_robot={self.is_robot}'
        if not first_arg:
            output+=', '
        first_arg=False
        output+=f'hub_type=\'{self.hub_type}\''
        if self.supports_drive_base!=False:
            if not first_arg:
                output+=', '
            first_arg=False
            output+=f'supports_drive_base={self.supports_drive_base}'
        if self.motor_config!=[]:
            if not first_arg:
                output+=', '
            first_arg=False
            output+=f'motor_config={self.motor_config}'
        if self.color_sensor_config!=[]:
            if not first_arg:
                output+=', '
            first_arg=False
            output+=f'color_sensor_config={self.color_sensor_config}'
        output+=')'
        return output
try:
    hub=CityHub()
    device=Device(hub_type='city')
except:
    try:
        hub=MoveHub()
        motor_left=Motor(Port.B, Direction.COUNTERCLOCKWISE)
        motor_right=Motor(Port.A, Direction.CLOCKWISE)
        drive_base=DriveBase(motor_left, motor_right, 50, 50)
        try:
            motor_external=Motor(Port.C)
            color_distance_sensor=ColorDistanceSensor(Port.D)
            device=Device(hub_type='move', supports_drive_base=True, motor_config=['motor_left', 'motor_right', 'motor_external'], color_sensor_config=['color_distance_sensor'])
        except:
            device=Device(hub_type='move', supports_drive_base=True, motor_config=['motor_left', 'motor_right'])
    except:
        try:
            hub=PrimeHub()
            try:
                motor_left=Motor(Port.E, Direction.COUNTERCLOCKWISE)
                motor_right=Motor(Port.A, Direction.CLOCKWISE)
                drive_base=DriveBase(motor_left, motor_right, 56, 113)
                color_sensor_left=ColorSensor(Port.F)
                color_sensor_right=ColorSensor(Port.B)
                device=Device(hub_type='prime', supports_drive_base=True, motor_config=['motor_left', 'motor_right'], color_sensor_config=['color_sensor_left', 'color_sensor_right'])
                #alias names from old PortMap for compatibility
                MotorLeft=motor_left
                MotorRight=motor_right
                driveBase=drive_base
                colorSensorLeft=color_sensor_left
                colorSensorRight=color_sensor_right
            except:
                device=Device(hub_type='prime')
        except:
            try:
                hub=TechnicHub()
                device=Device(hub_type='technic')
            except:
                try:
                    hub=InventorHub()
                    device=Device(hub_type='inventor')
                except:
                    try:
                        hub=EssentialHub()
                        device=Device(hub_type='essential')
                    except:
                        try:
                            hub=EV3Brick()
                            device=Device(hub_type='ev3')
                        except:
                            hub=None
                            device=Device(is_robot=False)