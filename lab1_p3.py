##############################
# APS106 Winter 2024
# Lab 1 - Part 3
# Electrostatic precipitator
##############################

def particle_position(q,E,m,t,L):
    """
    (float,float,float,float,float) -> float
    
    Function calculates the horizontal position of a charged particle
    within a electrostatic precipitator.
    Input parameters:
        q - charge of the particle in nanocoulombs
        E - electric field strength in kilonewtons/coulomb
        m - mass of particle in nanograms
        t - time since the particle entered the precipitator in microseconds
        L - the distance between the parallel plate electrodes in centimetres
        
    Returns the height of the particle in centimetres
    
    >>> particle_position(0,150,9.2,3.6,5.0)
    2.5
    
    >>> particle_position(2.3,150,9.2,26.8,5.0)
    3.847
    
    >>> particle_position(-2.3,160,9.2,36.8,5.0)
    0.0
    
    """
    
    ## TODO: Write your solution here

## TODO: Write your test code for particle_height here - MAKE SURE YOU DELETE THESE LINES BEFORE SUBMITTING

    pos = (1/20000)*(q*E/m)*(t*t)+(L/2)

    if(pos < 0):
        pos = 0
    elif(pos > L):
        pos = L

    return round((float(pos)),3)


## Write test cases above this line, DELETE EVERYTHING UP TO THIS LINE BEFORE SUBMITTING

#print(particle_position(0,150,9.2,3.6,5.0))
#print(particle_position(2.3,150,9.2,26.8,5.0))
#print(particle_position(-2.3,160,9.2,36.8,5.0))
