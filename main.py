import numpy as np
import matplotlib.pyplot as plt
from tqdm import tqdm

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
    full_record = {'r':[], 'x':[]}
    for j in tqdm(range(600)):
        r0 = 3.4 + j*0.001
        next_state = 0.2
        record = [next_state]
        
        for i in range(800):
            next_state = sys.next(next_state, r0)
            record.append(next_state)

        # Check for periodicity within the current record
        for k in range(len(record)): 
            for l in range(k+1, len(record)): # Compare against all subsequent states
                if abs(record[k] - record[l]) < 1e-4:
                    # period = (l - k)  # Calculate period length
                    # print(f"Periodicity detected at r={r0:.4f}: Period {period}")
                    full_record['r'].append(r0)
                    full_record['x'].append(record[k])

    plt.scatter(full_record['r'], full_record['x'], s=0.1)
    plt.show()