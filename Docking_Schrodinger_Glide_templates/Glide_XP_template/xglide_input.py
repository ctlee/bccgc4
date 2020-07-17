
#script to make input file for Schrodinger script xglide.py that's used for ensemble docking, i.e. providing multiple receptors for one set of ligands to dock to
#usage: "$SCHRODINGER/run xglide.py <input file>"

import os

clust = ''
path = '/scratch/jegan/GLIDE_XP_docking/'+clust+'_docking/all_poses/'

with open(path+clust+'_xglide.in', 'w') as newfile:
    for x in os.listdir('/home/jegan/final_centroids/mae_receptors/'+clust+'/'):
        pdb = 'RECEPTOR            /home/jegan/final_centroids/mae_receptors/'+clust+'/'+x+ '\n' #receptor centroid files location
        newfile.write(pdb)

    lig = 'LIGAND              /net/jam-amaro-shared/bccgc4/GLIDE_Docking/CatS_Ligands/ligprep_ligs.maegz\n' #ligand-prepped ligands from maestro
    newfile.write(lig)

    recep_grid_center = 'GRIDGEN_GRID_CENTER 5.4472, -0.7566, 13.6435\n' #predetermined centr of mass of the cocrystal ligand
    newfile.write(recep_grid_center)

    recep_grid_dim = 'GRIDGEN_OUTERBOX    32\n' #maximum box size
    newfile.write(recep_grid_dim)

    output_type = 'DOCK_POSE_OUTTYPE   poseviewer\n'
    newfile.write(output_type)

    precision = 'DOCK_PRECISION   XP\n' #change the automatic Standard Precision to Extra Precision
    newfile.write(precision)
    
   



