# THis script will read the inputfile, and present some of it in a way good to look at.

import os

from inputclass import inputparams
import numpy as np

me = 9.109e-31; #[kg] electron mass
q = 1.6021765650e-19; #[C] electron charge
kb = 1.3806488e-23;  #Blozman constant
eps_0 = 8.8548782e-12; #Vaccum permitivitty
mi = 131*1.6726219e-27 #[kg]


def main(path):
    """Main function of the preproc script"""

    #Read the inputs file
    inputsobject = inputparams(path= path)

    #take the parameters
    inputs = inputsobject.parameters

    #initialisation
    print("Initialisation parameters : ")
    print("density = ",inputs["n"], "m^-3")
    print("Ly = ",inputs["Ly"]*100," cm")
    print("Lx = ",inputs["Ly"]*inputs["xmax"]/inputs["ymax"]*1000," mm")
    print("")
    print("Simulation parameters")
    print("Ny = ",inputs["ymax"])
    print("Dx = Dy = ","{:3.1f}".format(inputs["Ly"]/(inputs["ymax"]+1)*1e6)," nm" )
    print("Nx = ",inputs["xmax"])

    #Z_theta
    try:
        Ztheta = inputs['Z_theta']
    except KeyError:
        Ztheta = False

    if Ztheta :
        print("the run is Z-theta !!!!")
        print("Lch = ",inputs["Lch"])
        print("Vdc = ",inputs["V0"])

    #Periodix
    try:
        Periodix = inputs['periodicx']
    except KeyError:
        Periodix = False

    if Periodix:
        print("This is Periodic in Ox !")
    else:
        print("This is a non periodic run ! ")

    test_expected(inputs)


def test_expected(inputs):
    """ printout the expected dX and dT
    """
    Te = inputs["Expected_Te"]
    ne = inputs["Expected_ne"]

    Lde = np.sqrt( eps_0 * Te / (ne * q) )

    dX = inputs["Ly"]/(inputs["ymax"] +1)

    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("Validation of the Numerical values : ")
    print(f"Expected Debye Lenght: {Lde:2.2e} m")
    print(f"Used cell size: {dX:2.2e} m")
    if dX > Lde/10:
        print(f"WARNING the cell size is too big (> Lde/10)!!!!\n")
    else:
        print(f"The cell size is alright\n")

    wpe = np.sqrt(ne*q**2/(me*eps_0))
    dT = inputs["dT"]

    print(f"Expected Plasma frequency: {wpe:2.2e} rad/s")
    print(f"Used sampling frequency: {1/dT:2.2e} Hz")
    if 1/dT > 10*wpe:
        print(f"WARNING the time step is too big (> wpe/10)!!!!\n")
    else:
        print(f"The time step is alright\n")

    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")



if __name__ == "__main__":
    import socket
    print(socket.gethostname())
    print(os.getcwd())
    main(os.getcwd())
