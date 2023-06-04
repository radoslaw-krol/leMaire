local cjson = require("cjson")
local inspect = require("inspect")

local file_path = "history.json"

local file = io.open(file_path, "r")




if file then
  local json_data = file:read("*all")
  local data = cjson.decode(json_data)
  local formatted_data = inspect(data)
  file:close()

  print(formatted_data)

else
  print("Failed to open the file: " ..file_path)
end


