import pandas

# data = pandas.read_csv("weather_data.csv")
# print(type(data))
# print(type(data["temp"]))

# #to print avg temp
# temp_list = data['temp'].to_list()
# average = sum(temp_list)/len(temp_list)
# print(average)
#
# print(data["temp"].mean())

# max temp
# print(data["temp"].max())

# #get data in row
# print(data[data.day == "Monday"])
# print(data[data.temp == data.temp.max()])

#from centeral_park_census_squirrel_data  count number of squriels in different colors and place it in squriel_count.csv file
data = pandas.read_csv("Centeral_Park_Squirrel_Census_Squirrel_Data.csv")

cinnamon = data[data['Primary Fur Color'] == "Cinnamon"]
gray = data[data['Primary Fur Color'] == "Gray"]
black = data[data['Primary Fur Color'] == "Black"]

data_dict={
    'Primary Fur Color' : { 0 : "Cinnamon" , 1 : "Gray", 2 : "Black"},
    "Count" : {0 : len(cinnamon), 1 : len(gray), 2 : len(black)},
}

new_data = pandas.DataFrame(data_dict)
new_data.to_csv("new_data.csv")