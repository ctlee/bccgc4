#path and making a list of all ligands
path = "/net/jam-amaro-shared/bccgc4/xtaldocking/TICA_docking_DONE"

ligands = [] #list of all ligands
for k in range(1,460):
    lig = 'CatS_'+str(k)
    ligands.append(lig)
    
#print(ligands)


min_lig = [] #list of ligands & their corresponding receptors with the minimum score
for i in ligands:
        lig = []
        with open(path+"/Docking_Results/score.txt") as scores:
            for line in scores:
                if " "+i+" " in line:
                    lig.append(line)
        #print(lig)
        nums = []
        for l in lig:
            if "-" in l:
                index = l.find("-")
                nums.append(l[index:])
            else:
                ind = l.find("CatS_** ")
                nums.append(l[ind:])
        #print(nums)
        min_score = max(nums) #I used max because it takes the largest magnitude
        #print(min_score)
        for l in lig:
            if str(min_score) in l:
                min_lig.append(l)
print(min_lig[0])

numbers = [] #list of min scores
for x in min_lig:
    delete = x.find("\n")
    new = x[:delete]
    if "-" in new:
        index = new.find("-")
        numbers.append(new[index:])
    else:
        ind = new.find("CatS_*** ")
        print(new[ind:])
        nums.append(new[ind:])

numbers = [float(y) for y in numbers]
#print(numbers)
ordered_scores = sorted(numbers) #ordered scores 
print(len(ordered_scores))

ordered_list = [] #list of receptor to ligand to score ordered by rank
for o in ordered_scores:
    for u in min_lig:
        if str(o) in u:
            ordered_list.append(u)
print(ordered_list[0])

import csv 

lig_rank_score = [] #list of lig to rank to score
for e in range(0,459):
    p = ordered_list[e]
    sl = p.find("CatS_")
    delete = p.find("\n")
    a = p[sl:delete]
    
    sli = a.find(" -")
    cats = a.find("CatS_")
    sl = a.find("-")
    string = []
    string.append(str(a[cats:sli]))
    string.append(str(e+1))
    string.append(str(a[sl:]))
    #print(string)
    lig_rank_score.append(string)


with open('/net/jam-amaro-shared/bccgc4/Sub_Format/TICA_Sub/structurebased/LigandScores.csv', 'w') as writeFile:
    writer = csv.writer(writeFile)
    writer.writerow(['Type: score'])
    writer.writerows(lig_rank_score)
    
writeFile.close()


#note!!! need to properly load openeye from cynthia's home directory, did this part in a separate Python Script

import subprocess
import os
from openeye import oechem
import glob

path_receptors = '/net/jam-amaro-shared/bccgc4/xtaldocking/TICA_docking_DONE/receptor_pdbs_converted_from_oebs/'

for z in ordered_list:
    #making receptor pdbs
    
    begin = z.find('/receptor')
    end = z.find('.oeb')
    recep = z[begin:end]
    edit = recep.find('rec')
    recep = recep[edit:]
    #print(recep)

    ok = z.find('CatS_')
    ed = z.find(' -')
    ligan = z[ok:ed]

    os.chdir(path_receptors)
    subprocess.getoutput('cp '+recep+'.pdb '+'/net/jam-amaro-shared/bccgc4/Sub_Format/TICA_Sub/structurebased/5QC4-'+ligan+'.pdb')


#making ligand mols

files=[]#list of paths to the correct poses 
for u in range(0,459):
    obj = ordered_list[u]
    begin = obj.find('/receptor')
    end = obj.find(' -')
    recep = obj[begin:end]
    edit = recep.find('rec')
    recep = recep[edit:] #receptor* CatS_*
    cats = recep.find('.oeb')
    catS = recep.find('CatS')
    
    string = '/net/jam-amaro-shared/bccgc4/xtaldocking/TICA_docking_DONE/ligand_poses_pdbs/Centroid'+ recep[8:cats]+'-'+recep[catS:]+'.pdb'
    files.append(string)
    
print(files[0])
    
ifs=oechem.oemolistream()
ofs=oechem.oemolostream()

for i in files:
    if ifs.open(i):
        #print(i)
        slic = i.find('CatS')
        Ligand= i[slic:]
        #print(Ligand)
        Ligand=Ligand[:-4]
        print(Ligand)
            
        #index=[x for x, s in enumerate(lig_rank_score) if str(Ligand) in s]
        #print(index)
        #index=index[0]+1
        #print(index)
        if ofs.open("/net/jam-amaro-shared/bccgc4/Sub_Format/TICA_Sub/structurebased/Structure-Based_Score/"+"5QC4-"+str(Ligand)+".mol"):
            for mol in ifs.GetOEGraphMols():
                oechem.OEWriteMolecule(ofs, mol)
        else:
            oechem.OEThrow.Fatal("Unable to create output")
    else:
        oechem.OEThrow.Fatal("Unable to open input")

