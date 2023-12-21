def get_codons(seq):
    """
    Esta función divide la secuencia en segmentos de 3
    y envía cada fragmento a una lista
    """
    codon_list = []

    for i in range(0, len(seq_rna), 3):
        codon = seq_rna[i:i + 3]
        if len(codon) < 3:
            codon_list.append("*")
        else:
            codon_list.append(codon)
    return codon_list