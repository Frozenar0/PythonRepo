def count_sheeps(sheepHerd):
    sheepCount=0
    for sheep in sheepHerd:
        if sheep is True:
            sheepCount = sheepCount+1
        else:
            continue
    return sheepCount