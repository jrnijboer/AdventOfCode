using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Text;
using System.Text.RegularExpressions;
using System.Threading.Tasks;

namespace AdventOfCode
{
    partial class Program
    {

        static void Day15b()
        {
            var ingredients = new List<Tuple<int, int, int, int, int>>();
            var inputIngredients = File.ReadAllLines("input/day15.input");
            foreach (var ingredient in inputIngredients)
            {
                var match = Regex.Match(ingredient, @"^(\w+): capacity (-?\d+), durability (-?\d), flavor (-?\d+), texture (-?\d+), calories (-?\d+)$");
                ingredients.Add(new Tuple<int, int, int, int, int>(int.Parse(match.Groups[2].Value), int.Parse(match.Groups[3].Value), int.Parse(match.Groups[4].Value), int.Parse(match.Groups[5].Value), int.Parse(match.Groups[6].Value)));
            }

            long maxScore = 0;

            for (int i = 0; i <= 100; i++)
            {
                for (int j = 0; j <= 100; j++)
                {
                    if (i + j > 100)
                        break;
                    for (int k = 0; k <= 100; k++)
                    {
                        if (i + j + k > 100)
                            break;
                        int l = Math.Max(0, 100 - (i + j + k));

                        long capacity = Math.Max(0, (i * ingredients[0].Item1) + (j * ingredients[1].Item1) + (k * ingredients[2].Item1) + (l * ingredients[3].Item1));
                        long durability = Math.Max(0, (i * ingredients[0].Item2) + j * ingredients[1].Item2 + k * ingredients[2].Item2 + l * ingredients[3].Item2);
                        long flavor = Math.Max(0, (i * ingredients[0].Item3) + j * ingredients[1].Item3 + k * ingredients[2].Item3 + l * ingredients[3].Item3);
                        long texture = Math.Max(0, (i * ingredients[0].Item4) + j * ingredients[1].Item4 + k * ingredients[2].Item4 + l * ingredients[3].Item4);
                        long calories = Math.Max(0, (i * ingredients[0].Item5) + j * ingredients[1].Item5 + k * ingredients[2].Item5 + l * ingredients[3].Item5);
                        if (calories != 500)
                            continue;
                        long score = capacity * durability * flavor * texture;
                        Console.WriteLine("{0}, {1}, {2}, {3}, {4}", score, i, j, k, l);
                        if (score > maxScore)
                        {                            
                            maxScore = score;
                        }

                    }
                }
            }
            Console.WriteLine("The best recipe has a total score of {0}", maxScore);
        }

        static void Day15a()
        {
            //Frosting: capacity 4, durability -2, flavor 0, texture 0, calories 5
            var ingredients = new List<Tuple<int, int, int, int, int>>();
            var inputIngredients = File.ReadAllLines("input/day15.input");
            foreach (var ingredient in inputIngredients)
            {
                var match = Regex.Match(ingredient, @"^(\w+): capacity (-?\d+), durability (-?\d), flavor (-?\d+), texture (-?\d+), calories (-?\d+)$");
                ingredients.Add(new Tuple<int, int, int, int, int>(int.Parse(match.Groups[2].Value), int.Parse(match.Groups[3].Value), int.Parse(match.Groups[4].Value), int.Parse(match.Groups[5].Value), int.Parse(match.Groups[6].Value)));
            }

            long maxScore = 0;

            for (int i = 0; i <= 100; i++)
            {
                for (int j = 0; j <= 100; j++)
                {
                    if (i + j > 100)
                        break;
                    for (int k = 0; k <= 100; k++)
                    {
                        if (i + j + k > 100)
                            break;
                        int l = Math.Max(0, 100 - (i + j + k));

                        long capacity = Math.Max(0, (i * ingredients[0].Item1) + (j * ingredients[1].Item1) + (k * ingredients[2].Item1) + (l * ingredients[3].Item1));
                        long durability = Math.Max(0, (i * ingredients[0].Item2) + j * ingredients[1].Item2 + k * ingredients[2].Item2 + l * ingredients[3].Item2);
                        long flavor = Math.Max(0, (i * ingredients[0].Item3) + j * ingredients[1].Item3 + k * ingredients[2].Item3 + l * ingredients[3].Item3);
                        long texture = Math.Max(0, (i * ingredients[0].Item4) + j * ingredients[1].Item4 + k * ingredients[2].Item4 + l * ingredients[3].Item4);
                        long score = capacity * durability * flavor * texture;
                        if (score > maxScore)
                            maxScore = score;


                    }
                }
            }
            Console.WriteLine("The best recipe has a total score of {0}", maxScore);
        }
    }
}
