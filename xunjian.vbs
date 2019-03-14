Dim OK
set bag=getobject("winmgmts:\\.\root\cimv2") 
set pipe=bag.ExecQuery("select * from win32_process where name='wscript.exe'")
if pipe.count > 1 then
    Msgbox "do not touch again"
else 
Set ws = CreateObject("Wscript.Shell")
Do
    ws.run "daily_check.exe",0
    Wscript.Sleep(1000*3600*24)
Loop
end if
