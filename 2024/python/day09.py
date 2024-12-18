diskmap = [int(v) for _, v in enumerate(list(open("../input/09.txt", encoding="utf-8").read().strip()))]
buffer_a, empty_space, files = [], [], {}
ptr, file_id = 0, 0

for ix, size in enumerate(diskmap):
    if ix % 2 == 0:
        buffer_a +=  [ix//2 for _ in range(size)]
        files[file_id] = (ptr, size)
        file_id += 1
    else:
        buffer_a += [-1 for _ in range(size)]
        empty_space.append((ptr, size))
    ptr += size

# calculate A
buf_index = buffer_a.index(-1)
for rev_index, i in enumerate(reversed(buffer_a)):
    if len(buffer_a) - rev_index <= buf_index:
        break
    if i >= 0 :
        buffer_a[buf_index] = i
        buffer_a[len(buffer_a) - rev_index - 1] = -1
        while buffer_a[buf_index] != -1:
            buf_index += 1

# calculate B
while file_id > 0:
    file_id -= 1
    ptr, filesize = files[file_id]
    for i, (start, length) in enumerate(empty_space):
        if start >= ptr:
            empty_space = empty_space[:i]
            break
        if length >= filesize:
            files[file_id] = (start, filesize)
            if filesize == length:
                empty_space.pop(i)
            elif filesize < length:
                empty_space[i] = (start+filesize, length-filesize)
            break

print("Answer A:", sum(k * v for k, v in enumerate(buffer_a) if v != -1))
print("Answer B:", sum(fid * x for fid, (ptr, filesize) in files.items() for x in range(ptr, ptr + filesize)))
