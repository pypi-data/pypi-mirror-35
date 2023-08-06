#This script will read the files of a run, will write a file, and a bash script will send this file to an email adress !

#put this file anywhare with the script
#All of these are on Nemo !
import numpy as np
import os
import h5py as hp
import glob
import sys

from LPPic import LPPic


def main(path):
    """This function is the main function of the script.

    It will use the LPPic class from LPPview, a litle bit differently, but quite similare.
    """

    #init the LPPview object
    lp = LPPic(path=path)

    #Overide the data Path because we are on the cluster
    lp._data_path = lp._path


    #Lets start with Temporal
    if os.path.isfile(lp._data_path+"temporal_values.dat"):
        lp.getallfiles('tempor')
    else :
        lp.getallfiles('history')

    data = np.loadtxt(lp.lastfile())
    #set first value to 0
    data[0,:] = 0.0

    #getting everything in some nice vectors
    time = data[:,0]
    elec = data[:,1]
    ions = data[:,2]
    SUMe_x = data[:,3]
    SUMe_y = data[:,4]
    SUMe_z = data[:,5]
    coll = data[:,6]
    ioni = data[:,7]
    mobi = data[:,8]
    elec_SEE = data[:,9]
    elec_SEE_sup = data[:,10]
    elec_wal = data[:,11]
    elec_cou = data[:,12]
    elec_Oz  = data[:,13]

    #get files
    lp.getallfiles(filetype="tabgrid")
    lastFile = lp.lastfile()

    fichier = hp.File(lastFile,'r')
    ne = np.array(fichier.get("Nume"))


    with open("temporal_file_py.txt","w") as f:
        f.write("t = {}\n".format(time[-1]))
        f.write("Ne = {}\n".format(elec[-1]))
        f.write("Ni = {}\n".format(ions[-1]))

        print(np.shape(ne))
        ne_mean = ne.mean(axis = 1)
        print(np.shape(ne_mean))

        ne_max = np.max(ne_mean)
        f.write("n_e,max = {}\n".format(ne_max))


if __name__ == "__main__":
    """execute the main function
    the commande line must contain the path argument
    """

    path = sys.argv[1]
    main(path)
