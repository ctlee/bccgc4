import mdtraj as md
import numpy as np
import matplotlib.pyplot as plot
import subprocess
import os

BCCID= ['TNRT6', '6WCGO','LLCXM','NEQSA', 'OVHRZ','VEH1I']

for j in range(len(BCCID)):
    mydir='scratch/ss01/clustering/Auto/'
    filedir='/scratch/bcc2018_trajectories/'+BCCID[j]+'/'


    traj1=md.load(filedir+'md1/'+BCCID[j]+'-Pro01.nc',top=filedir+BCCID[j]+'.prmtop')
    print (traj1)

    #alignment by alpha carbons
    alphacarbons_selection=traj1.top.select('name CA')
    alphacarbons=traj1.atom_slice(alphacarbons_selection)
    print(alphacarbons)
    alphacarbon_indices=traj1.topology.select('name CA')
    print(alphacarbon_indices)

    traj1.superpose(traj1, 0, alphacarbon_indices)

    #protein selection (trajectory.pdb)
    protein1selection=traj1.top.select('protein')
    print(protein1selection)
    protein1=traj1.atom_slice(protein1selection)
    print(protein1)
    print(protein1.topology)
    protein1.save_pdb( '/scratch/ss01/clustering/Auto/'+BCCID[j]+'/'+'trajectory.pdb')

    ###trajectory.pdb formatting
    #path= '/scratch/ss01/clustering/Auto/'+BCCID[j]+'/'
    #os.chdir(path)

    #f=open('trajectory.pdb','r')
    #lines=f.readlines()
    #f.close()
    #f=open('trajectory.pdb','w')
    #for line in lines:
    #    if (line [0:4]=='ATOM'):
    #        f.write(line)
    #f.close()

    #first frame selection
    protein1[0]
    print(protein1[0])
    first_frame=protein1[0]
    first_frame.save_pdb('/scratch/ss01/clustering/Auto/'+BCCID[j]+'/'+'first_frame.pdb')

    path= '/scratch/ss01/clustering/Auto/'+BCCID[j]
    os.chdir(path)

    #first frame formatting
    f=open('first_frame.pdb','r')
    lines=f.readlines()
    f.close()
    f=open('first_frame.pdb','w')
    for line in lines:
        if (line [0:4]=='ATOM'):
            f.write(line)
    f.close()

    #active site selection (active_site.pdb)
    residue_indices=traj1.topology.select('protein')
    ligand_indices=traj1.topology.select('resid 209')

    residuesNearLigand=md.compute_neighbors(traj1,
                                           0.3,
                                           ligand_indices,
                                           haystack_indices=residue_indices)

    i=residuesNearLigand[0]
    print(i)

    active_site=traj1.atom_slice(i)
    active_site1=active_site[0]
    print(active_site1)
    active_site1.save_pdb('/scratch/ss01/clustering/Auto/'+BCCID[j]+'/'+'active_site.pdb')

    get_ipython().system(" cat active_site.pdb | awk '{print $6}' | sort -n | uniq > resid_activesite.dat")

    # resid_activesite.dat formatting
    f=open('resid_activesite.dat','r')
    lines=f.readlines()
    f.close()
    f=open('resid_activesite.dat','w')
    for line in lines:
        if (line [0:1]!='\n'):
            if "," not in line:
                f.write(line)
    f.close()

    get_ipython().system('cat resid_activesite.dat | awk \'{print "cat first_frame.pdb | awk STARTif ($6==" $1  ") print $0 END" }\' | sed "s/START/\'{/g" | sed "s/END/}\'/g"  | csh > active_site_correct$| csh > active_site_correct_residues.pdb')

    get_ipython().system('cat active_site_correct_residues.pdb  | awk \'{printf $2 " "}\' > active_site_atoms_indices.dat')
    get_ipython().system('cat active_site_correct_residues.pdb | grep " CA " | awk \'{ if ( NR%15 == 0){ {printf "%4i", $2} {printf "\\n"} } else {printf "%4i ", $2} }\' > active_site.ndx')
    get_ipython().system('cat first_frame.pdb | grep " CA " | awk \'{ if ( NR%15 == 0){ {printf "%4i", $2} {printf "\\n"} } else {printf "%4i ", $2} }\' > alpha_carbons_indices.ndx')
    get_ipython().system('cat alpha_carbons_indices.ndx active_site.ndx > selections.ndx')

    f=open('active_site.ndx','r+')
    lines=f.readlines()
    f.seek(0)
    f.write('[ active_site_CA ] \n')
    for line in lines:
        f.write(line)
    f.close()

    f=open('alpha_carbons_indices.ndx','r+')
    lines=f.readlines()
    f.seek(0)
    f.write('[ C-alpha ] \n')
    for line in lines:
        f.write(line)
    f.close()

    get_ipython().system('cat alpha_carbons_indices.ndx active_site.ndx > selections.ndx')
    get_ipython().system(' awk \'FNR==1{print ""}1\' *.ndx > selections.ndx')

    with open('selections.ndx', 'r') as fin:
        data = fin.read().splitlines(True)
    with open('selections.ndx', 'w') as fout:
        fout.writelines(data[1:])

