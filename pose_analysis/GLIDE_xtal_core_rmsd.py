#this is a script for comparing the rmsd of the ligand poses for the xtal structure runs to the coxtal pose

from schrodinger import structure as struct
from schrodinger.structutils import analyze
from schrodinger.structutils import rmsd

#calculating rmsd of core structures for blind docking
docktypes = ['SP','SP_core','XP','XP_core'] #the holo runs use the same structure as the SP runs
home = '/home/jegan/pose_analysis/'

xtal = struct.Structure.read(home+'5QC4_holo.maegz', index = 1)
xtal_rec = analyze.evaluate_asl(xtal, '(( backbone ) ) AND (res.num 1-216)')
print(len(xtal_rec))

for docktype in docktypes:
    input_file = '/home/jegan/GLIDE_docking/GLIDE_'+docktype+'_docking/XTAL_'+docktype+'_pv.maegz'
    with open(home+'lig_core_rmsd/GLIDE_'+docktype+'_docking/XTAL_rmsd.csv','w') as datafile:
        datafile.write('Ligand, Receptor number, Score, RMSD of Core structure from XTAL Ligand\n')
        data = []
        for lig in struct.StructureReader(input_file, index = 2):
            #structure = struct._StructureProperty(lig) #finding the properties in the project table
            #print(structure.keys()) #printing out all available properties

            lig_title = lig.property['s_m_title'] #getting the title of each ligand
            score = float(lig.property['r_i_docking_score']) #getting the score of the ligand
            recep_num = 0 #there is only one receptor because these are only docked to the crystal structure
            recep = struct.Structure.read(input_file, index = recep_num) #defining the corresponding receptor in the epv file
            
            if docktype == 'SP': #there's a weird fluke with the residue enumeration
                rec_atoms = analyze.evaluate_asl(recep, '(( backbone ) ) AND (res.num 3-218)') #defining the backbone atoms of the corresponding receptor
            else:
                rec_atoms = analyze.evaluate_asl(recep, '(( backbone ) ) AND (res.num 2-217)') #defining the backbone atoms of the corresponding receptor
            
            rmsd.superimpose(recep, rec_atoms, xtal, xtal_rec, move_which = rmsd.CT) #superimposing the coxtal structure's backbone atoms on the atoms of the current receptor
            
            indices = analyze.evaluate_smarts_canvas(lig, 'c1nnc(c12)CCNC2') #getting the core indices of the ligand
            for index in indices: #because the nested list gives the rmsd calculation big problems......
                lig_core = index

            xtal_lig = analyze.evaluate_asl(xtal, '(res.ptype "BC7 ")') #getting the indices of the coxtal ligand after superposition
            xtal_lig_struct = (struct._AtomCollection(xtal, xtal_lig)).extractStructure() #extracting the coxtal ligand as a separate structure
            indices_2 = analyze.evaluate_smarts_canvas(xtal_lig_struct, 'c1nnc(c12)CCNC2') #getting core indices of coxtal ligand
            for index in indices_2:
                xtal_core = index
            
            core_rmsd = rmsd.calculate_in_place_rmsd(xtal_lig_struct, xtal_core, lig, lig_core) #calculating rmsd of cores
            
            line = [lig_title, recep_num, score, core_rmsd]
            data.append(line)
                
        data.sort(key = lambda x: x[2])
        print(docktype)
        print(data[0])
        for line in data:
            newline = line[0]+','+str(line[1])+','+str(line[2])+','+str(line[3])+'\n'
            datafile.write(newline)




        
