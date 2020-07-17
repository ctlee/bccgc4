
#uses the csv file from schrodinger to make a file where kendalls tau can be compared **this time for the epv file, with the attached structures

with open('scores_ranked.csv', 'w') as newfile:
    with open('scores.csv', 'r') as scores:
        
        scores = scores.readlines()
        
        ls = []
        for line in scores:
            obj = line.split(',')
            ls.append(obj)

        count = 1
        #starting after the title and after the 10 receptor files, also had to add in a new line section because this file now includes the receptor number that goes with it at the end of the line
        for k in ls[11:]:
            newfile.write(k[0]+','+str(count)+','+k[1]+'\n')
            count = count+1
            
        print('Num of Ligands = '+str(count-1))

