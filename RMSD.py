from __future__ import print_function
import mdtraj as md
import numpy as np
import matplotlib.pyplot as plt
import scipy.cluster.hierarchy as hcl
from scipy.spatial.distance import squareform
import glob

Traj=md.load("/net/jam-amaro-shared/bccgc4/Strided_Traj/joined_traj.xtc", top= "protein.h5")
selection=Traj.topology.select("protein")
traj=Traj.atom_slice(selection)
selection=traj.topology.select("resid 166 or resid 71 or resid 212 or resid 164 or resid 73 or resid 165")
active_site=md.compute_neighbors(traj[0], 0.8, selection)
traj=traj.atom_slice(active_site[0])
heavy=traj.topology.select("symbol != H")
traj=traj.atom_slice(heavy)

distances = np.empty((traj.n_frames, traj.n_frames))
for i in range(traj.n_frames):
    distances[i] = md.rmsd(traj, traj, i)
print('Max pairwise rmsd: %f nm' % np.max(distances))

#assert np.all(distances - distances.T < 1e-6)
reduced_distances = squareform(distances, checks=False)
print(np.max(reduced_distances))


linkage = hcl.linkage(reduced_distances, method='average')


#plt.title('RMSD Average linkage hierarchical clustering')
#_ = hcl.dendrogram(linkage, no_labels=True, count_sort='descendent')

#plt.savefig("RMSD.png")

Z= hcl.linkage(reduced_distances, method="average")

f=0

for i in range(1,10000):
    f=f+0.0001
    clusters=hcl.fcluster(Z, float(f),criterion="distance")
    if max(clusters)==20:
        print(f)
        break
        
clusters=hcl.fcluster(Z, float(f),criterion="distance")
print(clusters)
print(max(clusters))
print(min(clusters))

Clusters={}

for count in range(1,21):
    frames=[]
    indices = [d for d, x in enumerate(clusters) if x == count]
    frames.append(indices)
    Clusters[count]=frames

for key in Clusters:
    print(key)
    a=Traj[tuple(Clusters[key])]
    print(a)
    a.save_xtc('RMSD_Traj_all/Trajcluster'+str(key)+".xtc")

path="RMSD_Traj_all/*.xtc"
files=glob.glob(path)
print(files)
count=1
for k in files:

    t = md.load(k, top="protein.h5")
    atom_indices = [a.index for a in t.topology.atoms if a.element.symbol != 'H']
    distances = np.empty((t.n_frames, t.n_frames))
    for i in range(t.n_frames):
        distances[i] = md.rmsd(t, t, i, atom_indices=atom_indices)
    beta = 1
    index = np.exp(-beta*distances / distances.std()).sum(axis=1).argmax()
    print(index)
    
    centroid = t[index]
    print(centroid)
    centroid.save_pdb("RMSD_Traj_all/RMSD_Centroid_%s.pdb"%count)
    count=count+1
