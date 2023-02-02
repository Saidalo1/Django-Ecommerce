def split_to_4_parts(lst, sz):
    return [lst[i:i + sz] for i in range(0, len(lst), sz)]
