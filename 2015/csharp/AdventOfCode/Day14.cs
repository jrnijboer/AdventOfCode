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
        static void Day14b()
        {
            Dictionary<string, Tuple<int, int, int>> reindeers = new Dictionary<string, Tuple<int, int, int>>();
            var input = File.ReadAllLines("input/day14.input").ToList();

            string fastestReindeer = "";
            foreach (var reindeerProps in input)
            {
                var match = Regex.Match(reindeerProps, @"^(\w+) can fly (\d+) km/s for (\d+) seconds, but then must rest for (\d+) seconds\.$");
                reindeers[match.Groups[1].Value] = new Tuple<int, int, int>(int.Parse(match.Groups[2].Value), int.Parse(match.Groups[3].Value), int.Parse(match.Groups[4].Value));
            }

            int seconds = 1;

            Dictionary<string, int> reindeerPoints = new Dictionary<string, int>();
            Dictionary<string, int> reindeerDistance = new Dictionary<string, int>();
            foreach (var reindeer in reindeers)
            {
                reindeerPoints[reindeer.Key] = 0;
                reindeerDistance[reindeer.Key] = 0;
            }

            //blah, shlemiel the painter vv
            while (seconds <= 2503)
            {

                int maxDistance = 0;
                foreach (var reindeer in reindeers)
                {
                    int distance = getDistance(reindeer.Value, seconds);
                    reindeerDistance[reindeer.Key] = distance;
                    if (distance > maxDistance)
                        maxDistance = distance;

                }
                foreach (var key in reindeerDistance.Keys)
                {
                    if (reindeerDistance[key] == maxDistance)
                        reindeerPoints[key] += 1;
                }
                seconds++;
            }
            int maxpoints = 0;

            foreach (var key in reindeerPoints.Keys)
            {
                if (reindeerPoints[key] > maxpoints)
                {
                    maxpoints = reindeerPoints[key];
                    fastestReindeer = key;
                }
            }

            Console.WriteLine("The reindeer with most points is {0}, total points: {1}", fastestReindeer, maxpoints);
        }

        static void Day14a()
        {
            Dictionary<string, Tuple<int, int, int>> reindeers = new Dictionary<string, Tuple<int, int, int>>();
            var input = File.ReadAllLines("input/day14.input");
            int max = 0;
            string fastestReindeer = "";
            foreach (var reindeerProps in input)
            {
                var match = Regex.Match(reindeerProps, @"^(\w+) can fly (\d+) km/s for (\d+) seconds, but then must rest for (\d+) seconds\.$");
                reindeers[match.Groups[1].Value] = new Tuple<int, int, int>(int.Parse(match.Groups[2].Value), int.Parse(match.Groups[3].Value), int.Parse(match.Groups[4].Value));
            }
            foreach (var reindeer in reindeers)
            {
                int distance = getDistance(reindeer.Value, 2503);
                if (distance > max)
                {
                    max = distance;
                    fastestReindeer = reindeer.Key;
                }
            }

            Console.WriteLine("The fastest reindeer is {0}, distance traveled: {1}", fastestReindeer, max);
        }

        private static int getDistance(Tuple<int, int, int> value, int seconds)
        {
            int distance = 0;
            while (seconds >= value.Item2 + value.Item3)
            {
                distance += value.Item1 * value.Item2;
                seconds -= (value.Item2 + value.Item3);
            }

            distance += Math.Min(seconds, value.Item2) * value.Item1;

            return distance;
        }
    }
}
