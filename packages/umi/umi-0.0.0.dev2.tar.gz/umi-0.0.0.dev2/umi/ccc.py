#!/usr/bin/env python3


"""
Circular Consensus Clustering

# features

- reference guided (speed enchanced)
- uncompromising qual consolidation (posterior porb)
"""

import math
from collections import defaultdict
from functools import reduce
from itertools import combinations, groupby
from operator import itemgetter
from typing import Dict, List, Tuple

import numpy as np
from Bio import SeqIO, pairwise2
from Bio.Alphabet import SingleLetterAlphabet
from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord
from scipy.spatial.distance import squareform
from sklearn import cluster


def get_ref_seq(sample: str) -> str:
    if sample.startswith("flyS2_"):
        return next(SeqIO.parse("../ref/flyS2.fa", "fasta")).seq
    elif sample.startswith("flyS4_"):
        return next(SeqIO.parse("../ref/flyS4.fa", "fasta")).seq
    else:
        raise FileNotFoundError("no ref file...")


def call_mutation(query: str, ref: str) -> List:
    alignments = pairwise2.align.globalms(ref, query, 2, -3, -2, -1)
    #  print(pairwise2.format_alignment(*alignments[0]))
    mut = []
    indel = []
    ref_index = 0
    seq_index = 0
    for ref_site, query_site in zip(alignments[0][0], alignments[0][1]):
        if query_site != "-":
            seq_index += 1

        if ref_site != "-":
            ref_index += 1
            if (
                ref_site != query_site
                and ref_site in "GC"
                and query_site in "AT"
            ):
                mut.append(f"{ref_site}{ref_index}{query_site}")

        if ref_site == "-":
            indel.append(f"{seq_index}I")

        if query_site == "-":
            indel.append(f"{seq_index}D")

    return mut, indel


def compare_mutation(m1: List, m2: List) -> float:
    if len(m1) + len(m2) > 0:
        return 2.0 * len(set(m1) & set(m2)) / (len(m1) + len(m2))
    return 1.0


def shift_record(record: SeqRecord, indel: List) -> SeqRecord:
    ins_record = record[:1]
    ins_record.seq = "-"
    ins_record.letter_annotations["phred_quality"] = [0]

    new_record = record[:0]

    previous_index = 0
    for sm in indel:
        mut_index, mut_type = int(sm[:-1]) - 1, sm[-1]
        mut_index = 0 if mut_index == -1 else mut_index
        if mut_type == "I":
            new_record += record[previous_index:mut_index]
            previous_index = mut_index + 1
        if mut_type == "D":
            new_record += record[previous_index:mut_index] + ins_record
            previous_index = mut_index
    new_record += record[previous_index:]
    return new_record


def cluster_mutation(
    record_list: List, ref: str
) -> Dict[int, List[SeqRecord]]:
    """
    cluster by mutation
    """
    mut_list, indel_list = zip(
        *[call_mutation(r.seq, ref) for r in record_list]
    )
    dis_matrix = squareform(
        [1 - compare_mutation(m1, m2) for m1, m2 in combinations(mut_list, 2)]
    )
    aff_matrix = 1 - dis_matrix
    #  print(aff_matrix)
    cluster_fit = cluster.AffinityPropagation(
        damping=0.8, preference=0.8, max_iter=1000, affinity="precomputed"
    ).fit(aff_matrix)
    labels = cluster_fit.labels_
    if labels.ndim != 1:
        labels = np.arange(0, len(labels))
    cluster_dict = defaultdict(list)
    for k, record, indel in zip(labels, record_list, indel_list):
        cluster_dict[k].append(shift_record(record, indel))
    return cluster_dict


def ungap_record(record: SeqRecord) -> SeqRecord:
    ungap_record = SeqRecord(str(record.seq).replace("-", ""))
    ungap_record.letter_annotations["phred_quality"] = [
        record.letter_annotations["phred_quality"][i]
        for i, b in enumerate(record.seq)
        if b != "-"
    ]
    ungap_record.id = record.id
    ungap_record.name = record.name
    ungap_record.description = record.description

    return ungap_record


def iter_record(record: SeqRecord) -> Tuple:
    for nuc, qual in zip(record, record.letter_annotations["phred_quality"]):
        #  print(nuc, qual)
        yield nuc, qual


def merge_base(b1, b2):
    """
    b1 = ('A', 30)
    b2 = ('T', 10)
    """
    n1 = b1[0]
    n2 = b2[0]
    p1 = 10 ** -(b1[1] / 10)
    p2 = 10 ** -(b2[1] / 10)
    ps = p1 + p2 - 4 * p1 * p2 / 3
    if n1 == n2:
        return (n1, int(-10 * math.log10((p1 * p2 / 3) / (1 - ps))))
    if n1 != n2:
        if p1 < p2:
            return (n1, int(-10 * math.log10(p1 * (1 - p2 / 3) / ps)))
        elif p1 > p2:
            return (n2, int(-10 * math.log10(p2 * (1 - p1 / 3) / ps)))
        else:
            # n1 or n2 is equal prob
            return (n1, int(-10 * math.log10(p1 * (1 - p2 / 3) / ps)))


def consolidate_base(base_list: List[Tuple]) -> Tuple:
    result = reduce(merge_base, sorted(base_list))
    return result


def consolidate_cluster(record_list: List) -> SeqRecord:
    assert all(
        len(i) == len(record_list[0]) for i in record_list
    ), "The Sequence are not the same in length!!!"

    seq = ""
    qual = []
    for b in zip(*[iter_record(r) for r in record_list]):
        s, q = consolidate_base(b)
        seq += s
        qual.append(q)
    cons_record = SeqRecord(Seq(seq, SingleLetterAlphabet))
    cons_record.letter_annotations["phred_quality"] = qual
    return ungap_record(cons_record)


if __name__ == "__main__":
    #  testing
    SAMPLE = "flyS2_runB"

    REF = get_ref_seq(SAMPLE)

    seq_group = defaultdict(list)
    # group annotated fastq file
    for record in SeqIO.parse(
        f"./generate_consensus/{SAMPLE}_4consensus_ms.fq", "fastq"
    ):
        seq_group[record.description.split(" ")[1]].append(record)

    for group_name, gs in seq_group.items():
        for cluster_name, record_list in cluster_mutation(gs, REF).items():
            cons_record = consolidate_cluster(record_list)
            cons_record.id = f"{group_name}-CLUSTER{cluster_name}"
            cons_record.name = f"{group_name}-CLUSTER{cluster_name}"
            cons_record.description = ",".join(
                [record.id for record in record_list]
            )
            #  print(cons_record)
