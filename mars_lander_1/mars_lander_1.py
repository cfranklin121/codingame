import sys
import math

surface_n = int(input())  # the number of points used to draw the surface of Mars.
for i in range(surface_n):
    # land_x: X coordinate of a surface point. (0 to 6999)
    # land_y: Y coordinate of a surface point. By linking all the points together in a sequential fashion, you form the surface of Mars.
    land_x, land_y = [int(j) for j in input().split()]
    

# game loop
while True:
    # h_speed: the horizontal speed (in m/s), can be negative.
    # v_speed: the vertical speed (in m/s), can be negative.
    # fuel: the quantity of remaining fuel in liters.
    # rotate: the rotation angle in degrees (-90 to 90).
    # power: the thrust power (0 to 4).
    x, y, h_speed, v_speed, fuel, rotate, power = [int(i) for i in input().split()]

    if y >= 2000 and v_speed > -45:
        print("0 0")

    else:
        if v_speed >= -10:
            print("0 0")

        if v_speed >= -20 and v_speed < -10:
            print("0 1")

        if v_speed >= -30 and v_speed < -20:
            print("0 2")

        if v_speed >= -35 and v_speed < -30:
            print("0 3")

        if v_speed < -35:
            print("0 4")
