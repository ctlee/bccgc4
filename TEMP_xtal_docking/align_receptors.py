#ALIGN RECEPTOR
import mdtraj as md
import glob
import itertools
import sys
def main(argv=[__name__]):
    path="receptor_pdbs/5QC4_formd.pdb"
    files=glob.glob(path)
    print(files)

    path2="receptor_pdbs/*.pdb"
    files2=glob.glob(path)
    print(files2)

    traj=md.load(files[0]) #5QC4_formd.pdb= ref structure to align everything else to
    count=0
    for i in files2: #align all clustered receptors to ref
        
        traj1=md.load(i)
        
        s=traj1.superpose(traj, 0)

        s.save_pdb("aligned_receptor/aligned_receptor"+str(count)+".pdb")
        count=count+1


    return 0

if __name__ == "__main__":
    sys.exit(main(sys.argv))

