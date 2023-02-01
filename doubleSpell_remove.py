import sys

def main():
    origFile = sys.argv[1]
    uniqSet = set([])
    with open(origFile, 'r') as orig2read, open("new_"+origFile, 'w') as new2write:
        for line in orig2read:
            p1 = line.split(":")[0]
            if p1 not in uniqSet:
                uniqSet.add(p1)
                new2write.write(line)
            else:
                print(f"Duplicated! {line}")

if __name__ == '__main__':
    main()