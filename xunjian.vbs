do

set ws=createobject("wscript.shell")

ws.run"d:\daily_check\daily_check.exe",x 'x为参数，可选值如下.

wscript.sleep 36000 '36000为一分钟，具体可以自己改。

ws.run "taskkill /im daily_check.exe /f",vbhide

loop