import sys
from openeye import oechem
from openeye import oeomega


def main(argv=[__name__]):

    ifs = oechem.oemolistream()
    if not ifs.open("lig.smi"):     #input: ligand SMILES
        oechem.OEThrow.Fatal("Unable to open %s for reading" % argv[1])

    ofs = oechem.oemolostream()
    if not ofs.open("lig.oeb.gz"):  #output: OEBinary Format
        oechem.OEThrow.Fatal("Unable to open %s for writing" % argv[2])

    omegaOpts = oeomega.OEOmegaOptions()    #Parameters
    omegaOpts.SetMaxConfs(800)
    omegaOpts.SetCanonOrder(False)
    omegaOpts.SetSampleHydrogens(True)
    omegaOpts.SetEnergyWindow(15.0)
    omegaOpts.SetRMSThreshold(1.0)
    omegaOpts.SetStrictStereo(True)
    omegaOpts.SetRangeIncrement(8)
    omega = oeomega.OEOmega(omegaOpts)

    for mol in ifs.GetOEMols():
        oechem.OEThrow.Info("Title: %s" % mol.GetTitle())
        if omega(mol):
            oechem.OEWriteMolecule(ofs, mol)

    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
