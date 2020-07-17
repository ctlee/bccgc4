
#short script to format the glide output csv into a file for D3R submission and also other analyses

with open('scores_ranked.csv', 'w') as newfile:
    with open('scores.csv', 'r') as scores:
        
        scores = scores.readlines()
        
        ls = []
        for line in scores:
            obj = line.split(',')
            ls.append(obj)

        count = 1
        for k in ls[1:]:
            newfile.write(k[0]+','+str(count)+','+k[1])
            count = count+1

