def fix_the_networks(input):
    m = int(input[0]) #input()
    result = []
    for i in range(1, m+1): #range(m)
        r = input[i] #input()
        cidr = r.split("/")
        prefix = cidr[0].split(".")
        sufix = cidr[1]
        prefix_bin = ""

        for dec in prefix:
            dec = int(dec)
            binary = f"{dec:08b}"
            prefix_bin = prefix_bin + binary

        num_variable_bits = 32 - int(sufix)
        count = 0
        valid = True

        for i in range(-1, -1 - num_variable_bits, -1):
            if prefix_bin[i] != "1":
                count += 1
            else:
                valid = False
                break

        new_sufix = 0
        if not valid:
            new_sufix = 32 - count
            result.append(f"invalid {'.'.join(prefix)}/{new_sufix} {2**count}")
            
        else:
            if num_variable_bits == 1:
                result.append(f"valid {num_variable_bits*2}")
            else:
                result.append(f"valid {int((2**(num_variable_bits - 1))*2)}")

    return result