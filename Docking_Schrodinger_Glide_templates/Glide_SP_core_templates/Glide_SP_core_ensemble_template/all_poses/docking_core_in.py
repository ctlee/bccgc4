#code to make input files for ligand core constrained glide docking, with premade grids
#*note* the premade grids also have a positional filter calculated, but this is an optional filter and is not applied in this docking, and was not used in this work

import glob

clust = 'TICA' #clustering method
dock = 'SP' #docking 

for x in glob.glob('/scratch/jegan/GLIDE_'+dock+'_core_docking/'+clust+'_docking/grids/*.zip'): #grid files (should be premade)

    name = x.rsplit('/')[6]
    num = name[-5]
	
    with open('/scratch/jegan/GLIDE_'+dock+'_core_docking/'+clust+'_docking/all_poses/'+clust+'_core_'+num+'.in', 'w') as newfile: #making input files
        
        core_atms = 'CORE_ATOMS   2,3,4,5,6,32,36,37,39' #the atom indices of the common ligand core
        newfile.write(core_atms+'\n')
        
        core_def = 'CORE_DEFINITION   smarts' #core is defined by SMARTS
        newfile.write(core_def+'\n')
        
        core_rmsd = 'CORE_POS_MAX_RMSD   3.5' #maximum RMSD of the pose to constrain by
        newfile.write(core_rmsd+'\n')
        
        core_res = 'CORE_RESTRAIN   True' #use core constraint
        newfile.write(core_res+'\n')
        
        core_smart = 'CORE_SMARTS   c1nnc(c12)CCNC2' #the core SMARTS identification
        newfile.write(core_smart+'\n')
        
        pdb = 'GRIDFILE            '+x+'\n' #gridfile
        newfile.write(pdb)

        lig = 'LIGANDFILE          /net/jam-amaro-shared/bccgc4/GLIDE_Docking/CatS_Ligands/ligprep_ligs.maegz\n' #ligands
        newfile.write(lig)
        
        precision = 'PRECISION   SP'
        newfile.write(precision+'\n')
        
        ref_lig = 'REF_LIGAND_FILE   /scratch/jegan/GLIDE_holo_core_docking/xtal_lig_unflipped.mae' #reference file with only the original cocrystal ligand
        newfile.write(ref_lig+'\n')
        
        use = 'USE_REF_LIGAND   True'
        newfile.write(use+'\n')
        

             
        

        





