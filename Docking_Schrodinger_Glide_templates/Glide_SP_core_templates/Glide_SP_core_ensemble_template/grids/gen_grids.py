
#Code to write bash script that generates grids based off of the input files made by grid_in.py

method = 'TICA' #clustering method
dock = 'SP' #docking method

with open('gen_grids.sh','w') as newfile:
    for num in range(10):
        newfile.write('$SCHRODINGER/glide /scratch/jegan/GLIDE_'+dock+'_core_docking/'+method+'_docking/grids/'+method+'_grid_'+str(num)+'.in\n')
