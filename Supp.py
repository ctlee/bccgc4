
import subprocess
import os
from openeye import oechem
import glob

path_receptors = '/net/jam-amaro-shared/bccgc4/xtaldocking/PCA_docking_DONE/receptor_pdbs_converted_from_oebs/'

for c in range(10):
    receptor = 'receptor'+str(c)
    os.chdir(path_receptors)
    subprocess.getoutput('cp '+receptor+'.pdb '+'/net/jam-amaro-shared/bccgc4/Sub_Format/PCA_Sub/structurebased/SuppInfo/5QC4-'+receptor+'.pdb')


#making ligand mols

files=[]#list of paths to the correct poses 
for u in range(10):
    for w in range(1,460):
        string = '/net/jam-amaro-shared/bccgc4/xtaldocking/PCA_docking_DONE/ligand_poses_pdbs/Centroid'+str(u)+'-CatS_'+str(w)+'.pdb'
        files.append(string)
    
print(files[0])
    
ifs=oechem.oemolistream()
ofs=oechem.oemolostream()

for i in files:
    if ifs.open(i):
        slic = i.find('Centroid')
        ligand= i[slic:] #Centroid*-CatS_*.pdb
        edit = ligand[8:-4] #*-CatS_*
        Ligand= 'receptor'+edit
        #print(Ligand)
        if ofs.open("/net/jam-amaro-shared/bccgc4/Sub_Format/PCA_Sub/structurebased/SuppInfo/"+"5QC4-"+str(Ligand)+".mol"):
            for mol in ifs.GetOEGraphMols():
                oechem.OEWriteMolecule(ofs, mol)
        else:
            oechem.OEThrow.Fatal("Unable to create output")
    else:
        oechem.OEThrow.Fatal("Unable to open input")
