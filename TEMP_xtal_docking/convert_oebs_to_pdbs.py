from openeye import oechem
import glob
import sys

def main(argv=[__name__]):

    ifs=oechem.oemolistream()
    ofs=oechem.oemolostream()

    #Ligand Poses
    path="Docking_Results/*.oeb"
    files=glob.glob(path)
    print(files)

    for i in files:
        count=0
        if ifs.open(i):
            if ofs.open("ligand_poses_pdbs/"+"pose"+str(count)+".pdb"):
                for mol in ifs.GetOEGraphMols():
                     oechem.OEWriteMolecule(ofs, mol)
            else:
                oechem.OEThrow.Fatal("Unable to create output")
        else:
            oechem.OEThrow.Fatal("Unable to open input")
        count=count+1
    #Receptor
    path2="receptor_oebs/*.oeb"
    files=glob.glob(path2)
    print(files)

    for j in files:
        count2=0
        if ifs.open(j):
            if ofs.open("receptor_pdbs_converted_from_oebs/"+"receptor"+str(count2)+".pdb"):
                for mol in ifs.GetOEGraphMols():
                     oechem.OEWriteMolecule(ofs, mol)
            else:
                oechem.OEThrow.Fatal("Unable to create output")
        else:
            oechem.OEThrow.Fatal("Unable to open input")
        count2=count2+1
    return 0

if __name__ == "__main__":
    sys.exit(main(sys.argv))

