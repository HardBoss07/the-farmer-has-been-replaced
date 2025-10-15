def smart_water(entity):
    # Water once if soil is dry
    while get_water() < 0.5:
        use_item(Items.Water)
