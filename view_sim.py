import mujoco
import mujoco.viewer
import time
import math
 



XML = """
<mujoco>

    <asset>
        <texture type="skybox" builtin="gradient" rgb1="1 1 1" rgb2=".6 .8 1" width="256" height="256"/>
        <texture name="checkard" type="2d" gridsize= "4 1" builtin="checker" rgb1="0 0 0 " rgb2=".5 .5 .5"    width="256" height="256" />
        <material name="checkard" texture="checkard" texuniform="true"/>
    </asset>

    <worldbody>
        <light diffuse=" .5 .5 .5" pos=" 0 0 3" dir="0 0 -1" />
        <geom type="plane" material="checkard" size=" 3 3 3" />

        <body pos="0 0 .90">
            <joint name="free" type="free" />
            <geom type="box" size=" .2 .2 .2" rgba=" 0 .9 .9 1"/>

            <body pos="0 .1 -.2">
                <joint name="thigh" type="hinge" axis=" 0 1 0"/>
                <geom type="cylinder" rgba=" 0 .9 .5 1" fromto="0 0 0 0 0 -.6" size="0.04"/> 
            </body> 

            <body pos="0 -.1 -.2">
                <joint name="thigh2" type="hinge" axis=" 0 1 0"/>
                <geom type="cylinder" rgba=" 0 .9 .5 1" fromto="0 0 0 0 0 -.6" size="0.04"/> 
            </body> 
            
        </body>
    </worldbody>

</mujoco>
"""

m = mujoco.MjModel.from_xml_string(XML)
d = mujoco.MjData(m)

#d.ctrl[0] = 1


with mujoco.viewer.launch_passive(m, d) as viewer:
    start = time.time()

    while viewer.is_running() and time.time() - start < 30:
        step_time = time.time()

        mujoco.mj_step(m, d)

        with viewer.lock():
         viewer.opt.flags[mujoco.mjtVisFlag.mjVIS_CONTACTPOINT] = int(d.time % 2)

        # update model state for GUI
        viewer.sync()

        time_until_next_step = m.opt.timestep - (time.time() - step_time)
        if time_until_next_step > 0:
            time.sleep(time_until_next_step)