
x = [1, -4, -7, -6]
y = [1, -3, -6, -8]

#y = x
m1 = 1
b1 = 0

#y = 0.5x + 1
m2 = 0.5
b2 = 1
# We have three points, (1, 5), (2, 1), and (3, 3). We are trying to find a line that produces lowest loss.
# We have provided you the list of x-values, x, and y-values, y, for these points.
# Find the y-values that the line with weights m1 and
# b1 would predict for the x-values given. Store these in a list called y_predicted1.
y_predicted1 = [x_value * m1 + b1 for x_value in  x ]

# Find the y values that the line with weights m2 and
# b2 would predict for the x-values given. Store these in a list called y_predicted2.
y_predicted2 = [x_value * m2 + b2 for x_value in x]


# Create a variable called total_loss1 and set it equal to zero.
# Then, find the sum of the squared distance between the
# actual y-values of the points and the y_predicted1 values by looping through the list:
# Calculating the difference between y and y_predicted1
# Squaring the difference
# Adding it to total_loss1

total_loss1 = 0
total_loss2 = 0
for i in range(len(y)):
  total_loss1 += (y[i] - y_predicted1[i])**2

# Create a variable called total_loss2 and set it equal to zero.
# Then, find the sum of the squared distance between the
# actual y-values of the points and the y_predicted1 values by looping through the list:
# Calculating the difference between y and y_predicted2
# Squaring the difference
# Adding it to total_loss2

for i in range(len(y)):
  total_loss2 += (y[i] - y_predicted2[i])**2


# Print out total_loss1 and total_loss2.
# Out of these two lines, which would you use to model the points?
# Create a variable called better_fit and
# assign it to 1 if line 1 fits the data better and 2 if line 2 fits the data better.
print(total_loss1, total_loss2)
better_fit = 2