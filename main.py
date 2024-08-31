import numpy as np
import matplotlib.pyplot as plt

class System:
    def __init__(self, x0, r0=3.4):
        self.sys = lambda x,r: r*x*(1-x)
        self.x0 = x0
        self.r0 = r0

    def next(self, x, r):
        return self.sys(x, r)
    
    def forward(self):
        self.x0 = self.next(self.x0, self.r0)
        return self.x0
    
if __name__ == '__main__':
    sys = System(0.2)
    r0 = np.linspace(3.4,4,1000)
    next_state = 0.2
    
    for i in range(1000):
        next_state = sys.next(next_state, r0)
        
        if i > 700:
            plt.plot(r0, next_state, 'k.', markersize=0.1)

    plt.xlabel('r')
    plt.ylabel('x')
    plt.show()