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
        public static Dictionary<string, int> distances;
        public static List<Route> routes;
        static void Day9a()
        {
            var input = File.ReadAllLines("input/day9.input");
            var places = new List<string>();
            distances = new Dictionary<string, int>();
            routes = new List<Route>();

            foreach (var route in input)
            {
                //Faerun to Tristram = 65
                var match = Regex.Match(route, @"^(\w+) to (\w+) = (\d+)");
                places.Add(match.Groups[1].Value);
                places.Add(match.Groups[2].Value);
                distances[match.Groups[1].Value + "," + match.Groups[2].Value] = int.Parse(match.Groups[3].Value);
                distances[match.Groups[2].Value + "," + match.Groups[1].Value] = int.Parse(match.Groups[3].Value);
            }

            places = places.Distinct().ToList();

            foreach (var place in places)
            {
                Route r = new Route { VisitedPlaces = new List<string>() { place }, RouteLength = 0 };
                List<string> placesToVisit = new List<string>();
                places.ForEach(p => placesToVisit.Add(p));
                placesToVisit.Remove(place);
                calculateRoute(r, placesToVisit);
            }

            Route shortestRoute = new Route { RouteLength = int.MaxValue };
            routes.ForEach(r => 
            {
                int currentPlace = 1;
                int routeLength = 0;
                while (currentPlace < r.VisitedPlaces.Count)
                {
                    routeLength += distances[r.VisitedPlaces[currentPlace - 1]+ "," + r.VisitedPlaces[currentPlace]] ;
                    currentPlace++;
                }
                if (routeLength < shortestRoute.RouteLength)
                {
                    r.RouteLength = routeLength;
                    shortestRoute = r;
                }
            });
            Console.WriteLine("The shortest route = {0}", shortestRoute.RouteLength);
        }


        public static void calculateRoute(Route route, List<string> placesToVisit)
        {
            foreach (var nextPlace in placesToVisit)
            {
                string currentCity = route.VisitedPlaces.Last();
                Route newRoute = new Route();
                newRoute.VisitedPlaces = new List<string>();
                route.VisitedPlaces.ForEach(p =>
                {
                    newRoute.VisitedPlaces.Add(p);
                });                
                newRoute.VisitedPlaces.Add(nextPlace);
                newRoute.RouteLength = route.RouteLength + distances[currentCity + "," + nextPlace];
                List<string> remainingPlacesToVisit = new List<string>();
                placesToVisit.ForEach(p => remainingPlacesToVisit.Add(p));
                remainingPlacesToVisit.Remove(nextPlace);
                if (remainingPlacesToVisit.Count == 1)
                {
                    newRoute.VisitedPlaces.Add(remainingPlacesToVisit[0]);
                    newRoute.RouteLength += route.RouteLength + distances[currentCity + "," + remainingPlacesToVisit[0]];
                    routes.Add(newRoute);
                }
                else
                {
                    calculateRoute(newRoute, remainingPlacesToVisit);
                }
            }
        }

        public class Route
        {
            public List<string> VisitedPlaces { get; set; }
            public int RouteLength { get; set; }
        }
    }
}