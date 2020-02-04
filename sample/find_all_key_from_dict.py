def collect_key(json_data):
    if isinstance(json_data, dict):
        base = []
        base.extend(json_data.keys())
        for key in json_data:
            if collect_key(json_data[key]):
                base.extend(collect_key(json_data[key]))
        return base
    if isinstance(json_data, list):
        base = []
        for i in json_data:
            if isinstance(i, dict):
                base.extend(collect_key(i))
            elif isinstance(i, list):
                base.extend(collect_key(i))
            else:
                pass
        if not base:
            return 
        return base
    else:
        return 