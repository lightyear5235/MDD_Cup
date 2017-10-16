class Weather:
    def __init__(self, date, time, areaid, temp, wind, rain):
        self.date = date
        self.time = time
        self.areaid = areaid
        self.temp = temp
        self.wind = wind
        self.rain = rain

class Area:
    def __init__

def getAreaWeatherInfo(fileName):
    resultMap = {}
    fr = open(fileName, "r")
    fr.readline() #jump the first line
    for line in fr.readline():
        info = line[:-1].split(",")
        wi = Weather(info[0], line[1], line[3], line[4], line[5], line[6])
        key = info[0] + "\t" + info[1] + "\t" + info[3]
        resultMap[key] = wi
    return resultMap

areaWeatherInfo = getAreaWeatherInfo()
