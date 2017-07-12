import fileinput

f = open('final_small.map', 'w');
f.write("11\n");
f.write("15\n");
for line in fileinput.input():
    tiles = line.replace('\r\n','').split(',');

    '''
        a - sidewalk corner_up_right     0
        b - sidewalk corner_up_left  90
        c - sidewalk corner_down_left  180
        d - sidewalk corner_down_right  270

        e - roof corner_up_right  0
        f - roof corner_up_left   90
        g - roof corner_down_left  180
        h - roof corner_down_right  270

        i - sidewalk edge_up
        j - sidewalk edge_left
        k - sidewalk edge_down
        l - sidewalk edge_right

        m - roof edge_up
        n - roof edge_left
        o - roof edge_down
        p - roof edge_right

        q - asphalt
        r - box
    '''

    ret = "";
    conv = {'-1': 'x',
            '18':'f',
            '21':'g',
            '24':'h',
            '36':'e',
            '19':'p',
            '22':'o',
            '25':'n',
            '35':'m',
            '20':'b',
            '23':'c',
            '26':'d',
            '38':'a',
            '28':'k',
            '29':'l',
            '30':'j',
            '31':'i',
            '33':'q',
            '39':'r',
            '40':'@'};
    
    for tile in tiles:
        ret = ret + conv[tile];

    f.write(ret+"\n");
    
f.close();