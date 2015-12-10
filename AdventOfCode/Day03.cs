using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace AdventOfCode
{
    partial class Program
    {
        static void Day3b()
        {
            int xSanta = 0;
            int ySanta = 0;

            int xRobo = 0;
            int yRobo = 0;
            List<string> visitedLocations = new List<string>();

            var directions = File.ReadAllText("input/day3.input");
            int pos = 0;
            do
            {
                visitedLocations.Add(string.Format("{0},{1}", xSanta, ySanta));
                visitedLocations.Add(string.Format("{0},{1}", xRobo, yRobo));
                switch (directions[pos])
                {
                    case '^':
                        ySanta++;
                        break;
                    case '>':
                        xSanta++;
                        break;
                    case '<':
                        xSanta--;
                        break;
                    case 'v':
                        ySanta--;
                        break;
                }
                pos++;

                switch (directions[pos])
                {
                    case '^':
                        yRobo++;
                        break;
                    case '>':
                        xRobo++;
                        break;
                    case '<':
                        xRobo--;
                        break;
                    case 'v':
                        yRobo--;
                        break;
                }
                pos++;


            } while (pos < (directions.Length));
            int result = visitedLocations.Distinct().Count();

            Console.WriteLine("Santa and Robo-Santa visited {0} locations", result);
        }

        static void Day3a()
        {
            int x = 0;
            int y = 0;

            List<string> visitedLocations = new List<string>();

            var directions = File.ReadAllText("input/day3.input");
            int pos = 0;
            do
            {
                visitedLocations.Add(string.Format("{0},{1}", x, y));
                switch (directions[pos])
                {
                    case '^':
                        y++;
                        break;
                    case '>':
                        x++;
                        break;
                    case '<':
                        x--;
                        break;
                    case 'v':
                        y--;
                        break;
                }
                pos++;
            } while (pos < (directions.Length));
            int result = visitedLocations.Distinct().Count();

            Console.WriteLine("Santa visited {0} locations", result);
        }
    }
}
