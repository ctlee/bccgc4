from openeye import oechem
import glob
import sys

def main(argv=[__name__]):
    ifs=oechem.oemolistream()
    ofs=oechem.oemolostream()
    path="lig.oeb.gz"
    files=glob.glob(path)
    for i in files:                         #convert ligands in oeb format to pdb format
        if ifs.open(i):
            if ofs.open(str(i)+".pdb"):
                for mol in ifs.GetOEGraphMols():
                     oechem.OEWriteMolecule(ofs, mol)
            else:
                oechem.OEThrow.Fatal("Unable to create output")
        else:
            oechem.OEThrow.Fatal("Unable to open input")

    return 0

if __name__ == "__main__":
    sys.exit(main(sys.argv))

