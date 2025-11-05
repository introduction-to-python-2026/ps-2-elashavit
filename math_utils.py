def find_max_number(num1, num2, num3):
    if num1 >= num2 and num1 >= num3:
      return num1
    elif num2 >= num1 and num2 >= num3:
      return num2
    return num3


def find_mean(num1, num2, num3):
 sum_numbers = (num1 + nim2 + num3)
 mean_value = sum_numbers/3
 return mean_value

def find_mean_std(num1, num2, num3):
    mean = find_mean(num1, num2, num3)
    random = (num1 - mean) ** 2 + (num2 - mean) ** 2 + (num3 - mean) **2 
    random2 = random / 3
    std = random2 ** 0.5
    return mean , std

