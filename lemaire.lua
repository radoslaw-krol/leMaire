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

    -- Remove date header
      -- Remove the date header from the JSON data
    local json_content = json_data:gsub("%-%-%-%-%- %d%d%d%d%-%d%d%-%d%d %-%-%-%-%-\n", "")


    -- Parse the JSON data
    local data = cjson.decode(json_content)

    -- Check if data exists and is a table
    if type(data) == "table" then
        -- Iterate over each date entry
        for date, entry in pairs(data) do
            print("----- " .. date .. " -----")
            -- Access and display specific parts of the entry
            if entry and entry.symbol then
                print("Symbol: " .. entry.symbol)
            else
                print("Symbol field not found in JSON data")
            end

            if entry and entry.bid then
                print("Bid: " .. entry.bid)
            else
                print("Bid field not found in JSON data")
            end

            -- You can access and process other properties as needed
        end
    else
        print("Invalid JSON data")
    end
end

showArt()

--Run menu loop


local choice = 0

while choice ~= 3 do
 menu.showMenu()

choice = io.read("*n")

if choice == 1 then

  os.execute("python3 api.py")
elseif choice == 2 then
  print("Executing Program...")
  executeProgram()
  
elseif choice == 3 then
  print("Quiting Program...")
end
end
