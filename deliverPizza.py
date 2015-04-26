import numpy as np


def findWeightedCentroid(mr, mc, weights):
    totalWeight = np.sum(weights)
    return (int(np.floor(np.sum(np.multiply(mr, weights)) / totalWeight)), \
            int(np.floor(np.sum(np.multiply(mc, weights)) / totalWeight)))

def findCost(r, c, meshr, meshc, weights):
    return np.sum(np.multiply(np.absolute(meshr - r) + np.absolute(meshc - c), weights))


if __name__ == '__main__':
    from sys import stdin, stdout

    cases = stdin.readline()
    for case in range(int(cases)):
        n, m = [int(item) for item in stdin.readline().split()]

        mr, mc = np.meshgrid(np.arange(n), np.arange(m))

        data = np.zeros((m, n))
        for i in range(m):
            data[i, :] = np.fromstring(stdin.readline(), dtype=int, sep=" ")
        c = findWeightedCentroid(mr, mc, data)

        size = 7
        temp = 0
        scost = 0
        for i in range(-size, size + 1):
            for j in range(-size, size + 1):
                temp = findCost(c[0] + i, c[1] + j, mr, mc, data)
                if (i == 0) and (j == 0):
                    scost = temp
                elif (temp < scost):
                    scost = temp

        stdout.write("{0} blocks\n".format(int(scost)))