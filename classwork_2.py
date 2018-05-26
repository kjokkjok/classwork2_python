
# coding: utf-8

# In[2]:


from Bio.Blast import NCBIWWW
from Bio.Blast import NCBIXML
from Bio import SeqIO

import argparse

parser = argparse.ArgumentParser(description='script does query to blast database')
parser.add_argument( '-in', '--input_file', help = 'path to file in fasta format', type = str, metavar = 'str')
parser.add_argument( '-out', '--output_file', help = 'path to file for output', type = str, metavar = 'str')

args = parser.parse_args()


with open(args.output_file, "w") as out_handle:
    for record in SeqIO.parse(args.input_file, format="fasta"):

        result_handle = NCBIWWW.qblast("blastn", "nt", record.seq,hitlist_size=1, descriptions=1,alignments=1)

        blast_records = NCBIXML.parse(result_handle)

        for blast_record in blast_records:
            for alignment in blast_record.alignments:
                for hsp in alignment.hsps:
                    out_handle.write(">"+alignment.hit_def+"\n"+hsp.query+"\n")
                    break

