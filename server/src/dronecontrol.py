# import the necessary packages
import cv2
from djitellopy import Tello
import time
import threading

class DroneControl():
    def __init__(self):
        self.drone = Tello()                       # Instantiate a Tello Object
        self.drone.connect()                       # Connect to the drone
        self.drone.streamoff()                     # In case stream never exited before
        self.drone.streamon()                      # Turn on drone camera stream
        self.timer = 0                             # Timing for printing statements
        self.flying = False                        # Keep track of flying state
        # How many video frames have been requested
        self.frame_count = 0
        self.init_frames = 100                     # Begin flying only after init_frames
        self.myThread = threading.Thread(target=self.fly)

        self.drone.TIMEOUT = 20

    def __del__(self):
        self.drone.streamoff()

    def get_state(self):
        self.drone.get_battery()
        self.drone.send_read_command("acceleration?")
        self.drone.send_read_command("time?")
        self.drone.get_speed()
        self.drone.send_read_command("height?")
        self.drone.send_read_command("temp?")
        self.drone.send_read_command("attitude?")
        self.drone.send_read_command("baro?")
        self.drone.send_read_command("tof?")
        self.drone.send_read_command("wifi?")




#        self.drone.get_flight_time()
#        self.drone.get_height()
#        self.drone.get_temperature()
#        self.drone.get_pitch()
#        self.drone.get_roll()
#        self.drone.get_yaw()
#        self.drone.get_barometer()
#        self.drone.get_acceleration_x()
#        self.drone.get_acceleration_y()
#        self.drone.get_acceleration_z()
#        self.drone.get_distance_tof()
#        self.drone.query_wifi_signal_noise_ratio()
        
        ####################################################
        ############## ADD YOUR CODE HERE ##################
        ####################################################

    def fly(self):





##CHALLENGE 2 MODIFIED
##My room was too small to do challenge 2 so I created a modified version. The origial code is below.
        time.sleep(5)
        self.drone.takeoff()
        time.sleep(5)
        time.sleep(5)
        self.drone.move_forward(50)
        time.sleep(5)
        self.drone.rotate_counter_clockwise(45)
        time.sleep(5)
        self.drone.move_forward(50)
        time.sleep(5)
        self.drone.rotate_counter_clockwise(70)
#        time.sleep(5)
#        self.drone.flip_left()
        time.sleep(5)
        self.drone.move_down(25)
        time.sleep(5)
#        self.drone.flip_right()
#        time.sleep(5)
        self.drone.move_back(25)
        time.sleep(5)
#        self.drone.flip_back()
#        time.sleep(5)
        self.drone.rotate_clockwise(115)
        time.sleep(5)
        self.drone.send_control_command('curve %s %s %s %s %s %s %s' % (-50,0,-100,-108,25,-100,50))
##        self.drone.curve_xyz_speed(29,-50,-161,0,0,0,50)
        time.sleep(5)
        self.drone.land()

##CHALLENGE 2 ORIGINAL
#        time.sleep(5)
#        self.drone.takeoff()
#        time.sleep(5)
#        time.sleep(5)
#        self.drone.move_forward(100)
#        time.sleep(5)
#        self.drone.rotate_counter_clockwise(45)
#        time.sleep(5)
#        self.drone.move_forward(100)
#        time.sleep(5)
#        self.drone.rotate_counter_clockwise(70)
#        time.sleep(5)
#        self.drone.flip_left()
#        time.sleep(5)
#        self.drone.move_down(50)
#        time.sleep(5)
#        self.drone.flip_right()
#        time.sleep(5)
#        self.drone.flip_right()
#        time.sleep(5)
#        self.drone.move_back(75)
#        time.sleep(5)
#        self.drone.flip_back()
#        time.sleep(5)
#        self.drone.rotate_clockwise(115)
#        time.sleep(5)
#        self.drone.send_control_command('curve %s %s %s %s %s %s %s' % (-119,25,0,-238,50,38,50))
#        time.sleep(5)
#        self.drone.land()






##CHALLENGE 1
#        time.sleep(5)
#        self.drone.takeoff()
#        time.sleep(5)
#        self.drone.move_forward(100)
#        time.sleep(5)
#        self.drone.rotate_counter_clockwise(90)
#        time.sleep(5)
#        self.drone.move_forward(100)
#        time.sleep(5)
#        self.drone.rotate_counter_clockwise(90)
#        time.sleep(5)
#        self.drone.move_forward(100)
#        time.sleep(5)
#        self.drone.rotate_counter_clockwise(90)
#        time.sleep(5)
#        self.drone.move_forward(100)
#        time.sleep(5)
#        self.drone.rotate_counter_clockwise(90)
#        time.sleep(5)
#        self.drone.land()





        ####################################################
        ############## ADD YOUR CODE HERE ##################
        ####################################################

    def get_frame(self):
        # only begin flying once a video feed is established
        self.frame_count += 1
        if self.flying == False and self.frame_count > self.init_frames:
            self.flying = True
            # self.fly()
            self.myThread.start()
        # Grab a frame and resize it
        frame_read = self.drone.get_frame_read()
        if frame_read.stopped:
            return
        frame = cv2.resize(frame_read.frame, (360, 240))
        # Print status to the log every 10 seconds
        if(time.time() - self.timer > 10):
            self.timer = time.time()
            self.get_state()
        # encode OpenCV raw frame to jpeg
        ret, jpeg = cv2.imencode('.jpg', frame)
        return jpeg.tobytes()
