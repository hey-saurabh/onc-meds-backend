
def create_query(data):
    from datetime import datetime
    query = {}
    for key in data.keys():
        if not data[key]:
            continue
        if isinstance(data[key], dict):
            q = {}
            keys = list(data[key].keys())
            from_val, to_val =  data[key][keys[0]], data[key][keys[1]]
            if from_val:
                try:
                    from_val = datetime.strptime(from_val, "%Y-%m-%d %H:%M")
                except:
                    pass
                q['$gte'] = from_val
            if to_val:
                try:
                    to_val = datetime.strptime(to_val, "%Y-%m-%d %H:%M")
                except:
                    pass
                q['$lte'] = to_val
            if q:
                query[key] = q
        elif isinstance(data[key], list):
            query[key] = {'$in': data[key]}
        elif isinstance(data[key], str):
            query[key] = {"$regex": data[key], '$options': 'i'}
        else:
            query[key] = data[key]
    return query