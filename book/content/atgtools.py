def get_gc_content(seq):
    """
    Se acuerdan de esta opción de comentario

    Este es un programa que hace magia.
    Calcula el contenido de GC.
    """
    # if type(seq) == str
    if isinstance(seq, str):
        c = a = g = t = 0

        for nucl in seq:
            if nucl == "C":
                c += 1
            elif nucl == "G":
                g += 1
            elif nucl == "A":
                a += 1
            elif nucl == "T":
                t += 1

        gc_content = (g + c) * 100 / (a + t + g + c)
    else:
        pass
    return gc_content


def get_codons(seq_rna):
    """
    Esta función divide la secuencia en segmentos de 3
    y envía cada fragmento a una lista
    """
    codon_list = []

    for i in range(0, len(seq_rna), 3):
        codon = seq_rna[i : i + 3]
        if len(codon) < 3:
            codon_list.append("*")
        else:
            codon_list.append(codon)
    return codon_list


# Instal packages with piplite
import sys

if "pyodide" in sys.modules:
    import piplite

    await piplite.install("pyb2d-jupyterlite-backend>=0.4.2")
