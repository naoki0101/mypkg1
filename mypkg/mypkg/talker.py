import rclpy
from rclpy.node import Node
from person_msgs.srv import Query

<<<<<<< HEAD
class Talker():
    def __init__(self, node):
        self.pub = node.create_publisher(Int16, "countup", 10)
        self.n = 0
        node.create_timer(0.5, self.cb)

    def cb(self):
        msg = Int16()
        msg.data = self.n
        self.pub.publish(msg)
        self.n += 1

def main():
    rclpy.init()
    node = Node("talker")
    talker = Talker(node)
    rclpy.spin(node)
=======
def cb(request, response):
    if request.name == "大坪直生":
        response.age = 20
    else:
        response.age = 255
    
    return response
   
rclpy.init()
node = Node("talker")
srv = node.create_service(Query, "query", cb)
rclpy.spin(node)
>>>>>>> 21979bbadd24cd0a829297ee7e2d5d64d814aae4

