from .pid import PID_v01 as PID
# from .energy_balance import EnergyBalance_v01 as Simulator
from .energy_balance import EnergyBalance_v01 as EnergyBalance
import matplotlib.animation as animation
import numpy as np
import matplotlib.pyplot as plt

# fig size = (420, 420)
# step = 240 steps

ENV_LOOP = 600
class BsEnv_v01():
    def __init__(self, sp=30, pv_init=20):
        self.sp = sp
        self.pv_init = pv_init

        # PID setting
        self.pid = PID(sp, pv_init)
        self.pid.set_parameters(1.0, 1.0, 1.0)

        # EnergyBalanceSimulator class
        self.simulator = EnergyBalance()
        # self.pv_list.append(pv)

        self.outline = np.zeros(ENV_LOOP)
        self.baseline = np.ones(ENV_LOOP) * sp
        self.pvline = np.ones(ENV_LOOP) * pv_init

        self.observation_size = ENV_LOOP*2  # baseline + pvline
        self.action_size = 9


    def set_baseline(self):
        pv_previous = self.pv_init
        self.baseline[0] = pv_previous
        self.pid.set_max()

        for i in range(1, ENV_LOOP):
            OUT = self.pid.get_out(pv_previous)
            pv = self.simulator.get_temperature(pv_previous, OUT)
            self.baseline[i] = pv
            if pv >= self.sp-0.01:
                # print('sp={}, pv={}'.format(self.sp, pv))
                break
            else:
                pv_previous = pv


    def processing(self):
        pv_previous = self.pv_init
        self.pvline[0] = pv_previous
        self.outline[0] = .0

        # maxline.append(pv_previous)
        # self.pid.set_parameters(10000, 0, 0)

        for i in range(1, ENV_LOOP):
            out = self.pid.get_out(pv_previous)
            self.outline[i] = out
            pv = self.simulator.get_temperature(pv_previous, out)
            self.pvline[i] = pv
            pv_previous = pv


    def step(self, action):
        if action == 0:
            pass
        elif action == 1:  # Kp increase
            self.pid.increase_Kp()
        elif action == 2:  # Kp decrease
            self.pid.decrease_Kp()
        elif action == 3:  # Ki increase
            self.pid.increase_Ki()
        elif action == 4:  # Ki decrease
            self.pid.decrease_Ki()
        elif action == 5:  # Kd increase
            self.pid.increase_Kd()
        elif action == 6:  # Kd decrease
            self.pid.decrease_Kd()
        elif action == 7:  # Kp & Ki increase
            self.pid.increase_Kd()
            self.pid.increase_Ki()
        elif action == 8:  # Kp & Ki decrease
            self.pid.decrease_Kd()
            self.pid.decrease_Ki()
        else:
            print('Invalid action!')

        self.processing()

        reward = np.mean(np.subtract(self.baseline, self.pvline))

        # state_params = {'baseline': self.baseline, 'pvline': self.pvline, 'outline': self.outline }
        state = np.append(self.baseline, self.pvline)
        state = np.reshape(state, (1, self.observation_size))
        info = {'Kp': self.pid.Kp, 'Ki': self.pid.Ki, 'Kd': self.pid.Kd}

        return state, reward, info


    # def render_stream(self):
    #     fig = plt.figure(1)
    #     ax1 = fig.add_subplot(2, 1, 1)
    #     # line1, = ax1.plot(range(ENV_LOOP), self.baseline, 'k', range(ENV_LOOP), self.pvline, 'r')
    #     line1, = ax1.plot(range(ENV_LOOP), self.pvline, 'r')
    #     ax1.add_line(line1)

    #     ax2 = fig.add_subplot(2, 1, 2)
    #     line2, = ax2.step(range(ENV_LOOP), self.outline, 'b')
    #     ax2.add_line(line2)

    #     fig.canvas.draw()
    #     # grab the pixel buffer and dump it into a numpy array
    #     stream = np.array(fig.canvas.renderer._renderer)

    #     return stream


    def render(self):
        plt.figure(1)
        plt.subplot(211)
        plt.plot(range(ENV_LOOP), self.baseline, 'k', range(ENV_LOOP), self.pvline, 'r')

        plt.subplot(212)
        plt.step(range(ENV_LOOP), self.outline, 'b')

        plt.draw()
        plt.pause(5)
        plt.close()


    def render_animate(self, fps=10):
        fig = plt.figure(1)
        ax1 = fig.add_subplot(2, 1, 1)
        ax2 = fig.add_subplot(2, 1, 2)

        line1, = ax1.plot([], [], 'r-', lw=2)
        ax1.add_line(line1)
        ax1.set_xlim(-1, ENV_LOOP+1)
        ax1.set_ylim(-1, 51)
        ax1.grid(True)

        line2, = ax2.step([], [], 'b')
        ax2.add_line(line2)
        ax2.set_xlim(-1, ENV_LOOP+1)
        ax2.set_ylim(-1, 101)
        ax2.grid(True)

        def init():
            line1.set_data([], [])
            line2.set_data([], [])
            return line1, line2

        def animate(i):
            line1.set_data(range(len(self.pvline[:i])), self.pvline[:i])
            line2.set_data(range(len(self.outline[:i])), self.outline[:i])
            return line1, line2

        ani = animation.FuncAnimation(fig=fig, func=animate, init_func=init, interval=fps, blit=True)
        plt.draw()
        plt.pause(60/fps + 2)
        # # plt.clear()
        plt.close()


    def reset(self):
        self.pid.reset()

###########################################
# BsEnv_v02
###########################################
class BsEnv_v02():
    def __init__(self, sp=30, pv_init=20, loop=600):
        self.sp = sp
        self.pv_init = pv_init
        self.loop = loop

        # PID setting
        self.pid = PID(sp, pv_init)
        self.pid.set_parameters(1.0, 1.0, 1.0)

        self.outline = np.zeros(self.loop)
        self.baseline = np.ones(self.loop) * sp
        self.pvline = np.ones(self.loop) * pv_init

        self.observation_size = self.loop*2  # baseline + pvline
        # self.action_size = 9 # stay, Kp, Ki, Kd, Kp+Ki
        self.action_size = 5 # stay, Kp, Ki

        self.reward = 0


    def make(self, env_name='EnergyBalance'):
        if env_name == 'EnergyBalance':
            self.simulator = EnergyBalance()


    def set_baseline(self):
        pv_previous = self.pv_init
        self.baseline[0] = pv_previous
        self.pid.set_max()

        for i in range(1, self.loop):
            OUT = self.pid.get_out(pv_previous)
            pv = self.simulator.get_temperature(pv_previous, OUT)
            self.baseline[i] = pv
            if pv > self.sp-0.01:
                # print('sp={}, pv={}'.format(self.sp, pv))
                break
            else:
                pv_previous = pv


    def processing(self):
        pv_previous = self.pv_init
        self.pvline[0] = pv_previous
        self.outline[0] = .0

        # maxline.append(pv_previous)
        # self.pid.set_parameters(10000, 0, 0)

        self.reward = 0
        for i in range(1, self.loop):
            out = self.pid.get_out(pv_previous)
            self.outline[i] = out
            pv = self.simulator.get_temperature(pv_previous, out)
            
            if pv > self.sp-0.1 and pv < self.sp+0.1:
                self.reward += 80
            elif pv > self.sp-0.2 and pv < self.sp+0.2:
                self.reward += 40
            elif pv > self.sp-0.3 and pv < self.sp+0.3:
                self.reward += 20
            elif pv > self.sp-0.4 and pv < self.sp+0.4:
                self.reward += 10
            elif pv > self.sp-0.5 and pv < self.sp+0.5:
                self.reward += 5

            self.pvline[i] = pv
            pv_previous = pv


    def step(self, action):
        if action == 0:
            pass
        elif action == 1:  # Kp increase
            self.pid.increase_Kp()
        elif action == 2:  # Kp decrease
            self.pid.decrease_Kp()
        elif action == 3:  # Ki increase
            self.pid.increase_Ki()
        elif action == 4:  # Ki decrease
            self.pid.decrease_Ki()
        # elif action == 5:  # Kd increase
        #     self.pid.increase_Kd()
        # elif action == 6:  # Kd decrease
        #     self.pid.decrease_Kd()
        # elif action == 7:  # Kp & Ki increase
        #     self.pid.increase_Kd()
        #     self.pid.increase_Ki()
        # elif action == 8:  # Kp & Ki decrease
        #     self.pid.decrease_Kd()
        #     self.pid.decrease_Ki()
        else:
            print('Invalid action!')

        self.processing()

        self.reward += -np.mean(np.abs(np.subtract(self.baseline, self.pvline)))
        # self.reward += -np.mean(np.abs(np.subtract(np.zeros(self.loop), self.outline)))


        state = np.append(self.baseline, self.pvline)
        state = np.reshape(state, (1, self.observation_size))
        info = {
            'Kp': self.pid.Kp,
            'Ki': self.pid.Ki,
            'Kd': self.pid.Kd,
            'baseline': self.baseline,
            'pvline': self.pvline,
            'outline': self.outline
            }

        return state, self.reward, info


    def render(self):
        plt.figure(1)
        plt.subplot(211)
        plt.plot(range(self.loop), self.baseline, 'k', range(self.loop), self.pvline, 'r')

        plt.subplot(212)
        plt.step(range(self.loop), self.outline, 'b')

        # plt.draw()
        # plt.pause(5)
        # plt.close()


    def render_animate(self, fps=10):
        fig = plt.figure(1)
        ax1 = fig.add_subplot(2, 1, 1)
        ax2 = fig.add_subplot(2, 1, 2)

        line1, = ax1.plot([], [], 'r-', lw=2)
        ax1.add_line(line1)
        ax1.set_xlim(-1, self.loop+1)
        ax1.set_ylim(-1, 51)
        ax1.grid(True)

        line2, = ax2.step([], [], 'b')
        ax2.add_line(line2)
        ax2.set_xlim(-1, self.loop+1)
        ax2.set_ylim(-1, 101)
        ax2.grid(True)

        def init():
            line1.set_data([], [])
            line2.set_data([], [])
            return line1, line2

        def animate(i):
            line1.set_data(range(len(self.pvline[:i])), self.pvline[:i])
            line2.set_data(range(len(self.outline[:i])), self.outline[:i])
            return line1, line2

        ani = animation.FuncAnimation(fig=fig, func=animate, init_func=init, interval=fps, blit=True)
        plt.draw()
        plt.pause(60/fps)
        # # # plt.clear()
        # plt.close()


    def reset(self):
        self.pid.reset()
        self.reward = 0

