import sys
import time
from naoqi import ALProxy


def main(robotIP, port):
    names = list()
    times = list()
    keys = list()
        
    names.append("HeadPitch")
    times.append([0.45, 1.95, 2.55, 3.15, 3.75, 4.35, 4.95, 6])
    keys.append([[-0.012314, [3, -0.0833333, 0], [3, 0.566667, 0]], [0.00609404, [3, -0.566667, 0], [3, 0.2, 0]], [0.00609404, [3, -0.2, 0], [3, 0.2, 0]], [0.00609404, [3, -0.2, 0], [3, 0.2, 0]], [0.00609404, [3, -0.2, 0], [3, 0.2, 0]], [0.00609404, [3, -0.2, 0], [3, 0.2, 0]], [0.00609404, [3, -0.2, 0], [3, 0.35, 0]], [-0.000413602, [3, -0.35, 0], [3, 0, 0]]])

    names.append("HeadYaw")
    times.append([0.45, 1.95, 2.55, 3.15, 3.75, 4.35, 4.95, 6])
    keys.append([[0.00762803, [3, -0.0833333, 0], [3, 0.566667, 0]], [0.00762803, [3, -0.566667, 0], [3, 0.2, 0]], [0.00762803, [3, -0.2, 0], [3, 0.2, 0]], [0.00762803, [3, -0.2, 0], [3, 0.2, 0]], [0.00762803, [3, -0.2, 0], [3, 0.2, 0]], [0.00762803, [3, -0.2, 0], [3, 0.2, 0]], [0.00762803, [3, -0.2, 0], [3, 0.35, 0]], [0.00311635, [3, -0.35, 0], [3, 0, 0]]])

    names.append("LAnklePitch")
    times.append([0.45, 0.8, 1.95, 2.55, 3.15, 3.75, 4.35, 4.95, 6])
    keys.append([[0.191576, [3, -0.0833333, 0], [3, 0.183333, 0]], [0.205383, [3, -0.183333, 0], [3, 0.383333, 0]], [0.183907, [3, -0.383333, 0], [3, 0.2, 0]], [0.183907, [3, -0.2, 0], [3, 0.2, 0]], [0.183907, [3, -0.2, 0], [3, 0.2, 0]], [0.183907, [3, -0.2, 0], [3, 0.2, 0]], [0.183907, [3, -0.2, 0], [3, 0.2, 0]], [0.183907, [3, -0.2, 0], [3, 0.35, 0]], [-0.34587, [3, -0.35, 0], [3, 0, 0]]])

    names.append("LAnkleRoll")
    times.append([0.45, 0.8, 1.95, 2.55, 3.15, 3.75, 4.35, 4.95, 6])
    keys.append([[0.0659823, [3, -0.0833333, 0], [3, 0.183333, 0]], [0.0613804, [3, -0.183333, 0.00460191], [3, 0.383333, -0.00962217]], [-0.0107176, [3, -0.383333, 0], [3, 0.2, 0]], [-0.0107176, [3, -0.2, 0], [3, 0.2, 0]], [-0.0107176, [3, -0.2, 0], [3, 0.2, 0]], [-0.0107176, [3, -0.2, 0], [3, 0.2, 0]], [-0.0107176, [3, -0.2, 0], [3, 0.2, 0]], [-0.0107176, [3, -0.2, 0], [3, 0.35, 0]], [0.000208129, [3, -0.35, 0], [3, 0, 0]]])

    names.append("LElbowRoll")
    times.append([0.45, 1.35, 1.95, 2.55, 3.15, 3.75, 4.35, 4.95, 6])
    keys.append([[-1.4772, [3, -0.0833333, 0], [3, 0.366667, 0]], [-1.55697, [3, -0.366667, 0], [3, 0.2, 0]], [-0.010696, [3, -0.2, 0], [3, 0.2, 0]], [-1.54369, [3, -0.2, 0], [3, 0.2, 0]], [-0.010696, [3, -0.2, 0], [3, 0.2, 0]], [-1.54369, [3, -0.2, 0], [3, 0.2, 0]], [-0.010696, [3, -0.2, 0], [3, 0.2, 0]], [-1.54369, [3, -0.2, 0], [3, 0.35, 0]], [-1.00465, [3, -0.35, 0], [3, 0, 0]]])

    names.append("LElbowYaw")
    times.append([0.45, 1.35, 1.95, 2.55, 3.15, 3.75, 4.35, 4.95, 6])
    keys.append([[-1.71812, [3, -0.0833333, 0], [3, 0.366667, 0]], [-1.29627, [3, -0.366667, -0.323915], [3, 0.2, 0.176681]], [-0.216335, [3, -0.2, 0], [3, 0.2, 0]], [-0.219665, [3, -0.2, 0], [3, 0.2, 0]], [-0.216335, [3, -0.2, 0], [3, 0.2, 0]], [-0.219665, [3, -0.2, 0], [3, 0.2, 0]], [-0.216335, [3, -0.2, 0], [3, 0.2, 0]], [-0.219665, [3, -0.2, 0.0033301], [3, 0.35, -0.00582767]], [-1.38812, [3, -0.35, 0], [3, 0, 0]]])

    names.append("LHand")
    times.append([0.45, 1.95, 2.55, 3.15, 3.75, 4.35, 4.95, 6])
    keys.append([[0.997114, [3, -0.0833333, 0], [3, 0.566667, 0]], [0.995296, [3, -0.566667, 0], [3, 0.2, 0]], [0.997728, [3, -0.2, 0], [3, 0.2, 0]], [0.995296, [3, -0.2, 0], [3, 0.2, 0]], [0.997728, [3, -0.2, 0], [3, 0.2, 0]], [0.995296, [3, -0.2, 0], [3, 0.2, 0]], [0.997728, [3, -0.2, 0], [3, 0.35, 0]], [0.45, [3, -0.35, 0], [3, 0, 0]]])

    names.append("LHipPitch")
    times.append([0.45, 0.8, 1.95, 2.55, 3.15, 3.75, 4.35, 4.95, 6])
    keys.append([[0.179256, [3, -0.0833333, 0], [3, 0.183333, 0]], [0.162382, [3, -0.183333, 0.0168733], [3, 0.383333, -0.0352806]], [-0.24106, [3, -0.383333, 0], [3, 0.2, 0]], [-0.24106, [3, -0.2, 0], [3, 0.2, 0]], [-0.24106, [3, -0.2, 0], [3, 0.2, 0]], [-0.24106, [3, -0.2, 0], [3, 0.2, 0]], [-0.24106, [3, -0.2, 0], [3, 0.2, 0]], [-0.24106, [3, -0.2, 0], [3, 0.35, 0]], [-0.441429, [3, -0.35, 0], [3, 0, 0]]])

    names.append("LHipRoll")
    times.append([0.45, 0.8, 1.95, 2.55, 3.15, 3.75, 4.35, 4.95, 6])
    keys.append([[0.0580999, [3, -0.0833333, 0], [3, 0.183333, 0]], [0.07344, [3, -0.183333, 0], [3, 0.383333, 0]], [-0.145922, [3, -0.383333, 0], [3, 0.2, 0]], [-0.145922, [3, -0.2, 0], [3, 0.2, 0]], [-0.145922, [3, -0.2, 0], [3, 0.2, 0]], [-0.145922, [3, -0.2, 0], [3, 0.2, 0]], [-0.145922, [3, -0.2, 0], [3, 0.2, 0]], [-0.145922, [3, -0.2, 0], [3, 0.35, 0]], [-0.0089492, [3, -0.35, 0], [3, 0, 0]]])

    names.append("LHipYawPitch")
    times.append([0.45, 0.8, 1.95, 2.55, 3.15, 3.75, 4.35, 4.95, 6])
    keys.append([[-0.730228, [3, -0.0833333, 0], [3, 0.183333, 0]], [-0.739431, [3, -0.183333, 0], [3, 0.383333, 0]], [-0.487856, [3, -0.383333, 0], [3, 0.2, 0]], [-0.487856, [3, -0.2, 0], [3, 0.2, 0]], [-0.487856, [3, -0.2, 0], [3, 0.2, 0]], [-0.487856, [3, -0.2, 0], [3, 0.2, 0]], [-0.487856, [3, -0.2, 0], [3, 0.2, 0]], [-0.487856, [3, -0.2, 0], [3, 0.35, 0]], [0.00919563, [3, -0.35, 0], [3, 0, 0]]])

    names.append("LKneePitch")
    times.append([0.45, 0.8, 1.95, 2.55, 3.15, 3.75, 4.35, 4.95, 6])
    keys.append([[0.185295, [3, -0.0833333, 0], [3, 0.183333, 0]], [0.169954, [3, -0.183333, 0.00146728], [3, 0.383333, -0.00306794]], [0.166886, [3, -0.383333, 0], [3, 0.2, 0]], [0.166886, [3, -0.2, 0], [3, 0.2, 0]], [0.166886, [3, -0.2, 0], [3, 0.2, 0]], [0.166886, [3, -0.2, 0], [3, 0.2, 0]], [0.166886, [3, -0.2, 0], [3, 0.2, 0]], [0.166886, [3, -0.2, 0], [3, 0.35, 0]], [0.7, [3, -0.35, 0], [3, 0, 0]]])

    names.append("LShoulderPitch")
    times.append([0.45, 1.35, 1.95, 2.55, 3.15, 3.75, 4.35, 4.95, 6])
    keys.append([[1.53089, [3, -0.0833333, 0], [3, 0.366667, 0]], [0.179436, [3, -0.366667, 0], [3, 0.2, 0]], [1.7073, [3, -0.2, 0], [3, 0.2, 0]], [1.48726, [3, -0.2, 0], [3, 0.2, 0]], [1.7073, [3, -0.2, 0], [3, 0.2, 0]], [1.48726, [3, -0.2, 0], [3, 0.2, 0]], [1.7073, [3, -0.2, 0], [3, 0.2, 0]], [1.48726, [3, -0.2, 0.0362171], [3, 0.35, -0.06338]], [1.40851, [3, -0.35, 0], [3, 0, 0]]])

    names.append("LShoulderRoll")
    times.append([0.45, 1.35, 1.95, 2.55, 3.15, 3.75, 4.35, 4.95, 6])
    keys.append([[0.039842, [3, -0.0833333, 0], [3, 0.366667, 0]], [0, [3, -0.366667, 0], [3, 0.2, 0]], [1.35601, [3, -0.2, 0], [3, 0.2, 0]], [1.31828, [3, -0.2, 0], [3, 0.2, 0]], [1.35601, [3, -0.2, 0], [3, 0.2, 0]], [1.31828, [3, -0.2, 0], [3, 0.2, 0]], [1.35601, [3, -0.2, 0], [3, 0.2, 0]], [1.31828, [3, -0.2, 0.0377306], [3, 0.35, -0.0660286]], [0.300072, [3, -0.35, 0], [3, 0, 0]]])

    names.append("LWristYaw")
    times.append([0.45, 1.95, 2.55, 3.15, 3.75, 4.35, 4.95, 6])
    keys.append([[-0.277696, [3, -0.0833333, 0], [3, 0.566667, 0]], [-0.289967, [3, -0.566667, 0], [3, 0.2, 0]], [-0.154001, [3, -0.2, 0], [3, 0.2, 0]], [-0.289967, [3, -0.2, 0], [3, 0.2, 0]], [-0.154001, [3, -0.2, 0], [3, 0.2, 0]], [-0.289967, [3, -0.2, 0], [3, 0.2, 0]], [-0.154001, [3, -0.2, -0.034367], [3, 0.35, 0.0601422]], [-0.00643973, [3, -0.35, 0], [3, 0, 0]]])

    names.append("RAnklePitch")
    times.append([0.45, 0.8, 1.95, 2.55, 3.15, 3.75, 4.35, 4.95, 6])
    keys.append([[-0.411138, [3, -0.0833333, 0], [3, 0.183333, 0]], [-0.401935, [3, -0.183333, -0.00920312], [3, 0.383333, 0.0192429]], [0.352792, [3, -0.383333, 0], [3, 0.2, 0]], [0.352792, [3, -0.2, 0], [3, 0.2, 0]], [0.352792, [3, -0.2, 0], [3, 0.2, 0]], [0.352792, [3, -0.2, 0], [3, 0.2, 0]], [0.352792, [3, -0.2, 0], [3, 0.2, 0]], [0.352792, [3, -0.2, 0], [3, 0.35, 0]], [-0.345713, [3, -0.35, 0], [3, 0, 0]]])

    names.append("RAnkleRoll")
    times.append([0.45, 0.8, 1.95, 2.55, 3.15, 3.75, 4.35, 4.95, 6])
    keys.append([[0.0322537, [3, -0.0833333, 0], [3, 0.183333, 0]], [0.0337877, [3, -0.183333, -0.00153397], [3, 0.383333, 0.00320739]], [0.248547, [3, -0.383333, 0], [3, 0.2, 0]], [0.248547, [3, -0.2, 0], [3, 0.2, 0]], [0.248547, [3, -0.2, 0], [3, 0.2, 0]], [0.248547, [3, -0.2, 0], [3, 0.2, 0]], [0.248547, [3, -0.2, 0], [3, 0.2, 0]], [0.248547, [3, -0.2, 0], [3, 0.35, 0]], [0.00244106, [3, -0.35, 0], [3, 0, 0]]])

    names.append("RElbowRoll")
    times.append([0.45, 1.35, 1.95, 2.55, 3.15, 3.75, 4.35, 4.95, 6])
    keys.append([[1.46348, [3, -0.0833333, 0], [3, 0.366667, 0]], [1.56319, [3, -0.366667, 0], [3, 0.2, 0]], [1.54171, [3, -0.2, 0.00517636], [3, 0.2, -0.00517636]], [1.53213, [3, -0.2, 0], [3, 0.2, 0]], [1.54171, [3, -0.2, 0], [3, 0.2, 0]], [1.53213, [3, -0.2, 0], [3, 0.2, 0]], [1.54171, [3, -0.2, 0], [3, 0.2, 0]], [1.53213, [3, -0.2, 0.00958192], [3, 0.35, -0.0167684]], [1.00439, [3, -0.35, 0], [3, 0, 0]]])

    names.append("RElbowYaw")
    times.append([0.45, 1.35, 1.95, 2.55, 3.15, 3.75, 4.35, 4.95, 6])
    keys.append([[1.52015, [3, -0.0833333, 0], [3, 0.366667, 0]], [1.44499, [3, -0.366667, 0], [3, 0.2, 0]], [1.65821, [3, -0.2, 0], [3, 0.2, 0]], [1.65242, [3, -0.2, 0], [3, 0.2, 0]], [1.65821, [3, -0.2, 0], [3, 0.2, 0]], [1.65242, [3, -0.2, 0], [3, 0.2, 0]], [1.65821, [3, -0.2, 0], [3, 0.2, 0]], [1.65242, [3, -0.2, 0.00578918], [3, 0.35, -0.0101311]], [1.38817, [3, -0.35, 0], [3, 0, 0]]])

    names.append("RHand")
    times.append([0.45, 1.95, 2.55, 3.15, 3.75, 4.35, 4.95, 6])
    keys.append([[1, [3, -0.0833333, 0], [3, 0.566667, 0]], [1, [3, -0.566667, 0], [3, 0.2, 0]], [0.998624, [3, -0.2, 0], [3, 0.2, 0]], [1, [3, -0.2, 0], [3, 0.2, 0]], [0.998624, [3, -0.2, 0], [3, 0.2, 0]], [1, [3, -0.2, 0], [3, 0.2, 0]], [0.998624, [3, -0.2, 0.00137597], [3, 0.35, -0.00240795]], [0.45, [3, -0.35, 0], [3, 0, 0]]])

    names.append("RHipPitch")
    times.append([0.45, 0.8, 1.95, 2.55, 3.15, 3.75, 4.35, 4.95, 6])
    keys.append([[0.489289, [3, -0.0833333, 0], [3, 0.183333, 0]], [0.490823, [3, -0.183333, 0], [3, 0.383333, 0]], [-0.279246, [3, -0.383333, 0], [3, 0.2, 0]], [-0.279246, [3, -0.2, 0], [3, 0.2, 0]], [-0.279246, [3, -0.2, 0], [3, 0.2, 0]], [-0.279246, [3, -0.2, 0], [3, 0.2, 0]], [-0.279246, [3, -0.2, 0], [3, 0.2, 0]], [-0.279246, [3, -0.2, 0], [3, 0.35, 0]], [-0.441813, [3, -0.35, 0], [3, 0, 0]]])

    names.append("RHipRoll")
    times.append([0.45, 0.8, 1.95, 2.55, 3.15, 3.75, 4.35, 4.95, 6])
    keys.append([[-0.148778, [3, -0.0833333, 0], [3, 0.183333, 0]], [-0.15338, [3, -0.183333, 0.00460191], [3, 0.383333, -0.00962217]], [-0.257691, [3, -0.383333, 0], [3, 0.2, 0]], [-0.257691, [3, -0.2, 0], [3, 0.2, 0]], [-0.257691, [3, -0.2, 0], [3, 0.2, 0]], [-0.257691, [3, -0.2, 0], [3, 0.2, 0]], [-0.257691, [3, -0.2, 0], [3, 0.2, 0]], [-0.257691, [3, -0.2, 0], [3, 0.35, 0]], [0.00711878, [3, -0.35, 0], [3, 0, 0]]])

    names.append("RKneePitch")
    times.append([0.45, 0.8, 1.95, 2.55, 3.15, 3.75, 4.35, 4.95, 6])
    keys.append([[0.47666, [3, -0.0833333, 0], [3, 0.183333, 0]], [0.455184, [3, -0.183333, 0.0214763], [3, 0.383333, -0.044905]], [0.0195278, [3, -0.383333, 0], [3, 0.2, 0]], [0.0195278, [3, -0.2, 0], [3, 0.2, 0]], [0.0195278, [3, -0.2, 0], [3, 0.2, 0]], [0.0195278, [3, -0.2, 0], [3, 0.2, 0]], [0.0195278, [3, -0.2, 0], [3, 0.2, 0]], [0.0195278, [3, -0.2, 0], [3, 0.35, 0]], [0.7, [3, -0.35, 0], [3, 0, 0]]])

    names.append("RShoulderPitch")
    times.append([0.45, 1.35, 1.95, 2.55, 3.15, 3.75, 4.35, 4.95, 6])
    keys.append([[0.00464395, [3, -0.0833333, 0], [3, 0.366667, 0]], [2.07247, [3, -0.366667, 0], [3, 0.2, 0]], [1.56779, [3, -0.2, 0.0066113], [3, 0.2, -0.0066113]], [1.56118, [3, -0.2, 0], [3, 0.2, 0]], [1.56779, [3, -0.2, 0], [3, 0.2, 0]], [1.56118, [3, -0.2, 0], [3, 0.2, 0]], [1.56779, [3, -0.2, 0], [3, 0.2, 0]], [1.56118, [3, -0.2, 0.0066113], [3, 0.35, -0.0115698]], [1.4087, [3, -0.35, 0], [3, 0, 0]]])

    names.append("RShoulderRoll")
    times.append([0.45, 1.35, 1.95, 2.55, 3.15, 3.75, 4.35, 4.95, 6])
    keys.append([[-0.11816, [3, -0.0833333, 0], [3, 0.366667, 0]], [-0.154976, [3, -0.366667, 0.0138962], [3, 0.2, -0.00757972]], [-0.182588, [3, -0.2, 0.00663554], [3, 0.2, -0.00663554]], [-0.194789, [3, -0.2, 0], [3, 0.2, 0]], [-0.182588, [3, -0.2, 0], [3, 0.2, 0]], [-0.194789, [3, -0.2, 0], [3, 0.2, 0]], [-0.182588, [3, -0.2, 0], [3, 0.2, 0]], [-0.194789, [3, -0.2, 0.0122016], [3, 0.35, -0.0213528]], [-0.300072, [3, -0.35, 0], [3, 0, 0]]])

    names.append("RWristYaw")
    times.append([0.45, 1.95, 2.55, 3.15, 3.75, 4.35, 4.95, 6])
    keys.append([[0.408002, [3, -0.0833333, 0], [3, 0.566667, 0]], [0.41107, [3, -0.566667, -0.00237923], [3, 0.2, 0.000839729]], [0.417659, [3, -0.2, 0], [3, 0.2, 0]], [0.41107, [3, -0.2, 0], [3, 0.2, 0]], [0.417659, [3, -0.2, 0], [3, 0.2, 0]], [0.41107, [3, -0.2, 0], [3, 0.2, 0]], [0.417659, [3, -0.2, 0], [3, 0.35, 0]], [0.00607343, [3, -0.35, 0], [3, 0, 0]]])

    try:
      motion = ALProxy("ALMotion",robotIP,port)
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
