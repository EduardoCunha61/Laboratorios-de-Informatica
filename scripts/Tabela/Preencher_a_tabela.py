# -*- coding: utf-8 -*-

from Bio import Entrez
from Bio import SeqIO
import uniprot #package tem de ser instalado: pip install uniprot ; pode ser também necessário instalar: pip install requests


### PARA PREENCHER A TABELA

def download_ncbi(data_base, ident, file_name): # tutorial Biopython 9.6 --> esta funcao guarda um ficheiro genbank com o genoma inteiro 
    handle = Entrez.efetch(db=data_base, id=ident, rettype="gbwithparts", retmode="text")
    with open(file_name, 'w') as file:
        file.write(handle.read())
        
##descomentar a linha seguinte para fazer download do ficheiro contendo o genoma (inteiro) em estudo
#download_ncbi("nucleotide", "NC_002942.5", 'genoma_inteiro.gb') 

##descomentar as duas linhas a seguir para ver o conteúdo do ficheiro com o genoma inteiro na consola
#record_genome = SeqIO.read('genoma_inteiro.gb','genbank')  
#print(record_genome)


##Para obter toda a informação das funções seguintes pode-se descomentar apenas a função access_uniprot, que chama todas as anteriores


def inf_tabela(): #comparar as nossas proteinas com as CDS do genoma inteiro e se forem iguais retirar algumas informações
    list_protein=[]
    list_files_prot=["prot1.fasta", "prot2.fasta", "prot3.fasta", "prot4.fasta", "prot5.fasta"] #ficheiros retirados do biocyc
    
    for file in list_files_prot:
        for prot in SeqIO.parse(file, "fasta"):
            list_protein.append(prot.seq)
            
    id_protein=[]
    
    for rec in SeqIO.parse("genoma_inteiro.gb", "genbank"):
        if rec.features:
            for feature in rec.features:
                for protein in list_protein:
                    if feature.type == "CDS" and "".join(feature.qualifiers["translation"]) == protein:
                        print(feature.qualifiers["gene"])
                        print (feature.qualifiers["db_xref"])
                        print ("locus_tag:", feature.qualifiers["locus_tag"])
						
                        #print("Strand:", feature.location.strand) #if, elif e else a seguir fazem mais ou menos o mesmo que esta linha, só que mais completo
                        if feature.location.strand == 1:
                            print("Top Strand")
                        elif feature.loctaion.strand == -1:
                            print("Bottom Strand")
                        elif feature.location.strand == 0:
                            print("The strand is important, but unknown")
                        else:
                            print("The strand doesn't matter")                        
                            
                        try: #faz-se try porque o EC_number pode ou não existir
                            print ("EC_number:", feature.qualifiers["EC_number"])
                        except:
                            print("O EC_number não foi encontrado")
                            
                        print (feature.qualifiers["function"], "\n")
                        id_protein.append(feature.qualifiers["protein_id"])
    
    return id_protein

##descomentar a linha seguinte para obter algumas informações sobre as nossas proteinas
#inf_tabela()

            
def download_file_protein(): #fazer download dos ficheiros com informação do ncbi completa correspondente às nossas proteinas (pelo protein_id obtido nas linhas anteriores)
    p=0
    id_protein=inf_tabela() #faz print das restantes informações das proteinas contidas em inf_tabela()
    for protein in id_protein:
        p +=1
        file_name="Prot" + str(p) + "_comp.gb"
        download_ncbi("Protein", protein, file_name )
        
##descomentar a linha seguinte para fazer download dos ficheiros com informação completa do ncbi correspondente às nossas proteinas
#download_file_protein()


def inf_tabela2 (): #retirar mais informação para a tabela dos ficheiros completos das proteinas (retirados nas linhas anteriores)
    
    download_file_protein()
    
    file_list_prot_comp=["Prot1_comp.gb", "Prot2_comp.gb", "Prot3_comp.gb", "Prot4_comp.gb", "Prot5_comp.gb"]
    
    access_num_prot=[]
    
    for file in file_list_prot_comp:
        for rec in SeqIO.parse(file, "genbank"):
            print("\n", "Nome:", rec.description)
            print("Accession Number:", rec.annotations["accessions"])
            print("Número de aminoácidos:", len(rec.seq))
            
            access_num_prot.append(rec.annotations["accessions"])
    
    return access_num_prot
       
##descomentar a linha seguinte para obter informação sobre a proteina (chama também a inf_tabela e o download_file_protein)
#inf_tabela2()
    

def access_uniprot(): #aceder à uniprot e retirar o uniprot_id das nossas proteinas através do accession number do ncbi 
    
    access_num_prot=inf_tabela2() #faz print das restantes informações da prot e faz download do ficheiro das proteinas
    
    for x in range(len(access_num_prot)):
        uniprot_id = uniprot.map(access_num_prot[x], f='P_REFSEQ_AC', t='ACC')
        print("\n", uniprot_id)

##descomentar a linha seguinte para obter o uniprot_id das proteinas (chama também a inf_tabela, download_file_protein e inf_tabela2)
access_uniprot()





