
import mdtraj as md
import os

methods = ['TICA', 'TICA_CBA', 'PCA', 'PCA_CBA', 'GROMOS', 'GROMOS_CBA']
path = '/home/jegan/final_centroids/'
home = '/home/jegan/centroid_analysis/b-fact_fig/'

for method in methods:
    
    #making a fake combined trajectory where each frame is one centroid of the method
    traj_0 = md.load(path+method+'/'+method+'_0.pdb')
    for x in range(1,10):
        for k in os.listdir(path+method+'/'):
            if k == (method+'_'+str(x)+'.pdb'):
                print(k)
                traj = md.load(path+method+'/'+k)
                joined_traj = traj.join(traj_0)

    joined_traj = joined_traj.superpose(traj_0,0)
    joined_traj.save_pdb(home+'pdb_trajs/'+method+'_traj.pdb')
    
    #calculating the rmsf
    rmsf = (md.rmsf(joined_traj,traj_0)) * 10 #mdtraj calculates in nanometers, so need to convert to angstroms    
    print(len(rmsf))
    
    #replacing the b-factor
    with open(path+'XTAL/XTAL_0.pdb','r') as data:
        with open(home+'pdb_figures/'+method+'_fig.pdb','w') as writefile:
            data = data.readlines()
            
            writefile.write(data[0])
            writefile.write(data[1])
            
            for line,value in zip(data[2:3326],rmsf):
                
                val = round(value,3)
                adjust = str(val).rjust(6)
                newline = line.replace((line[60:67]), adjust)
                writefile.write(newline+'\n')
                
            for line in data[3327:]:
                writefile.write(line)
                
            
    
