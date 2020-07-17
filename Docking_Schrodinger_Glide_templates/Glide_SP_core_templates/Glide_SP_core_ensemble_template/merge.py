
#script to write the bash script merge.sh that merges all the poses produced from ensemble docking for each centroid using schrodinger command glide_ensemble_merge, only preserving the minimum score pose in the final poseviewer file

import glob

method = 'TICA'

with open('merge.sh', 'w') as newfile:

    newfile.write('module load schrodinger\n')
    newfile.write('$SCHRODINGER/utilities/glide_ensemble_merge -epv -JOBID ')
    
    for num in range(10):
        for path in glob.glob('./all_poses/*.maegz'):

            name = path.split('/')[-1]
            recep = [int(i) for i in name if i.isdigit()]
            for x in recep: #making sure to put them in order
                recep_num = x

            if recep_num == num: 
                newfile.write(path+' ')
                print(recep_num)
    
#after running this bash script, run schrodinger proplister command to format out scores in a nice csv:

#$SCHRODINGER/utilities/proplister -p title -p "docking score" -p 'best receptor' -c -o scores.csv glide_ensemble_merge_epv.maegz

#^produces a csv file that has the ligand title, docking score, and number of the receptor the best score came from
    

