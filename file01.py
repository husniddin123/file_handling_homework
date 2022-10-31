from re import X


def main(data:str):
    """
    The data is from the file. Return data as a list type.
    Args:
        data: str
    Returns:
        list: return answer
    """
    x = data.split(',')

    return x 



# Read data from file

print(main('1,2,3,4,5,6,7'))
