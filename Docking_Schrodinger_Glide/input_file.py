
import os

clust = 'GROMOS_recepatoms'

with open('/net/jam-amaro-shared/bccgc4/GLIDE_Docking/'+clust+'_docking/cluster_dock_input_'+clust, 'w') as newfile:
    for x in os.listdir('/net/jam-amaro-shared/bccgc4/receptor_centroids/'+clust+'/'):
        pdb = 'RECEPTOR            /net/jam-amaro-shared/bccgc4/receptor_centroids/'+clust+'/'+x+ '\n'
        newfile.write(pdb)

    lig = 'LIGAND              /net/jam-amaro-shared/bccgc4/GLIDE_Docking/CatS_Ligands/ligprep_ligs.maegz\n'
    newfile.write(lig)

    recep_grid_center = 'GRIDGEN_GRID_CENTER 5.4472, -0.7566, 13.6435\n'
    newfile.write(recep_grid_center)

    recep_grid_dim = 'GRIDGEN_OUTERBOX    32\n'
    newfile.write(recep_grid_dim)

    output_type = 'DOCK_POSE_OUTTYPE   poseviewer\n'
    newfile.write(output_type)


