import rclpy
from rclpy.node import Node
from std_msgs.msg import Int16
rclpy.init()
node = Node("listener")

def honsuu_cb(honsuu_pub):
    global node
    node.get_logger().info("タバコを%d本吸いました" % honsuu_pub.data)
        

def zyumyou_cb(zyumyou_pub):
    global node
    node.get_logger().info("寿命が%d分減りました" % zyumyou_pub.data)



def main():
    honsuu_pub = node.create_subscription(Int16, "honsuu", honsuu_cb, 10)
    zyumyou_pub = node.create_subscription(Int16, "zyumyou", zyumyou_cb, 10)
    rclpy.spin(node)
