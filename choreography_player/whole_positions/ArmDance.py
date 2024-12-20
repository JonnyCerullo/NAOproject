from naoqi import ALProxy
import sys
import motion
import almath
import math
import time


def main(nao_ip, nao_port):
    names = list()
    times = list()
    keys = list()

    names.append("HeadPitch")
    times.append([1, 2, 2.4, 3, 3.6, 4.2, 4.8, 5.4])
    keys.append([[-0.18719, [3, -0.333333, 0], [3, 0.333333, 0]],
                 [-0.185656, [3, -0.333333, -0.00153415],
                     [3, 0.133333, 0.000613659]],
                 [0.0291041, [3, -0.133333, 0], [3, 0.2, 0]
                  ], [-0.185656, [3, -0.2, 0], [3, 0.2, 0]],
                 [0.00149202, [3, -0.2, 0], [3, 0.2, 0]
                  ], [-0.185656, [3, -0.2, 0], [3, 0.2, 0]],
                 [0.0812599, [3, -0.2, 0], [3, 0.2, 0]], [-0.185656, [3, -0.2, 0], [3, 0, 0]]])

    names.append("HeadYaw")
    times.append([1, 2, 2.4, 3, 3.6, 4.2, 4.8, 5.4])
    keys.append([[-0.00157595, [3, -0.333333, 0], [3, 0.333333, 0]], [-0.00157595, [3, -0.333333, 0], [3, 0.133333, 0]],
                 [-0.00157595, [3, -0.133333, 0], [3, 0.2, 0]
                  ], [0.00609397, [3, -0.2, 0], [3, 0.2, 0]],
                 [-4.19617e-05, [3, -0.2, 0], [3, 0.2, 0]
                  ], [0.00609397, [3, -0.2, 0], [3, 0.2, 0]],
                 [-4.19617e-05, [3, -0.2, 0], [3, 0.2, 0]], [0.00609397, [3, -0.2, 0], [3, 0, 0]]])

    names.append("LAnklePitch")
    times.append([1, 2, 3.32, 5.4])
    keys.append(
        [[0.105804, [3, -0.333333, 0], [3, 0.333333, 0]], [-0.417291, [3, -0.333333, 0.102487], [3, 0.44, -0.135283]],
         [-0.607505, [3, -0.44, 0], [3, 0.693333, 0]], [-0.421891, [3, -0.693333, 0], [3, 0, 0]]])

    names.append("LAnkleRoll")
    times.append([1, 2, 3.32, 5.4])
    keys.append([[-0.0735901, [3, -0.333333, 0], [3, 0.333333, 0]],
                 [-0.0858622, [3, -0.333333, 0.00749368], [3, 0.44, -0.00989166]],
                 [-0.125746, [3, -0.44, 0], [3, 0.693333, 0]], [-0.0858622, [3, -0.693333, 0], [3, 0, 0]]])

    names.append("LElbowRoll")
    times.append([1, 2, 2.2, 2.4, 2.6, 2.8, 3, 3.2, 3.4, 3.6,
                 3.8, 4, 4.2, 4.4, 4.6, 4.8, 5, 5.2, 5.4])
    keys.append([[-0.435615, [3, -0.333333, 0], [3, 0.333333, 0]], [-1.24863, [3, -0.333333, 0], [3, 0.0666667, 0]],
                 [-1.07529, [3, -0.0666667, -0.0429523], [3, 0.0666667, 0.0429523]],
                 [-0.990921, [3, -0.0666667, 0], [3, 0.0666667, 0]],
                 [-1.4005, [3, -0.0666667, 0.0922825], [3, 0.0666667, -0.0922825]],
                 [-1.54462, [3, -0.0666667, 0], [3, 0.0666667, 0]],
                 [-1.39897, [3, -0.0666667, -0.0493303], [3, 0.0666667, 0.0493303]],
                 [-1.24863, [3, -0.0666667, -0.0539458], [3, 0.0666667, 0.0539458]],
                 [-1.07529, [3, -0.0666667, -0.0429523], [3, 0.0666667, 0.0429523]],
                 [-0.990921, [3, -0.0666667, 0], [3, 0.0666667, 0]],
                 [-1.4005, [3, -0.0666667, 0.0922825], [3, 0.0666667, -0.0922825]],
                 [-1.54462, [3, -0.0666667, 0], [3, 0.0666667, 0]],
                 [-1.39897, [3, -0.0666667, -0.0493303], [3, 0.0666667, 0.0493303]],
                 [-1.24863, [3, -0.0666667, -0.0539458], [3, 0.0666667, 0.0539458]],
                 [-1.07529, [3, -0.0666667, -0.0429523], [3, 0.0666667, 0.0429523]],
                 [-0.990921, [3, -0.0666667, 0], [3, 0.0666667, 0]],
                 [-1.4005, [3, -0.0666667, 0.0922825], [3, 0.0666667, -0.0922825]],
                 [-1.54462, [3, -0.0666667, 0], [3, 0.0666667, 0]], [-1.39897, [3, -0.0666667, 0], [3, 0, 0]]])

    names.append("LElbowYaw")
    times.append([1, 2, 2.2, 2.4, 2.6, 2.8, 3, 3.2, 3.4, 3.6,
                 3.8, 4, 4.2, 4.4, 4.6, 4.8, 5, 5.2, 5.4])
    keys.append([[-1.21344, [3, -0.333333, 0], [3, 0.333333, 0]],
                 [-0.434165, [3, -0.333333, -0.248849], [3, 0.0666667, 0.0497698]],
                 [-0.31758, [3, -0.0666667, -0.0449974], [3, 0.0666667, 0.0449974]],
                 [-0.16418, [3, -0.0666667, -0.0631497], [3, 0.0666667, 0.0631497]],
                 [0.061318, [3, -0.0666667, -0.0590701], [3, 0.0666667, 0.0590701]],
                 [0.190241, [3, -0.0666667, 0], [3, 0.0666667, 0]],
                 [-0.176453, [3, -0.0666667, 0.104068], [3, 0.0666667, -0.104068]],
                 [-0.434165, [3, -0.0666667, 0], [3, 0.0666667, 0]],
                 [-0.31758, [3, -0.0666667, -0.0447418], [3, 0.0666667, 0.0447418]],
                 [-0.165714, [3, -0.0666667, -0.0631497], [3, 0.0666667, 0.0631497]],
                 [0.061318, [3, -0.0666667, -0.0593258], [3, 0.0666667, 0.0593258]],
                 [0.190241, [3, -0.0666667, 0], [3, 0.0666667, 0]],
                 [-0.176453, [3, -0.0666667, 0.104068], [3, 0.0666667, -0.104068]],
                 [-0.434165, [3, -0.0666667, 0], [3, 0.0666667, 0]],
                 [-0.31758, [3, -0.0666667, -0.0449974], [3, 0.0666667, 0.0449974]],
                 [-0.16418, [3, -0.0666667, -0.0631497], [3, 0.0666667, 0.0631497]],
                 [0.061318, [3, -0.0666667, -0.0590701], [3, 0.0666667, 0.0590701]],
                 [0.190241, [3, -0.0666667, 0], [3, 0.0666667, 0]], [-0.176453, [3, -0.0666667, 0], [3, 0, 0]]])

    names.append("LHand")
    times.append([1, 2, 2.2, 2.4, 2.6, 2.8, 3, 3.2, 3.4, 3.6,
                 3.8, 4, 4.2, 4.4, 4.6, 4.8, 5, 5.2, 5.4])
    keys.append([[0.3136, [3, -0.333333, 0], [3, 0.333333, 0]], [0, [3, -0.333333, 0], [3, 0.0666667, 0]],
                 [0.1872, [3, -0.0666667, -0.000799999],
                     [3, 0.0666667, 0.000799999]],
                 [0.188, [3, -0.0666667, 0], [3, 0.0666667, 0]],
                 [0.184, [3, -0.0666667, 0.00399999], [3, 0.0666667, -0.00399999]],
                 [0, [3, -0.0666667, 0], [3, 0.0666667, 0]], [0.1908,
                                                              [3, -0.0666667, 0], [3, 0.0666667, 0]],
                 [0, [3, -0.0666667, 0], [3, 0.0666667, 0]],
                 [0.1872, [3, -0.0666667, -0.000799999],
                     [3, 0.0666667, 0.000799999]],
                 [0.188, [3, -0.0666667, 0], [3, 0.0666667, 0]],
                 [0.184, [3, -0.0666667, 0.00399999], [3, 0.0666667, -0.00399999]],
                 [0, [3, -0.0666667, 0], [3, 0.0666667, 0]], [0.1908,
                                                              [3, -0.0666667, 0], [3, 0.0666667, 0]],
                 [0, [3, -0.0666667, 0], [3, 0.0666667, 0]],
                 [0.1872, [3, -0.0666667, -0.000799999],
                     [3, 0.0666667, 0.000799999]],
                 [0.188, [3, -0.0666667, 0], [3, 0.0666667, 0]],
                 [0.184, [3, -0.0666667, 0.00399999], [3, 0.0666667, -0.00399999]],
                 [0, [3, -0.0666667, 0], [3, 0.0666667, 0]], [0.1908, [3, -0.0666667, 0], [3, 0, 0]]])

    names.append("LHipPitch")
    times.append([1, 2, 3.32, 5.4])
    keys.append(
        [[0.131966, [3, -0.333333, 0], [3, 0.333333, 0]], [-0.052114, [3, -0.333333, 0.0670023], [3, 0.44, -0.0884431]],
         [-0.33437, [3, -0.44, 0], [3, 0.693333, 0]], [-0.052114, [3, -0.693333, 0], [3, 0, 0]]])

    names.append("LHipRoll")
    times.append([1, 2, 3.32, 5.4])
    keys.append(
        [[0.06447, [3, -0.333333, 0], [3, 0.333333, 0]], [0.1335, [3, -0.333333, -0.0158691], [3, 0.44, 0.0209472]],
         [0.174919, [3, -0.44, 0], [3, 0.693333, 0]], [0.131966, [3, -0.693333, 0], [3, 0, 0]]])

    names.append("LHipYawPitch")
    times.append([1, 2, 3.32, 5.4])
    keys.append(
        [[-0.170232, [3, -0.333333, 0], [3, 0.333333, 0]], [-0.36505, [3, -0.333333, 0.0104588], [3, 0.44, -0.0138056]],
         [-0.378855, [3, -0.44, 0], [3, 0.693333, 0]], [-0.36505, [3, -0.693333, 0], [3, 0, 0]]])

    names.append("LKneePitch")
    times.append([1, 2, 3.32, 5.4])
    keys.append(
        [[-0.0874801, [3, -0.333333, 0], [3, 0.333333, 0]], [0.731677, [3, -0.333333, -0.17544], [3, 0.44, 0.231581]],
         [1.13358, [3, -0.44, 0], [3, 0.693333, 0]], [0.730143, [3, -0.693333, 0], [3, 0, 0]]])

    names.append("LShoulderPitch")
    times.append([1, 2, 2.2, 2.4, 2.6, 2.8, 3, 3.2, 3.4, 3.6,
                 3.8, 4, 4.2, 4.4, 4.6, 4.8, 5, 5.2, 5.4])
    keys.append([[1.4818, [3, -0.333333, 0], [3, 0.333333, 0]], [0.357381, [3, -0.333333, 0], [3, 0.0666667, 0]],
                 [0.510779, [3, -0.0666667, -0.0378384], [3, 0.0666667, 0.0378384]],
                 [0.584411, [3, -0.0666667, -0.0158514], [3, 0.0666667, 0.0158514]],
                 [0.605888, [3, -0.0666667, 0], [3, 0.0666667, 0]
                  ], [0.101229, [3, -0.0666667, 0], [3, 0.0666667, 0]],
                 [0.282215, [3, -0.0666667, -0.0426919], [3, 0.0666667, 0.0426919]],
                 [0.357381, [3, -0.0666667, -0.0380941], [3, 0.0666667, 0.0380941]],
                 [0.510779, [3, -0.0666667, -0.0378384], [3, 0.0666667, 0.0378384]],
                 [0.584411, [3, -0.0666667, -0.0158514], [3, 0.0666667, 0.0158514]],
                 [0.605888, [3, -0.0666667, 0], [3, 0.0666667, 0]
                  ], [0.101229, [3, -0.0666667, 0], [3, 0.0666667, 0]],
                 [0.282215, [3, -0.0666667, -0.0426919], [3, 0.0666667, 0.0426919]],
                 [0.357381, [3, -0.0666667, -0.0380941], [3, 0.0666667, 0.0380941]],
                 [0.510779, [3, -0.0666667, -0.0378384], [3, 0.0666667, 0.0378384]],
                 [0.584411, [3, -0.0666667, -0.0158514], [3, 0.0666667, 0.0158514]],
                 [0.605888, [3, -0.0666667, 0], [3, 0.0666667, 0]
                  ], [0.101229, [3, -0.0666667, 0], [3, 0.0666667, 0]],
                 [0.282215, [3, -0.0666667, 0], [3, 0, 0]]])

    names.append("LShoulderRoll")
    times.append([1, 2, 2.2, 2.4, 2.6, 2.8, 3, 3.2, 3.4, 3.6,
                 3.8, 4, 4.2, 4.4, 4.6, 4.8, 5, 5.2, 5.4])
    keys.append([[0.0797259, [3, -0.333333, 0], [3, 0.333333, 0]], [0.159494, [3, -0.333333, 0], [3, 0.0666667, 0]],
                 [0.141086, [3, -0.0666667, 0], [3, 0.0666667, 0]
                  ], [0.151824, [3, -0.0666667, 0], [3, 0.0666667, 0]],
                 [0.0889301, [3, -0.0666667, 0.0404302],
                     [3, 0.0666667, -0.0404302]],
                 [-0.0907571, [3, -0.0666667, 0], [3, 0.0666667, 0]],
                 [-0.066004, [3, -0.0666667, -0.0247531], [3, 0.0666667, 0.0247531]],
                 [0.159494, [3, -0.0666667, 0], [3, 0.0666667, 0]
                  ], [0.141086, [3, -0.0666667, 0], [3, 0.0666667, 0]],
                 [0.151824, [3, -0.0666667, 0], [3, 0.0666667, 0]],
                 [0.0889301, [3, -0.0666667, 0.0404302],
                     [3, 0.0666667, -0.0404302]],
                 [-0.0907571, [3, -0.0666667, 0], [3, 0.0666667, 0]],
                 [-0.066004, [3, -0.0666667, -0.0247531], [3, 0.0666667, 0.0247531]],
                 [0.159494, [3, -0.0666667, 0], [3, 0.0666667, 0]
                  ], [0.141086, [3, -0.0666667, 0], [3, 0.0666667, 0]],
                 [0.151824, [3, -0.0666667, 0], [3, 0.0666667, 0]],
                 [0.0889301, [3, -0.0666667, 0.0404302],
                     [3, 0.0666667, -0.0404302]],
                 [-0.0907571, [3, -0.0666667, 0], [3, 0.0666667, 0]], [-0.066004, [3, -0.0666667, 0], [3, 0, 0]]])

    names.append("LWristYaw")
    times.append([1, 2, 2.2, 2.4, 2.6, 2.8, 3, 3.2, 3.4, 3.6,
                 3.8, 4, 4.2, 4.4, 4.6, 4.8, 5, 5.2, 5.4])
    keys.append([[-0.213269, [3, -0.333333, 0], [3, 0.333333, 0]],
                 [-0.573758, [3, -0.333333, 0.111641], [3, 0.0666667, -0.0223282]],
                 [-0.615176, [3, -0.0666667, 0], [3, 0.0666667, 0]],
                 [-0.412688, [3, -0.0666667, -0.0700526], [3, 0.0666667, 0.0700526]],
                 [-0.194861, [3, -0.0666667, 0], [3, 0.0666667, 0]
                  ], [-0.961676, [3, -0.0666667, 0], [3, 0.0666667, 0]],
                 [-0.763974, [3, -0.0666667, -0.0646531], [3, 0.0666667, 0.0646531]],
                 [-0.573758, [3, -0.0666667, 0], [3, 0.0666667, 0]
                  ], [-0.615176, [3, -0.0666667, 0], [3, 0.0666667, 0]],
                 [-0.412688, [3, -0.0666667, -0.0700526], [3, 0.0666667, 0.0700526]],
                 [-0.194861, [3, -0.0666667, 0], [3, 0.0666667, 0]
                  ], [-0.961676, [3, -0.0666667, 0], [3, 0.0666667, 0]],
                 [-0.763974, [3, -0.0666667, -0.0646531], [3, 0.0666667, 0.0646531]],
                 [-0.573758, [3, -0.0666667, 0], [3, 0.0666667, 0]
                  ], [-0.615176, [3, -0.0666667, 0], [3, 0.0666667, 0]],
                 [-0.411154, [3, -0.0666667, -0.0700526], [3, 0.0666667, 0.0700526]],
                 [-0.194861, [3, -0.0666667, 0], [3, 0.0666667, 0]
                  ], [-0.961676, [3, -0.0666667, 0], [3, 0.0666667, 0]],
                 [-0.763974, [3, -0.0666667, 0], [3, 0, 0]]])

    names.append("RAnklePitch")
    times.append([1, 2, 3.32, 5.4])
    keys.append(
        [[0.0951499, [3, -0.333333, 0], [3, 0.333333, 0]], [-0.31136, [3, -0.333333, 0.0337021], [3, 0.44, -0.0444867]],
         [-0.355846, [3, -0.44, 0], [3, 0.693333, 0]], [-0.31136, [3, -0.693333, 0], [3, 0, 0]]])

    names.append("RAnkleRoll")
    times.append([1, 2, 3.32, 5.4])
    keys.append([[0.122762, [3, -0.333333, 0], [3, 0.333333, 0]],
                 [0.124296, [3, -0.333333, -0.00153397], [3, 0.44, 0.00202484]],
                 [0.144238, [3, -0.44, 0], [3, 0.693333, 0]], [0.124296, [3, -0.693333, 0], [3, 0, 0]]])

    names.append("RElbowRoll")
    times.append([1, 2, 2.2, 2.4, 2.6, 2.8, 3, 3.2, 3.4, 3.6,
                 3.8, 4, 4.2, 4.4, 4.6, 4.8, 5, 5.2, 5.4])
    keys.append([[0.385075, [3, -0.333333, 0], [3, 0.333333, 0]],
                 [1.33309, [3, -0.333333, -0.0690278], [3, 0.0666667, 0.0138056]],
                 [1.34689, [3, -0.0666667, -0.0138056], [3, 0.0666667, 0.0138056]],
                 [1.43126, [3, -0.0666667, 0], [3, 0.0666667, 0]],
                 [1.31468, [3, -0.0666667, 0.0999658], [3, 0.0666667, -0.0999658]],
                 [0.83147, [3, -0.0666667, 0], [3, 0.0666667, 0]],
                 [1.16281, [3, -0.0666667, -0.083603], [3, 0.0666667, 0.083603]],
                 [1.33309, [3, -0.0666667, -0.0138056], [3, 0.0666667, 0.0138056]],
                 [1.34689, [3, -0.0666667, -0.0138056], [3, 0.0666667, 0.0138056]],
                 [1.43126, [3, -0.0666667, 0], [3, 0.0666667, 0]],
                 [1.31468, [3, -0.0666667, 0.0999658], [3, 0.0666667, -0.0999658]],
                 [0.83147, [3, -0.0666667, 0], [3, 0.0666667, 0]],
                 [1.16281, [3, -0.0666667, -0.083603], [3, 0.0666667, 0.083603]],
                 [1.33309, [3, -0.0666667, -0.0138056], [3, 0.0666667, 0.0138056]],
                 [1.34689, [3, -0.0666667, -0.0138056], [3, 0.0666667, 0.0138056]],
                 [1.43126, [3, -0.0666667, 0], [3, 0.0666667, 0]],
                 [1.31468, [3, -0.0666667, 0.0999658], [3, 0.0666667, -0.0999658]],
                 [0.83147, [3, -0.0666667, 0], [3, 0.0666667, 0]], [1.16281, [3, -0.0666667, 0], [3, 0, 0]]])

    names.append("RElbowYaw")
    times.append([1, 2, 2.2, 2.4, 2.6, 2.8, 3, 3.2, 3.4, 3.6,
                 3.8, 4, 4.2, 4.4, 4.6, 4.8, 5, 5.2, 5.4])
    keys.append(
        [[1.23176, [3, -0.333333, 0], [3, 0.333333, 0]], [0.185572, [3, -0.333333, 0.20709], [3, 0.0666667, -0.041418]],
         [0.144154, [3, -0.0666667, 0], [3, 0.0666667, 0]],
         [0.174835, [3, -0.0666667, -0.0306808], [3, 0.0666667, 0.0306808]],
         [0.351244, [3, -0.0666667, -0.0452529], [3, 0.0666667, 0.0452529]],
         [0.446352, [3, -0.0666667, 0], [3, 0.0666667, 0]
          ], [-0.036858, [3, -0.0666667, 0], [3, 0.0666667, 0]],
         [0.185572, [3, -0.0666667, 0], [3, 0.0666667, 0]
          ], [0.144154, [3, -0.0666667, 0], [3, 0.0666667, 0]],
         [0.176367, [3, -0.0666667, -0.0322132], [3, 0.0666667, 0.0322132]],
         [0.351244, [3, -0.0666667, -0.0449975], [3, 0.0666667, 0.0449975]],
         [0.446352, [3, -0.0666667, 0], [3, 0.0666667, 0]
          ], [-0.036858, [3, -0.0666667, 0], [3, 0.0666667, 0]],
         [0.185572, [3, -0.0666667, 0], [3, 0.0666667, 0]
          ], [0.144154, [3, -0.0666667, 0], [3, 0.0666667, 0]],
         [0.174835, [3, -0.0666667, -0.0306808], [3, 0.0666667, 0.0306808]],
         [0.351244, [3, -0.0666667, -0.0452529], [3, 0.0666667, 0.0452529]],
         [0.446352, [3, -0.0666667, 0], [3, 0.0666667, 0]], [-0.036858, [3, -0.0666667, 0], [3, 0, 0]]])

    names.append("RHand")
    times.append([1, 2, 2.2, 2.4, 2.6, 2.8, 3, 3.2, 3.4, 3.6,
                 3.8, 4, 4.2, 4.4, 4.6, 4.8, 5, 5.2, 5.4])
    keys.append([[0.3112, [3, -0.333333, 0], [3, 0.333333, 0]], [0, [3, -0.333333, 0], [3, 0.0666667, 0]],
                 [0.1568, [3, -0.0666667, -0.0212], [3, 0.0666667, 0.0212]],
                 [0.178, [3, -0.0666667, 0], [3, 0.0666667, 0]
                  ], [0.1616, [3, -0.0666667, 0], [3, 0.0666667, 0]],
                 [0.1672, [3, -0.0666667, 0], [3, 0.0666667, 0]],
                 [0.1668, [3, -0.0666667, 0.000399992],
                     [3, 0.0666667, -0.000399992]],
                 [0, [3, -0.0666667, 0], [3, 0.0666667, 0]], [0.1568,
                                                              [3, -0.0666667, -0.0212], [3, 0.0666667, 0.0212]],
                 [0.178, [3, -0.0666667, 0], [3, 0.0666667, 0]
                  ], [0.1616, [3, -0.0666667, 0], [3, 0.0666667, 0]],
                 [0.1672, [3, -0.0666667, 0], [3, 0.0666667, 0]],
                 [0.1668, [3, -0.0666667, 0.000399992],
                     [3, 0.0666667, -0.000399992]],
                 [0, [3, -0.0666667, 0], [3, 0.0666667, 0]], [0.1568,
                                                              [3, -0.0666667, -0.0212], [3, 0.0666667, 0.0212]],
                 [0.178, [3, -0.0666667, 0], [3, 0.0666667, 0]
                  ], [0.1616, [3, -0.0666667, 0], [3, 0.0666667, 0]],
                 [0.1672, [3, -0.0666667, 0], [3, 0.0666667, 0]], [0.1668, [3, -0.0666667, 0], [3, 0, 0]]])

    names.append("RHipPitch")
    times.append([1, 2, 3.32, 5.4])
    keys.append(
        [[0.139552, [3, -0.333333, 0], [3, 0.333333, 0]], [-0.0767419, [3, -0.333333, 0.0844141], [3, 0.44, -0.111427]],
         [-0.44797, [3, -0.44, 0], [3, 0.693333, 0]], [-0.0798099, [3, -0.693333, 0], [3, 0, 0]]])

    names.append("RHipRoll")
    times.append([1, 2, 3.32, 5.4])
    keys.append([[-0.116542, [3, -0.333333, 0], [3, 0.333333, 0]], [-0.128814, [3, -0.333333, 0], [3, 0.44, 0]],
                 [-0.108872, [3, -0.44, 0], [3, 0.693333, 0]], [-0.128814, [3, -0.693333, 0], [3, 0, 0]]])

    names.append("RHipYawPitch")
    times.append([1, 2, 3.32, 5.4])
    keys.append(
        [[-0.170232, [3, -0.333333, 0], [3, 0.333333, 0]], [-0.36505, [3, -0.333333, 0.0104588], [3, 0.44, -0.0138056]],
         [-0.378855, [3, -0.44, 0], [3, 0.693333, 0]], [-0.36505, [3, -0.693333, 0], [3, 0, 0]]])

    names.append("RKneePitch")
    times.append([1, 2, 3.32, 5.4])
    keys.append(
        [[-0.0858622, [3, -0.333333, 0], [3, 0.333333, 0]], [0.653526, [3, -0.333333, -0.156706], [3, 0.44, 0.206852]],
         [1.00481, [3, -0.44, 0], [3, 0.693333, 0]], [0.650458, [3, -0.693333, 0], [3, 0, 0]]])

    names.append("RShoulderPitch")
    times.append([1, 2, 2.2, 2.4, 2.6, 2.8, 3, 3.2, 3.4, 3.6,
                 3.8, 4, 4.2, 4.4, 4.6, 4.8, 5, 5.2, 5.4])
    keys.append([[1.46808, [3, -0.333333, 0], [3, 0.333333, 0]], [0.624379, [3, -0.333333, 0], [3, 0.0666667, 0]],
                 [0.744032, [3, -0.0666667, 0], [3, 0.0666667, 0]],
                 [0.510865, [3, -0.0666667, 0.0723538], [3, 0.0666667, -0.0723538]],
                 [0.309909, [3, -0.0666667, 0], [3, 0.0666667, 0]],
                 [0.61671, [3, -0.0666667, -0.0692858], [3, 0.0666667, 0.0692858]],
                 [0.725624, [3, -0.0666667, 0], [3, 0.0666667, 0]
                  ], [0.624379, [3, -0.0666667, 0], [3, 0.0666667, 0]],
                 [0.744032, [3, -0.0666667, 0], [3, 0.0666667, 0]],
                 [0.510865, [3, -0.0666667, 0.0723538], [3, 0.0666667, -0.0723538]],
                 [0.309909, [3, -0.0666667, 0], [3, 0.0666667, 0]],
                 [0.61671, [3, -0.0666667, -0.0692858], [3, 0.0666667, 0.0692858]],
                 [0.725624, [3, -0.0666667, 0], [3, 0.0666667, 0]
                  ], [0.624379, [3, -0.0666667, 0], [3, 0.0666667, 0]],
                 [0.744032, [3, -0.0666667, 0], [3, 0.0666667, 0]],
                 [0.510865, [3, -0.0666667, 0.0723538], [3, 0.0666667, -0.0723538]],
                 [0.309909, [3, -0.0666667, 0], [3, 0.0666667, 0]],
                 [0.61671, [3, -0.0666667, -0.0692858], [3, 0.0666667, 0.0692858]],
                 [0.725624, [3, -0.0666667, 0], [3, 0, 0]]])

    names.append("RShoulderRoll")
    times.append([1, 2, 2.2, 2.4, 2.6, 2.8, 3, 3.2, 3.4, 3.6,
                 3.8, 4, 4.2, 4.4, 4.6, 4.8, 5, 5.2, 5.4])
    keys.append([[-0.067538, [3, -0.333333, 0], [3, 0.333333, 0]],
                 [-0.0337899, [3, -0.333333, -0.033748],
                     [3, 0.0666667, 0.00674961]],
                 [0.164096, [3, -0.0666667, 0], [3, 0.0666667, 0]
                  ], [0.124212, [3, -0.0666667, 0], [3, 0.0666667, 0]],
                 [0.182504, [3, -0.0666667, 0], [3, 0.0666667, 0]],
                 [0.0843279, [3, -0.0666667, 0.0217316],
                     [3, 0.0666667, -0.0217316]],
                 [0.052114, [3, -0.0666667, 0.0196863], [3, 0.0666667, -0.0196863]],
                 [-0.0337899, [3, -0.0666667, 0], [3, 0.0666667, 0]
                  ], [0.164096, [3, -0.0666667, 0], [3, 0.0666667, 0]],
                 [0.124212, [3, -0.0666667, 0], [3, 0.0666667, 0]
                  ], [0.182504, [3, -0.0666667, 0], [3, 0.0666667, 0]],
                 [0.0843279, [3, -0.0666667, 0.0217316],
                     [3, 0.0666667, -0.0217316]],
                 [0.052114, [3, -0.0666667, 0.0196863], [3, 0.0666667, -0.0196863]],
                 [-0.0337899, [3, -0.0666667, 0], [3, 0.0666667, 0]
                  ], [0.164096, [3, -0.0666667, 0], [3, 0.0666667, 0]],
                 [0.124212, [3, -0.0666667, 0], [3, 0.0666667, 0]
                  ], [0.182504, [3, -0.0666667, 0], [3, 0.0666667, 0]],
                 [0.0843279, [3, -0.0666667, 0.0217316],
                     [3, 0.0666667, -0.0217316]],
                 [0.052114, [3, -0.0666667, 0], [3, 0, 0]]])

    names.append("RWristYaw")
    times.append([1, 2, 2.2, 2.4, 2.6, 2.8, 3, 3.2, 3.4, 3.6,
                 3.8, 4, 4.2, 4.4, 4.6, 4.8, 5, 5.2, 5.4])
    keys.append([[-0.10282, [3, -0.333333, 0], [3, 0.333333, 0]], [0.421808, [3, -0.333333, 0], [3, 0.0666667, 0]],
                 [0.409536, [3, -0.0666667, 0], [3, 0.0666667, 0]],
                 [0.46476, [3, -0.0666667, -0.0127834], [3, 0.0666667, 0.0127834]],
                 [0.486237, [3, -0.0666667, 0], [3, 0.0666667, 0]],
                 [0.472429, [3, -0.0666667, 0.0138073], [3, 0.0666667, -0.0138073]],
                 [0.131882, [3, -0.0666667, 0], [3, 0.0666667, 0]
                  ], [0.421808, [3, -0.0666667, 0], [3, 0.0666667, 0]],
                 [0.409536, [3, -0.0666667, 0], [3, 0.0666667, 0]],
                 [0.46476, [3, -0.0666667, -0.0127834], [3, 0.0666667, 0.0127834]],
                 [0.486237, [3, -0.0666667, 0], [3, 0.0666667, 0]],
                 [0.472429, [3, -0.0666667, 0.0138073], [3, 0.0666667, -0.0138073]],
                 [0.131882, [3, -0.0666667, 0], [3, 0.0666667, 0]
                  ], [0.421808, [3, -0.0666667, 0], [3, 0.0666667, 0]],
                 [0.409536, [3, -0.0666667, 0], [3, 0.0666667, 0]],
                 [0.46476, [3, -0.0666667, -0.0127834], [3, 0.0666667, 0.0127834]],
                 [0.486237, [3, -0.0666667, 0], [3, 0.0666667, 0]],
                 [0.472429, [3, -0.0666667, 0.0138073], [3, 0.0666667, -0.0138073]],
                 [0.131882, [3, -0.0666667, 0], [3, 0, 0]]])

    try:
        motion = ALProxy("ALMotion", nao_ip, nao_port)
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
