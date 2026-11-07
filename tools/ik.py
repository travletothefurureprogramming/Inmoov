import math

def z(f, real_W, pixel_w):
    return (f * real_W) / pixel_w

def x_y(resolution, x_center, y_center, Z, f):
    camera_x = resolution[0] / 2
    camera_y = resolution[1] / 2

    X = ((camera_x - x_center) * Z) / f 
    Y = ((camera_y - y_center) * Z) / f

    return X, Y

def theta_2(X, Y, L1, L2):
    return math.acos((X**2 + Y**2 - L1**2 - L2**2) / (2*L1*L2))

def theta_1(X, Y, L1, L2, theta2):
    return math.atan2(Y, X) - math.atan2(L2 * math.sin(theta2), L1 + L2 * math.cos(theta2))

def ik(X, Y, L1, L2):
    return math.degrees(theta_1(X, Y, L1, L2, theta_2(X, Y, L1, L2))), math.degrees(theta_2(X, Y, L1, L2))