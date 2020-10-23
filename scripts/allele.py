


def read(file_name):
    with open(file_name) as f:
        s = f.read()
    lines = s.split('\n')[:-1]
    positions = []
    afs = []
    for line in lines:
        position, af = line.split('\t')
        positions.append(int(position))
        afs.append(float(af))
    return positions, afs


names = ['Peruvian', 'Synthetic', 'MXL', 'YRI', 'CEU']
file_names = ['s1af.txt', 's2af.txt', 'mxl.txt', 'yri.txt', 'ceu.txt']

positions_set = None
positions_list = []
afs_list = []
for file_name in file_names:
    positions, afs = read(file_name)
    positions_list.append(positions)
    afs_list.append(afs)
    if positions_set is None:
        positions_set = set(positions)
    else:
        positions_set = positions_set.intersection(positions)
positions_intersection = sorted(list(positions_set))
print(positions_intersection)
