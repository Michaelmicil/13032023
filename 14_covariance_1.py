#
# Covariance for Python program
#
import statistics, math

def my_covariance(input_x, input_y):
    print(f'Input x:{input_x}, Input y: {input_y}')
    length_x= len(input_x)
    length_y= len(input_y)
    cov=0
    mean_x = sum(input_x)/ float(length_x)
    mean_y = sum(input_y)/ float(length_y)
    print(f'Mean x: {mean_x}, Mean y: {mean_y} ')
    cov = sum([(input_x[idx] - mean_x) * (input_y[idx] - mean_y) for idx in range(length_x)]) / length_x
    return cov

# 1. Input
input_x = [10,20,30]
input_y = [12,21,33]

# 2. Process
answer = my_covariance(input_x, input_y)
answer = round(answer, 2)

# 3. Output
print(f'Covariance: {answer}')
