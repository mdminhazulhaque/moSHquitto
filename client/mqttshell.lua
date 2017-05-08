-- @AUTHOR Md. Minhazul Haque
-- @DATE   2017-05-08
-- @BRIEF  SSH over MQTT

local mqtt   = require "mosquitto"

function get_mac()
    io.input("/sys/class/net/eth0/address")
    t = io.read("*line")
    return t
end

function exec_cmd(command)
    local handle = io.popen(command, "r")
    local result = handle:read("*a")
    handle:close()
    return result
end

local mac = get_mac()
local topic_cmd = "shell/"..mac.."/execute"
local topic_fb = "shell/"..mac.."/result"
local prompt = mac.." > "

local client = mqtt.new()

client.ON_MESSAGE = function(mid, topic, payload)
    local data = prompt..payload.."\n"..exec_cmd(payload)
    client:publish(topic_fb, data, 2)
end

client.ON_CONNECT = function()
    client:subscribe(topic_cmd, 2)
end

client:login_set("minhaz", "minhaz")
client:connect("localhost", 1883)
client:loop_forever()
