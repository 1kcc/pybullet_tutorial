
#!/usr/bin/env python

import time
import math

import pybullet as p
import pybullet_data

CLIENT = p.connect(p.GUI, options='--width=1024 --height=786')

def setup_world():
    """
    function to init the world
    """
    p.resetSimulation()
    p.setPhysicsEngineParameter(deterministicOverlappingPairs=1)
    p.setRealTimeSimulation(0, CLIENT)

def main():
    """
    main function
    """
    setup_world()
    
    p.setAdditionalSearchPath(pybullet_data.getDataPath())
    p.setGravity(0, 0, -10)

    # urdf_fn = '/Users/krishneelchaudhary/Downloads/bullet3/data/kuka_lwr/kuka.urdf'
    urdf_fn = '/Users/krishneelchaudhary/Downloads/bullet3/examples/pybullet/gym/pybullet_data/kuka_iiwa/model_for_sdf.urdf'

    base_pos = [0, 0, 0]
    base_ori = p.getQuaternionFromEuler([0, 0, math.pi])
    kuka_id = p.loadURDF(urdf_fn, base_pos, base_ori, flags=p.URDF_USE_SELF_COLLISION)

    for _ in range(10000):
        p.saveBullet('snap', CLIENT)

        # position, quaternion = p.getBasePositionAndOrientation(kuka_id)
        # angles = p.getEulerFromQuaternion(quaternion)
        # p.stepSimulation()
        time.sleep(1/240.0)

    p.disconnect()

if __name__ == '__main__':
    main()
