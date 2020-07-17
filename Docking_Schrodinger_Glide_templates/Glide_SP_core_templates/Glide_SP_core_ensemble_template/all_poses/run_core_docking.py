
#script to make a bash script that runs each docking in 1.15 hour intervals because I'm not allowed to use that many schrodinger licenses at once

import glob
import numpy as np

method = 'TICA' #clustering method
dock = 'SP' #docking

with open('run_core_docking.sh','w') as writefile:

	#running centroid 0 docking first with the input file 
    writefile.write('$SCHRODINGER/glide -HOST ghosttrees:24 /scratch/jegan/GLIDE_'+dock+'_core_docking/'+method+'_docking/all_poses/'+method+'_core_0.in\n') 
    
	#running the next centroids in 75 minute intervals in order, using all 24 CPUs on my machine
    for inp,num in zip(glob.glob('/scratch/jegan/GLIDE_'+dock+'_core_docking/'+method+'_docking/all_poses/*.in'),range(75,825,75)):
        if method+'_core_0.in' not in inp:
            writefile.write('echo "$SCHRODINGER/glide -HOST ghosttrees:24 '+inp+'" | at -m now + '+str(num)+' minutes\n')
