# import csv
#
# with open("weather_data.csv") as weather:
#     weather_list = csv.reader(weather)
#     temperature = []
#     for temp in weather_list:
#         if temp[1] != "temp":
#             temperature.append(int(temp[1]))
#     print(temperature)

import pandas

# data = pandas.read_csv("weather_data.csv")
# data_dict = data.to_dict()
#
# average = data["temp"].mean()
# print(round(average, 2))
#
# max_val = data["temp"].max()
# print(max_val)
#
# # getting data from columns
# print(data.condition)
# print(data["condition"])

# # extracting a row
# print(data[data.day == "Monday"])
# print(data[data.temp == data.temp.max()])

# # getting data in a row
# monday = data[data.day == "Monday"]
# monday_temp_f = (int(monday.temp) * (9/5)) + 32
# print(monday_temp_f)

# create dataframe from scratch
data_dict = {
    "students": ["Amy", "James", "Ishaan"],
    "scores": [76, 56, 65]
}

data = pandas.DataFrame(data_dict)
# data.to_csv('new_data.csv')
print(data)
