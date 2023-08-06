###########################
# PID
# Created by Bongsang Kim
###########################

OUT_MAX = 100
OUT_MIN = 0
Kp_MAX = 100
Kp_MIN = 1.0
Ki_MAX = 10
Ki_MIN = .1
Kd_MAX = 100
Kd_MIN = 0


class PID_v01():
    def __init__(self, SP=30, PV=20):
        self.Kp = 1.0
        self.Ki = 0.1
        self.Kd = 0.0

        self.OUT = 0.0
        
        self.SP = SP
        self.PV_previous = PV

        self.proportional_error = 0
        self.integral_error = 0
        self.derivative_error = 0

        self.dt = 1.0


    def print_parameters(self):
        print('Kp={}, Ki={}, Kd={}'.format(self.Kp, self.Ki, self.Kd))


    def get_parameters(self):
        params = {'Kp': self.Kp, 'Ki': self.Ki, 'Kd': self.Kd}
        return params


    def get_out(self, PV):
        # Propotional equation
        self.proportional_error = self.SP - PV

        # Integral equation
        self.integral_error += self.Ki * self.proportional_error * self.dt

        # Derivative equation
        self.derivative_error = (PV - self.PV_previous) / self.dt

        # calculate the PID output
        P = self.Kp * self.proportional_error
        I = self.integral_error
        D = -self.Kd * self.derivative_error
        self.OUT += P + I + D

        # implement anti-reset windup
        if self.OUT <= OUT_MIN or self.OUT >= OUT_MAX:
            self.integral_error -= self.Ki * self.proportional_error * self.dt
            # clip output
            self.OUT = max(OUT_MIN, min(OUT_MAX, self.OUT))

        # return the controller output and PID terms
        self.PV_previous = PV

        return self.OUT


    def set_parameters(self, Kp, Ki, Kd):
        if Kp > 0 and Kp < 10000:
            self.Kp = Kp

        if Ki > 0 and Ki < 1000:
            self.Ki = Ki

        if Kd > 0 and Kd < 100:
            self.Kd = Kd


    def set_max(self):
        self.Kp = Kp_MAX
        self.Ki = Ki_MIN
        self.Kd = Kd_MIN


    def increase_Kp(self):
        self.Kp += 1.0
        if self.Kp >= Kp_MAX:
            self.Kp = Kp_MAX
    
    def decrease_Kp(self):
        self.Kp -= 1.0
        if self.Kp <= Kp_MIN:
            self.Kp = Kp_MIN

    def increase_Ki(self):
        self.Ki += .01
        if self.Ki >= Ki_MAX:
            self.Ki = Ki_MAX
    
    def decrease_Ki(self):
        self.Ki -= .01
        if self.Ki <= Ki_MIN:
            self.Ki = Ki_MIN

    def increase_Kd(self):
        self.Kd += .1
        if self.Kd >= Kd_MAX:
            self.Kd = Kd_MAX

    def decrease_Kd(self):
        self.Kd -= .1
        if self.Kd <= Kd_MIN:
            self.Kd = Kd_MIN


    def reset(self):
        self.Kp = Kp_MIN
        self.Ki = Ki_MIN
        self.Kd = Kd_MIN
