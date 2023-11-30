lines = [line.strip() for line in open("../2015/input/day22.input", encoding="utf-8").readlines()]
bossHitpoints = int(lines[0].split(": ")[1])
bossDamage = int(lines[1].split(": ")[1])

actions = ["missile", "drain", "shield", "poison", "recharge"]
actionCosts = {
    "missile": 53,
    "drain": 73,
    "shield": 113,
    "poison": 173,
    "recharge": 229
}

actionDamage = {
    "missile": 4,
    "drain": 2,
    "shield": 0,
    "poison": 0,
    "recharge": 0
}

actionHeal = {
    "missile": 0,
    "drain": 2,
    "shield": 0,
    "poison": 0,
    "recharge": 0
}

actionDuration = {
    "missile": 0,
    "drain": 0,
    "shield": 6,
    "poison": 6,
    "recharge": 5
}

effects = dict()
effects["poison"] = 2
wins = []
losses = []
bossHitpoints = 4
bossDamage = 8
Q = [{"playerHP": 10, "playerMana": 250, "spentMana": 0, "bossHP": bossHitpoints, "bossDamage": bossDamage, "activeEffects": effects, "gameLog": []}]
while Q:
    # pop queue
    gamedict = Q.pop(0)

    playerHitpoints = gamedict["playerHP"]
    playerMana = gamedict["playerMana"]
    spentMana = gamedict["spentMana"]
    bossHitpoints = gamedict["bossHP"]
    bossDamage = gamedict["bossDamage"]
    activeEffects = gamedict["activeEffects"]
    gamelog = gamedict["gameLog"]
    playerArmor = 0
    turnLog = []

    # player turn
    # log info
    turnLog.append("--Player turn--")
    turnLog.append(f"-Player has {playerHitpoints} hit points, {playerArmor} armor, {playerMana} mana")
    turnLog.append(f"-Boss has {bossHitpoints} hit points")

    # handle effects
    nextEffects = dict()
    # playerArmor = 0

    for effect, duration in effects.items():
        if effect == "shield" and duration > 0:
            playerArmor = 7
            nextEffects[effect] = duration - 1

            turnLog.append(f"Shield's timer is now {duration}")
        elif effect == "poison" and duration > 0:
            bossHitpoints -= 3
            nextEffects[effect] = duration - 1

            turnLog.append(f"Poison deals 3 damage; it's timer is now {duration}")
        elif effect == "recharge" and duration > 0:
            playerMana += 101
            nextEffects[effect] = duration - 1

            turnLog.append(f"Recharge provides 101 mana; it's timer is now {duration}")

        if bossHitpoints <= 0:
            wins.append(spentMana)
            continue

    # cast
    for action in actions:
        actionlog = []

        if action in effects.keys() or actionCosts[action] > playerMana:
            continue
        actionlog.append(f"Player casts {action}")
        if action == "missile" and bossHitpoints - actionDamage[action] <= 0:
            wins.append(spentMana + actionCosts[action])
            continue
        elif action == "drain" and bossHitpoints - actionDamage[action] <= 0:
            wins.append(spentMana + actionCosts[action])
            continue
    # boss turn
    # log info

    #     if playerHitpoints + actionHeal[action] > bossDamage:
    #         actionlog.append("")
    #         actionlog.append("--Boss turn--")
    #         actionlog.append(f"-Player has {playerHitpoints} hit points, {playerArmor} armor, {playerMana} mana")
    #         actionlog.append(f"-Boss has {bossHitpoints} hit points")

    # # handle effects

    #         nextEffects = dict()
    #         for effect, duration in effects.items():
    #             if effect == "shield" and duration > 0:
    #                 playerArmor = 7
    #                 nextEffects[effect] = duration - 1
    #                 actionlog.append(f"Shield's timer is now {duration}")
    #             elif effect == "poison" and duration > 0:
    #                 bossHitpoints -= 3
    #                 nextEffects[effect] = duration - 1
    #                 actionlog.append(f"Poison deals 3 damage; it's timer is now {duration}")
    #             elif effect == "recharge" and duration > 0:
    #                 playerMana += 101
    #                 nextEffects[effect] = duration - 1
    #                 actionlog.append(f"Recharge provides 101 mana; it's timer is now {duration}")

    #         if bossHitpoints <= 0:
    #             wins.append(spentMana)
    #             continue
    #         logAppend += actionlog
    # # boss attack

    #         Q.append((playerHitpoints + actionHeal[action] - (bossDamage - playerArmor), playerMana - actionCosts[action], spentMana + actionCosts[action], bossHitpoints - actionDamage[action], bossDamage, nextEffects | {action: actionDuration[action]}, logAppend + actionlog))
    #     else:
    #         print()
    #         print("##############")
    #         print(f"DEAD")
    #         print(actionlog)
    #         print()

print(min(wins))