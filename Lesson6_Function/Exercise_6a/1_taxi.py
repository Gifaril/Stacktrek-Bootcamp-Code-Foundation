
def taxi(distance):
    if distance > 140:
        add = (distance / 140) * 0.25
        add2 = add + 4
        return  (format (add2, ".2f"))
    return  (format (4, ".2f"))



