
#code to write ten input files for grid generation with optional constraints
#the reason why this has to be done with all core constraint Glide docking is because the xglide.py script doesn't accept constraints
#therefore we must generate individual grids for each receptor and dock to each individually, then use the glide_ensemble_merge command to merge together all the files and parse out the minimum score pose out of the 10 centroids for the final line-up

import glob

method = 'TICA' #clustering method
dock = 'SP'
path = '/scratch/jegan/GLIDE_'+dock+'_core_docking/'+method+'_docking/grids/'

for num in range(10):
    with open(path+'/'+method+'_grid_'+str(num)+'.in','w') as grid_in: #individual input grid files for each centroid
        
        center = 'GRID_CENTER   5.4472, -0.7566, 13.6435\n' #predetermined center of mass of the cocrystal ligand
        grid_in.write(center)
        
        filename = 'GRIDFILE   '+path+method+'_grid_'+str(num)+'.zip\n'
        grid_in.write(filename)
        
        inbox = 'INNERBOX   10, 10, 10\n'
        grid_in.write(inbox)
        
        outbox = 'OUTERBOX   42, 42, 42\n'
        grid_in.write(outbox)
        
        com_constraint = 'POSIT_CONSTRAINTS   "com 7.580000 -2.110000 9.290000 6.000000"\n' #an optional positional constraint that is at a certain point and restrained within a 6 angstrom sphere. However, we didn't end up using this in our results as preliminary docking was uneffective
        grid_in.write(com_constraint)
        
        receptor = 'RECEP_FILE   /home/jegan/final_centroids/mae_receptors/holo/'+method+'/'+method+'_'+str(num)+'.maegz\n' #the receptor file in maestro format
        grid_in.write(receptor)
