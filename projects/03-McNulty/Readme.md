The goal of this project was to use data from ultrasonic sensors (which measure distance) that were place around the 'waist' 
of a robot in order to classify which direction the robot should move in order to navigate clockwise around the room 
without running into walls. The direction labels were provided through the manual control of the robot. Therefore,
another consideration was to find the classifier that needed the fewest training example to do so such that the time needed to 
manually train the robot is the smallest.

3 different sets of features were used:
1) Readings from all 24 ultrasonic sensors
2) Readings from 4 zones of sensors (Left,Front,Right,Back)
3) Readings from 2 zones of sensors(Left,Front)
