#code to format the coxtal to cats l2 norm file into latex format

home = '/home/jegan/lig_struct_analysis/similarity_rdkit/'

with open(home+'latex_coxtal_cats.txt','w') as writefile:
    with open(home+'coxtal_cats_distances.csv','r') as data:
        
        data = data.readlines()
        
        for line in data[1:]:
            line = line.split(',')
            newline = (line[0].ljust(2)) +' & '+ line[1] +' & '+ line[2] +' & '+ ((line[3].rstrip()).ljust(5)) + '  \\\\' + '\n'
            writefile.write(newline)

