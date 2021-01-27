import math
pi = math.pi

def find_volume_sphere(radius) :
    volume = 4*pi*radius**3/3
    return volume
def find_volume_cube(side):
    volume = side**3
    return volume


gum_ball_radius = (input("Enter the gum ball radius (in.) => "))

print(gum_ball_radius)
weekly_sales = int((input("Enter the weekly sales => ")))
print(weekly_sales)
print()
gum_ball_radius=float(gum_ball_radius)
total_sales = math.ceil(weekly_sales * 1.25)
balls_each_edge =math.ceil( total_sales**(1/3))
total_edge_length = gum_ball_radius*2*balls_each_edge
extra_sales = balls_each_edge**3-total_sales
volume_ball = find_volume_sphere(gum_ball_radius)
volume_target_balls = volume_ball*total_sales
volume_all_balls = volume_ball*balls_each_edge**3
volume_box = find_volume_cube(total_edge_length)
wasted_space_target = volume_box- volume_target_balls
wasted_space = volume_box - volume_all_balls

print("The machine needs to hold" ,balls_each_edge, "gum balls along each edge.")
print("Total edge length is {:.2f} inches.".format(total_edge_length))
print("Target sales were {0}, but the machine will hold {1} extra gum balls.".format(total_sales,extra_sales))
print("Wasted space is {0:.2f} cubic inches with the target number of gum balls,\nor {1:.2f} cubic inches if you fill up the machine.".format(wasted_space_target,wasted_space))