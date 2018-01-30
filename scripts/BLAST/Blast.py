# -*-coding: utf-8 -*-

from Bio import SeqIO
from Bio.Blast import NCBIWWW
from Bio.Blast import NCBIXML

def do_blast_xml():
    for num_prot in range(1,6):
    
        name_file = "prot" + str(num_prot) + ".fasta"
        my_query = SeqIO.read(name_file, format="fasta")
        result_handle = NCBIWWW.qblast("blastp", "refseq_protein", my_query.seq)
        
        name_blast = "prot" + str(num_prot) + "_blast.xml"
        blast_result = open(name_blast, "w")
        blast_result.write(result_handle.read())
        
        blast_result.close()
        result_handle.close()
        
    print("O Blast foi realizado com sucesso e os seus resultados guardados em ficheiros xml!")

##descomentar a linha a seguir para correr o blastp das nossas 5 proteinas e guardar os resultados em xml
#do_blast_xml()
    

def do_blast_txt():
    for num_prot in range(1,6):
    
        name_file = "prot" + str(num_prot) + ".fasta"
        my_query = SeqIO.read(name_file, format="fasta")
        result_handle = NCBIWWW.qblast("blastp", "refseq_protein", my_query.seq, format_type="Text")
        
        name_blast = "prot" + str(num_prot) + "_blast_text.txt"
        blast_result = open(name_blast, "w")
        blast_result.write(result_handle.read())
        
        blast_result.close()
        result_handle.close()
        
    print("O Blast foi realizado com sucesso e os seus resultados guardados em ficheiros txt!")

##descomentar a linha a seguir para correr o blastp das nossas 5 proteinas e guardar os resultados em txt
#do_blast_txt()
    
   
     
def analysis_blast(): #análise dos resultados de blast guardados em xml; resultados são guardados em ficheiros txt
    do_blast_xml()
	for num_prot in range(1,6):
        file_blast = "prot" + str(num_prot) + "_blast.xml"
        opened_file = open(file_blast, "r")
        blast_result = NCBIXML.parse(opened_file)
        
        analysis_name = "prot" + str(num_prot) + "_blast_analysis.txt"
        analysis_file = open(analysis_name, "w")
        
        e_value_max = 0.01
        
        for blast_result in blast_result:
            for alignment in blast_result.alignments:
                for hsp in alignment.hsps:
                    if hsp.expect < e_value_max:
                        to_write = "***Alignment*** \n" + "Sequence:" + alignment.title + "\n e-value:" + str(hsp.expect) + "\n Score:" + str(hsp.score) + "\n"
                        analysis_file.write(to_write)
                        
        analysis_file.close()

        opened_file.close()
    
    print("Análise concluida! Os resultados foram guardados em ficheiros txt!")
        
##descomentar a linha seguinte para obter os ficheiros (em txt) de análise dos ficheiros (em xml) do blast das proteinas
#analysis_blast()