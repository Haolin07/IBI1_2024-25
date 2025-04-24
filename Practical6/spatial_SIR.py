import numpy as np
import matplotlib.pyplot as plt

# initialized and set variables
beta = 0.3  #infected prabobility  
gamma = 0.05  #recover probability
size = 100    #picture size
timesteps = 100  

# Create initial fully susceptible population grid
population = np.zeros((size, size), dtype=int)
#Initial infection sites were randomly selected
outbreak = np.random.choice(size, 2)
population[outbreak[0], outbreak[1]] = 1

#Create an orbit window
plt.figure(figsize=(6, 4), dpi=150)

for t in range(timesteps):
    #find infected position
    infected = np.where(population == 1)
    rows, cols = infected[0], infected[1]
    #Infection stage: traverse the infected neighbors of each infected person
    new_infections = []
    for i in range(len(rows)):
        r, c = rows[i], cols[i]
       #Check 8 neighborhood
        for dr in [-1, 0, 1]:
            for dc in [-1, 0, 1]:
                if dr == 0 and dc == 0:
                    continue  
                nr, nc = r+dr, c+dc
                if 0 <= nr < size and 0 <= nc < size:
                    if population[nr, nc] == 0 and np.random.rand() < beta:
                        new_infections.append((nr, nc))
    #Apply new infections
    for (r, c) in new_infections:
        population[r, c] = 1
    
    #Recovery stage: the infected person recovers with gamma probability
    recovery_mask = np.random.rand(len(rows)) < gamma
    population[rows[recovery_mask], cols[recovery_mask]] = 2
    
    # draw the picture
    plt.clf()
    plt.imshow(population, cmap='viridis', vmin=0, vmax=2, interpolation='nearest')
    plt.title(f'Time Step {t+1} | Infected: {len(rows)}')
    plt.colorbar(ticks=[0, 1, 2], label='State (0:S, 1:I, 2:R)')
    plt.pause(0.1)

plt.show()