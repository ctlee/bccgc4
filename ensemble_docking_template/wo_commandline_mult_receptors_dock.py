from __future__ import print_function
import sys
from openeye import oechem
from openeye import oedocking
import glob

def main(argv=[__name__]):
    itf = oechem.OEInterface()
    oedocking.OEDockMethodConfigure(itf, "-method")
    oedocking.OESearchResolutionConfigure(itf, "-resolution")
    receptors=[]
    path="receptor_oebs/*.oeb"  #input: receptor oebs
    files=glob.glob(path)
    for i in files:
        receptor=oechem.OEGraphMol()
        if not oedocking.OEReadReceptorFile(receptor, i):
            oechem.OEThrow.Fatal("Unable to read receptor from %s" %i)
        receptors.append(receptor)
    dockMethod=5    #Set scoring function (5=Chemscore)
    dockResolution=2    #set search resolution (2=Standard)
    dock = oedocking.OEDock(dockMethod, dockResolution) #Selecting exhaustive search and scoring functions
    for receptor_idx, receptor in enumerate(receptors):
        Centroid_number=files[receptor_idx][-5:-4]
        omstr=oechem.oemolostream("Docking_Results/Receptor_%s.oeb"%(Centroid_number))
        dock.Initialize(receptor) #initialize with receptor object
        imstr = oechem.oemolistream("lig.oeb.gz")
        for mcmol in imstr.GetOEMols():
            print("docking", mcmol.GetTitle())
            dockedMol = oechem.OEMol()
            dock.DockMultiConformerMolecule(dockedMol, mcmol) #Docking
            sdtag = oedocking.OEDockMethodGetName(dockMethod)
            oedocking.OESetSDScore(dockedMol, dock, sdtag)
            dock.AnnotatePose(dockedMol)
            oechem.OEWriteMolecule(omstr, dockedMol)
            g=open("Docking_Results/score.txt","a+")  #write scores to file 
            g.write(str(files[receptor_idx])+" "+str(mcmol.GetTitle())+" "+str(oechem.OEMCMolBase.GetEnergy(dockedMol))+"\r\n")
            g.close()                
    return 0

InterfaceData = """
# Begin the definition of the -receptor command line parameter.
!PARAMETER -receptors

  # allows the use of -rec on the command as a shortcut for -receptors
  !ALIAS -rec

  # Parameter is a of type string
  !TYPE string

  # parameter can support multiple receptors ala
  #  -receptors *.oeb.gz
  !LIST true

  # Tells the OEParseCommandLine function to throw an error if this
  # parameter isn't specified on the command line
  !REQUIRED true

  # Specifies that only strings ending in .oeb or .oeb.gz are legal
  # settings for this parameter (OEParseCommandLine will throw an error)
  !LEGAL_VALUE *.oeb
  !LEGAL_VALUE *.oeb.gz

  # Description of the parameter (accessible by the users via --help command)
  !BRIEF A receptor file the molecules pass to the -in flag will be posed to

# End the definition of -receptor parameter
!END


# Begin definition of -in command line parameter
!PARAMETER -in

  # Parameter is of type string
  !TYPE string

  # Parameter must be specified on the command line or OEParseCommandLine
  # function will throw nd error.
  !REQUIRED true

  # Description of the parameter (accessible by the users via --help command)
  !BRIEF Multiconformer file of molecules to be posed.

# End of the definition of -in
!END


# Begin definition of -prefix command line parameter
!PARAMETER -prefix

  # Parameter is of type string
  !TYPE string

  # Parameter must be specified on the command line or OEParseCommandLine
  # function will throw an error.
  !REQUIRED true

  # Description of the parameter (accessible by the users via --help command)
  !BRIEF Posed molecules will be written to this file using this prefix <prefix>_<receptor#>.oeb

# End of the definition of -prefix
!END
"""


if __name__ == "__main__":
     sys.exit(main(sys.argv))
