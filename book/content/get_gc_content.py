def get_gc_content(seq):
    """
    Se acuerdan de esta opción de comentario

    Este es un programa que hace magia.
    Calcula el contenido de GC.
    """
    if type(seq) == str:
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