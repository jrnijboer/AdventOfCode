using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace AdventOfCode
{
    partial class Program
    {
        static void Day20a()
        {          
            int presentTarget = 33100000;
            int presentsA = 0;
            int presentsB = 0;
            int house = 1;
            bool foundA = false, foundB = false;

            while ((presentsA < presentTarget || presentsB < presentTarget) && !(foundA && foundB))
            {
                if (!foundA)
                {
                    presentsA = GetPresentsAtHouse(house);
                    if (presentsA >= presentTarget)
                    {
                        foundA = true;
                        Console.WriteLine("Question A: First house to receive the number of presents = {0}", house);
                    }
                }

                if (!foundB)
                {
                    presentsB = GetPresentsAtHouse2(house);
                    if (presentsB >= presentTarget)
                    {
                        foundB = true;
                        Console.WriteLine("Question B: First house to receive the number of presents = {0}", house);
                    }
                }
                house++;
            }            
        }

        static int GetPresentsAtHouse(int house)
        {
            int visits = 0;
            int stop = (int)Math.Sqrt(house) + 1;
            for (int i = 1; i <= stop; i++)
            {
                if (house % i == 0)
                    visits += i + (house / i);
            }
            //           Console.WriteLine("Delivered {0} presents at house {1}", sum * 10, house);
            return visits * 10;
        }

        static int GetPresentsAtHouse2(int house)
        {
            int visits = 0;
            int stop = (int)Math.Sqrt(house) + 1;
            for (int i = 1; i <= stop; i++)
            {
                if (house % i == 0)
                {
                    if (house / i <= 50)
                    {
                        visits += i;
                    }
                    if (i <= 50)
                        visits += house / i;                    
                }

            }
            //           Console.WriteLine("Delivered {0} presents at house {1}", sum * 10, house);
            return visits * 11;
        }
    }
}