import pyalps
from subprocess import check_call 

L=2
W=2
Nup = 3 
Ndn = 3 
t0 = 1.0
U = 4.0 

parms = []
for t1 in [0.1, 0.5, 1.0]:
    parms.append({
          'LATTICE_LIBRARY'           : 'mylattices.xml',
          'MODEL_LIBRARY'             : 'mymodels.xml',
   	      'LATTICE'                   : "plaquette lattice", 
          'MODEL'                     : "fermion Hubbard",
	      'CONSERVED_QUANTUMNUMBERS'  : 'Nup, Ndown',
 	      'TRANSLATION_SYMMETRY'      : 'true',
          'L'                         : L,
          'W'                         : W,
          't0'                        : t0,  
          't1'                        : t1,  
          'U'                         : U,  
	      'Nup_total'                 : Nup, 
	      'Ndown_total'               : Ndn, 
          'NUMBER_EIGENVALUES'        : 1, 
          'BCx'                       : "periodic",
          'BCy'                       : "periodic"
#          'MEASURE_CORRELATIONS[corr]': 'cdag:c',
#          'MEASURE_CORRELATIONS[nncorr]': 'n:n',
#          'INITIAL_SITE'              : 0
          #"PRINT_EIGENVECTORS"        : 1
        })


input_file = pyalps.writeInputFiles('plaquette',parms)
#res = pyalps.runApplication('sparsediag',input_file,writexml=False)

resfolder = 'data/'
for p in parms:
    parmname = resfolder + str(p['LATTICE']).replace(" ", "")+'L'+str(p['L'])+'_W'+str(p['W'])+'_Nup'+str(p['Nup_total'])+'_Ndn'+str(p['Ndown_total']) +'_t1'+str(p['t1']) +'_U'+str(p['U'])
    input_file = pyalps.writeInputFiles(parmname, [p])
    pyalps.runApplication('sparsediag',input_file) #,writexml=True)#,MPI=2)
#    check_call(['bsub','-oo',input_file.replace('.in.xml','.log'),'-W','08:00','sparsediag',input_file])
    #check_call(['bsub', '-n', '5','-oo',input_file.replace('.in.xml','.log'),'-W','08:00','mpirun', 'sparsediag', '--mpi', input_file])
