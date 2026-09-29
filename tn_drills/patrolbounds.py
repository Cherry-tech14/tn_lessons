def patrol_bounds(positions):
    rows = [p[0] for p in positions]
    cols = [p[1] for p in positions]

    return [min(rows), max(rows), min(cols), max(cols)]