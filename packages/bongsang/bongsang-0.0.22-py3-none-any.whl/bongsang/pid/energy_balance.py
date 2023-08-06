# Bongsang EMS AI Simulator
import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

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


class EnergyBalance_v02():  # for winter
    def __init__(self):
        self.wall_temperature = 12 + 273.15   # K
        self.overall_heat_transfer_coefficient = 10.0           # W/m^2-K
        self.mass = 15000    # kg
        self.heat_capacity = 1 * 1000.0  # J/kg-K
        self.surface_area = 400 # Area in m^2
        self.alpha = 7000       # W / % heater
        self.emissivity = 0.9 # Emissivity
        self.stefan_boltzman_constant = 5.67e-8    # Stefan-Boltzman
        self.kelvin = 273.15


    def physics_equation(self, T, t, OUT):
        # Temperature State
        T_previous = T[0]

        # # Nonlinear Energy Balance
        # kelvin_temperature = (1.0 / (self.mass * self.heat_capacity)) * \
        # (self.overall_heat_transfer_coefficient * self.surface_area * \
        # (self.ambient_temperature - T_previous) + self.emissivity * \
        # self.stefan_boltzman_constant * self.surface_area * \
        # (self.ambient_temperature**4 - T_previous**4) - self.alpha*OUT)

        # Nonlinear Energy Balance
        kelvin_temperature = (1.0 / (self.mass * self.heat_capacity)) * \
        (self.overall_heat_transfer_coefficient * self.surface_area * \
        (T_previous-self.wall_temperature) + self.emissivity * \
        self.stefan_boltzman_constant * self.surface_area * \
        (T_previous**4-self.wall_temperature**4 ) + self.alpha*OUT)



        return kelvin_temperature


    def get_temperature(self, PV, OUT):
        dt = 1
        PV_next = odeint(self.physics_equation, PV + self.kelvin, [0, dt], args=(OUT,))
        
        return PV_next[1][0] - self.kelvin


    def set_parameters(self, wall_temperature, overall_heat_transfer_coefficient, mass, heat_capacity, surface_area, alpha, emissivity):
        self.wall_temperature = wall_temperature + self.kelvin
        self.overall_heat_transfer_coefficient = overall_heat_transfer_coefficient
        self.mass = mass
        self.heat_capacity = heat_capacity
        self.surface_area = surface_area
        self.alpha = alpha
        self.emissivity = emissivity



class EnergyBalance_v03():  # For summer
    def __init__(self):
        self.wall_temperature = 22 + 273.15   # K
        self.overall_heat_transfer_coefficient = 10.0           # W/m^2-K
        self.mass = 15000     # kg
        self.heat_capacity = 1 * 1000.0  # J/kg-K
        self.surface_area = 400 # Area in m^2
        self.alpha = 10000       # W / % heater
        self.emissivity = 0.9 # Emissivity
        self.stefan_boltzman_constant = 5.67e-8    # Stefan-Boltzman
        self.kelvin = 273.15


    def physics_equation(self, T, t, OUT):
        # Temperature State
        T_previous = T[0]

        # # Nonlinear Energy Balance
        # kelvin_temperature = (1.0 / (self.mass * self.heat_capacity)) * \
        # (self.overall_heat_transfer_coefficient * self.surface_area * \
        # (self.ambient_temperature - T_previous) + self.emissivity * \
        # self.stefan_boltzman_constant * self.surface_area * \
        # (self.ambient_temperature**4 - T_previous**4) - self.alpha*OUT)

        # Nonlinear Energy Balance
        kelvin_temperature = (1.0 / (self.mass * self.heat_capacity)) * \
        (self.overall_heat_transfer_coefficient * self.surface_area * \
        (T_previous-self.wall_temperature) + self.emissivity * \
        self.stefan_boltzman_constant * self.surface_area * \
        (T_previous**4-self.wall_temperature**4) - self.alpha*OUT)

        #print('kelvin_temperature=', kelvin_temperature)


        return kelvin_temperature


    def get_temperature(self, PV, OUT):
        dt = 1
        PV_next = odeint(self.physics_equation, PV + self.kelvin, [0, dt], args=(OUT,))
        
        return PV_next[1][0] - self.kelvin


    def set_parameters(self, wall_temperature, overall_heat_transfer_coefficient, mass, heat_capacity, surface_area, alpha, emissivity):
        self.wall_temperature = wall_temperature + self.kelvin
        self.overall_heat_transfer_coefficient = overall_heat_transfer_coefficient
        self.mass = mass
        self.heat_capacity = heat_capacity
        self.surface_area = surface_area
        self.alpha = alpha
        self.emissivity = emissivity


class EnergyBalance_v04():  # For summer & winter
    def __init__(self, mode='summer'):
        if 'summer' in mode:
            self.wall_temperature = 22 + 273.15   # K
            self.overall_heat_transfer_coefficient = 10.0           # W/m^2-K
            self.mass = 15000     # kg
            self.heat_capacity = 1 * 1000.0  # J/kg-K
            self.surface_area = 400 # Area in m^2
            self.alpha = 10000       # W / % heater
            self.emissivity = 0.9 # Emissivity
            self.stefan_boltzman_constant = 5.67e-8    # Stefan-Boltzman
            self.kelvin = 273.15
        elif 'winter' in mode:
            self.wall_temperature = 12 + 273.15   # K
            self.overall_heat_transfer_coefficient = 10.0           # W/m^2-K
            self.mass = 15000    # kg
            self.heat_capacity = 1 * 1000.0  # J/kg-K
            self.surface_area = 400 # Area in m^2
            self.alpha = 7000       # W / % heater
            self.emissivity = 0.9 # Emissivity
            self.stefan_boltzman_constant = 5.67e-8    # Stefan-Boltzman
            self.kelvin = 273.15

        self.mode = mode


    def physics_equation(self, T, t, OUT):
        # Temperature State
        T_previous = T[0]

        if 'summer' in self.mode:
            # Nonlinear Energy Balance
            kelvin_temperature = (1.0 / (self.mass * self.heat_capacity)) * \
                                 (self.overall_heat_transfer_coefficient * self.surface_area * \
                                 (T_previous-self.wall_temperature) + self.emissivity * \
                                 self.stefan_boltzman_constant * self.surface_area * \
                                 (T_previous**4-self.wall_temperature**4) - self.alpha*OUT)
        elif 'winter' in self.mode:
            kelvin_temperature = (1.0 / (self.mass * self.heat_capacity)) * \
                                 (self.overall_heat_transfer_coefficient * self.surface_area * \
                                 (T_previous-self.wall_temperature) + self.emissivity * \
                                 self.stefan_boltzman_constant * self.surface_area * \
                                 (T_previous**4-self.wall_temperature**4 ) + self.alpha*OUT)

        return kelvin_temperature


    def get_temperature(self, PV, OUT):
        dt = 1
        PV_next = odeint(self.physics_equation, PV + self.kelvin, [0, dt], args=(OUT,))
        
        return PV_next[1][0] - self.kelvin


    def set_parameters(self, wall_temperature, overall_heat_transfer_coefficient, mass, heat_capacity, surface_area, alpha, emissivity):
        self.wall_temperature = wall_temperature + self.kelvin
        self.overall_heat_transfer_coefficient = overall_heat_transfer_coefficient
        self.mass = mass
        self.heat_capacity = heat_capacity
        self.surface_area = surface_area
        self.alpha = alpha
        self.emissivity = emissivity


if __name__ == '__main__':
    from bongsang.pid.pid import PID_v02 as PID

    simulator = EnergyBalance_v04('summer')
    # simulator = EnergyBalance_v04('winter')
    pv_previous = 30
    sp = 25
    pid = PID(sp, pv_previous)

    out_list = [100, 100, 100, 100, 100, 80, 80, 80, 80, 80, 70, 70, 70, 70, 70, 60, 60, 60, 60, 60, 50, 50, 50, 50, 50, 40, 40, 40, 40, 40, 30, 30, 30, 30, 30, 20, 20, 20, 20, 20, 10, 10, 10, 10, 10, 0, 0, 0, 0, 0]

    pv_list = []
    pv_list.append(pv_previous)
    out_list = []
    out_list.append(0)

    for i in range(5000):
        # pv_next = simulator.get_temperature(pv_previous, out_list[i-1])
        out = pid.get_out(pv_previous)
        out_list.append(out)
        pv_next = simulator.get_temperature(pv_previous, out)
        pv_list.append(pv_next)
        pv_previous = pv_next

    baseline = np.ones(len(pv_list)) * sp
    plt.subplot(211)
    plt.plot(range(len(baseline)), baseline, range(len(pv_list)), pv_list)
    plt.subplot(212)
    plt.step(range(len(out_list)), out_list)
    plt.show()