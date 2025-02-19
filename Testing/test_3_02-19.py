def volume_cyclinder(height, radius):
    pi = 3.141592653589
    volume = pi * radius ** 2 * height
    return volume
#end function for the calculation of volume of a cylinder here

can_radius = 1.5
can_height = 6
#defining the cylinder dimensions

can_volume = volume_cyclinder(can_height, can_radius)
#saves this info to a variable

print(can_volume)
#displays the value of the defined variable on line 11


