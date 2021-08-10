import pandas

squirrel_data = pandas.read_csv("Central_Park_Squirrel_census.csv")
print(type(squirrel_data))
squirrel_fur_color = squirrel_data["Primary Fur Color"]
black = 0
gray = 0
cinnamon = 0
for color in squirrel_fur_color:
    if color == "Black":
        black += 1
    elif color == "Gray":
        gray += 1
    elif color == "Cinnamon":
        cinnamon += 1
    else:
        pass

squirrel_color = {
    "colors": ["Black", "Gray", "Cinnamon"],
    "squirrel_no": [black, gray, cinnamon]
}

squirrel_color_no = pandas.DataFrame(squirrel_color)
squirrel_color_no.to_csv("Squirrel_color.csv")
