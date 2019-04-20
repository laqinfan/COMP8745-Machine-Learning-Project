from collections import Counter

# removing over-represented samples from the two lists x, y
def balance_classes(x, y):
    freqs = Counter(y)
    # the least common class is the maximum number we want for all classes
    max_allowable = freqs.most_common()[-1][1]
    print(max_allowable)
    num_added = {clss: 0 for clss in freqs.keys()}
    new_y = []
    new_x = []
    for i, j in enumerate(y):
        if num_added[j] < max_allowable:
            new_y.append(j)
            new_x.append(x[i])
            num_added[j] += 1
    return new_x, new_y