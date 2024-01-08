# (p5.py) Class C describes a point (x,y) in the plane. The point coordinates are given when creating (initializing) the object. The class contains the m1() method that returns the number of the quadrant of the Cartesian system in which the point (x,y) is located ( https://en.wikipedia.org/wiki/Quadrant_(plane_geometry) ). The m1() method returns 0 if the point (x,y) is located on the X-axis or Y-axis. The class contains the m2(a,b) method that returns true when the point (x,y) is in the same quadrant of the Cartesian system as the point with coordinates a,b. Otherwise, the method returns false. The class contains the m3(a,b) method that returns true when the distance between points (x,y) and (a,b) is greater than 5. Otherwise, the method returns false. Example:
# p = C(2,3)
# p.m1() -> 1
# p.m2(7,4) -> True
# p.m2(-3,1) -> False
# p.m3(8,5) -> True
# p.m3(4,7) -> False
# p1 = C(0,5)
# p1.m1() -> 0
# p1.m2(4,7) -> False
# p1.m2(-7,0) -> True
