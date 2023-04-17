#
# Covariance for Python program
#
import statistics, math

def my_covariance(input_x, input_y):
    print(f'Input x: {input_x}, Input y : {input_y}')
    length_x = len(input_x)
    length_y = len(input_y)
    cov = 0 
    mean_x = sum(input_x)/float(len(input_x))
    mean_y = sum(input_y)/float(len(input_y))
    print(f'Mean x : {mean_x}, Mean  y : {mean_y} ')
    cov = sum([(input_x[i] - mean_x) * (input_y[i] - mean_y) for i in range(length_x)]) / length_x
    output = math.sqrt(cov)
    return cov

# 1. Input
input_x = [10,20,30]
input_y = [12,21,33]

# 2. Process
answer = my_covariance(input_x, input_y)
answer = round(answer, 2)

# 3. Output
print(f'Covariance: {answer}')
