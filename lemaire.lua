#!/usr/bin/env lua


local cjson = require("cjson")

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

