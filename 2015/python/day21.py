from itertools import combinations
lines = [line.strip() for line in open("../2015/input/day21.input", encoding="utf-8").readlines()]
bossHitpoints = int(lines[0].split(": ")[1])
bossDamage = int(lines[1].split(": ")[1])
bossArmor = int(lines[2].split(": ")[1])

Weapons = {"Dagger": (8, 4, 0), "Shortsword": (10, 5, 0), "Warhammer": (25, 6, 0), "Longsword": (40, 7, 0), "Greataxe": (74, 8, 0)}
Armors = {"None": (0, 0, 0), "Leather": (13, 0, 1), "Chainmail": (31, 0, 2), "Splintmail": (53, 0, 3), "Bandedmail": (75, 0, 4), "Platemail": (102, 0, 6)}
Rings = {"None": (0, 0, 0), "Damage +1": (25, 1, 0), "Damage +2": (50, 2, 0), "Damage +3": (100, 3, 0), "Defense +1": (20, 0, 1), "Defense +2": (40, 0, 2), "Defense +3": (80, 0, 3)}

RingCombos = [list(ringcombo) for ringcombo in combinations(Rings.items(), 2)] + [[("None", (0, 0, 0))]]

def Battle(weaponStats, armorStats, rings, bossHitpoints):
    playerHealth = 100
    damage = weaponStats[1]
    armor = armorStats[2]
    bossHealth = bossHitpoints
    for ring in rings:
        armor += ring[1][2]
        damage += ring[1][1]
    while True:
        bossHitpoints -= max(1, damage - bossArmor)
        if bossHitpoints <= 0:
            return True
        playerHealth -= max(1, bossDamage - armor)
        if playerHealth <= 0:
            return False

wins, losses = [], []
for weaponName, weaponStats in Weapons.items():
    for armorName, armorStats in Armors.items():
        for ringcombo in RingCombos:
            cost = weaponStats[0] + armorStats[0] + sum([v[0] for _, v in ringcombo])
            if Battle(weaponStats, armorStats, ringcombo, bossHitpoints):
                wins.append(cost)
            else:
                losses.append(cost)

print("Answer A:", min(wins))
print("Answer B:", max(losses))
