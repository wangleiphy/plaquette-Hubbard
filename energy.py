import pyalps
import matplotlib.pyplot as plt
import pyalps.plot
import numpy as np
import re
import sys

if __name__=='__main__':
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument("-fileheader", default='plaquettelatticeL2_W2_Nup3_Ndn3', help="fileheader")
    parser.add_argument("-dir", default='./data/', help="dir")
    args = parser.parse_args()

    resfiles = pyalps.getResultFiles(dirname= args.dir, prefix=args.fileheader)
    resfiles.sort() 
    #print resfiles 

    data = pyalps.loadSpectra(resfiles)

    #print data,len(data)

    for sim in data:

        L = int(sim[0].props['L'])
        U = sim[0].props['U']
        t1 = sim[0].props['t1']
        
        # for all momentum sector 
        all_energies = []
        for sec in sim:
            all_energies += list(sec.y)

        index = np.argsort(all_energies)
        print L, U, t1, all_energies[index[0]] 

        #print "#kx, ky, Energy"
        # for all momentum sector 
        #for sec in sim:
        #    kx, ky =  sec.props['TOTAL_MOMENTUM'].split() 
        #    print "{:10.4f}".format(float(kx)/np.pi),  "{:10.4f}".format(float(ky)/np.pi), sec.y
