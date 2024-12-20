import sys
import time
from naoqi import ALProxy


def main(robotIP, port):
    names = list()
    times = list()
    keys = list()

    names.append("HeadPitch")
    times.append([0.48, 1, 1.8, 2.6, 3.4, 4.2, 5, 5.8])
    keys.append([[-0.324631, [3, -0.0133333, 0], [3, 0.253333, 0]], [0.18675, [3, -0.253333, 0], [3, 0.266667, 0]], [-0.324631, [3, -0.266667, 0], [3, 0.266667, 0]], [0.18675, [3, -0.266667, 0], [3, 0.266667, 0]], [-0.324631, [3, -0.266667, 0], [3, 0.266667, 0]], [0.18675, [3, -0.266667, 0], [3, 0.266667, 0]], [-0.324631, [3, -0.266667, 0], [3, 0.266667, 0]], [0.18675, [3, -0.266667, 0], [3, 0, 0]]])

    names.append("HeadYaw")
    times.append([0.48, 1, 1.8, 2.6, 3.4, 4.2, 5, 5.8])
    keys.append([[0, [3, -0.0133333, 0], [3, 0.253333, 0]], [0, [3, -0.253333, 0], [3, 0.266667, 0]], [0, [3, -0.266667, 0], [3, 0.266667, 0]], [0, [3, -0.266667, 0], [3, 0.266667, 0]], [0, [3, -0.266667, 0], [3, 0.266667, 0]], [0, [3, -0.266667, 0], [3, 0.266667, 0]], [0, [3, -0.266667, 0], [3, 0.266667, 0]], [0, [3, -0.266667, 0], [3, 0, 0]]])

    names.append("LAnklePitch")
    times.append([0.48, 1, 1.8, 2.6, 3.4, 4.2, 5, 5.8])
    keys.append([[0.153589, [3, -0.0133333, 0], [3, 0.253333, 0]], [-0.984366, [3, -0.253333, 0], [3, 0.266667, 0]], [0.153589, [3, -0.266667, 0], [3, 0.266667, 0]], [-0.984366, [3, -0.266667, 0], [3, 0.266667, 0]], [0.153589, [3, -0.266667, 0], [3, 0.266667, 0]], [-0.984366, [3, -0.266667, 0], [3, 0.266667, 0]], [0.153589, [3, -0.266667, 0], [3, 0.266667, 0]], [-0.984366, [3, -0.266667, 0], [3, 0, 0]]])

    names.append("LAnkleRoll")
    times.append([0.48, 1, 1.8, 2.6, 3.4, 4.2, 5, 5.8])
    keys.append([[-0.00960779, [3, -0.0133333, 0], [3, 0.253333, 0]], [-0.00960779, [3, -0.253333, 0], [3, 0.266667, 0]], [-0.00960779, [3, -0.266667, 0], [3, 0.266667, 0]], [-0.00960779, [3, -0.266667, 0], [3, 0.266667, 0]], [-0.00960779, [3, -0.266667, 0], [3, 0.266667, 0]], [-0.00960779, [3, -0.266667, 0], [3, 0.266667, 0]], [-0.00960779, [3, -0.266667, 0], [3, 0.266667, 0]], [-0.00960779, [3, -0.266667, 0], [3, 0, 0]]])

    names.append("LElbowRoll")
    times.append([0.48, 1, 1.8, 2.6, 3.4, 4.2, 5, 5.8])
    keys.append([[-0.239864, [3, -0.0133333, 0], [3, 0.253333, 0]], [-0.874349, [3, -0.253333, 0], [3, 0.266667, 0]], [-0.239864, [3, -0.266667, 0], [3, 0.266667, 0]], [-0.874349, [3, -0.266667, 0], [3, 0.266667, 0]], [-0.239864, [3, -0.266667, 0], [3, 0.266667, 0]], [-0.874349, [3, -0.266667, 0], [3, 0.266667, 0]], [-0.239864, [3, -0.266667, 0], [3, 0.266667, 0]], [-0.874349, [3, -0.266667, 0], [3, 0, 0]]])

    names.append("LElbowYaw")
    times.append([0.48, 1, 1.8, 2.6, 3.4, 4.2, 5, 5.8])
    keys.append([[-0.612981, [3, -0.0133333, 0], [3, 0.253333, 0]], [-0.635537, [3, -0.253333, 0], [3, 0.266667, 0]], [-0.612981, [3, -0.266667, 0], [3, 0.266667, 0]], [-0.635537, [3, -0.266667, 0], [3, 0.266667, 0]], [-0.612981, [3, -0.266667, 0], [3, 0.266667, 0]], [-0.635537, [3, -0.266667, 0], [3, 0.266667, 0]], [-0.612981, [3, -0.266667, 0], [3, 0.266667, 0]], [-0.635537, [3, -0.266667, 0], [3, 0, 0]]])

    names.append("LHand")
    times.append([0.48, 1, 1.8, 2.6, 3.4, 4.2, 5, 5.8])
    keys.append([[1, [3, -0.0133333, 0], [3, 0.253333, 0]], [1, [3, -0.253333, 0], [3, 0.266667, 0]], [1, [3, -0.266667, 0], [3, 0.266667, 0]], [1, [3, -0.266667, 0], [3, 0.266667, 0]], [1, [3, -0.266667, 0], [3, 0.266667, 0]], [1, [3, -0.266667, 0], [3, 0.266667, 0]], [1, [3, -0.266667, 0], [3, 0.266667, 0]], [1, [3, -0.266667, 0], [3, 0, 0]]])

    names.append("LHipPitch")
    times.append([0.48, 1, 1.8, 2.6, 3.4, 4.2, 5, 5.8])
    keys.append([[-0.0401426, [3, -0.0133333, 0], [3, 0.253333, 0]], [-0.724889, [3, -0.253333, 0], [3, 0.266667, 0]], [-0.0401426, [3, -0.266667, 0], [3, 0.266667, 0]], [-0.724889, [3, -0.266667, 0], [3, 0.266667, 0]], [-0.0401426, [3, -0.266667, 0], [3, 0.266667, 0]], [-0.724889, [3, -0.266667, 0], [3, 0.266667, 0]], [-0.0401426, [3, -0.266667, 0], [3, 0.266667, 0]], [-0.724889, [3, -0.266667, 0], [3, 0, 0]]])

    names.append("LHipRoll")
    times.append([0.48, 1, 1.8, 2.6, 3.4, 4.2, 5, 5.8])
    keys.append([[0.0331613, [3, -0.0133333, 0], [3, 0.253333, 0]], [0.00285782, [3, -0.253333, 0], [3, 0.266667, 0]], [0.0331613, [3, -0.266667, 0], [3, 0.266667, 0]], [0.00285782, [3, -0.266667, 0], [3, 0.266667, 0]], [0.0331613, [3, -0.266667, 0], [3, 0.266667, 0]], [0.00285782, [3, -0.266667, 0], [3, 0.266667, 0]], [0.0331613, [3, -0.266667, 0], [3, 0.266667, 0]], [0.00285782, [3, -0.266667, 0], [3, 0, 0]]])

    names.append("LHipYawPitch")
    times.append([0.48, 1, 1.8, 2.6, 3.4, 4.2, 5, 5.8])
    keys.append([[-0.00488875, [3, -0.0133333, 0], [3, 0.253333, 0]], [-0.00488875, [3, -0.253333, 0], [3, 0.266667, 0]], [-0.00488875, [3, -0.266667, 0], [3, 0.266667, 0]], [-0.00488875, [3, -0.266667, 0], [3, 0.266667, 0]], [-0.00488875, [3, -0.266667, 0], [3, 0.266667, 0]], [-0.00488875, [3, -0.266667, 0], [3, 0.266667, 0]], [-0.00488875, [3, -0.266667, 0], [3, 0.266667, 0]], [-0.00488875, [3, -0.266667, 0], [3, 0, 0]]])

    names.append("LKneePitch")
    times.append([0.48, 1, 1.8, 2.6, 3.4, 4.2, 5, 5.8])
    keys.append([[-0.0855396, [3, -0.0133333, 0], [3, 0.253333, 0]], [1.6825, [3, -0.253333, 0], [3, 0.266667, 0]], [-0.0855396, [3, -0.266667, 0], [3, 0.266667, 0]], [1.6825, [3, -0.266667, 0], [3, 0.266667, 0]], [-0.0855396, [3, -0.266667, 0], [3, 0.266667, 0]], [1.6825, [3, -0.266667, 0], [3, 0.266667, 0]], [-0.0855396, [3, -0.266667, 0], [3, 0.266667, 0]], [1.6825, [3, -0.266667, 0], [3, 0, 0]]])

    names.append("LShoulderPitch")
    times.append([0.48, 1, 1.8, 2.6, 3.4, 4.2, 5, 5.8])
    keys.append([[-1.42409, [3, -0.0133333, 0], [3, 0.253333, 0]], [0.151349, [3, -0.253333, 0], [3, 0.266667, 0]], [-1.42409, [3, -0.266667, 0], [3, 0.266667, 0]], [0.151349, [3, -0.266667, 0], [3, 0.266667, 0]], [-1.42409, [3, -0.266667, 0], [3, 0.266667, 0]], [0.151349, [3, -0.266667, 0], [3, 0.266667, 0]], [-1.42409, [3, -0.266667, 0], [3, 0.266667, 0]], [0.151349, [3, -0.266667, 0], [3, 0, 0]]])

    names.append("LShoulderRoll")
    times.append([0.48, 1, 1.8, 2.6, 3.4, 4.2, 5, 5.8])
    keys.append([[1.3237, [3, -0.0133333, 0], [3, 0.253333, 0]], [-0.019487, [3, -0.253333, 0], [3, 0.266667, 0]], [1.3237, [3, -0.266667, 0], [3, 0.266667, 0]], [-0.019487, [3, -0.266667, 0], [3, 0.266667, 0]], [1.3237, [3, -0.266667, 0], [3, 0.266667, 0]], [-0.019487, [3, -0.266667, 0], [3, 0.266667, 0]], [1.3237, [3, -0.266667, 0], [3, 0.266667, 0]], [-0.019487, [3, -0.266667, 0], [3, 0, 0]]])

    names.append("LWristYaw")
    times.append([0.48, 1, 1.8, 2.6, 3.4, 4.2, 5, 5.8])
    keys.append([[-0.603413, [3, -0.0133333, 0], [3, 0.253333, 0]], [-0.603413, [3, -0.253333, 0], [3, 0.266667, 0]], [-0.603413, [3, -0.266667, 0], [3, 0.266667, 0]], [-0.603413, [3, -0.266667, 0], [3, 0.266667, 0]], [-0.603413, [3, -0.266667, 0], [3, 0.266667, 0]], [-0.603413, [3, -0.266667, 0], [3, 0.266667, 0]], [-0.603413, [3, -0.266667, 0], [3, 0.266667, 0]], [-0.603413, [3, -0.266667, 0], [3, 0, 0]]])

    names.append("RAnklePitch")
    times.append([0.48, 1, 1.8, 2.6, 3.4, 4.2, 5, 5.8])
    keys.append([[0.153589, [3, -0.0133333, 0], [3, 0.253333, 0]], [-0.984366, [3, -0.253333, 0], [3, 0.266667, 0]], [0.153589, [3, -0.266667, 0], [3, 0.266667, 0]], [-0.984366, [3, -0.266667, 0], [3, 0.266667, 0]], [0.153589, [3, -0.266667, 0], [3, 0.266667, 0]], [-0.984366, [3, -0.266667, 0], [3, 0.266667, 0]], [0.153589, [3, -0.266667, 0], [3, 0.266667, 0]], [-0.984366, [3, -0.266667, 0], [3, 0, 0]]])

    names.append("RAnkleRoll")
    times.append([0.48, 1, 1.8, 2.6, 3.4, 4.2, 5, 5.8])
    keys.append([[0.00939223, [3, -0.0133333, 0], [3, 0.253333, 0]], [0.00939223, [3, -0.253333, 0], [3, 0.266667, 0]], [0.00939223, [3, -0.266667, 0], [3, 0.266667, 0]], [0.00939223, [3, -0.266667, 0], [3, 0.266667, 0]], [0.00939223, [3, -0.266667, 0], [3, 0.266667, 0]], [0.00939223, [3, -0.266667, 0], [3, 0.266667, 0]], [0.00939223, [3, -0.266667, 0], [3, 0.266667, 0]], [0.00939223, [3, -0.266667, 0], [3, 0, 0]]])

    names.append("RElbowRoll")
    times.append([0.48, 1, 1.8, 2.6, 3.4, 4.2, 5, 5.8])
    keys.append([[0.239864, [3, -0.0133333, 0], [3, 0.253333, 0]], [0.874349, [3, -0.253333, 0], [3, 0.266667, 0]], [0.239864, [3, -0.266667, 0], [3, 0.266667, 0]], [0.874349, [3, -0.266667, 0], [3, 0.266667, 0]], [0.239864, [3, -0.266667, 0], [3, 0.266667, 0]], [0.874349, [3, -0.266667, 0], [3, 0.266667, 0]], [0.239864, [3, -0.266667, 0], [3, 0.266667, 0]], [0.874349, [3, -0.266667, 0], [3, 0, 0]]])

    names.append("RElbowYaw")
    times.append([0.48, 1, 1.8, 2.6, 3.4, 4.2, 5, 5.8])
    keys.append([[0.612981, [3, -0.0133333, 0], [3, 0.253333, 0]], [0.635537, [3, -0.253333, 0], [3, 0.266667, 0]], [0.612981, [3, -0.266667, 0], [3, 0.266667, 0]], [0.635537, [3, -0.266667, 0], [3, 0.266667, 0]], [0.612981, [3, -0.266667, 0], [3, 0.266667, 0]], [0.635537, [3, -0.266667, 0], [3, 0.266667, 0]], [0.612981, [3, -0.266667, 0], [3, 0.266667, 0]], [0.635537, [3, -0.266667, 0], [3, 0, 0]]])

    names.append("RHand")
    times.append([0.48, 1, 1.8, 2.6, 3.4, 4.2, 5, 5.8])
    keys.append([[1, [3, -0.0133333, 0], [3, 0.253333, 0]], [1, [3, -0.253333, 0], [3, 0.266667, 0]], [1, [3, -0.266667, 0], [3, 0.266667, 0]], [1, [3, -0.266667, 0], [3, 0.266667, 0]], [1, [3, -0.266667, 0], [3, 0.266667, 0]], [1, [3, -0.266667, 0], [3, 0.266667, 0]], [1, [3, -0.266667, 0], [3, 0.266667, 0]], [1, [3, -0.266667, 0], [3, 0, 0]]])

    names.append("RHipPitch")
    times.append([0.48, 1, 1.8, 2.6, 3.4, 4.2, 5, 5.8])
    keys.append([[-0.0401426, [3, -0.0133333, 0], [3, 0.253333, 0]], [-0.724889, [3, -0.253333, 0], [3, 0.266667, 0]], [-0.0401426, [3, -0.266667, 0], [3, 0.266667, 0]], [-0.724889, [3, -0.266667, 0], [3, 0.266667, 0]], [-0.0401426, [3, -0.266667, 0], [3, 0.266667, 0]], [-0.724889, [3, -0.266667, 0], [3, 0.266667, 0]], [-0.0401426, [3, -0.266667, 0], [3, 0.266667, 0]], [-0.724889, [3, -0.266667, 0], [3, 0, 0]]])

    names.append("RHipRoll")
    times.append([0.48, 1, 1.8, 2.6, 3.4, 4.2, 5, 5.8])
    keys.append([[-0.0331613, [3, -0.0133333, 0], [3, 0.253333, 0]], [-0.000333042, [3, -0.253333, 0], [3, 0.266667, 0]], [-0.0331613, [3, -0.266667, 0], [3, 0.266667, 0]], [-0.000333042, [3, -0.266667, 0], [3, 0.266667, 0]], [-0.0331613, [3, -0.266667, 0], [3, 0.266667, 0]], [-0.000333042, [3, -0.266667, 0], [3, 0.266667, 0]], [-0.0331613, [3, -0.266667, 0], [3, 0.266667, 0]], [-0.000333042, [3, -0.266667, 0], [3, 0, 0]]])

    names.append("RHipYawPitch")
    times.append([0.48, 1, 1.8, 2.6, 3.4, 4.2, 5, 5.8])
    keys.append([[-0.00488875, [3, -0.0133333, 0], [3, 0.253333, 0]], [-0.00488875, [3, -0.253333, 0], [3, 0.266667, 0]], [-0.00488875, [3, -0.266667, 0], [3, 0.266667, 0]], [-0.00488875, [3, -0.266667, 0], [3, 0.266667, 0]], [-0.00488875, [3, -0.266667, 0], [3, 0.266667, 0]], [-0.00488875, [3, -0.266667, 0], [3, 0.266667, 0]], [-0.00488875, [3, -0.266667, 0], [3, 0.266667, 0]], [-0.00488875, [3, -0.266667, 0], [3, 0, 0]]])

    names.append("RKneePitch")
    times.append([0.48, 1, 1.8, 2.6, 3.4, 4.2, 5, 5.8])
    keys.append([[-0.0855396, [3, -0.0133333, 0], [3, 0.253333, 0]], [1.6825, [3, -0.253333, 0], [3, 0.266667, 0]], [-0.0855396, [3, -0.266667, 0], [3, 0.266667, 0]], [1.6825, [3, -0.266667, 0], [3, 0.266667, 0]], [-0.0855396, [3, -0.266667, 0], [3, 0.266667, 0]], [1.6825, [3, -0.266667, 0], [3, 0.266667, 0]], [-0.0855396, [3, -0.266667, 0], [3, 0.266667, 0]], [1.6825, [3, -0.266667, 0], [3, 0, 0]]])

    names.append("RShoulderPitch")
    times.append([0.48, 1, 1.8, 2.6, 3.4, 4.2, 5, 5.8])
    keys.append([[-1.42409, [3, -0.0133333, 0], [3, 0.253333, 0]], [0.151349, [3, -0.253333, 0], [3, 0.266667, 0]], [-1.42409, [3, -0.266667, 0], [3, 0.266667, 0]], [0.151349, [3, -0.266667, 0], [3, 0.266667, 0]], [-1.42409, [3, -0.266667, 0], [3, 0.266667, 0]], [0.151349, [3, -0.266667, 0], [3, 0.266667, 0]], [-1.42409, [3, -0.266667, 0], [3, 0.266667, 0]], [0.151349, [3, -0.266667, 0], [3, 0, 0]]])

    names.append("RShoulderRoll")
    times.append([0.48, 1, 1.8, 2.6, 3.4, 4.2, 5, 5.8])
    keys.append([[-1.3237, [3, -0.0133333, 0], [3, 0.253333, 0]], [0.019487, [3, -0.253333, 0], [3, 0.266667, 0]], [-1.3237, [3, -0.266667, 0], [3, 0.266667, 0]], [0.019487, [3, -0.266667, 0], [3, 0.266667, 0]], [-1.3237, [3, -0.266667, 0], [3, 0.266667, 0]], [0.019487, [3, -0.266667, 0], [3, 0.266667, 0]], [-1.3237, [3, -0.266667, 0], [3, 0.266667, 0]], [0.019487, [3, -0.266667, 0], [3, 0, 0]]])

    names.append("RWristYaw")
    times.append([0.48, 1, 1.8, 2.6, 3.4, 4.2, 5, 5.8])
    keys.append([[0.603413, [3, -0.0133333, 0], [3, 0.253333, 0]], [0.603413, [3, -0.253333, 0], [3, 0.266667, 0]], [0.603413, [3, -0.266667, 0], [3, 0.266667, 0]], [0.603413, [3, -0.266667, 0], [3, 0.266667, 0]], [0.603413, [3, -0.266667, 0], [3, 0.266667, 0]], [0.603413, [3, -0.266667, 0], [3, 0.266667, 0]], [0.603413, [3, -0.266667, 0], [3, 0.266667, 0]], [0.603413, [3, -0.266667, 0], [3, 0, 0]]])

    try:
        motion = ALProxy("ALMotion", robotIP, port)
        motion.angleInterpolationBezier(names, times, keys)
    except BaseException, err:
        print err


if __name__ == "__main__":

    robotIP = "127.0.0.1"
    port = 9559

    if len(sys.argv) <= 1:
        print "(robotIP default: 127.0.0.1)"
    elif len(sys.argv) <= 2:
        robotIP = sys.argv[1]
    else:
        port = int(sys.argv[2])
        robotIP = sys.argv[1]

    main(robotIP, port)
