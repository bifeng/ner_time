from difflib import SequenceMatcher


def differ_str(sent1, sent2):
    s = SequenceMatcher(None, sent1, sent2)

    new_dict = {}

    match_dict = {}
    for tag, i1, i2, j1, j2 in s.get_opcodes():
        match_dict[tag+'_'+str(i1)] = {sent1[i1:i2]:sent2[j1:j2]}

    if any([1 for i in match_dict.keys() if i.startswith('replace')]):
        replaced = [value for key,value in match_dict.items() if key.startswith('replace')]
        for i in replaced:
            new_dict.update(i)

    return new_dict