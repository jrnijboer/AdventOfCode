using System;
using System.Collections.Generic;
using System.IO;

namespace day1
{
    class Program
    {
        static void Main(string[] args)
        {
            var input = File.ReadAllLines("input.txt")[0];
            var turns = input.Split(", ");
            SolveA(turns);
            SolveB(turns);
        }

        static void SolveA(string[] turns)
        {
            var direction = 0;
            var steps = new Dictionary<int, int>
            {
                [0] = 0, //n
                [1] = 0, //e
                [2] = 0, //s
                [3] = 0  //w
            };

            foreach (var turn in turns)
            {
                direction += turn[0] == 'L' ? -1 : 1;

                if (direction < 0)
                    direction += 4;
                if (direction > 3)
                    direction = 0;

                steps[direction] += int.Parse(turn.Substring(1));
            }

            var result = Math.Abs(steps[0] - steps[2] + steps[1] - steps[3]);
            Console.WriteLine("result part 1: {0}", result);
        }

        static void SolveB(string[] turns)
        {
            var direction = 0;
            var steps = new Dictionary<int, int>
            {
                [0] = 0, //n
                [1] = 0, //e
                [2] = 0, //s
                [3] = 0  //w
            };

            var visitedLocations = new HashSet<string> { "0,0" };
            var posX = 0;
            var posY = 0;
            int deltaX = 0;
            int deltaY = 0;
            bool sameLocation = false;
            var i = 0;
            while (i < turns.Length && !sameLocation)
            {
                var turn = turns[i];
                
                direction += turn[0] == 'L' ? -1 : 1;

                if (direction < 0)
                    direction += 4;
                if (direction > 3)
                    direction = 0;

                switch (direction)
                {
                    case 0:
                        deltaX = 0;
                        deltaY = 1;
                        break;
                    case 1:
                        deltaX = 1;
                        deltaY = 0;
                        break;
                    case 2:
                        deltaX = 0;
                        deltaY = -1;
                        break;
                    case 3:
                        deltaX = -1;
                        deltaY = 0;
                        break;
                }
                var stepcount = int.Parse(turn.Substring(1));
                while (stepcount > 0)
                {
                    steps[direction]++;
                    posX += deltaX;
                    posY += deltaY;
                    var location = string.Format("{0},{1}", posX, posY);
                    if (visitedLocations.Contains(location))
                    {
                        sameLocation = true;
                        break;
                    }
                    else visitedLocations.Add(location);
                    stepcount--;
                }
                i++;
            }

            var result = Math.Abs(steps[0] - steps[2] + steps[1] - steps[3]);
            Console.WriteLine("result part 2: {0}", result);            
        }
    }
}
