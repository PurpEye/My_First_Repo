from sklearn.cluster import KMeans
import numpy as np
from collections import Counter


def cluster_data(filename):
    # filename= '/home/rahul/Desktop/cluster/large/500chunks/sk'

    ips_file = open(filename, 'r').readlines()
    values = np.loadtxt(ips_file).reshape(-1, 1)  # change to 1-D array

    kmeans_result = KMeans(n_clusters=4, random_state=0).fit(values)
    cluster_numbers = kmeans_result.predict(values)

    map_value_cluster = np.column_stack((values, cluster_numbers))
    most_common_value = Counter(cluster_numbers).popitem()

    common_cluster = most_common_value[0]
    no_of_values = most_common_value[1]

    filtered_rows = np.zeros(0)  # Initialize np array with nothing

    for row in map_value_cluster:
        if row[1] == common_cluster:
            filtered_rows = np.append(filtered_rows, row[0])

    outname = filename[:-4] + '_cluster.txt'

    out = open(outname, 'w')
    np.savetxt(out, filtered_rows, fmt='%.18g', )
    return outname

# cluster_data('/home/rahul/Desktop/cluster/large/500chunks/sk')
