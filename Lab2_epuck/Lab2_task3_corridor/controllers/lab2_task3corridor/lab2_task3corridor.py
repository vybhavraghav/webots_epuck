"""lab2_task3corridor controller."""

# You may need to import some classes of the controller module. Ex:
#  from controller import Robot, Motor, DistanceSensor
from controller import Robot, Camera, DistanceSensor
import time
# create the Robot instance.
robot = Robot()

def wall_follow(side):
    global fval , rval , lval , lps_val , rps_val
    while robot.step(timestep) != -1:
        fval , rval , lval = fds.getValue()*39.75 , rds.getValue()*39.75 , lds.getValue()*39.75
        lps_val = lps.getValue() 
        rps_val =rps.getValue()
        print('lps:' , lps_val , 'rps:' , rps_val)
        
        mean_val=7
        proportionality = 1
        
        print(f'fds : {fval} , rds {rval} , lds :{lval}')
        print(f'R variance: {5-rval} , L variance: {5 - lval}')
        
    
        if fval <= 7:
    
            rightMotor.setVelocity(0)
            leftMotor.setVelocity(0)
            print('stop')
            break
    
            
        else :
            if side == 'left':
                 variance = lval - mean_val
                 head_direction(-variance*proportionality , 10)
            elif side == 'right':
                 variance = rval - mean_val
                 head_direction(variance*proportionality , 10)
        
def head_direction(direction , vel):
    left_d = (50 + direction)/100
    right_d = (50 - direction)/100
    rightMotor.setVelocity(right_d*vel)
    leftMotor.setVelocity(left_d*vel)

def turn():
    global fval , rval , lval , lps_val , rps_val
    print(f'rps {rps_val} , lps :{lps_val}')
    
    if rval > 10:
        while robot.step(timestep) != -1:
            print('lps;',lps.getValue())
            if lps.getValue() < (lps_val + 3.3):
                head_direction(100,2)
            else:
                head_direction(0,0)
                break
    elif lval > 10 :
        while robot.step(timestep) != -1:
            print('rps;',rps.getValue())
            if rps.getValue() > (rps_val - 1.15):
                print('a')
                head_direction(-100,2)
            else:
                head_direction(0,0)
                break
    else :
        while robot.step(timestep) != -1:
            print(lps.getValue())
            if lps.getValue() <(lps_val + 6.6):
                head_direction(100,2)
            else:
                head_direction(0,0)
                break
# get the time step of the current world.
timestep = int(robot.getBasicTimeStep())

# You should insert a getDevice-like function in order to get the
# instance of a device of the robot. Something like:
#  motor = robot.getMotor('motorname')
#  ds = robot.getDistanceSensor('dsname')
#  ds.enable(timestep)

fds = robot.getDistanceSensor('front_ds')
lds = robot.getDistanceSensor('left_ds')
rds = robot.getDistanceSensor('right_ds')
fds.enable(timestep)
lds.enable(timestep)
rds.enable(timestep)


# enable camera and recognition
camera = robot.getCamera('camera1')
camera.enable(timestep)
camera.recognitionEnable(timestep)

# get handler to motors and set target position to infinity
leftMotor = robot.getMotor('left wheel motor')
rightMotor = robot.getMotor('right wheel motor')
leftMotor.setPosition(float('inf'))
rightMotor.setPosition(float('inf'))
leftMotor.setVelocity(0)
rightMotor.setVelocity(0)


lps= robot.getPositionSensor('left wheel sensor')
lps.enable(timestep)
lps_val= lps.getValue()
robot.step(timestep)
print(lps_val)
rps= robot.getPositionSensor('left wheel sensor')
rps.enable(timestep)
# Main loop:
# - perform simulation steps until Webots is stopping the controller
fval = rval = lval = lps_val = rps_val = float()



for i in range(4):
    print(i)
    wall_follow('left')
    turn()
    
print('completed left')
lps_val = lps.getValue()

while robot.step(timestep) != -1:
    print(lps.getValue())
    if lps.getValue() > lps_val - 1:
        head_direction(0,-2)
    else:
        head_direction(0,0)
        break
        
lps_val = lps.getValue()
while robot.step(timestep) != -1:
    print(lps.getValue())
    if lps.getValue() < lps_val + 3.3:
        head_direction(100,2)
    else:
        head_direction(0,0)
        break
        
for i in range(4):
    print(i)
    wall_follow('right')
    turn()
        
        

