from naoqi import ALProxy
from whole_positions import *
from positions import *
import os
import time
import sys

# Defining the class to support the use of NAO robot
class Nao:
    def __init__(self, NAO_IP, PORT):
        try:
            self.player = ALProxy("ALAudioPlayer", NAO_IP, PORT)
            self.motion = ALProxy("ALMotion", NAO_IP, PORT)
            self.posture = ALProxy("ALRobotPosture", NAO_IP, PORT)
        except Exception as e:
            print("Failed to connect to ALProxy:", e)
            sys.exit(1)  # Exit if connection fails


        self.ip = NAO_IP
        self.port = PORT

    def playMusic(self, music_path):
        return self.player.post.playFile(music_path)

    def stopMusic(self, song):
        return self.player.stop(song)

    def applyPosture(self, string):
        switch = {
            'Alternate': Alternate,
            'ArmDance': ArmDance,
            'BlowKisses': BlowKisses,
            'Bow': Bow,
            'Clap': Clap,
            'ComeOn': ComeOn,
            'Crouch': Crouch,
            'DanceMove': DanceMove,
            'DiagonalLeft': DiagonalLeft,
            'DiagonalRight': DiagonalRight,
            'ExtClap': ExtClap,
            'FingerFace': FingerFace,
            'HandsOnHips': HandsOnHips,
            'HeadFlex': HeadFlex,
            'Hello': Hello,
            'Joy': Joy,
            'MoveBackward': MoveBackward,
            'MoveForward': MoveForward,
            'PulpFiction': PulpFiction,
            'Rhythm': Rhythm,
            'Shuffle': Shuffle,
            'Sit': Sit,
            'SitRelax': SitRelax,
            'Sprinkler': Sprinkler,
            'Stand': Stand,
            'StandInit': StandInit,
            'StandZero': StandZero,
            'StayingAlive': StayingAlive,
            'TheRobot': TheRobot,
            'Wave': Wave,
            'WipeForehead': WipeForehead
        }

        function = switch.get(string, None)

        if function == None:
            raise ValueError('Unknown position' + str(function))
        else:
            function.main(self.ip, self.port)

def main():
    NAO_IP = sys.argv[1]     # retrieving first input argument
    PORT = int(sys.argv[2])  # retrieving second input argument

    print('')
    print('IP: ' + str(NAO_IP))
    print('PORT: ' + str(PORT))
    print('')

    music_path = os.path.abspath(os.getcwd()) + '/ferrari.wav'

    nao = Nao(NAO_IP, PORT)

    with open('choreography.txt', 'r') as file:
        choreography = [line.strip() for line in file]
    
    time.sleep(0.2)

    try:
        
        for move in choreography:
            nao.applyPosture(move)
        
            if move == 'StandInit':
                song = nao.playMusic(music_path)
                start = time.time()
            
            end = time.time()
            
            if move in MANDATORY_POSITIONS:
                print('\n' + move.upper() + '\n') #' {' + str(end-start) + ' s}' # uncomment to view the execution time
            else:
                print(move) #' {' + str(end-start) + ' s}') # uncomment to view the execution time 

    except Exception as e:
        nao.stopMusic(song)
        print(e)
    
    time.sleep(1.44)
    nao.stopMusic(song)


if __name__ == '__main__':
    main()
