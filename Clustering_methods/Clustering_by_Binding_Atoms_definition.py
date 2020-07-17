#selecting for binding atoms for reclustering based on location of previous docking

import mdtraj as md
import os

path = '/home/jegan/receptor_fig/'

#methods atoms
indices = []
methods = ['TICA_OE','TICA_GLIDE','PCA_OE','PCA_GLIDE','GROMOS_OE','GROMOS_GLIDE']
for x in methods:
    for k in os.listdir(path):
        if x == k:
            for u in os.listdir(path+x):
                cx = md.load(path+x+'/'+u)
                print(x)
                selection = cx.topology.select('resname UNL or resname UNK')
                protein = cx.topology.select('protein or resname UNL or resname UNK')
                atoms = cx.atom_slice(protein)
                 
                receptor = md.compute_neighbors(atoms,0.2,selection)

                for q in receptor:
                    for e in q:
                        indices.append(e)

#xtal oe atoms
xtal_oe = md.load(path+'XTAL_OE/XTAL_OE.pdb')
print(xtal_oe)
select = xtal_oe.topology.select('resname UNL or resname UNK')

oe_recep = md.compute_neighbors(xtal_oe,0.2,select)
print(oe_recep)
for r in oe_recep:
    for z in r:
        indices.append(z)

#xtal glide atoms
xtal_glide = md.load(path+'XTAL_GLIDE/XTAL_cx_0.pdb')
lig = xtal_glide.topology.select('resname UNL')
prote = xtal_glide.topology.select('protein or resname UNL')
glide = xtal_glide.atom_slice(prote)

glide_recep = md.compute_neighbors(glide,0.2,lig)

for o in glide_recep:
    for j in o:
        indices.append(o)

#deleting duplicates of indices
recep_indices = []
recep_indices = list(set(indices))

receptor_indices = []
for w in recep_indices:
    if w < 3324:
        receptor_indices.append(w)

print(receptor_indices)

#writing out indices
with open('receptor_indices.txt','w') as newfile:
    for p in receptor_indices:
        newfile.write(str(p)+', ')
