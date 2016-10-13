using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace AdventOfCode
{
    partial class Program
    {
        static int bossHitpoints = 103;
        static int bossDamage = 9;
        static int bossArmor = 2;

        static List<Tuple<int, int, int>> Weapons = new List<Tuple<int, int, int>>
        {
            new Tuple<int, int, int>(8, 4, 0),
            new Tuple<int, int, int>(10, 5, 0),
            new Tuple<int, int, int>(25, 6, 0),
            new Tuple<int, int, int>(40, 7, 0),
            new Tuple<int, int, int>(74, 8, 0)
        };

        static List<Tuple<int, int, int>> Armor = new List<Tuple<int, int, int>>()
        {
            new Tuple<int, int, int>(0, 0, 0),
            new Tuple<int, int, int>(13, 0, 1),
            new Tuple<int, int, int>(31, 0, 2),
            new Tuple<int, int, int>(53, 0, 3),
            new Tuple<int, int, int>(75, 0, 4),
            new Tuple<int, int, int>(102, 0, 5)
        };

        static List<Tuple<int, int, int>> Rings = new List<Tuple<int, int, int>>()
        {
            new Tuple<int, int, int>(0, 0, 0),
            new Tuple<int, int, int>(25, 1, 0),
            new Tuple<int, int, int>(50, 2, 0),
            new Tuple<int, int, int>(100,3, 0),
            new Tuple<int, int, int>(20, 0, 1),
            new Tuple<int, int, int>(40, 0, 2),
            new Tuple<int, int, int>(80, 0, 3)
        };

        static void Day21b()
        {
            int maxGold = 0;
            foreach (var weapon in Weapons)
                foreach (var armor in Armor)
                    foreach (var leftRing in Rings)
                        foreach (var rightRing in Rings.Except(new List<Tuple<int, int, int>> { leftRing }).ToList())
                        {
                            if (!GetCombatResult(weapon.Item2, armor.Item3, leftRing, rightRing) && weapon.Item1 + armor.Item1 + leftRing.Item1 + rightRing.Item1 > maxGold)                            
                                maxGold = weapon.Item1 + armor.Item1 + leftRing.Item1 + rightRing.Item1;                            
                        }
                        
            Console.WriteLine("Battle can still be lost after spending {0} gold", maxGold);
        }

        static void Day21a()
        {
            int minGold = int.MaxValue;
            foreach (var weapon in Weapons)
                foreach (var armor in Armor)
                    foreach (var leftRing in Rings)
                        foreach (var rightRing in Rings.Except(new List<Tuple<int, int, int>> { leftRing }).ToList())
                        {
                            if (GetCombatResult(weapon.Item2, armor.Item3, leftRing, rightRing) && weapon.Item1 + armor.Item1 + leftRing.Item1 + rightRing.Item1 < minGold)
                                minGold = weapon.Item1 + armor.Item1 + leftRing.Item1 + rightRing.Item1;
                        }
            Console.WriteLine("Battle can be won by spending {0} gold", minGold);
        }

        private static bool GetCombatResult(int weapon, int armor, Tuple<int, int, int> leftRing, Tuple<int, int, int> rightRing, bool printBattle = false)
        {
            int bossHP = bossHitpoints;
            int playerHP = 100;
            while (true)
            {
                bossHP -= Math.Max(1, (weapon + leftRing.Item2 + rightRing.Item2) - bossArmor);                
                if (bossHP <= 0)
                    return true;

                playerHP -= Math.Max(1, bossDamage - (armor + leftRing.Item3 + rightRing.Item3));
                if (playerHP <= 0)
                    return false;
            }            
        }
    }
}