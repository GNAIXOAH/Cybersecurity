ls = ['alf',
    'hcu',
    'um_',
    '{ga',
    'wow',
    'rev',
    'r_h',
    'cum',
    '_hc',
    '_wo',
    'gni',
    'gal',
    'w{g',
    '}gn',
    'isr',
    'ow{',
    'nis',
    'm_w',
    'er_',
    'eve',
    'sre',
    'ver',]
flag = 'fla'
for i in ls:
    ls[i] = i[:: -1]
for i in ls:
    for j in ls:
        if list(ls[i])[-2, -1] == list(ls[j])[1, 2]:
            flag =

