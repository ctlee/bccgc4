# Schrodinger's Glide Docking 

To improve upon our rank ordering results from [OpenEye's FRED docking](https://www.eyesopen.com/oedocking), we chose to change our docking software to [Schrodinger's Glide](https://www.schrodinger.com/glide).
We experimented with various docking conditions with the Glide in attempts to  continue to improve rankings.

**Conditions:**

* Glide Standard Precision on apo structures and blinded docking (SP-AB)
* Glide Standard Precision on apo structures and core constrained docking (SP-AC)
* Glide Extra Precision on apo structures and blinded docking (XP-AB)
* Glide Extra Precision on apo structures and core constrained docking (XP-AC)
* Glide Standard Precision on holo structures and blinded docking (SP-HB)
* Glide Standard Precision on holo structures and core constrained docking (SP-HC)

The core constrained docking bound the ligand core within 3.5 angstroms of the original co-crystal ligand. 

**Templates:**

In each subfolder, we include separate templates for performing:

* Ensemble docking, with multiple receptors extracted from Molecular Dynamics (MD) trajectories
* Rigid docking, with the single co-crystal structure

Note that the code for performing docking on the holo structures is identical to the Glide Standard Precision code, with changes on the initial receptor files only.

