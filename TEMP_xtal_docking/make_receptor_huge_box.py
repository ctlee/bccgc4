
from openeye import oechem
from openeye import oedocking

import mdtraj as md
import glob
import sys

def main(argv=[__name__]):
    path="protein_only_pdbs/*.pdb"
    files=glob.glob(path)
    for i in files:
        count=0
        imstr = oechem.oemolistream(i)
        proteinStructure = oechem.OEGraphMol()
        oechem.OEReadMolecule(imstr, proteinStructure)

        coordinates_dictionary=oechem.OEMolBase.GetCoords(proteinStructure)
        print(coordinates_dictionary[0], coordinates_dictionary[1])
        x_coord=[]
        y_coord=[]
        z_coord=[]

        for key in coordinates_dictionary:
            x=coordinates_dictionary[key][0]
            y=coordinates_dictionary[key][1]
            z=coordinates_dictionary[key][2]
            x_coord.append(x)
            y_coord.append(y)
            z_coord.append(z)

        print(x_coord[0])

        x_max=max(x_coord)
        x_min=min(x_coord)
        y_max=max(y_coord)
        y_min=min(y_coord)
        z_max=max(z_coord)
        z_min=min(z_coord)

        print(x_max, y_max, z_max, x_min, y_min, z_min)
        box=oedocking.OEBox(x_max, y_max, z_max, x_min, y_min,z_min)
        receptor = oechem.OEGraphMol()
        oedocking.OEMakeReceptor(receptor, proteinStructure, box)

        oedocking.OEWriteReceptorFile(receptor,"receptor_oebs/receptor"+str(count)+".oeb") 
        count=count+1
        return 0

if __name__ == "__main__":
    sys.exit(main(sys.argv))
