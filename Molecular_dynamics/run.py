#!/bin/env python
import sys, os, subprocess

systems = ['md1','md2','md3','md4','md5']

for system in systems:
    os.chdir('%s'%(system))
    print "Entering directory: %s"%(system)
    for i in xrange(1, 100):
        if not os.path.isfile('%d.out'%(i)):
            break
    generation = i
    args = "mv 0.prmtop system.prmtop"
    subprocess.call(args, shell=True)
    
    args = "sbatch -J %s_amber --export=NAME=%s,OLD=%d,GEN=%d /oasis/scratch/comet/bjagger/temp_project/D3R_GC4/CatSMD/amberjob.slurm"%(system, system, generation-1, generation)
    print args
    subprocess.call(args, shell=True)
    print "======================================="
    os.chdir('..')
