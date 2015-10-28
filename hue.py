__author__ = 'robert'

def fun():
    print "test"
    from phue import Bridge
    b = Bridge('192.168.11.8')
    b.connect()
    b.get_api()
    b.set_light(1, 'on', True)
    b.set_light(1, 'bri', 254)

if __name__ == "__main__":
    from sklearn.cluster import KMeans
    import matplotlib.pyplot as plt
    import argparse
    import utils
    import cv2