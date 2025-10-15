import farm

def plant_maze():
    farm.reset_pos()
    plant(Entities.Bush)
    n_substance = get_world_size() * num_unlocked(Unlocks.Mazes)
    use_item(Items.Weird_Substance, n_substance)
