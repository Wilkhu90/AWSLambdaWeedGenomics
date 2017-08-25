from Bio.Blast.Applications import NcbiblastnCommandline
from Bio.Blast import NCBIXML
from Bio.Blast import NCBIWWW
import re, math


def lambdaFunc(event, context):
    sequence = event['sequence']
    gene_description = event['gene_description']
    sid = event['sid']
    result_handle = NCBIWWW.qblast("blastn", "nt", sequence)
    blast_records = NCBIXML.read(result_handle)
    results = blast_records.alignments
    hits = []
    for result in results:
        for hit in result.hsps:
            changedQuery = re.sub(r"-", "_", hit.query)
            times = int(math.ceil(len(changedQuery)/60.0))
            size = 60
            length = len(hit.match)
            new_seq = []
            for i in range(0, times):
                new_seq.append({"Hit_query": changedQuery[i*size:(i+1)*size], "Hit_match": hit.match[i*size:(i+1)*size], "Hit_sbject": hit.sbjct[i*size:(i+1)*size]})

            hits.append({"Hit_exp": hit.expect, "new_seq": new_seq, "length": length,
                         "description": gene_description, "ID": sid, "Hit_id": result.hit_id})
    return hits

def blastX(event, context):
    sequence = event['sequence']
    gene_description = event['gene_description']
    sid = event['sid']
    result_handle = NCBIWWW.qblast("blastx", "nr", sequence)
    blast_records = NCBIXML.read(result_handle)
    results = blast_records.alignments
    hits = []
    for result in results:
        for hit in result.hsps:
            changedQuery = re.sub(r"-", "_", hit.query)
            times = int(math.ceil(len(changedQuery)/60.0))
            size = 60
            length = len(hit.match)
            new_seq = []
            for i in range(0, times):
                new_seq.append({"Hit_query": changedQuery[i*size:(i+1)*size], "Hit_match": hit.match[i*size:(i+1)*size], "Hit_sbject": hit.sbjct[i*size:(i+1)*size]})

            hits.append({"Hit_exp": hit.expect, "new_seq": new_seq, "length": length,
                         "description": gene_description, "ID": sid, "Hit_id": result.hit_id})
    return hits
