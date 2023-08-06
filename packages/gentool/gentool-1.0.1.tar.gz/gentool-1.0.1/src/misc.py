
def log_num(lower_limit, upper_limit=0):
    try:
        low = int(lower_limit)
        if(upper_limit):
            high = int(upper_limit)
            for i in range(low, high+1):
               print(i)
        else:
            for i in range(low+1):
                print(i)
    except:
        return None
