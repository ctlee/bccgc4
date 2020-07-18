#this code saves out ligand ranking csvs for every centroid docked to in each clustering method (not just the best scores)

import glob

path = '/home/jegan/bccgc4/GLIDE_Docking/'
home = '/home/jegan/OE_Glide_correlation/'
methods = ['TICA','TICA_CBA','PCA','PCA_CBA','GROMOS','GROMOS_CBA']
dirs = ['TICA_bkbnpos','TICA_recepatoms','PCA','PCA_recepatoms','GROMOS_str100','GROMOS_recepatoms']

with open('/home/jegan/OE_Glide_correlation/glide_csvs.sh','w') as newfile:
    for x,y in zip(methods,dirs):
        for i in glob.glob(path+y+'_docking/all_poses/*.maegz'):
            print(i.rsplit('/')[7])
            for num in range(10):
                if str(num) in (i.rsplit('/')[7]):
                    newfile.write('$SCHRODINGER/utilities/proplister -p title -p "docking score" -c -o '+home+'csvs_unordered/GD_'+x+'_'+str(num)+'.csv '+i+'\n')
