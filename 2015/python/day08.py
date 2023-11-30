lines = [line.strip() for line in open("../input/day08.input", encoding="utf-8").readlines()]
print("Answer A:", sum([len(line) - len(eval(line)) for line in lines]))
print("Answer B:", sum([2 + len(line.replace("\\", "\\\\").replace("\"", "\\\"")) - len(line) for line in lines]))
