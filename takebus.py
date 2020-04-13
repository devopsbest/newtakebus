#coding=utf-8
import requests
import json


url = "https://shanghaicity.openservice.kankanews.com/public/bus/Getstop"
requests.packages.urllib3.disable_warnings()

changde_id =18


def get_cars_detail(stopid):
    my_url = url
    data = {
        "stoptype": 1,
        "stopid": "{}.".format(stopid),
        "sid": "56a7be0ecd56f84406d39759c67ee665"
    }
    get_response = requests.post(url=my_url, data=data, verify=False)

    if get_response.status_code == 200:

        result = json.loads(get_response.text)

        return result[0]["terminal"],int(result[0]["stopdis"]),int(result[0]["distance"]),int(result[0]["time"])

    else:
        print("Didn't kick off, please realex!")


import arrow

current_time = arrow.now()
import math

if __name__ == "__main__":
    car,stop_num,distance,minutes=get_cars_detail(changde_id)

    next_id = changde_id -1 if stop_num ==0 else changde_id - stop_num

    next_car,next_stop_num,next_distance,next_minutes=get_cars_detail(next_id)
    print("927 first bus info: bus {},stop number {},distance {},{} minutes".format(car,stop_num,distance, math.ceil(minutes/60)))
    print("about reach at {}".format(current_time.shift(seconds=+(minutes)).format("HH:mm:ss")))

    print("927 second bus info: bus {},stop number {},distance {},{} minutes".format(next_car,stop_num+next_stop_num,distance+next_distance, math.ceil((minutes+next_minutes)/60)))
    print("about reach at {}".format(current_time.shift(seconds=+(minutes+next_minutes)).format("HH:mm:ss")))
