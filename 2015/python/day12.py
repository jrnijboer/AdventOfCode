import re, json
text = open("../input/day12.input", encoding="utf-8").read().strip()
numbers = re.findall("-?\d+", text)
data = json.loads(text)

def sum_numbers(obj):
    if isinstance(obj, dict):
        if "red" in obj.values():
            return 0
        return sum([sum_numbers(v) for v in obj.values()])
    elif isinstance(obj, list):
        return sum([sum_numbers(v) for v in obj])
    elif isinstance(obj, int):
        return obj
    return 0

print("Answer A:", sum(map(int, numbers)))
print("Answer B:", sum_numbers(data))
