#!/bin/bash
#SBATCH --job-name="amber"
#SBATCH --output="slurm.out"
#SBATCH --partition=gpu-shared
#SBATCH --gres=gpu:p100:1
#SBATCH --ntasks-per-node=7
#SBATCH --export=ALL
#SBATCH -t 48:0:00

module load amber/18 
echo $CUDA_VISIBLE_DEVICES
$AMBERHOME/bin/pmemd.cuda -O -i /net/jam-amaro-shared/bccgc4/CatS_holo_md/S10-Pro01-MD.in -o $GEN.out -p system.prmtop -c $OLD.rst -r $GEN.rst -x $GEN.nc
