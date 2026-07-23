
XML = """
<mujoco>

    <asset>
        <texture type="skybox" builtin="gradient" rgb1="1 1 1" rgb2=".6 .8 1" width="256" height="256"/>
        <texture name="checkard" type="2d" gridsize= "4 1" builtin="checker" rgb1="0 0 0 " rgb2=".5 .5 .5"    width="256" height="256" />
        <material name="checkard" texture="checkard" texuniform="true"/>
    </asset>

    <worldbody>
        <light diffuse=" .5 .5 .5" pos=" 0 0 3" dir="0 0 -1" />
        <geom type="plane" material="checkard" size=" 7 7 7" />

        <body pos="0 0 .20">
            <joint name="slide" type="slide" axis=" 1 0 0"/>
            <geom type="box" size=" .2 .2 .2" rgba=" 0 .9 .9 1"/>
            <body>
                <joint name="pendulum" type="hinge" axis=" 0 1 0"/>
                <geom type="cylinder" rgba=" 0 .9 .5 1" fromto="0 0 0.1 0 0 .6" size="0.04"/>  
            </body> 
            <body>
                <joint name="pendulum2" type="hinge" axis=" 0 1 0"/>
                <geom type="cylinder" rgba=" 0 .9 .5 1" fromto="0 0 0.5 0 0 .12" size="0.1"/>  
            </body> 
        </body>
    </worldbody>

    <actuator>
        <motor joint="slide" name="slide" gear="100"/>
    </actuator>
</mujoco>
"""