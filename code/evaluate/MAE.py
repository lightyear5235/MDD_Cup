import math
import sys

def MAE_evaluate(filename):
    lineCnt = 0
    maeSum = 0.0
    fr = open(filename, "r")
    for line in fr.readline():
        info = line[:-1].split("\t")
        lineCnt += 1
        maeSum += math.fabs(int(info[2]) - int(info[1]))
    return maeSum / lineCnt

MAE_evaluate(sys.argv[1])
