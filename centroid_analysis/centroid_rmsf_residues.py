#so we want rmsf by residue now, so we need to use cpptraj because mdtraj can't do it by residue, only by atom index 

mds = ['apo','holo']

home = '/home/jegan/centroid_analysis/RMSF/'

with open(home+'rmsf_residues.sh', 'w') as run:
    run.write('module load amber/18\n')
    for md in mds:
        
        with open(home+md+'_rmsf.in', 'w') as file:
            file.write('trajin '+home+md+'_traj.pdb\n')
            file.write('rmsd @C,CA,N first\n')
            file.write('atomicfluct out '+home+md+'.dat @C,CA,N byres\n')
            
        run.write('cpptraj /home/jegan/final_centroids/holo_centroids/XTAL/XTAL_0.pdb '+home+md+'_rmsf.in  > '+home+md+'_rmsf.log\n')
