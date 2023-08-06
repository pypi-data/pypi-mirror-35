def paginate_offset(selection, offset=0, limit=None):
    return selection[offset:(limit + offset if limit is not None else None)]

def paginate(selection, page=1, limit=None):
    offset = page*limit
    return selection[offset:(limit + offset if limit is not None and offset < len(selection) else None)]
