lengthofline = int(input())
n = int(input())

section_header = [0] 
old_key = 0

for i in range(n):
    entry = input()
    a = entry.split()
    title = a[0]
    page = a[1]
 
    fill = ""
    indent = ""
    adjusted_title = title
    
    key = 0
    for i in range(len(title)):
        if title[i] == ">":
            indent = indent + "    "
            adjusted_title = title[(i+1):]
            key += 1
        else:
            break
    
    if key <= old_key:
        section_header[key] += 1
        del section_header[key+1:]
        old_key = key

    else:
        section_header.append(1)
        old_key += 1

    num_dots = lengthofline - len(str(section_header[key]))- len(indent) - len(adjusted_title) - len(page) - 1

    for j in range(num_dots):
        fill = fill + "."
    print(indent + str(section_header[key]) + " " + adjusted_title + fill + page)
