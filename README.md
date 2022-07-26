# PythonExcercise

Python Exercise Requirements:

Given a 2D room and a set of line segments each described by two 2D points:

Write a function which returns the line segment closest to a given point (origin) in a given direction (angle in degrees).
Identify all relevant test cases and write unit tests for them.
Add type hints to all your functions and variables


# Files Included:
  * ex5.py: This is the main python file where the excercise has been solved.
  * test_dist.py: This is the test file for the function defined in ex5.py.
  
# Approach:
  A mathematical approach is being followed wherein we are computing the point of intersection of the line segment given as two cartesian coordinate points and the   line from the origin in the direction given(angle in degrees).
  From this point of intersection, we are calculating the distance of the line segment from the origin to the point of intersection.
  This is being repeated for all of the line segments and we are giving the minimum distance as the output.
  
# Assumption:
  The coordinates of the line segments  are being given in the main file. The point from which the direction is calculated is the origin (0,0).
  The direction is obtained from the user as the angle in degrees.
  
# Function Flow:
  * The input angle direction is obtained from the user in degrees.
  * A loop is executed to iterate over each of the line segments.
  * Each line segment denoted by two sets of points(x,y) is being passed to the function line_from_points(point1, point2).
  * The function forms a line using the slope intercept form of a line, here the slope is tan(angle) and we are computing the intercept using y= mx + c
  * The point of intersection of the line segment and line from origin with slope tan(angle) is determined.
  * The function checks if the point of interesection lies in the line segment and if so returns this line segment and distance.
  * Edge cases where the line segments are parallel to x-axis and y-axis are also checked.
  
  * The return values of the function is stored and filtered for None values and the minimum distance is computed using math.dist function.
  * The line segment with the minimum distance to the origin in a given direction is returned.
  
  * Test cases for the lines_from_points function is executed using different input angle values.
  

  
