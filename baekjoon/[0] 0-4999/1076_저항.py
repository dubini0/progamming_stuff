colors = {"black": [0, 1], "brown": [1, 10], "red": [2, 100], "orange": [3, 1000], "yellow":[4, 10000],
            "green": [5, 100000], "blue": [6, 1000000], "violet": [7, 10000000], "grey": [8, 100000000], "white": [9, 1000000000]}

color1 = input().lower()
color2 = input().lower()
color3 = input().lower()

value = str(colors[color1][0]) + str(colors[color2][0])
multiply = colors[color3][1]

print(int(value) * multiply)
