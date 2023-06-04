import json
import plotext as plt

with open("history.json", "r") as file:
    json_data = file.read()

data =  json.loads(json_data)

open_values = list(data["Open"].values())


plt.plot_size(90,20)

plt.plot(open_values)

plt.show()

