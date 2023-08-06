
def mapencode(data, mapping, nastate=False):
    """Encode data array with mapped labels

    Parameters:
    -----------
    data : list
        array with labels that

    mapping : list of list
        the index of each element is used as encoding.
        Each element is a single label (str) or list
        of labels that are mapped to the encoding.

    nastate : bool
        If False (Default) unmatched data labels are
        encoded as None. If nastate=True then unmatched
        data labels are encoded with the integer
        enc=len(mapping).
    """
    if nastate:
        naenc = len(mapping)
    else:
        naenc = None

    out = list()

    for label in data:

        enc = naenc

        for j, c in enumerate(mapping):
            if isinstance(c, str):
                if label == c:
                    enc = j
                    break
            else:  # list
                if label in c:
                    enc = j
                    break

        out.append(enc)

    return out
