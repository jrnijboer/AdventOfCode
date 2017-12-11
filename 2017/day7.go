package main
import (
        "fmt"
        "bufio"
        "os"
        "strconv"
        "strings"
	"regexp"
)

func main() {
        var programs = []string{}
	var programsDict = make(map[string]int)
	var childsDict = make(map[string]string)
	var parentsDict = make(map[string][]string)
	file, _ := os.Open("day7.input")
        defer file.Close()
        scanner := bufio.NewScanner(file)
	re := regexp.MustCompile(`(?P<p>\S+) \((?P<w>\d+)\)`)
	var groups = []string{}
        for scanner.Scan() {
		line := scanner.Text()
		values := strings.Split(line, "->")
		prog := values[0]
		groups = re.FindStringSubmatch(prog)
		programs = append(programs, groups[1])
		programsDict[groups[1]], _ = strconv.Atoi(groups[2])
		childsArray := []string{}
		if len(values) > 1 {
			childs := strings.Split(values[1], ",")
			for _, c := range childs {
				c = strings.TrimSpace(c)
				childsArray = append(childsArray, c)
				childsDict[c] = strings.TrimSpace(groups[1])
			}
		}
		parentsDict[groups[1]] = childsArray
	}
	rootNode := solveA(programs, childsDict)
	var adjustment int
	node := rootNode
	var a int

	for rootNode != "" {
		_, rootNode, a = getWeights(rootNode, parentsDict, childsDict, programsDict)
		if rootNode != "" {
			node = rootNode
			adjustment = a
		}
	}
	fmt.Printf("Node %v is the lowest unbalanced node, it's weight is %v, it should be %v\n", node, programsDict[node], programsDict[node] + adjustment)
}

func solveA(programs []string, childs map[string]string) string {
	for _, p := range programs {
		if childs[p] == "" {
			fmt.Printf("root node is %v\n", p)
			return p
		}
	}
	panic("Nooo!")
}

func getWeights(parent string, parentsChildDict map[string][]string, childParentsDict map[string]string, programsDict map[string]int) (int, string, int){
	var childWeights = make(map[string]int)
	var nodeBalances = make(map[int][]string)
	sum := programsDict[parent]
	for _, child := range parentsChildDict[parent] {
		weight := 0
		if len(child) > 0 {
			w, _, _ := getWeights(child, parentsChildDict, childParentsDict, programsDict)
			weight += w
			sum += weight
		}
		nodeWeight := weight + programsDict[child]
		childWeights[child] = nodeWeight
		nodeBalances[weight] = append(nodeBalances[weight], child)
	}
	expectedWeight := 0
	unbalancedWeight := 0
	var unbalancedNode string
	for k, v := range nodeBalances {
		if len(v) == 1 {
			unbalancedWeight = k
			unbalancedNode = v[0]
		} else {
			expectedWeight = k
		}
	}
	if expectedWeight > 0 && unbalancedWeight > 0{
		return sum, unbalancedNode, expectedWeight - unbalancedWeight
	} else {
		return sum, "", 0
	}
}

