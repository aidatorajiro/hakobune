import requests
import time
import lxml.etree

# search record
def search(db, term, retmax, retstart):
    time.sleep(1)
    return requests.get("https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi", 
        params={"db" : db, "term" : term, "retmax" : retmax, "retstart" : retstart}).content

# fetch record independently
def fetch(db, key):
    time.sleep(1)
    return requests.get("https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi",
        params={"db" : db, "id" : key, "retmode" : "xml"}).content

# search and fetch records
def search_and_fetch(db, term, retmax, retstart):
    time.sleep(1)
    search_data = requests.get("https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi", 
        params={"db" : db, "term" : term, "retmax" : retmax, "retstart" : retstart, "usehistory" : "y"}).content
    tree = lxml.etree.XML(search_data)
    webenv = tree.find("WebEnv").text
    query_key = tree.find("QueryKey").text
    fetch_data = requests.get("https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi", 
        params={"db" : db, "retmax" : retmax, "retstart" : retstart, "query_key" : query_key, "WebEnv" : webenv, "retmode" : "xml"}).content
    return fetch_data

# get all transcription variants and corresponding peptides
#    from an Entrezgene XML element
# returns : list of mrna IDs, list of list of peptide IDs
def get_all_transcription_variants(entrezgene):
    mrna_list = []
    protein_list_list = []
    for mRNA in entrezgene.find("Entrezgene_locus").findall("Gene-commentary/Gene-commentary_products/"):
        protein_list = []
        for peptide in mRNA.findall("Gene-commentary_products/"):
            accession = peptide.find("Gene-commentary_accession")
            if accession == None:
                continue
            protein_list.append(accession.text)
        mrna_list.append(mRNA.find("Gene-commentary_accession").text)
        protein_list_list.append(protein_list)
    return mrna_list, protein_list_list

# search gene ids
def search_gene_ids(query, num=100, start=0):
    index_data = search("gene", query, num, start)

    tree = lxml.etree.XML(index_data)

    return list(map(lambda x: x.text, index_data.findall("IdList/")))    

# get all gene data from search result
def get_all_gene_data(term, retmax, retstart):
    result = search_and_fetch("gene", term, retmax, retstart)
    mrna_list = []
    for gene in lxml.etree.XML(result).findall("Entrezgene"):
        mrna_list += get_all_transcription_variants(gene)[0]
    nuccore_data = fetch("nuccore", ",".join(mrna_list))
    tree = lxml.etree.XML(nuccore_data)
    mrna_list = []
    for mrna in tree.findall('GBSeq'):
        mrna_id = mrna.find("GBSeq_locus").text
        transcription = mrna.find("GBSeq_sequence").text
        peptide_list = []
        for label in mrna.xpath('GBSeq_feature-table/GBFeature/GBFeature_quals/GBQualifier/GBQualifier_name[text()="translation"]'):
            protein_id = label.xpath('../../GBQualifier/GBQualifier_name[text()="protein_id"]')[0].find("../GBQualifier_value").text
            translation = label.find("../GBQualifier_value").text
            peptide_list.append([protein_id, translation])
        mrna_list.append([mrna_id, transcription, peptide_list])
    return mrna_list

def translate(rna_or_dna):
    

get_all_gene_data("NC_000001.11[Nucleotide Accession]", 10, 100)