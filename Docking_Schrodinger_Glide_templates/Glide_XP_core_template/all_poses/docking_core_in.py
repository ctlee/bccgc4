#code to make input files for ligand core glide docking, using the grids from positional filter docking, but not including that filter

import glob

clust = '' #clustering method
dock = 'SP' #docking

for x in glob.glob('/scratch/jegan/GLIDE_SP_core_docking/'+clust+'_docking/grids/*.zip'): #grid files can be borrowed from the SP core docking runs. Once grid files are calculated for a receptor, they can be reused as long as you don't need to calculate extra parameters

    name = x.rsplit('/')[6]
    num = name[-5]
	
    with open('/scratch/jegan/GLIDE_'+dock+'_core_docking/'+clust+'_docking/all_poses/'+clust+'_core_'+num+'.in', 'w') as newfile:
        
        core_atms = 'CORE_ATOMS   2,3,4,5,6,32,36,37,39' #the atom indices of the common ligand core
        newfile.write(core_atms+'\n')
        
        core_def = 'CORE_DEFINITION   smarts'
        newfile.write(core_def+'\n')
        
        core_rmsd = 'CORE_POS_MAX_RMSD   3.5'
        newfile.write(core_rmsd+'\n')
        
        core_res = 'CORE_RESTRAIN   True'
        newfile.write(core_res+'\n')
        
        core_smart = 'CORE_SMARTS   c1nnc(c12)CCNC2'
        newfile.write(core_smart+'\n')
        
        pdb = 'GRIDFILE            '+x+'\n'
        newfile.write(pdb)

        lig = 'LIGANDFILE          /net/jam-amaro-shared/bccgc4/GLIDE_Docking/CatS_Ligands/ligprep_ligs.maegz\n'
        newfile.write(lig)
        
        precision = 'PRECISION   XP' #change precision from SP to XP
        newfile.write(precision+'\n')
        
        ref_lig = 'REF_LIGAND_FILE   /home/jegan/GLIDE_core_docking/xtal_lig_unflipped.mae'
        newfile.write(ref_lig+'\n')
        
        use = 'USE_REF_LIGAND   True'
        newfile.write(use+'\n')
        

             
        

        





