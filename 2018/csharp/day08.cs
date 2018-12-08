using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;

namespace aoc2018
{
    class Day8
    {
        public static void Solve()
        {
            Queue<int> Q = new Queue<int>();
            File.ReadAllText(Path.Combine("..", "input", "day8.input")).Split(" ").Select(int.Parse).ToList().ForEach(x => Q.Enqueue(x));
            int sum = 0;
            Node root = BuildNode(Q, ref sum);
            Console.WriteLine("day8, part a: {0}", sum);
            Console.WriteLine("day8, part b: {0}", GetNodeValue(root));
        }

        public static int GetNodeValue(Node node)
        {
            if (node.children.Count > 0)
            {
                int value = 0;
                node.values.Where(x => x > 0 && x <= node.children.Count).ToList().ForEach(x => value += GetNodeValue(node.children[x - 1]));
                return value;
            }
            else
                return node.values.Sum();
        }

        public static Node BuildNode(Queue<int> Q, ref int sum)
        {
            int countChildren = Q.Dequeue(), countValues = Q.Dequeue();
            var node = new Node { children = new List<Node>(), values = new List<int>() };
            for (int i = 0; i < countChildren; i++)
                node.children.Add(BuildNode(Q, ref sum));
            for (int i = 0; i < countValues; i++)
            {
                node.values.Add(Q.Dequeue());
                sum += node.values[node.values.Count - 1];
            }
            return node;
        }
    }

    struct Node
    {
        public List<Node> children;
        public List<int> values;
    }
}
