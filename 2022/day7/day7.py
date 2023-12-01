from collections import defaultdict

def toFill(): 
    a = defaultdict()
    a['files'] = []
    #a['size'] = 0
    return a


def genDirs(location : str):

    f = open(location, "r")

    data = f.read().splitlines()

    f.close()

    cwd = "/"
    dirs = defaultdict(toFill)

    dirs["/"]

    for command in data[1:]:

        command = command.split()

        if command[0] == "$":
            if command[1] == "cd":
                if command[2] == "..":
                    cwd = cwd[:cwd[:-1].rfind("/")+1]

                    if cwd == "":
                        cwd = "/"

                else:
                    cwd += command[2] + "/"
            
            if command[1] == "ls":
                continue
        
        else:
            try:
                dirs[cwd]['files'].append(int(command[0]))

            except ValueError:

                dirs[cwd]['files'].append(cwd + command[1] + "/")
    #print(dirs)
    return dirs


def sizes(dirs : defaultdict, index : str) -> int:
    total = 0
    for f in dirs[index]["files"]:
        try:
            total += f
        except:
            total += sizes(dirs, f)
        #print(total, "a")
    dirs[index]['size'] = total
    return total

def part1(dirs) -> int:
    total = 0
    for key in dirs:
        #print(dirs[key], key)
        total += dirs[key]['size'] if dirs[key]['size'] <= 100000 else 0
    return total

def part2(dirs):
    total = dirs['/']['size']
    space = 70000000

    sizes = [[dirs[key]['size'], key] for key in dirs.keys()]

    sizes = sorted(sizes, key = lambda x : x[0])

    for size in sizes:
        if space - total + size[0] >= 30000000:
            return size[0]


dirs = genDirs("input.txt")
sizes(dirs, "/")
#print(dirs.keys())
print(part2(dirs))
