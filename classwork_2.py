
# coding: utf-8

# In[2]:


from Bio.Blast import NCBIWWW
from Bio.Blast import NCBIXML
from Bio import SeqIO
with open("blast_result.fasta", "w") as out_handle:

        for record in SeqIO.parse("./classwork2.fasta", format="fasta"):

            result_handle = NCBIWWW.qblast("blastn", "nt", record.seq,hitlist_size=1, descriptions=1,alignments=1)

            blast_records = NCBIXML.parse(result_handle)
        
            for blast_record in blast_records:
                for alignment in blast_record.alignments:
                    for hsp in alignment.hsps:
                        out_handle.write(">"+alignment.hit_def+"\n"+hsp.query+"\n")
                        break

