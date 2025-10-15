import watering

def cycle(entity):
    watering.smart_water(entity)
    cost = get_cost(entity)
    enough = True

    if cost != None:
        for item in cost:
            if num_items(item) < cost[item]:
                enough = False
                break

    if not enough:
        if num_items(Items.Hay) < 32:
            plant(Entities.Grass)
        elif num_items(Items.Wood) < 32:
            plant(Entities.Bush)
        else:
            plant(Entities.Carrot)
    else:
        if can_harvest():
            harvest()
        plant(entity)
