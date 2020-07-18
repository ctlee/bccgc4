# Code for BioChemCoRe GC4 Team

The Drug Design Data Resource ([D3R](https://drugdesigndata.org/)) hosts community drug discovery challenges that include goals of pose prediction, ligand affinity ranking, and free energy calculation.
We participated in the ligand affinity ranking aspect of [Grand Challenge 4, subchallenge 2](https://drugdesigndata.org/about/grand-challenge-4/cathepsin_s), which focused on the Cathepsin S (CatS) system and 459 ligands.

This is a repository of relevant analysis scripts and methods on our work before the challenge and much exploration that was performed after the challenge. 

## Molecular Dynamics and Clustering

We first generated Molecular Dynamics (MD) trajectories of the CatS protein (PDBID: 5qc4) without the ligand (apo MD) and with the ligand (holo MD).

We then clustered the MD trajectories by 3 different algorithms:

* Time-lagged Independent Components Analysis and K-means (TICA) in [PyEMMA](http://www.emma-project.org/v2.4/api/generated/pyemma.coordinates.tica.html)
* Principal Components Analysis and K-means (PCA) in [PyEMMA](http://www.emma-project.org/v2.4/api/generated/pyemma.coordinates.pca.html)
* RMSD-Based Clustering in [Gromacs](http://manual.gromacs.org/documentation/2018/onlinehelp/gmx-cluster.html) (Gromos)

And by 2 different atom selections:

* Backbone atom positions (TICA and PCA) or Carbon alphas (Gromos)
* Binding Atoms (defined as within 2 angstroms of initial docked poses)

For a total of 6 clustering methods, which from each we extracted 10 docking structures as the centroid of each of 10 discrete clusters.

## Docking

We initially docked to OpenEye's Fast Exhaustive Docking ([FRED](https://www.eyesopen.com/oedocking)), however, we did not produce results that effectively ranked the ligands.

We changed our docking software to Schrodinger's [Glide](https://www.schrodinger.com/glide), and explored various modifications of the docking conditions.

To obtain a rank ordering, we took the minimum score of each ligand out of the 10 scores it received for each clustering method.

## Analysis

**Centroid Analysis**

We analyzed the structural variations in the centroids we obtained from clustering the MD trajectories across various methods, through investigating the Root-Mean-Squared-Deviations (RMSD) and Root-Mean-Squared-Fluctuations (RMSF) of the centroids, in [MDTraj](http://mdtraj.org/1.9.3/) and AMBER18's cpptraj.

**Kendall's Tau and Scoring Analysis**

To analyze the how effective the Kendall's Taus of our results were, we compared the them against a distribution of random rank ordering.

In addition, we explored different scoring schemes where we took the average or weighted average ligand score instead of the minimum of the ensemble.

**Pose Analysis**

To investigate the accuracy of our poses, we compared the common ligand core RMSDs to the original co-crystal ligand in Schrodinger.

**Ligand Analysis**

To justify the comparison of pose accuracy to cocrystal poses, we investigated the similarity of the given test set ligands to the current [co-crystal ligands](https://www.rcsb.org/search?request=%7B%22query%22%3A%7B%22parameters%22%3A%7B%22attribute%22%3A%22rcsb_polymer_entity.pdbx_description%22%2C%22operator%22%3A%22contains_phrase%22%2C%22value%22%3A%22Cathepsin%20S%22%7D%2C%22service%22%3A%22text%22%2C%22type%22%3A%22terminal%22%2C%22node_id%22%3A0%7D%2C%22return_type%22%3A%22entry%22%2C%22request_options%22%3A%7B%22pager%22%3A%7B%22start%22%3A0%2C%22rows%22%3A100%7D%2C%22scoring_strategy%22%3A%22combined%22%2C%22sort%22%3A%5B%7B%22sort_by%22%3A%22score%22%2C%22direction%22%3A%22desc%22%7D%5D%7D%2C%22request_info%22%3A%7B%22src%22%3A%22ui%22%2C%22query_id%22%3A%2226c807bfd62453b07e06eb087386d14f%22%7D%7D) available in the [RCSB PDB](https://www.rcsb.org/) databank through Tanimoto Coefficient. 

## Citing this Repository

Please cite _______ if you use these scripts or analyses in your work.
