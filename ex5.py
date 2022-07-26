import math

# the line segment coordinates

line1: list = [[1, -1], [1, 1]]
line2: list = [[2, -1], [2, 1]]
line3: list = [[-1, 4], [1, 4]]

lines: list = [line1, line2, line3]
distance_array: list = []
direction: int = int(input("enter angle in degrees to indicate the direction:"))


def line_from_points(point1, point2) -> tuple[list, float] | None:
    a = point2[1] - point1[1]  # y2-y1
    b = point2[0] - point1[0]  # x2-x1
    # Case where line is parallel to x-axis and angle is zero
    # or angle is 90 and line segments are parallel to y-axis
    if a == 0 and direction == 0 or (direction == 90 and b == 0):
        return
    # Case where slope of line segment is not perpendicular to y-axis
    elif b != 0:
        slope_of_line_segment = a / b
        c = point1[1] - (slope_of_line_segment * P[0])
        slope_of_line_from_origin = math.tan(math.radians(direction))
        x_intercept = round(c / (slope_of_line_from_origin - slope_of_line_segment), 2)
        y_intercept = round(slope_of_line_segment * x_intercept + c, 2)
    # Case where slope of line segment is perpendicular to y-axis
    else:
        x_intercept = point1[0]  # x1
        slope_of_line_from_origin = (math.tan(math.radians(direction)))
        y_intercept = slope_of_line_from_origin * x_intercept
    # Checking if the intercept is in the range of the line segments as it is finite
    if min(point1[0], point2[0]) <= x_intercept <= max(point1[0], point2[0]) and min(point1[1], point2[1]) <= \
            y_intercept <= max(point1[1], point2[1]):
        return [point1, point2], math.dist((0, 0), (x_intercept, y_intercept))


for line in lines:
    P, Q = line
    return_val = line_from_points(P, Q)
    distance_array.append(return_val)

distance_array = list(filter(None, distance_array))  # Filtering the None values
if len(distance_array) != 0:
    print("The line segment with the minimum distance is", min(distance_array, key=lambda t: t[1]))
else:
    print("No line segments found in that particular direction")
