using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace AdventOfCode
{
    partial class Program
    {
        static int magicbossDamage = 9;
        static int minSpentMana = int.MaxValue;
        static List<Spell> magicSpells = new List<Spell>
        {
            new Spell {name = "Poison", cost = 173, damage = 3, healing = 0, armor = 0, turnsLeft = 6, mana = 0 },
            new Spell {name = "Recharge", cost = 229, damage = 0, healing = 0, armor = 0, turnsLeft = 5, mana = 101 },
            new Spell {name = "Shield", cost = 113, damage = 0, healing = 0, armor = 7, turnsLeft = 6, mana = 0 },
            new Spell {name = "MagicMissile", cost = 53, damage = 4, healing = 0, armor = 0, turnsLeft = 1, mana = 0 },
            new Spell {name = "Drain", cost = 73, damage = 2, healing = 2, armor = 0, turnsLeft = 1, mana = 0 },
        };

        static void Day22a()
        {
            int availableMana = 500;
            int hitpoints = 50;
            int magicbossHitpoints = 51;
            var castSpells = new List<Spell>();
            DoBattleTurn(availableMana, hitpoints, magicbossHitpoints, castSpells, 0);
        }

        static void Day22b()
        {
            int availableMana = 500;
            int hitpoints = 50;
            int magicbossHitpoints = 51;
            var castSpells = new List<Spell>();
            DoBattleTurn(availableMana, hitpoints, magicbossHitpoints, castSpells, 1);
        }

        private static void DoBattleTurn(int availableMana, int hitpoints, int bossHitpointsLeft, List<Spell> castSpells, int extraDamage)
        {
            foreach (var spell in magicSpells.ToList())
            {
                var newCastSpells = cloneSpellList(castSpells);
                int spentMana = newCastSpells.Sum(s => s.cost);
                if (spell.cost > availableMana || spentMana + spell.cost >= minSpentMana)
                    continue;

                int newPlayerArmor = 0;
                int newAvailableMana = availableMana;
                int newHitpoints = hitpoints - extraDamage;
                int newBossHitpointsLeft = bossHitpointsLeft;

                //player health controle
                if (newHitpoints < 1)
                {
                    continue;
                }

                var newActiveSpells = newCastSpells.Where(s => s.turnsLeft > 0).ToList();

                handleActiveSpells(newActiveSpells, ref newHitpoints, ref newAvailableMana, ref newBossHitpointsLeft, ref newPlayerArmor);

                if (newActiveSpells.Any(s => s.turnsLeft == 0))
                    throw new Exception("inactive spell found");

                if (newBossHitpointsLeft < 1)
                {
                    Console.WriteLine("Boss died: spent {0} mana, spells cast:", spentMana);
                    newCastSpells.ForEach(s => Console.Write(s.name.Substring(0, 2) + ", "));
                    Console.WriteLine();
                    if (spentMana < minSpentMana)
                        minSpentMana = spentMana;
                    continue;
                }

                //check of spell niet nog actief is
                if (!newActiveSpells.Any(s => s.name == spell.name))
                {
                    newCastSpells.Add(new Spell
                    {
                        armor = spell.armor,
                        cost = spell.cost,
                        damage = spell.damage,
                        healing = spell.healing,
                        mana = spell.mana,
                        name = spell.name,
                        turnsLeft = spell.turnsLeft
                    });

                    newActiveSpells = newCastSpells.Where(s => s.turnsLeft > 0).ToList();

                    newAvailableMana -= spell.cost;
                    spentMana += spell.cost;

                    //Enemy turn
                    newHitpoints -= extraDamage;
                    handleActiveSpells(newActiveSpells, ref newHitpoints, ref newAvailableMana, ref newBossHitpointsLeft, ref newPlayerArmor);
                    if (newBossHitpointsLeft < 1)
                    {
                        Console.WriteLine("Boss died: spent {0} mana, spells cast:", spentMana);
                        newCastSpells.ForEach(s => Console.Write(s.name.Substring(0, 2) + ", "));
                        Console.WriteLine();
                        if (spentMana < minSpentMana)
                            minSpentMana = spentMana;
                        continue;
                    }

                    //boss damage afhandelen
                    int damage = Math.Max(1, magicbossDamage - newPlayerArmor);
                    newHitpoints -= damage;

                    //player health controle
                    if (newHitpoints < 1)
                    {
                        continue;
                    }

                    DoBattleTurn(newAvailableMana, newHitpoints, newBossHitpointsLeft, newCastSpells, extraDamage);
                }
            }
        }

        private static List<Spell> cloneSpellList(List<Spell> activeSpells)
        {
            List<Spell> newList = new List<Spell>();
            newList = activeSpells.Select(s => new Spell
            {
                armor = s.armor,
                cost = s.cost,
                damage = s.damage,
                healing = s.healing,
                mana = s.mana,
                name = s.name,
                turnsLeft = s.turnsLeft
            }).ToList();

            return newList;
        }

        private static List<Spell> handleActiveSpells(List<Spell> activeSpells, ref int newPlayerHitpoints, ref int newMana, ref int newBossHitpoints, ref int armor)
        {
            if (activeSpells.Any(s => s.turnsLeft <= 0))
                throw new Exception("inactive spell found");
            foreach (var spell in activeSpells.ToList())
            {
                newBossHitpoints -= spell.damage;
                newMana += spell.mana;
                newPlayerHitpoints += spell.healing;
                spell.turnsLeft--;
                armor = Math.Max(armor, spell.armor);
                if (spell.turnsLeft == 0)
                    activeSpells.Remove(spell);
            }
            return activeSpells;
        }

        public class Spell
        {
            public string name { get; set; }
            public int cost { get; set; }
            public int damage { get; set; }
            public int healing { get; set; }
            public int armor { get; set; }
            public int turnsLeft { get; set; }
            public int mana { get; set; }
        }
    }
}