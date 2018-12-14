using System;
using System.Collections.Generic;
using System.Drawing;
using System.IO;
using System.Linq;

namespace aoc2018
{
    class Day13
    {
        public static void Solve()
        {
            var input = File.ReadAllLines(Path.Combine("..", "input", "day13.input")).ToList();
            var grid = new char[input.Count, input[0].Length];
            var carts = new List<Cart>();
            for (int y = 0; y < input.Count; y++)
                for (int x = 0; x < input[y].Length; x++)
                    switch (input[y][x])
                    {
                        case 'v':
                        case '^':
                            carts.Add(new Cart(x, y, input[y][x] == 'v' ? Direction.South : Direction.North));
                            grid[y, x] = '|';
                            break;
                        case '<':
                        case '>':
                            carts.Add(new Cart(x, y, input[y][x] == '<' ? Direction.West : Direction.East));
                            grid[y, x] = '-';
                            break;
                        default:
                            grid[y, x] = input[y][x];
                            break;
                    }

            bool printCrash = true;
            while (true)
            {
                carts.OrderBy(c => c.Position.Y).ThenBy(c => c.Position.X);
                foreach (var cart in carts)
                    cart.Move(carts, grid);

                if (carts.Any(c => c.IsCrashed))
                {
                    if (printCrash)
                    {
                        var crashedCart = carts.Where(c => c.IsCrashed).First();
                        Console.WriteLine("day 13, answer a: {0},{1}", crashedCart.Position.X, crashedCart.Position.Y);
                        printCrash = false;
                    }
                    carts = carts.Where(c => !c.IsCrashed).ToList();
                }
                if (carts.Count == 1)
                {
                    Console.WriteLine("day 13, answer b: {0},{1}", carts[0].Position.X, carts[0].Position.Y);
                    break;
                }
            }
        }
    }

    public class Cart
    {
        private static List<Point> DirectionList = new List<Point> { new Point(0, -1), new Point(1, 0), new Point(0, 1), new Point(-1, 0) };
        public Direction Direction { get; set; }
        public Point Position { get; set; }
        public int NextTurn { get; set; }
        public bool IsCrashed { get; set; }

        public Cart(int x, int y, Direction direction)
        {
            IsCrashed = false;
            Position = new Point(x, y);
            NextTurn = -1;
            Direction = direction;
        }

        public void Move(List<Cart> carts, char[,] grid)
        {
            Position = new Point(Position.X + DirectionList[(int)Direction].X, Position.Y + DirectionList[(int)Direction].Y);
            if (carts.Count(c => c.Position == Position && !c.IsCrashed) > 1)
                carts.Where(c => c.Position == Position).ToList().ForEach(c => c.IsCrashed = true);
            else
            {
                switch (grid[Position.Y, Position.X])
                {
                    case '+':
                        Direction = (Direction)((4 + (int)Direction + NextTurn) % 4);
                        NextTurn = NextTurn == 1 ? -1 : NextTurn + 1;
                        break;
                    case '\\':
                        if (Direction == Direction.South || Direction == Direction.North)
                            Direction = (Direction)((4 + (int)Direction - 1) % 4);
                        else
                            Direction = (Direction)(((int)Direction + 1) % 4);
                        break;
                    case '/':
                        if (Direction == Direction.South || Direction == Direction.North)
                            Direction = (Direction)(((int)Direction + 1) % 4);
                        else
                            Direction = (Direction)((4 + (int)Direction - 1) % 4);
                        break;
                }
            }
        }
    }

    public enum Direction
    {
        North = 0,
        East = 1,
        South = 2,
        West = 3
    }
}
