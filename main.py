from vision.tracker import find_object
from tools import ik

L1 = 15.0
L2 = 15.0
PING_PONG_W = 4.0

f = 650

cls_name = input("Enter object name to find: ")

x_center, y_center, pixel_w = find_object(cls_name)

if x_center is not None:
    print(f"Συντεταγμένες: X={x_center}, Y={y_center}, Width={pixel_w}")
else:
    print("Η μπάλα δεν βρέθηκε σε αυτό το καρέ.")

if pixel_w is not None:
    Z = ik.z(f, PING_PONG_W, pixel_w)
    X, Y = ik.x_y([640, 480], x_center, y_center, Z, f)


    shoulder_degrees, elbow_degrees = ik.ik(X, Y, L1, L2)
    print("shoulder_degrees: ", shoulder_degrees, "elbow_degrees: ", elbow_degrees)