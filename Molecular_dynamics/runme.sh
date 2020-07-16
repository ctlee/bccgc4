#!/bin/bash

# Run minimization steps
mpirun -np 12 $AMBERHOME/bin/pmemd.MPI -O -i S01-Min01-Proton.in        -o S01-Min01.out -p 5QC4.prmtop -ref 5QC4.inpcrd -c 5QC4.inpcrd -r S01-Min01.rst
mpirun -np 12 $AMBERHOME/bin/pmemd.MPI -O -i S02-Min02-Solvent.in       -o S02-Min02.out -p 5QC4.prmtop -ref 5QC4.inpcrd -c S01-Min01.rst  -r S02-Min02.rst
mpirun -np 12 $AMBERHOME/bin/pmemd.MPI -O -i S03-Min03-Focused.in       -o S03-Min03.out -p 5QC4.prmtop -ref 5QC4.inpcrd -c S02-Min02.rst  -r S03-Min03.rst
mpirun -np 12 $AMBERHOME/bin/pmemd.MPI -O -i S04-Min04-Sidechains.in    -o S04-Min04.out -p 5QC4.prmtop -ref 5QC4.inpcrd -c S03-Min03.rst  -r S04-Min04.rst
mpirun -np 12 $AMBERHOME/bin/pmemd.MPI -O -i S05-Min05-All.in           -o S05-Min05.out -p 5QC4.prmtop -ref 5QC4.inpcrd -c S04-Min04.rst  -r S05-Min05.rst

# Run heating steps
mpirun -np 12 $AMBERHOME/bin/pmemd.MPI -O -i S06-Eql01-Heating-NTV.in   -o S06-Eql01.out -p 5QC4.prmtop -c S05-Min05.rst -r S06-Eql01.rst -ref S05-Min05.rst -x S06-Eql01.nc
mpirun -np 12 $AMBERHOME/bin/pmemd.MPI -O -i S07-Eql02-Heating-NTP.in   -o S07-Eql02.out -p 5QC4.prmtop -c S06-Eql01.rst -r S07-Eql02.rst -ref S06-Eql01.rst -x S07-Eql02.nc

# Run equilibration steps
$AMBERHOME/bin/pmemd.cuda -O -i S08-Eql03-EqlOnlyStage01.in -o S08-Eql03.out -p 5QC4.prmtop -c S07-Eql02.rst -r S08-Eql03.rst -ref S07-Eql02.rst -x S08-Eql03.nc
$AMBERHOME/bin/pmemd.cuda -O -i S09-Eql04-EqlOnlyStage02.in -o S09-Eql04.out -p 5QC4.prmtop -c S012-Eql03.rst -r S09-Eql04.rst -ref S012-Eql03.rst -x S09-Eql04.nc

# Run production
#$AMBERHOME/bin/pmemd.cuda -O -i S10-Pro01-MD.in -o OVHRZ-Pro01.out -p OVHRZ.prmtop -c S09-Eql04.rst -r OVHRZ-Pro01.rst -ref S09-Eql04.rst -x OVHRZ-Pro01.nc
