import glob
import sys

def main(argv=[__name__]):

    path="ligand_poses_pdbs/*.pdb"
    files=glob.glob(path)
    print(files)

    for i in files:
        fread=open(i,"r")
        Lines=fread.readlines()
        print(Lines[0])
        count=0
        header=""
        print(header)
        for line in Lines:
            
            
            if "COMPND" in line and line != header:
                header=line
                count +=1
                fwrite=open("ligand_poses_pdbs/CatS_%s.pdb"%(count),"w")
                fwrite.write(line)
            else:
                fwrite.write(line)
        fwrite.close()
        fread.close()
    return 0

    
if __name__ == "__main__":
    sys.exit(main(sys.argv))
       

