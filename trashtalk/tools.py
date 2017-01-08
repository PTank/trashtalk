

def human_readable_from_bytes(num):
    if not num or type(num) is str:
        return num
    for unit in ['', 'K', 'M', 'G', 'T', 'P', 'E', 'Z']:
        if abs(num) < 1024:
            return ("%.2f" % num).rstrip('0').rstrip('.') + unit
        num /= 1024.0

    return ("%.2f" % num).rstrip('0').rstrip('.') + 'Y'
