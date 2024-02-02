##############################
# APS106 Winter 2024 - lab2  #
# Circle overlap             #
##############################

def circle_overlap(circ1_centre_x, circ1_centre_y, circ1_radius, circ2_centre_x, circ2_centre_y, circ2_radius):

    centre_distances = ((circ1_centre_x - circ2_centre_x) ** 2 + (circ1_centre_y - circ2_centre_y) ** 2) ** 0.5
    radius_sum = circ1_radius + circ2_radius

    if circ1_radius == circ2_radius and centre_distances == 0:
        return 'identical circles'
    elif radius_sum < centre_distances:
        return 'no overlap'
    elif centre_distances+circ1_radius < circ2_radius:
        return 'circle 1 is contained within circle 2'
    elif centre_distances+circ2_radius < circ1_radius:
        return 'circle 2 is contained within circle 1'
    else:
        return 'circles overlap'
