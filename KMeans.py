# Name: Denim Datta

import time
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
    region = [[]] * k
    print(region)
    print(centroids)

    for feature in data:
        n_feature = np.array(feature)
        n_centroid = [np.array(centroid) for centroid in centroids]
        print(feature)
        print(centroids)
        print("{} - {}".format(n_feature.shape, n_centroid[0].shape))
        euclidian = []
        for centroid in n_centroid:
            euclidian.append(np.linalg.norm(centroid - n_feature))
        min_index = euclidian.index(min(euclidian))
        # print(euclidian)
        print(min_index)
        print(centroids is region)
        print(centroids[min_index])
        print("B: C: {}".format(centroids))
        print("B: R: {}".format(region))
        region[min_index].append(feature)

        print("M: C: {}".format(centroids))
        print("M: R: {}".format(region))

        region[min_index].append([feature])

        print("A: C: {}".format(centroids))
        print("A: R: {}".format(region))

    print(len(region))
    for r in region:
        print(r)





def accuracy(_actual_list, _prediction_list):
    correct = 0
    for index in range(len(_prediction_list)):
        if _actual_list[index] == _prediction_list[index]:
            correct += 1

    return round((correct / len(_prediction_list)) * 100.0, 3)


def main():
    clusters = [2, 3, 4, 5, 6, 7, 8]
    feature_data = read_data('data/bc.txt')

    for k in clusters[:2]:
        kmean_cluster(feature_data, k)

    # plt.ylim(0, int(math.ceil((max(tst_error) + 1) / 10.0)) * 10)
    # plt.ylabel("Test Error")
    # plt.xlabel("K Value")
    # plt.title("Test Error Vs. K value")
    # plt.plot(k_vals, tst_error, 'rv--')
    # plt.show()


ts_time = time.time()
main()
te_time = time.time()
print("Time : {} Sec".format(te_time - ts_time))
