from openeye import oechem
import glob
import sys

def main(argv=[__name__]):
    ifs=oechem.oemolistream()
    ofs=oechem.oemolostream()
    path="Docking_Results/*.oeb"    #Convert ligand poses from oeb to pdb format
    files=glob.glob(path)
    for i in files:
        centroid_number=i[-5:-4]
        if ifs.open(i):
            if ofs.open("ligand_poses_pdbs/"+"pose"+str(centroid_number)+".pdb"):
                for mol in ifs.GetOEGraphMols():
                     oechem.OEWriteMolecule(ofs, mol)
            else:
                oechem.OEThrow.Fatal("Unable to create output")
        else:
            oechem.OEThrow.Fatal("Unable to open input")
    path2="receptor_oebs/*.oeb" #Convert receptors from oeb to pdb format
    files=glob.glob(path2)
    for j in files:
        centroid_number=j[-5:-4]
        if ifs.open(j):
            if ofs.open("receptor_pdbs_converted_from_oebs/"+"receptor"+str(centroid_number)+".pdb"):
                for mol in ifs.GetOEGraphMols():
                     oechem.OEWriteMolecule(ofs, mol)
            else:
                oechem.OEThrow.Fatal("Unable to create output")
        else:
            oechem.OEThrow.Fatal("Unable to open input")
    return 0

if __name__ == "__main__":
    sys.exit(main(sys.argv))

