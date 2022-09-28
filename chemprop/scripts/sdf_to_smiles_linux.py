import os

from rdkit import Chem
from rdkit import rdBase
total_mols = 0
for filename in os.listdir('./data/raw/pubchem'):
    print(filename)
    if filename.endswith(".sdf"):
        i=0
        sdf = Chem.SDMolSupplier( './data/raw/pubchem/' + str(filename))
        no_sdf = filename[0:-4]
        with open('./data/raw/pubchem/' + str(no_sdf) + '.smi', 'w+') as f:
            for mol in sdf:
                i+=1
                try:
                    if i%1000 == 0:
                        print('Progress = ' + str(i))
                    smi = Chem.MolToSmiles(mol)
                    f.write("{}\n".format(smi))
                    total_mols+=1
                except:
                    print('No smiles' + str(i) )
            f.close()

print('Total Molecules Given Smiles = ' + str(total_mols))
