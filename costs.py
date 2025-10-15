# Map each crop entity to its cost and what it produces
# Format:
#   costs[Entity] = {"cost": {Items.X: amount, ...}, "produces": {Items.Y: amount, ...}}

costs = {
    Entities.Carrot: {
        "cost": {Items.Hay: 32, Items.Wood: 32},
        "produces": {Items.Carrot: 512}
    },
    Entities.Grass: {
        "cost": {},
        "produces": {Items.Hay: 512}
    },
    Entities.Bush: {
        "cost": {},
        "produces": {Items.Wood: 512}
    },
    Entities.Tree: {
        "cost": {},
        "produces": {Items.Wood: 2560}
    },
    Entities.Pumpkin: {
        "cost": {Items.Carrot: 256},
        "produces": {Items.Pumpkin: 256}
    },
    Entities.Sunflower: {
        "cost": {Items.Carrot: 1},
        "produces": {Items.Power: 5}
    }
}

def get_entity_info(entity):
    if entity in costs:
        return costs[entity]
    return {"cost": {}, "produces": {}}
