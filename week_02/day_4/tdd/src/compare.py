def compare(num1, num2):
    num1_touse = int(num1)
    num2_touse = int(num2)

    if num1_touse > num2_touse:
        return f"{num1_touse} is greater than {num2_touse}"
    if num1_touse < num2_touse:
        return f"{num1_touse} is less than {num2_touse}"
    if num1_touse == num2_touse:
        return f"{num1_touse} is equal to {num2_touse}"