"""
.. module:: helpers
   :synopsis: Helper functions

.. moduleauthor:: tom hoag <tomhoag@gmail.com>

Helper functions and probably not much use outside the scope of nms


"""
import cv2
import math
import numpy as np



def createImage(width=800, height=800, depth=3):
    """ Return a black image with an optional scale on the edge

    :param width: width of the returned image
    :type width: int
    :param height: height of the returned image
    :type height: int
    :param depth: either 3 (rgb/bgr) or 1 (mono).  If 1, no scale is drawn
    :type depth: int
    :return: A zero'd out matrix/black image of size (width, height)
    :rtype: np.array
    """
    # create a black image and put a scale on the edge

    assert depth == 3 or depth == 1
    assert width > 0
    assert height > 0

    hashDistance = 50
    hashLength = 20

    img = np.zeros((int(height), int(width), depth), np.uint8)

    if(depth == 3):
        for x in range(0, int(width / hashDistance)):
            cv2.line(img, (x * hashDistance, 0), (x * hashDistance, hashLength), (0,0,255), 1)

        for y in range(0, int(width / hashDistance)):
            cv2.line(img, (0, y * hashDistance), (hashLength, y * hashDistance), (0,0,255), 1)

    return img


def polygon_intersection_area(polygons):
    """ Compute the area of intersection of an array of polygons

    :param polygons: a list of polygons
    :type polygons: list
    :return: the area of intersection of the polygons
    :rtype: list
    """
    if len(polygons) == 0:
        return 0

    dx = 0
    dy = 0

    maxx = np.amax(np.array(polygons)[...,0])
    minx = np.amin(np.array(polygons)[...,0])
    maxy = np.amax(np.array(polygons)[...,1])
    miny = np.amin(np.array(polygons)[...,1])

    if minx < 0:
        dx = -int(minx)
        maxx = maxx + dx
    if miny < 0:
        dy = -int(miny)
        maxy = maxy + dy
    # (dx, dy) is used as an offset in fillPoly

    for i, polypoints in enumerate(polygons):

        newImage = createImage(maxx, maxy, 1)

        polypoints = np.array(polypoints, np.int32)
        polypoints = polypoints.reshape(-1, 1, 2)

        cv2.fillPoly(newImage, [polypoints], (255, 255, 255), cv2.LINE_8, 0, (dx, dy))

        if(i == 0):
            compositeImage = newImage
        else:
            compositeImage = cv2.bitwise_and(compositeImage, newImage)

        area = cv2.countNonZero(compositeImage)

    return area


def get_max_score_index(scores, threshold=0, top_k=0, descending=True):
    """ Get the max scores with corresponding indicies

    Adapted from the openCV c++ source in `nms.inl.hpp <https://github.com/opencv/opencv/blob/ee1e1ce377aa61ddea47a6c2114f99951153bb4f/modules/dnn/src/nms.inl.hpp#L33>`_

    :param scores: a list of scores
    :type scores: list
    :param threshold: consider scores higher than this threshold
    :type threshold: float
    :param top_k: return at most top_k scores; if 0, keep all
    :type top_k: int
    :param descending: if True, list is returened in descending order, else ascending
    :returns: a  sorted by score list  of [score, index]
    """
    score_index = []

    # Generate index score pairs
    for i, score in enumerate(scores):
        if (threshold > 0) and (score > threshold):
            score_index.append([score, i])
        else:
            score_index.append([score, i])

    # Sort the score pair according to the scores in descending order
    npscores = np.array(score_index)

    if descending:
        npscores = npscores[npscores[:,0].argsort()[::-1]] #descending order
    else:
        npscores = npscores[npscores[:,0].argsort()] # ascending order

    if top_k > 0:
        npscores = npscores[0:top_k]

    return npscores.tolist()


def rects2polys(rects, thetas, origins, ratioWidth=1, ratioHeight=1):
    """Convert rectangles (x,y, w, h) into polygons [(x0,y0), (x1, y1), (x2, y2), (x3, y3])

    :param rects: a list of rectangles, each specified as (x, y, w, h)
    :type rects: tuple
    :param thetas: the angle of rotation for each rectangle in radians
    :type theta: list of float
    :param origin: the point to rotate each rectangle around
    :type origin: list of tuple
    :param ratioWidth: optional width scaling factor, default 1.0
    :type ratioWidth: float
    :param ratioHeight: optional height scaling factor, default 1.0
    :type ratioHeight: float
    :return: a list of polygons, each specified by its (x,y) verticies
    :rtype: list
    """
    polygons = []
    for i, box in enumerate(rects):
        upperLeftX = box[0]
        upperLeftY = box[1]
        lowerRightX = box[0] + box[2]
        lowerRightY = box[1] + box[3]

        # scale the bounding box coordinates based on the respective ratios
        upperLeftX = int(upperLeftX * ratioWidth)
        upperLeftY = int(upperLeftY * ratioHeight)
        lowerRightX = int(lowerRightX * ratioWidth)
        lowerRightY = int(lowerRightY * ratioHeight)

        # create an array of the rectangle's verticies
        points = [
            (upperLeftX, upperLeftY),
            (lowerRightX, upperLeftY),
            (lowerRightX, lowerRightY),
            (upperLeftX, lowerRightY)
        ]

        # the offset is the point at which the rectangle is rotated
        rotationPoint = (int(origins[i][0] * ratioWidth), int(origins[i][1] * ratioHeight))

        polygons.append(rotatePoints(points, thetas[i], rotationPoint))

    return polygons


def rotatePoints(points, theta, origin):
    """Rotate the list of points theta radians around origin

    :param points: list of points, each given as (x,y)
    :type points:  tuple
    :param theta: the angle to rotate the points in radians
    :type theta: float
    :param origin: the point about which the points are to be rotated
    :type origin: tuple
    :return: list of rotated points
    :rtype: list
    """
    rotated = []
    for xy in points:
        rotated.append(rotate_around_point(xy, theta, around))

    return rotated


def rotate_around_point(xy, radians, origin=(0, 0)):
    """Rotate a point around a given point.

    Adapted from `LyleScott/rotate_2d_point.py` <https://gist.github.com/LyleScott/e36e08bfb23b1f87af68c9051f985302>`_

    :param xy: the (x,y) point to rotate
    :type xy: tuple
    :param radians: the angle in radians to rotate
    :type radians: float
    :param origin: the point to rotate around, defaults to (0,0)
    :returns: the rotated point
    """
    x, y = xy
    offset_x, offset_y = origin
    adjusted_x = (x - offset_x)
    adjusted_y = (y - offset_y)
    cos_rad = math.cos(radians)
    sin_rad = math.sin(radians)
    qx = offset_x + cos_rad * adjusted_x + sin_rad * adjusted_y
    qy = offset_y + -sin_rad * adjusted_x + cos_rad * adjusted_y

    return qx, qy