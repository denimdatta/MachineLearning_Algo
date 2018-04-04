# Name: Denim Datta

import time

import matplotlib.pyplot as plt
import numpy as np


def read_data(filename):
    dataset = []

    with open(filename, "r") as file:
        data = file.readlines()

    for line in data:
        values = line.rstrip().split(",")
        tmp = []
        for v in values[1:-1]:
            tmp.append(float(v))
        dataset.append(tmp)

    return dataset


def kmean_cluster(data, k):
    centroids = [feature for feature in data[0:k]]
    centroids.sort()

    tempRound = 0
    while True:
        tempRound += 1
        region = {}
        for i in range(k):
            region[i] = []

        for feature in data:
            n_feature = np.array(feature)
            n_centroid = [np.array(centroid) for centroid in centroids]
            euclidian = []
            for centroid in n_centroid:
                euclidian.append(np.linalg.norm(centroid - n_feature))
            min_index = euclidian.index(min(euclidian))
            region[min_index].append(feature)

        empty_region_count = 0
        empty_regions = []
        largest_region_index = 0
        for r in region.keys():
            if len(region[r]) > len(region[largest_region_index]):
                largest_region_index = r

            if len(region[r]) == 0:
                empty_region_count += 1
                empty_regions.append(r)

        if empty_region_count > 0:
            for i in range(empty_region_count):
                region_index = empty_regions[i]
                region[region_index].append(region[largest_region_index][i])
            region[largest_region_index] = region[largest_region_index][empty_region_count:]

        centroids_updated = find_centroids(region)
        # for r in region.keys():
        #     print("K:{} -- S:{}\nV:{}\n".format(r, len(region[r]), region[r]))
        # for c in centroids_updated:
        #     print("New: {}".format(c))

        converged = True

        for i in range(k):
            if not np.array_equal(centroids[i], centroids_updated[i]):
                converged = False
                break

        if converged:
            break
        else:
            centroids = centroids_updated

    print("[Total] {}".format(tempRound))

    return centroids, region


def find_centroids(regions):
    feature_size = len(regions[0][0])
    new_centroids = [[0 for i in range(feature_size)] for j in range(len(regions))]
    for r in regions:
        new_centroids[r] = (np.average(regions[r], axis=0)).tolist()
    # new_centroids = new_centroids.tolist()
    new_centroids.sort()
    return new_centroids


def potential_fn(centroid, region):
    potential = 0

    for i in range(len(centroid)):
        dist = [np.linalg.norm(np.array(centroid[i]) - data) for data in region[i]]
        for d in dist:
            # potential += (d*d)
            potential += d
        # print("DL:{} -- DSL:{}\nDIST: {}".format(len(region[i]), len(dist), dist))
    print(potential)
    return potential


def main():
    clusters = [2, 3, 4, 5, 6, 7, 8]
    feature_data = read_data('data/bc.txt')
    potentials = []

    for k in clusters:
        (centroids, regions) = kmean_cluster(feature_data, k)
        # for c in centroids:
        #     print("C: {}".format(c))
        # for r in regions:
        #     print("R: {}".format(regions[r]))
        potential = potential_fn(centroids, regions)
        potentials.append(potential)

    # plt.ylim(int(math.floor(min(potentials)/10.0)) *10 , int(math.ceil((max(potentials) + 1) / 10.0)) * 10)
    plt.ylabel("Potential Function")
    plt.xlabel("K Value")
    plt.title("Potential Function Vs. K value")
    plt.plot(clusters, potentials, 'rv--')
    plt.show()


ts_time = time.time()
main()
te_time = time.time()
print("Time : {} Sec".format(te_time - ts_time))
