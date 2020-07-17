
#script to make input file for Schrodinger script xglide.py that's used for ensemble docking, i.e. providing multiple receptors for one set of ligands to dock to
#usage: "$SCHRODINGER/run xglide.py <input file>"

import glob

clust = 'PCA_CBA' #clustering method

with open('/scratch/jegan/GLIDE_SP_docking/'+clust+'_docking/'+clust+'_xglide.in', 'w') as newfile:
    
    files = glob.glob('/home/jegan/Clustering_methods/PCA/'+clust+'_centroids/*') #receptor centroid files location
    files.sort
    for x in files:
        pdb = 'RECEPTOR         '+x+'\n' #receptors extracted from clustering
        newfile.write(pdb)

    lig = 'LIGAND              /net/jam-amaro-shared/bccgc4/GLIDE_Docking/CatS_Ligands/ligprep_ligs.maegz\n' #ligand-prepped ligands from maestro
    newfile.write(lig)

    recep_grid_center = 'GRIDGEN_GRID_CENTER 5.4472,-0.7566,13.6435\n' #predetermined centr of mass of the cocrystal ligand
    newfile.write(recep_grid_center)

    recep_grid_dim = 'GRIDGEN_OUTERBOX    32\n' #maximum box size
    newfile.write(recep_grid_dim)

    output_type = 'DOCK_POSE_OUTTYPE   poseviewer\n'
    newfile.write(output_type)




