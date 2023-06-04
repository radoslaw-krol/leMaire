local json = require("json")
local inspect = require("inspect")

-- Assuming you have a JSON file named "data.json"
local file = io.open("data.json", "r")
local content = file:read("*a")
file:close()

local data = json.decode(content)

local formattedData = inspect(data)


-- Print the JSON data as a nicely formatted list
print(formattedData)

