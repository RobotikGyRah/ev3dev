from ev3dev.auto import *
import time

m = LargeMotor(OUTPUT_A)
m.run_timed(duty_cycle_sp=42,  time_sp=2000, stop_command="brake")

while m.state:
    time.sleep(0.01)