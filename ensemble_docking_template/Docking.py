import lig_gen_omega
import make_receptor_huge_box
import wo_commandline_mult_receptors_dock
import convert_oebs_to_pdbs
import split_pdb
import convert_lig

lig_gen_omega.main() #Using parameters from Jeff
make_receptor_huge_box.main() #Make receptors--> Max and min coordinates of protein used for each receptor's box
wo_commandline_mult_receptors_dock.main() #Docking
convert_oebs_to_pdbs.main() #Convert ligand poses and receptor
split_pdb.main() #One ligand per pdb 
convert_lig.main() #Convert omega oeb to pdb
