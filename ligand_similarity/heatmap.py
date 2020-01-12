import numpy as np
import matplotlib.pyplot as plt
plt.switch_backend('agg')
from matplotlib.pyplot import cm

method = 'top'
#dock = 'OE'

matrix = []
with open('/home/jegan/structural_analysis/similarity/'+method+'_ligs/'+method+'_ligs_tanimoto_matrix_smi.csv', 'r') as readfile:
    next(readfile)
    for line in readfile:
        lis = line.rsplit(',')
        nums = [float(i) for i in lis[1:]]
        matrix.append(nums)
        #final = ','.join(nums)

    array = np.array(matrix)
    np.save('/home/jegan/structural_analysis/similarity/'+method+'_ligs/'+method+'_ligs_tanimoto_np_smi.npy',array)

tanimotos = np.load('/home/jegan/structural_analysis/similarity/'+method+'_ligs/'+method+'_ligs_tanimoto_np_smi.npy')

fig, ax = plt.subplots()
im = ax.imshow(tanimotos, cmap = cm.viridis)
plt.tick_params(axis='x',bottom = False, top = False, labelbottom =False)
plt.yticks([])

cbar = plt.colorbar(im)
cbar.set_label('Pairwise Tanimoto Coefficients', rotation = 270, labelpad= 20)
plt.title('Pairwise Tanimoto Comparing Top Quartile Ligands')
plt.savefig('/home/jegan/structural_analysis/figs/similarity/heatmap_'+method+'_smi.png')
