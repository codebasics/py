# This program shows that without using pandas getting answers on below questions is hard and not convinient
# (1) Max temperature in New York in month of January
# (2) List of days when it rained
# (3) Average speed of wind in month of january
__parsed_rows = []

def parse_csv():
    import csv
    __file_path = "nyc_weather.csv"
    __index = {
        'date': 0,
        'temperature': 1,
        'DewPoint': 2,
        'Humidity': 3,
        'Sea_Level_PressureIn': 4,
        'VisibilityMiles': 5,
        'WindSpeedMPH': 6,
        'PrecipitationIn': 7,
        'CloudCover': 8,
        'Events' : 9,
        'WindDirDegrees': 10
    }

    global __parsed_rows
    with open(__file_path, "r") as f:
        reader = csv.reader(f)
        next(reader, None)
        for row in reader:
            __parsed_rows.append({
                'date':  row[__index['date']],
                'temperature': row[__index['temperature']],
                'DewPoint': row[__index['DewPoint']],
                'Humidity': row[__index['Humidity']],
                'Sea_Level_PressureIn': row[__index['Sea_Level_PressureIn']],
                'VisibilityMiles': row[__index['VisibilityMiles']],
                'WindSpeedMPH': row[__index['WindSpeedMPH']],
                'PrecipitationIn': row[__index['PrecipitationIn']],
                'CloudCover': row[__index['CloudCover']],
                'Events': row[__index['Events']],
                'WindDirDegrees': row[__index['WindDirDegrees']]
            })


def get_days_for_event(event_name):
    days = []
    for row in __parsed_rows:
        if row['Events'] == event_name:
            days.append(row['date'])
    return days

def get_max_temperature():
    max_temp = 0
    for row in __parsed_rows:
        if int(row['temperature']) > max_temp:
            max_temp = int(row['temperature'])
    return max_temp

def get_average_wind_speed():
    total = 0
    count = 0
    for row in __parsed_rows:
        speed = 0 if row['WindSpeedMPH']=='' else int(row['WindSpeedMPH'])
        total += speed
        count+=1
    return total/count

if __name__=="__main__":
    parse_csv()

    print("Max temperature is: ",get_max_temperature())
    print ("Days of rain: ", get_days_for_event('Rain'))
    print("Average wind speed is: ", get_average_wind_speed())





