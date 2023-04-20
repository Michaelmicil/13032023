#
# Covariance for Python program
#
import statistics, math

def my_covariance(input_x, input_y):
    
    length= len(input_x)
    print(f'Input x: {input_x}, Input y:{input_y}')
    cov=0

    Mean_x= statistics.mean(input_x)
    Mean_y= statistics.mean(input_y)
    print(f'Mean x:{Mean_x}, Mean y:{Mean_y}')

    cov= sum([(input_x[i]-Mean_x)*(input_y[i]-Mean_y) for i in range(length)])/length
    

    return cov

# 1. Input
input_x = [10,20,30]
input_y = [12,21,33]

# 2. Process
answer = my_covariance(input_x, input_y)
answer = round(answer, 2)

# 3. Output
print(f'Covariance: {answer}')
