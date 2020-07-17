import glob
import sys

def main(argv=[__name__]):
    path="ligand_poses_pdbs/*.pdb"  #10 pdbs, 1 per docked receptor--> split each pdb into 459 pdbs (1 per ligand)
    files=glob.glob(path)
    for i in files:
        centroid_number=i[-5:-4]
        fread=open(i,"r")
        Lines=fread.readlines()
        count=0
        header=""
        for line in Lines:
            if "COMPND" in line and line != header:
                header=line
                count +=1
                fwrite=open("ligand_poses_pdbs/Centroid%s-CatS_%s.pdb"%(centroid_number,count),"w")
                fwrite.write(line)
            else:
                fwrite.write(line)
        fwrite.close()
        fread.close()
    return 0

if __name__ == "__main__":
    sys.exit(main(sys.argv))
       

