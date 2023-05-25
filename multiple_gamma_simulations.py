# Execute this file with "python3 multiple_simulations.py" on Mac or "python multiple_simulations.py"/"python3 multiple_simulations.py" on Windows (depending on the way Python was installed on your Windows) 
# This code allows you to run several replicates and several conditions for the simulation with only one command
# You can easily change the number of replicates and the conditions without modifying the main simulation file (2strains_4colors.py)



# Library
import subprocess # to call python files
import os # directory manager

# get your current working directory (has to be the directory with this file and the other two)
path = os.getcwd()

#folder to store the simulation. You can change it if you want to test different parameters and store the simulated data in a different folder
f = "/Simuls"  # f = "/Simuls/Ntot1e5" if you want to change the total population to 1e5 (simulations are faster). You also have to change the N_tot value to 1e5 below
if not os.path.exists(path+f) :
    os.makedirs(path+f)  # create the "Simuls" folder  if it doesn't exists yet (to store the simulations )


# choose the mean selective advantage and mutation rates values you want to test
s_list = [round(10**(exp_s/10-4), 5) for exp_s in range(0,31)]  # from 10^(-4) to 10^(-1) with logarithmic scale. "round" allows for a shorter output file name as we use the parameters values to name it
u_list = [round(10**(exp_u/10-8), 9) for exp_u in range(0,10)] + [round(10**(exp_u/10-7), 8) for exp_u in range(0,31)] # from 10^(-8) to 10^(-4) with logarithmic scale (same)


# choose the number of replicates you want for each set of parameters
replica_numbers = 10
# Size of the total population
N_tot = 1e6
# Initial proportion of invaders
p = 0.1
# shape of the gamma law
k = 1  # variance = s^2/k 

# Call the simulation code for the different parameters you chose
for u in u_list :
    print("~~~~~~~~~~")
    for s in s_list :
        print("============")
        for rep in range(1, replica_numbers + 1) :
            subprocess.run(["python", "2strains_4colors_gamma.py", "-u", str(u), "-s", str(s), "-k", str(k), "-N", str(N_tot), "-r", str(rep), "-p", str(p), "-f", f])
            # "python3" on mac, "python" or "python3" on Windows (depending on your python installation)



# NB : with small u, the code is very fast and a lot of printing appear in the terminal, but with larger u (Ntot*u > 10) it is much slower and the printings allow you 
# to follow the progression of the simulations

# you can follow the progression of the code by looking at your data folder and seeing the new simulations appearing (if you sort them by date of modification/creation)

# Be careful : the length of execution of this code depends on the numbers and values of the parameters it is provided with
# Each individual simulation (making one replica with one set of parameters) only takes a few miliseconds (for small u) to a few seconds (for larger u) on my computer (Windows 10 Pro 8 cores)
# However, with the current choice of parameters, you have to multiply this by 30 x 40 x 10 = 12000 -> running this whole code took ~4h on my computer

