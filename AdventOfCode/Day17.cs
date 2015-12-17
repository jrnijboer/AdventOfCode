using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace AdventOfCode
{
    partial class Program
    {
        static int totalVolume = 150;
        static List<List<int>> combinations = new List<List<int>>();
        static List<int> containers = new List<int> { 33, 14, 18, 20, 45, 35, 16, 35, 1, 13, 18, 13, 50, 44, 48, 6, 24, 41, 30, 42 };

        static void Day17b()
        {
            GetContainerCombinations(containers, new List<int>());
            int minCount = int.MaxValue;
            int combinationsWithMinCount = 0;
            combinations.ForEach(combination =>
            {
                if (combination.Count < minCount)
                {
                    minCount = combination.Count;
                    combinationsWithMinCount = 1;
                }
                else if (combination.Count == minCount)
                    combinationsWithMinCount++;
            });
            Console.WriteLine("There are {0} possible combinations with a minimum count of {1} containers", combinationsWithMinCount, minCount);
        }

        static void Day17a()
        {
            GetContainerCombinations(containers, new List<int>());
            Console.WriteLine("There are {0} possible combinations with the containers", combinations.Count);
        }

        static void GetContainerCombinations(List<int> availableContainers, List<int> usedContainers)
        {
            int currentVolume = usedContainers.Sum();

            if (currentVolume == totalVolume)
            {
                combinations.Add(usedContainers);
            }
            else
            {
                var newAvailableContainers = availableContainers.Select(c => c).ToList();

                while (newAvailableContainers.Count > 0 && newAvailableContainers[0] + currentVolume > totalVolume)
                    newAvailableContainers.RemoveAt(0);

                while (newAvailableContainers.Count > 0)
                {
                    var newUsedContainers = usedContainers.Select(c => c).ToList();
                    newUsedContainers.Add(newAvailableContainers[0]);
                    newAvailableContainers.RemoveAt(0);
                    GetContainerCombinations(newAvailableContainers, newUsedContainers);
                }
            }
        }
    }
}