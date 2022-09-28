import pubchempy as pcp #for Apollo ver.
import csv

name= 'pubchem' 
for i in range (0,892): #892 #500000
    smiles_list=[]
    with open('./data/raw/pubchem'+ str(i*500000)+'_'+ str(((i+1)*500000)-1) + '.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['cid', 'smiles'])
        for j in range ((i*500000),((i+1)*500000)):
            try:
                c= pcp.Compound.from_cid(j)
                writer.writerow([j, c.isomeric_smiles])
            except:
                print('No Smiles at' + str(j))



