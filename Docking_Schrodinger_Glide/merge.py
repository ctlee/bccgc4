
import glob

with open('merge.sh', 'w') as newfile:
    #glob.glob('/home/jegan/bccgc4/GLIDE_Docking/'+method+'_Docking/cluster_dock_input_'+method+'__testing_TICA_pdb_*__dock_pv.maegz')
    #print(paths)

    paths = glob.glob('./all_poses/*.maegz')
    print(paths)
    newfile.write('module load schrodinger\n')
    newfile.write('$SCHRODINGER/utilities/glide_ensemble_merge -JOBID ')
    for k in paths:
        newfile.write(k+' ')
