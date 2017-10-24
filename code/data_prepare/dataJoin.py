def getTimeHour(t):
    return t

def getTimeMinute():

class Weather:
    def __init__(self, date, time, areaid, temp, wind, rain):
        self.date = date
        self.time = time
        self.areaid = areaid
        self.temp = temp
        self.wind = wind
        self.rain = rain

class Area:
    def __init__(self, date, time, areaid, working_rider_num, notbusy_working_rider_num, not_fetched_order_num, deliverying_order_num):
        self.date = date
        self.time = time
        self.areaid = areaid
        self.working_rider_num = working_rider_num
        self.notbusy_working_rider_num = notbusy_working_rider_num
        self.not_fetched_order_num = not_fetched_order_num
        self.deliverying_order_num = deliverying_order_num

class Order:
    def __init__(self, order_id, poi_id,area_id,food_total_value,box_total_value,food_num,delivery_distance,order_time,arriveshop_time,fetch_time,finish_time,waiting_order_num,delivery_duration):
        self.order_id = order_id
        self.poi_id = poi_id
        self.area_id = area_id
        self.food_total_value = food_total_value
        self.box_total_value = box_total_value
        self.food_num = food_num
        self.delivery_distance = delivery_distance
        self.date = getTimeDate(order_time)
        self.orderHour = getTimeHour(order_time)
        self.orderMinute = getTimeMinute(order_time)
        self.arriveshopHour = arriveshop_time
        self.fetch_time = fetch_time
        self.finish_time = finish_time
        self.waiting_order_num = waiting_order_num
        self.delivery_duration = delivery_duration


def getAreaWeatherInfo(fileName):
    resultMap = {}
    fr = open(fileName, "r")
    fr.readline() #jump the first line
    for line in fr.readline():
        info = line[:-1].split(",")
        wi = Weather(info[0], line[1], line[3], line[4], line[5], line[6])
        key = wi.date + "\t" + wi.time + "\t" + wi.areaid
        resultMap[key] = wi
    fr.close()
    return resultMap

def getAreaInfo(fileName):
    resultMap = {}
    fr = open(fileName, "r")
    fr.readline() # jump the first line
    for line in fr.readline():
        info = line[:-1].split(",")
        ai = Area(info[0], info[1], info[3], info[4], info[5], info[6], info[7])
        key = ai.date + "\t" + ai.time + "\t" + ai.areaid
        resultMap[key] = ai
    fr.close()
    return resultMap

def genTrainDataFeature(fileName, areaInfoMap, areaWeatherInfoMap):
    fr = open(fileName, "r")
    fr.readline() # jump the first line
    for line in fr.readline():



areaWeatherInfoMap = getAreaWeatherInfo("../../data/train/weather_realtime.csv")
areaInfoMap = getAreaInfo("../../data/train/area_realtime.csv")
genTrainDataFeature("../../data/train/waybill_info.csv", areaInfoMap, areaWeatherInfoMap)
