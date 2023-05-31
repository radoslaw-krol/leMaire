#!/usr/bin/env lua

--dependancies

local cjson = require("cjson")
local menu = require("menu")
local art = require("art")


local function executeProgram()
  
-- Read the JSON data from file
local file = io.open("result.json", "r")
local json_data = file:read("*a")
file:close()

-- Parse the JSON data
local data = cjson.decode(json_data)

-- Access and display specific parts of the JSON
if data and data.symbol then
    print("Symbol: " .. data.symbol)
else
    print("Symbol field not found in JSON data")
end

if data and data.bid then
    print("Bid: " .. data.bid)
else
    print("Bid field not found in JSON data")
end

end

-- Display dashboard art

showArt()

--Run menu loop


local choice = 0

while choice ~= 3 do
 menu.showMenu()

choice = io.read("*n")

if choice == 1 then

  os.execute("python3 apicall.py")
elseif choice == 2 then
  print("Executing Program...")
  executeProgram()
  
elseif choice == 3 then
  print("Quiting Program...")
end
end
