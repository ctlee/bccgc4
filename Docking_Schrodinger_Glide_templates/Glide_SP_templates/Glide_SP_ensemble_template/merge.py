
#script to write the bash script merge.sh that merges all the poses produced from xglide.py for each centroid using schrodinger command glide_ensemble_merge, only preserving the minimum score pose in the final poseviewer file

import glob

with open('merge.sh', 'w') as newfile:
    paths = glob.glob('./all_poses/*.maegz')
    print(paths)
    newfile.write('module load schrodinger\n')
    newfile.write('$SCHRODINGER/utilities/glide_ensemble_merge -JOBID ')
    for k in paths:
        newfile.write(k+' ')
		

#after running this bash script, run schrodinger proplister command to format out scores in a nice csv:

#$SCHRODINGER/utilities/proplister -p title -p "docking score" -p 'best receptor' -c -o scores.csv glide_ensemble_merge_epv.maegz

#^produces a csv file that has the ligand title, docking score, and number of the receptor the best score came from

