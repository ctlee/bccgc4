#this script makes a combined ligand file with all the methods in order, both OE and GLIDE, and then generates fingerprints and a pairwise taminoto similarity matrix

import os

docks = ['OE','GLIDE']
clusters = ['TICA','PCA','GROMOS','XTAL']
typ = 'top'
method = 'ligands_struct_quarts'
home = '/home/jegan/structural_analysis/similarity/'
path = '/home/jegan/structural_analysis'

#arranging a single ligand file that is ordered by docking method (oe then glide) and scoring method (tica, pca,gromos, xtal)
with open(home+'fp_tanimoto_matrix.sh','w') as newfile:
    newfile.write('$SCHRODINGER/utilities/structcat ')
    for dock in docks:
        for cluster in clusters:
            for x in os.listdir(home+method+'/all_'+typ+'_predicts/'):
                if (cluster+'_'+dock) in x:
                    newfile.write('-imae '+home+method+'/all_'+typ+'_predicts/'+x+' ')

    newfile.write('-omae '+home+method+'/all_'+typ+'_predicts/all_'+typ+'_ligs.mae\n')

    #generating fingerprints from the combined ligand file
    newfile.write('$SCHRODINGER/utilities/canvasFPGen -imae '+home+method+'/all_'+typ+'_predicts/all_'+typ+'_ligs.mae -o '+home+'similarity/'+typ+'_ligs/'+typ+'_ligs_fps.fp\n')

    #generating a tanimoto coefficient matrix from the fingerprint file
    newfile.write('$SCHRODINGER/utilities/canvasFPMatrix -ifp '+home+'similarity/'+typ+'_ligs/'+typ+'_ligs_fps.fp -ocsv '+home+'similarity/'+typ+'_ligs/'+typ+'_ligs_tanimoto_matrix.csv -metric 21\n')
