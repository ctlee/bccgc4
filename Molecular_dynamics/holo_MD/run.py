#Ben's script to run 5 separate mds for the apo structure, repurposed for my holo strucutre

#!/bin/env python
import sys, os, subprocess

systems = ['md1','md2','md3','md4','md5']

for system in systems:
    
    os.chdir('%s'%(system)) #changing working directory
    print "Entering directory: %s"%(system)
    
    for i in xrange(1, 100): #checking which run it's currently on...?
        if not os.path.isfile('%d.out'%(i)): #if the file i.out doesn't exist
            break

    generation = i #the number of the run
    args = "mv 0.prmtop system.prmtop" #I think each dir has to start with the parmtop file
    subprocess.call(args, shell=True)  #running the args in the command line
    
    args = "sbatch -J %s_amber --export=NAME=%s,OLD=%d,GEN=%d /net/jam-amaro-shared/bccgc4/CatS_holo_md/amberjob.slurm"%(system, system, generation-1, generation) #I think this is managing jobs, naming it md#_amber , exporting certain environment variables like the name(md#), the older run, and the generation #, and finally giving the .slurm script 
    print args
    subprocess.call(args, shell=True) #running that command on the commandline
    print "======================================="
    os.chdir('..')
