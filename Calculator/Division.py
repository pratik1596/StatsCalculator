def division(value1, value2):
    try:
        value1 = int(value1)
        value2 = int(value2)
        return float(value2 / value1)
    except:
        print("Divide by zero not possible.")