#!/usr/bin/env python

import pybullet as p
import pybullet_data


pclient = p.connect(p.GUI)

def setup():
    p.resetSimulation()
    p.setAdditionalSearchPath(pybullet_data.getDataPath())
    p.setGravity(0, 0, -10)

def main():

    setup()
    robot_id = p.loadURDF('r2d2.urdf')

    num_joint = p.getNumJoints(robot_id)
    print(f'Joints: {num_joint}')

    for i in range(num_joint):
        print(f'Info: {p.getJointState(robot_id, i)}')
    
    p.disconnect()
    
    
    

if __name__ == '__main__':
    main()
