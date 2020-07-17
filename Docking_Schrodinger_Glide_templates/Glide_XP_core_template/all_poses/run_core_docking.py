
#script to run each docking in 2.5 hour intervals because I can't use that many schrodinger licenses at once for XP docking (takes awhile longer than SP docking)

import glob
import numpy as np

method = '' #clustering method

with open('run_core_docking.sh','w') as writefile:
    writefile.write('$SCHRODINGER/glide -HOST ghosttrees:24 /scratch/jegan/GLIDE_XP_core_docking/'+method+'_docking/all_poses/'+method+'_core_0.in\n') 
    
    for inp,num in zip(glob.glob('/scratch/jegan/GLIDE_XP_core_docking/'+method+'_docking/all_poses/*.in'),range(210,2310,210)):
	#running the next centroids in 210 minute intervals in order, using all 24 CPUs on my machine
        if method+'_core_0.in' not in inp:
            writefile.write('echo "$SCHRODINGER/glide -HOST ghosttrees:24 '+inp+'" | at -m now + '+str(num)+' minutes\n')
