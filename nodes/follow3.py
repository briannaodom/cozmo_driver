#!/usr/bin/env python
import rospy
from geometry_msgs.msg import PointStamped
from geometry_msgs.msg import Twist
#from math import cos, sin

#rospy.loginfo("To stop cozmo CTRL + C")
#rospy.on_shutdown(shutdown)

tag_pos = PointStamped

#prev_error = 0
#integral = 0
#sampT = 1000                  # sample time (1 sec in ms) for constant interval
#Kp = 30                       # proportional gain
#Ki = 0*sampT              # integral gain
#Kd = 20*sampT               # derivative gain
#tprev = 0
#lastTagPose = 0


def main():

    while not rospy.is_shutdown():
        #calc_PID(tag_pos)
        #cozmo_follow(PICval)
        cozmo_follow(tag_pos)


#def calc_PID(tag_pos):
    #tnow = rospy.get_time()/1000                                 # changed to milliseconds
    #global prev_error, integral, Kp, Ki, Kd, tprev, lastTagPose  # PID controller
    #if tnow-tprev >= sampT:
        #error = 1-tag_pos.point.x
        #integral = integral+error                              # ki*error
        #if integral >  # maxVal:
           # integral = 0  # max integralMax?
        #else:
          #  integral = integral
        #deriv = error - prev_error               
        #PIDval = Kp*error+Ki*integral+Kd*deriv
        #if PIDval >  # maxVal:
        #    PIDval = 0  # maxPID?
        #else:
        #    PIDval = PIDval
        #tprev = tnow
        #prev_error = error
        #lastTagPose = tag_pos.point.x
        #return PIDvalval
    #else:
        #PIDval = 0
        #return PIDval


#def cozmo_follow(PIDval):
def cozmo_follow(tag_pos):
        coz_vel = Twist()
       #coz_vel.linear.x = error + PIDval               # working to add correct x lin vel
        coz_vel.linear.x = 1-tag_pos.point.x
        coz_vel.linear.y = 0
        coz_vel.linear.z = 0
        coz_vel.angular.x = 0
        coz_vel.angular.y = 0
        coz_vel.angular.z = 0                           # working to add omega term
        cozmo_follow_pub.publish(coz_vel)


if __name__ == '__main__':

    try:
        rospy.init_node('cozmo_following_ar_tag', anonymous=TRUE)

        tag_sub = rospy.Subscriber('tag_position', PointStamped, cozmo_follow)

        cozmo_follow_pub = rospy.Publisher('cmd_vel', Twist, queue_size=100)

        rospy.spin()

    except rospy.ROSInterruptException:
        pass
