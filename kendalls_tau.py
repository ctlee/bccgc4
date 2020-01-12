import scipy.stats as stats

dock = 'GLIDE_Docking'
#dock = 'OE_new_docking'
cluster = 'TICA_mindist'

guess = open("/home/jegan/bccgc4/"+dock+"/"+cluster+"_docking/scores_ranked.csv","r")
#guess = open("/home/jegan/bccgc4/"+dock+"/"+cluster+"_recepatoms_docking/Scores.csv","r")
answer = open("Answers.csv","r")

rguess = guess.readlines()
ranswer = answer.readlines()

guesslist = []
for i in rguess:
    entry = i.split(" ")
    guesslist.append(entry)
answerlist=[]
for i in ranswer:
    entry = i.split(" ")
    answerlist.append(entry)

#dict = {}
ans = []
for k in answerlist:
    for h in k:
        h = h.split(",")
        #dict[h[0]] = int(h[1])
        num = h[1]
        ans.append(num)

gues = []
for y in answerlist:
    for u in y:
        u = u.split(',')
        for p in guesslist:
            for v in p:
                v = v.split(',')
                if u[0] == v[0]:
                    gues.append(v[1])
#print(ans)
#print(gues)
                    
gues = [int(i) for i in gues]
ans = [int(i) for i in ans]

tau,p_value = stats.kendalltau(ans,gues)

print(tau)
print(p_value)

with open('taus.txt','a') as newfile:
    newfile.write(cluster+' Kendall Tau = '+str(tau)+'\n')
    newfile.write(cluster+" P value = "+str(p_value)+'\n')
exit()
