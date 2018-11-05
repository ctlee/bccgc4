

from openeye import oechem
import glob
import sys
import csv
import operator

def main(argv=[__name__]):


    f=open("Docking_Results/score.txt","r")
    lines=f.readlines()

    s=[]
    for i in lines:
            entry=i.split(" ")
            s.append(entry)

    dict={}

    for k in s:
            dict[k[1]]=k[2]

    sorted_dict=sorted(dict.items(),key=operator.itemgetter(1),reverse=True)

    print(sorted_dict)
    count=1
    All=[]
    for a in sorted_dict:
            line=[]
            print(a)
            print(count)
            line.append(a[0])
            line.append(count)
            line.append(float(a[1]))
            count=count+1
            All.append(line)
    print(All)

    with open("Submission_Format/LigandScores.csv","w") as g:
            writer=csv.writer(g,dialect="excel")
            writer.writerow(['Type: energy'])
            writer.writerows(All)
    ifs=oechem.oemolistream()
    ofs=oechem.oemolostream()

    #Ligand Poses
    path="ligand_poses_pdbs/C*"
    files=glob.glob(path)
    print(files)

    for i in files:
        if ifs.open(i):
            print(i)
            Ligand= i[18:]
            print(Ligand)
            Ligand=Ligand[:-4]
            print(Ligand)
            
            index=[x for x, s in enumerate(All) if str(Ligand) in s]
            
            index=index[0]+1
            print(index)
            if ofs.open("Submission_Format/"+"5QC4-"+str(Ligand)+"-"+str(index)+".mol"):
                for mol in ifs.GetOEGraphMols():
                     oechem.OEWriteMolecule(ofs, mol)
            else:
                oechem.OEThrow.Fatal("Unable to create output")
        else:
            oechem.OEThrow.Fatal("Unable to open input")
        
       # Receptor
        path2="receptor_oebs/receptor0.oeb"
        files2=glob.glob(path2)
        print(files2)

        for j in files2:
            if ifs.open(j):
                if ofs.open("Submission_Format/"+"5QC4-"+str(Ligand)+"-"+str(index)+".pdb"):
                    for mol in ifs.GetOEGraphMols():
                         oechem.OEWriteMolecule(ofs, mol)
                else:
                    oechem.OEThrow.Fatal("Unable to create output")
            else:
                oechem.OEThrow.Fatal("Unable to open input")



    return 0

if __name__ == "__main__":
    sys.exit(main(sys.argv))


