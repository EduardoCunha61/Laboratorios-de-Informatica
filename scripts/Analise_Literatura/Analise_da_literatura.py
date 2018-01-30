# -*- coding: utf-8 -*-

### ANÁLISE DA LITERATURA

from Bio import Entrez
from Bio import Medline

def pubmed_nr_articles(item):  # dá o número de artigos do pubmed que abordam o termo colocado em item
    Entrez.email = "carolina.dias.silva@gmail.com"
    handle = Entrez.egquery(term=item)
    record = Entrez.read(handle)
    for row in record["eGQueryResult"]:
        if row["DbName"]=="pubmed":
            print(row["Count"])
        
def pubmed_extraction(item):   # mostra o titulo, autores, souce, (...) dos artigos com o item indicado
    handle = Entrez.esearch(db="pubmed", term=item , retmax=463)
    record = Entrez.read(handle)
    handle.close()
    idlist = record["IdList"]
    print(idlist)     
    handle = Entrez.efetch(db="pubmed", id=idlist, rettype="medline", retmode="text")
    records = Medline.parse(handle)
    records = list(records)
    for record in records:
        print("title:", record.get("TI", "?"))
        print("authors:", record.get("AU", "?"))
        print("source:", record.get("SO", "?"))
        print("")


