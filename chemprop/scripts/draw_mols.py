import rdkit
from rdkit import Chem
from rdkit.Chem import Draw

file = "./raw_data/screening_3/final/EC/processed/EC_hitlist_with_smiles.csv"
smiles = []
cid = []
tnn_smiles = []
pred_score = []
Bioactivity = []
with open(file) as f:
    for row in f:
        split_row = row.split(',')
#        print(smiles)
        smiles.append(split_row[0])
        Bioactivity.append(split_row[1])
#        cid.append(split_row[8])
        # pred_score.append(split_row[4])
        # tnn_smiles.append(split_row[1])
# smiles = [row.split(',')[0] for row in f]
# pred_score = [row.split(',')[4] for row in f] 
mols = [Chem.MolFromSmiles(s) for s in smiles]
mols_per_image = 32
mols_per_row = 8

for i in range(0, len(mols), mols_per_image):
    if mols_per_image > (len(smiles)-i):
        mols_per_image = (len(smiles)-i)
    img = Draw.MolsToGridImage(
        mols[i:i + mols_per_image],
        molsPerRow=mols_per_row,
        subImgSize=(600, 600),
        legends=[Bioactivity[j] for j in range(i, i + mols_per_image)]
    )
    img.save("./raw_data/screening_3/final/EC/processed/draw_hitlist/" + (str(i // mols_per_image) + '.png'))
