import os

cmd_pid = "adb shell ps |grep com.huami.midong|grep -v service|awk '{print $2}'"
pid = os.popen(cmd_pid).read().strip()

if pid == "":
    print "Midong is not installed or not launced!!!"

if pid == "error: no devices/emulators found":
    print "No device connected!!!"

if pid != "":
    print "pid is : " + pid

    cmd_uid = "adb shell cat /proc/" + pid + "/status | grep Uid|awk '{print $2}'"
    uid = os.popen(cmd_uid).read().strip()
    print "uid is : " + uid

    cmd_tcp_rcv = "adb shell cat /proc/uid_stat/" + uid + "/tcp_rcv"
    cmd_tcp_snd = "adb shell cat /proc/uid_stat/" + uid + "/tcp_snd"
    tcp_rcv = os.popen(cmd_tcp_rcv).read()
    tcp_snd = os.popen(cmd_tcp_snd).read()
    rcv_K = int(tcp_rcv) / 1024
    snd_K = int(tcp_snd) / 1024
    rcv_M = int(tcp_rcv) / 1024 / 1024
    snd_M = int(tcp_snd) / 1024 / 1024
    print "tcp receive for midong is : " + str(rcv_K) + "K / " + str(rcv_M) + "M"
    print "tcp send from midong is : " + str(snd_K) + "K / " + str(snd_M) + "M"
