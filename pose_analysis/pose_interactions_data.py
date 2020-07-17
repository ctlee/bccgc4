#this is a script that parses out Schrodinger's pose viewer information that helps characterize ligand poses from Glide docking runs
#### *note* we didn't use this data eventually in our conclusions, but it was an interesting angle on the poses that may be useful for other types of analyses with other systems that have more interesting poses

from schrodinger import structure as struct
from schrodinger.structutils import analyze
import schrodinger.structutils.interactions.hbond as hbond_tool
from schrodinger.structutils import interactions
from schrodinger.structutils import measure

#calculating rmsd of core structures for blind docking
docktype = 'XP'
methods = ['TICA','TICA_CBA','PCA','PCA_CBA','GROMOS','GROMOS_CBA']
path = '/home/jegan/GLIDE_'+docktype+'_docking/'
home = '/home/jegan/pose_analysis/'
              
for method in methods:
    input_file = path+method+'_'+docktype+'_epv.maegz'
    with open(home+'pv_interactions/GLIDE_'+docktype+'_docking/'+method+'_inter.csv','w') as datafile:
        datafile.write('Ligand, Receptor number, Ranking, Interaction type, Receptor residue, distance\n')
        data = []
        for lig in struct.StructureReader(input_file, index = 11):
            #structure = struct._StructureProperty(lig) #finding the properties in the project table
            #print(structure.keys()) #printing out all available properties

            recep_num = lig.property['i_epv_best_receptor'] #getting the receptor number of each ligand
            recep = struct.Structure.read(input_file, index = recep_num) #defining the corresponding receptor in the epv file
            lig_title = lig.property['s_m_title'] #getting the title of each ligand
            score = float(lig.property['r_i_docking_score']) #getting the score of the ligand

            #getting the interactions between the ligand & protein...hbonds, halogen bonds (xbonds), pi cation, and pipi interactions
            lig_atoms = [atom for atom in lig.atom] #ligand atoms
            contacts = [] #all the recep residues that are involved in an hbond, xbond, salt bridge, pication, or pipi interaction with the ligand

            hbonds = hbond_tool.get_hydrogen_bonds(lig, st2 = recep) 
            for bond in hbonds:
                dist = measure.measure_distance(bond[0],bond[1]) #measuring the distance of the bond in case that might be interesting
                for atom in bond:
                    if atom not in lig_atoms: #no repeats please
                        res = atom.getResidue()
                        contacts.append(['hbond',res,dist]) #appending data
                        
            xbonds = hbond_tool.get_halogen_bonds(lig, st2 = recep) 
            for bond in xbonds:
                dist = measure.measure_distance(bond[0],bond[1])
                for atom in bond:
                    if atom not in lig_atoms:
                        res = atom.getResidue()
                        contacts.append(['xbond',res,dist])
            
            salt_brs = interactions.get_salt_bridges(lig, struc2 = recep)
            for br in salt_brs:
                dist = measure.measure_distance(br[0],br[1])
                for atom in br:
                    if atom not in lig_atoms:
                        res = atom.getResidue()
                        contacts.append(['saltbr',res,dist])
            
            picats = interactions.find_pi_cation_interactions(lig, struct2 = recep)             
            for picat in picats:
                dist = picat.distance
                pi_atom = picat.pi_structure.atom[picat.pi_centroid.atoms[0]]
                cat_atom = picat.cation_structure.atom[picat.cation_centroid.atoms[0]]
                if picat.pi_structure == lig:
                    rec_atom = cat_atom
                else:
                    rec_atom = pi_atom
                res = rec_atom.getResidue()                            
                contacts.append(['picat',res,dist])
            
            pipi = interactions.find_pi_pi_interactions(lig, struct2 = recep)      
            for pi in pipi:
                dist = pi.distance
                recep_ring_atm = pi.struct2.atom[pi.ring2.atoms[0]]
                res = recep_ring_atm.getResidue()
                contacts.append(['pipi',res,dist])
            
            for item in contacts:
                line = [lig_title, recep_num, score, item[0], item[1], item[2]] #creating a new line of data for every type of interaction
                data.append(line)
                
        data.sort(key = lambda x: x[2]) 
        
        for line in data:
            newline = line[0]+','+str(line[1])+','+str(line[2])+','+line[3]+','+str(line[4])+','+str(line[5])+'\n'
            datafile.write(newline)




        
