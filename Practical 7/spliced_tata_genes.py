import re
#input the splice donor and output the file name based on it
splice_donor=input("please input a splice donor")
input=open('Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa','r')
output=open(f'{splice_donor}_genes.fa','w')
#find the gene contain the splice
gene_name=[]
gene_seq=[]
time=[]
splice=splice_donor[2:]
donor=splice_donor[:2]
m=-1
#store all the gene name and seq
for line in input:
    if  re.search(r'gene:',line):
        name=re.findall(r'gene:(\S+)\s',line)
        n=''.join(map(str, name))
        gene_name.append(n)
        gene_seq.append('')
        m+=1
    else:
        gene_seq[m]+=line.strip()
#count the TATA box in each gene
target_seq1="TATATAT"
target_seq2="TATATAA"
target_seq3="TATAAAA"
target_seq4="TATAAAT"
for p in range(m):
        t1=gene_seq[p].count(target_seq1)
        t2=gene_seq[p].count(target_seq2)
        t3=gene_seq[p].count(target_seq3)
        t4=gene_seq[p].count(target_seq4)
        tt=str(t1+t2+t3+t4)
        time.append(tt)
#find whether it contain the input splice donor
for i in range (m):
    if re.search(f'{donor}.+{splice}',gene_seq[i]) and int(time[i])>0:
        output.write('>'+gene_name[i]+' ')
        output.write(time[i]+ '\n')
        output.write(gene_seq[i]+'\n')

input.close()
output.close()