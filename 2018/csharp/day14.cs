using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;

namespace aoc2018
{
    class Day14
    {
        public static void Solve()
        {
            int input = int.Parse(File.ReadAllText(Path.Combine("..", "input", "day14.input")));
            List<int> recipes = new List<int>(25000000) { 3, 7 };
            int ix1 = 0, ix2 = 1, ix = 0, newRecipe;
            bool foundA = false;
            while (true)
            {
                newRecipe = recipes[ix1] + recipes[ix2];
                if (newRecipe >= 10)
                {
                    recipes.Add(newRecipe / 10);
                    recipes.Add(newRecipe % 10);
                    ix = recipes.Count;
                    if (foundA &&
                        recipes[ix - 2] == input % 10 &&
                        recipes[ix - 7] == input / 100000 &&
                        recipes[ix - 6] == input / 10000 % 10 &&
                        recipes[ix - 5] == input / 1000 % 10 &&
                        recipes[ix - 4] == input / 100 % 10 &&
                        recipes[ix - 3] == input / 10 % 10)
                    {
                        Console.WriteLine(recipes.Count - 7);
                        break;
                    }
                }
                else
                {
                    recipes.Add(newRecipe % 10);
                    ix = recipes.Count;
                    if (foundA &&
                        recipes[ix - 1] == input % 10 &&
                        recipes[ix - 6] == input / 100000 &&
                        recipes[ix - 5] == input / 10000 % 10 &&
                        recipes[ix - 4] == input / 1000 % 10 &&
                        recipes[ix - 3] == input / 100 % 10 &&
                        recipes[ix - 2] == input / 10 % 10)
                    {
                        Console.WriteLine(recipes.Count - 6);
                        break;
                    }
                }
                ix1 = (ix1 + 1 + recipes[ix1]) % ix;
                ix2 = (ix2 + 1 + recipes[ix2]) % ix;

                if (!foundA && recipes.Count == input + 10)
                {
                    foundA = true;
                    recipes.Skip(input).Take(10).ToList().ForEach(c => Console.Write(c));
                    Console.Write('\n');
                }
            }
        }
    }
}
