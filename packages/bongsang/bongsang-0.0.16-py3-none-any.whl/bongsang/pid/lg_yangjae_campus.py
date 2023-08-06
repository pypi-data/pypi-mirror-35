# Bongsang EMS AI Simulator
import numpy as np
from scipy.integrate import odeint
from .pid import PID_v01 as PID
from .building import RemoteControl_v01 as RemoteControl
######################################################
# Real World Building Model                          #
######################################################


class LgYangjaeCampus_v01():
    def __init__(self):
        self.simulator = RemoteControl()

    def login(self):
        self.simulator.login()

    def logout(self):
        self.simulator.login()

    def ai_mode_on(self):
        self.simulator.set_mode('manual')
    
    def ai_mode_off(self):
        self.simulator.set_mode('automatic')

    def send_output(self, output):
        self.simulator.set_output(output)

    def get_temperature(self):
        self.simulator.get_temperatue()

