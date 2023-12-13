#!/usr/bin/env python3

import rospy
import rospkg
import time
import os 

from airsim_base.types import DrivetrainType, YawMode 
import numpy as np

from airsim_gym.environment import Env

PATH_FILE = os.path.abspath(__file__)

if __name__ == "__main__":
    rospy.init_node("image_collect", anonymous=False)

    pkg_name = rospkg.get_package_name(PATH_FILE)
    
    env = Env(pkg_name)
    
    targetp = [(30, (np.pi/3)), (30, (5*np.pi/6)), (30, (5*np.pi/4)), (30, (7*np.pi/4))]
    

    env.client.takeoffAsync(vehicle_name='Hydrone').join()
    env.client.hoverAsync("Hydrone").join()
    z = 100

    env.client.moveToZAsync(z, 1, vehicle_name='Hydrone').join()
    

    path = [env.spawn_resources._oriented_target_vision_to_vehicle('Hydrone', 'eolic', tp[0], 20, tp[1]) for tp in targetp]
    rospy.logwarn(f"path -> {path}")
    env.client.simSetTraceLine([1.0, 0.0, 0.0, 1.0], 50, "Hydrone")
    """
    
    for x, y, phi in path:
        rospy.logwarn(f"pose -> {x, y, phi}")
        env.client.moveToPositionAsync(x, y, z, 10, drivetrain=DrivetrainType.MaxDegreeOfFreedom).join()
        time.sleep(2)
        env.spawn_resources._set_vehicle_pose('Hydrone', (x, y, z), (0, 0, phi))
        time.sleep(5)
        env.debbug_resources.save_assync_images(['Stereo_Cam', 'Stereo_Cam', 'Segmentation_Image'], [0,1,5])
        time.sleep(2)
        rospy.logwarn(f"finishing pose... -> {x, y, phi}")
    
    """