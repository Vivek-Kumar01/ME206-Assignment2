import math


R = 30  # in mi
theta = 60  # in deg
phi = 12  # in deg
u = 800  # in mi/hr
v = 2500  # in mi/hr
B_coor = (20, 50, 10)  # in mi

theta = theta * math.pi / 180
phi = phi * math.pi / 180


def calc_rel_speed(B_coor, R, theta, phi, u, v):
    rel_x = B_coor[0] - (R*math.cos(phi)*math.cos(theta))
    rel_y = B_coor[1] - (R*math.cos(phi)*math.sin(theta))
    rel_z = B_coor[2] - (R*math.sin(phi))

    rel_dist = pow(pow(rel_x, 2) + pow(rel_y, 2) + pow(rel_z, 2), 0.5)

    rel_vel_x = -v*rel_x/rel_dist
    rel_vel_y = u - (v*rel_y/rel_dist)
    rel_vel_z = -v*(rel_z/rel_dist)

    rel_speed = pow(pow(rel_vel_x, 2) + pow(rel_vel_y, 2) + pow(rel_vel_z, 2), 0.5)

    return rel_speed


rel_speed = calc_rel_speed(B_coor, R, theta, phi, u, v)
# rel_speed = rel_speed * 1609/3600 (for value in m/s)

print()
print(f'Relative speed (rate of decrease of distance between B and A) is {rel_speed} mi/hr.')