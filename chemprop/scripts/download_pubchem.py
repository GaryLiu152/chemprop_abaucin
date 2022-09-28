#Strictly for creating commands to download PubChem files

def proper_digs(number):
    add_zero = 9 - len(str(number))
    ans = '0'* add_zero + str(number)
    return(ans)

with open('raw_data/pubchem/command_gen.txt', 'w') as f:
    for i in range(1,892):
        int_1 = ((i-1)*500000)+1
        int_2 = int_1 + 499999
        int_1 = proper_digs(int_1)
        int_2 = proper_digs(int_2)

        f.write('wget https://ftp.ncbi.nlm.nih.gov/pubchem/Substance/CURRENT-Full/SDF/Substance_' + str(int_1) + '_' + str(int_2) +'.sdf.gz;\n')

