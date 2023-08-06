# Bongsang EMS AI Simulator
import numpy as np
from scipy.integrate import odeint
from .pid import PID_v01 as PID

######################################################
# Energy balance model                               #
######################################################
class EnergyBalance_v01():
    def __init__(self):
        self.Ta = 10 + 273.15   # K
        self.U = 10.0           # W/m^2-K
        self.m = 4.0/1000.0     # kg
        # self.m = 12.0/1000.0     # kg
        self.Cp = 0.5 * 1000.0  # J/kg-K
        self.A = 12.0 / 100.0**2 # Area in m^2
        # self.A = 24.0 / 100.0**2 # Area in m^2
        self.alpha = 0.01       # W / % heater
        self.emissivity = 0.9          # Emissivity
        self.stefan_boltzman = 5.67e-8    # Stefan-Boltzman
        self.kelvin = 273.15


    def physics_equation(self, T, t, OUT):
        # Temperature State
        T_previous = T[0]

        # Nonlinear Energy Balance
        kelvin_temperature = (1.0 / (self.m * self.Cp)) * (self.U * self.A * (self.Ta - T_previous) \
                + self.emissivity * self.stefan_boltzman * self.A * (self.Ta**4 - T_previous**4) \
                + self.alpha*OUT)

        return kelvin_temperature


    def get_temperature(self, PV, OUT):
        dt = 1
        PV_next = odeint(self.physics_equation, PV + self.kelvin, [0, dt], args=(OUT,))
        
        return PV_next[1][0] - self.kelvin
