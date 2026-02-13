def filter_line_segments(lines):
    def in_quad2(x1, y1, x2, y2):
        # A line segment lying on the x-axis or y-axis is not considered a
        # quad 2 line segment
        if (x1 == 0 and x2 == 0) or (y1 == 0 and y2 == 0):
            return False
        elif x1 <= 0 and y1 >= 0 and x2 <= 0 and y2 >= 0:
            return True
        else:
            return False

    quadrant2_segments = [id for id, coord1, coord2 in lines if in_quad2(*coord1, *coord2)]
    if not quadrant2_segments:
        return None

    return quadrant2_segments
