
#uses the csv file from schrodinger to make a file where kendalls tau can be compared **this time for the epv file, with the attached structures

with open('scores_ranked.csv', 'w') as newfile:
    with open('scores.csv', 'r') as scores:
        
        scores = scores.readlines()
        
        ls = []
        for line in scores:
            obj = line.split(',')
            ls.append(obj)

        count = 1
        for k in ls[2:]:
            newfile.write(k[0]+','+str(count)+','+k[1]+'\n')
            count = count+1
            
        print('Num of Ligands = '+str(count-1))

