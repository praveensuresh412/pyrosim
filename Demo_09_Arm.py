from pyrosim import PYROSIM

ARM_LENGTH = 0.5

ARM_RADIUS = ARM_LENGTH / 10.0

sim = PYROSIM(playPaused = False , evalTime = 1000)

sim.Send_Cylinder(objectID = 0 , x=0, y=0, z=ARM_LENGTH/2.0 + ARM_RADIUS, r1=0, r2=0, r3=1, length=ARM_LENGTH, radius=ARM_RADIUS)

sim.Send_Cylinder(objectID = 1 , x=0, y=ARM_LENGTH/2.0, z=ARM_LENGTH + ARM_RADIUS, r1=0, r2=1, r3=0, length=ARM_LENGTH, radius=ARM_RADIUS)

sim.Start()

# sim.Collect_Sensor_Data()
