#!/usr/bin/env python3
import rospy
import subprocess
import re
from turtlebro.msg import WiFi

rospy.init_node('wifi_signal_publisher')
pub = rospy.Publisher('/wifi_signal', WiFi, queue_size=1)
rate = rospy.Rate(1)

def getSignalMsg():

    wifi_signal = WiFi()

    devices = subprocess.check_output(['iwconfig','wlan0'])

    # decode it to strings
    devices = devices.decode('ascii')
    str = devices.replace("\r","")
    match = re.search(r'Bit Rate:(\d+) Mb/s', str)
    wifi_signal.bit_rate =  match[1]

    match = re.search(r'Link Quality=(\d+)/100', str)
    wifi_signal.link_quality =  int(match[1])    

    match = re.search(r'Signal level=(\d+)/100', str)
    wifi_signal.signal_level =  int(match[1])    

    return wifi_signal
    
while not rospy.is_shutdown():

    wifi_signal = getSignalMsg()
    pub.publish(wifi_signal)
    rate.sleep()

