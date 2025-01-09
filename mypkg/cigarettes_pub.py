# SPDX-FileCopyrightText: 2025 Shizen Kotake
# SPDX-License-Identifier: BSD-3-Clause
import rclpy
from rclpy.node import Node
from std_msgs.msg import Int16
import time

rclpy.init()
time.sleep(7)
node = Node("cigarettes_pub")
honsuu_pub = node.create_publisher(Int16, "honsuu", 10)
zyumyou_pub = node.create_publisher(Int16, "zyumyou", 10)

n = 1

def cb():
    global n
    honsuu_msg = Int16()
    zyumyou_msg = Int16()
    honsuu_msg.data = n
    zyumyou_msg.data = n * 6
    honsuu_pub.publish(honsuu_msg)
    zyumyou_pub.publish(zyumyou_msg)
    n += 1

def main():
    node.create_timer(1, cb)
    rclpy.spin(node)
