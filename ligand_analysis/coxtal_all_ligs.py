#code to generate fingerprints and calculate similarity between top quartile ligands of all methods and current cocrystal ligands using rdkit
#supplemental figure 1 and table 1

from __future__ import print_function
from rdkit import Chem
from rdkit import DataStructs
import glob
import numpy as np
import math

#getting the SMILES for the cats ligands

lig_smiles = []
count = 0
with open('/home/jegan/lig_struct_analysis/similarity_rdkit/CatS_smiles.csv','r') as cats_smiles: #getting the smiles for the ligands
    for line in cats_smiles:
        line = line.split(',')
        lig_smiles.append(line)
        count += 1
print('CatS ligands = ' + str(count))

#getting fingerprints for CatS ligands

mols = [Chem.MolFromSmiles(smile[0]) for smile in lig_smiles] #converting into rdkit mol objects
dock_fps = [Chem.RDKFingerprint(mol) for mol in mols] #converting mol objects into fingerprints


#getting fingerprint arrays for coxtal ligands

coxtal_smiles_pdb = []
count = 0
with open('/home/jegan/lig_struct_analysis/similarity_rdkit/xtal_ligands/coxtal_smiles_pdb.csv','r') as data:
    for line in data:
        line = line.split(',')
        coxtal_smiles_pdb.append(line)
        count += 1
print('Coxtal ligands = '+str(count))

#getting fingerprints for coxtal ligands

mols = [Chem.MolFromSmiles(smile[0]) for smile in coxtal_smiles_pdb] #converting into rdkit mol objects
coxtal_fps = [Chem.RDKFingerprint(mol) for mol in mols] #converting mol objects into fingerprints


#computing tanimotos and putting into a numpy array

matrix = []
with open('/home/jegan/lig_struct_analysis/similarity_rdkit/coxtal_cats_distances.csv','w') as writefile:
    writefile.write('Cocrystal #, PDBID, Ligand ID, L2 Norm\n')
    lines = []
    for lig, dat in zip(coxtal_fps, coxtal_smiles_pdb):
        tanimotos = DataStructs.BulkTanimotoSimilarity(lig,dock_fps) #getting one line of tanimotos for CatS ligs for each coxtal ligand
        
        #finding the l2 norm of each coxtal ligand to all the CatS ligands - i.e. the "average" tanimoto (really avg distance) of the catS ligands from that particular coxtal ligand
        total = 0
        for tanimoto in tanimotos:
            square = tanimoto**2
            total += square
        l2_norm = round((math.sqrt(total)), 2) # need to order them in terms of this value
        
        line = [dat[2].rstrip(), dat[1], l2_norm, tanimotos] #pdbid, lig id, l2 norm, tanimoto list
        lines.append(line)
    
    sort_lines = sorted(lines, key = lambda x: x[2], reverse = True) #sorting the line list by the l2_norm
    
    for line, num in zip(sort_lines, range(len(sort_lines))):
        writefile.write(str(num)+','+line[0]+','+line[1]+','+str(line[2])+'\n') #the coxtal number, pdbid, lig id, l2 norm
        print(num, line[0], line[1], line[2])
        matrix.append(line[3]) #appending the tanimoto list to the matrix

print(len(matrix))
array = np.array(matrix)

np.save('/home/jegan/lig_struct_analysis/similarity_rdkit/coxtal_cats_tanimoto.npy',array)


#figure was tweaked and plotted in heatmap.ipynb
#table script for latex format was also done with latex_coxtal_cats.py
