磁盘空间#df -lP | grep -e 'boot$' | awk '{print $5}'#<85%
磁盘空间#df -lP | grep -e '/$' | awk '{print $5}'#>5%
内存#free -m | sed -n '3p' | awk '{printf("%d%\n", 1319/30793*100)}'#<70%
swap使用情况#free -m | awk '{if(NR==4){print $3}}'#=0
nginx1进程存在#ps -ef | grep nginx1 | grep master | wc -l#=1
nginx2进程存在#ps -ef | grep nginx2 | grep master | wc -l#=2
kafka进程存在#ps -ef | grep java | grep kafka | wc -l#=2
zookeeper进程存在#ps -ef | grep java | grep -e 'zoo.cfg$' | wc -l#=1