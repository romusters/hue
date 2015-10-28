#http://www.pyimagesearch.com/2014/05/26/opencv-python-k-means-color-clustering/


def fun():
    print "test"
    from phue import Bridge
    b = Bridge('192.168.11.8')
    b.connect()
    b.get_api()
    b.set_light(1, 'on')
    b.set_light(1, 'bri', 127)


def centroid_histogram(clt):
    # grab the number of different clusters and create a histogram
    # based on the number of pixels assigned to each cluster
    numLabels = np.arange(0, len(np.unique(clt.labels_)) + 1)
    (hist, _) = np.histogram(clt.labels_, bins = numLabels)
 
    # normalize the histogram, such that it sums to one
    hist = hist.astype("float")
    hist /= hist.sum()
 
    # return the histogram
    return hist


def plot_colors(hist, centroids):
    # initialize the bar chart representing the relative frequency
    # of each of the colors
    bar = np.zeros((50, 300, 3), dtype = "uint8")
    startX = 0
 
    # loop over the percentage of each cluster and the color of
    # each cluster
    for (percent, color) in zip(hist, centroids):
        # plot the relative percentage of each cluster
        endX = startX + (percent * 300)
        cv2.rectangle(bar, (int(startX), 0), (int(endX), 50),
            color.astype("uint8").tolist(), -1)
        startX = endX
    
    # return the bar chart
    return bar

if __name__ == "__main__":
    #fun()
    from sklearn.cluster import KMeans
    import matplotlib.pyplot as plt
    import argparse
    import utils
    import cv2
    import numpy as np

    cam = cv2.VideoCapture(1)   # 0 -> index of camera
    
    while True:
        s, img = cam.read()

        image = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

        image = image.reshape((image.shape[0] * image.shape[1], 3))
        # cluster the pixel intensities
        clt = KMeans(n_clusters = 5, n_jobs=-1)
        clt.fit(image)

        hist = centroid_histogram(clt)
        bar = plot_colors(hist, clt.cluster_centers_)
        print clt.cluster_centers_[np.argmax(hist)]
       