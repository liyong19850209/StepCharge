#     A
#    / \
#   B   C
#  / \   \
# D   E   F
class Node:
    def __init__(self,left,right,value):
        self.left = left
        self.right = right
        self.value = value
def travel_ver0(x):
    if x.left and x.right:
        print x.value
        travel_ver0(x.left)
        travel_ver0(x.right)
    elif x.left and not x.right:
        print x.value
        travel_ver0(x.left)
    elif not x.left and x.right:
        print x.value
        travel_ver0(x.right)
    else:
        print x.value
def travel_ver1(x):
    print x.value
    if x.left and x.right:
        travel_ver1(x.left)
        travel_ver1(x.right)
    elif x.left and not x.right:
        travel_ver1(x.left)
    elif not x.left and x.right:
        travel_ver1(x.right)
################################################
# L&R NULL
#      #############              ############
#     #             ##############            #
#     #             #           #              #
#    # L not Null  # L&R not Null#  R not Null #
#     # R Null     #            #    L Null    #
#     #            ##############              #
#      ############              ##############
#
################################################
def travel_ver2(x):
    print x.value
    if x.left:
        travel_ver2(x.left)
    if x.right:
        travel_ver2(x.right)
if __name__ == "__main__":
    D = Node(None,None,"D")
    E = Node(None,None,"E")
    F = Node(None,None,"F")
    B = Node(D,E,"B")
    C = Node(None,F,"C")
    A = Node(B,C,"A")
    travel_ver0(A)
    travel_ver1(A)
    travel_ver2(A)
