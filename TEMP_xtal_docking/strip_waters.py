import sys

import mdtraj as md
import glob
def main(argv=[__name__]):

    path="aligned_receptor/*.pdb"
    files=glob.glob(path)
    for i in files:
        count=0
        traj=md.load(i)
        i=traj.topology.select("protein")
        new_traj=traj.atom_slice(i)
        print(new_traj)
        new_traj.save_pdb("protein_only_pdbs/protein"+str(count)+".pdb")
        count=count+1
    return 0

if __name__ == "__main__":
    sys.exit(main(sys.argv))

