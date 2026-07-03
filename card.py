class Card:
    def __init__(self, id, packid, name, hp, type, rarity, pack, count, evolution):
        self.id = id
        self.packid = packid
        self.name = name
        self.evolution = evolution
        self.hp = hp
        self.type = type
        self.rarity = rarity
        self.pack = pack
        self.count = count

        to_dict()
        # （Card → JSON）
        from_dict()
        # （JSON → Card）