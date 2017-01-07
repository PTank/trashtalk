

def human_readable_from_bytes(num):
    
    if type(num) is not int:
        return num
    for unit in ['', 'K', 'M', 'G', 'T', 'P', 'E', 'Z']:
        if abs(num) < 1024:
            return ("%.2f%s" % (num, unit)).rstrip('0').rstrip('.')
        num /= 1024.0

    return ("%.2f%s" % (num, unit)).rstrip('0').rstrip('.')
