#!/usr/bin/python3
if __name__ == '__main__':

    import hidden_4

    names = dir(hidden_4)
    names.sort()
    for i in range(len(names)):
        if names[i][0] == '_' and names[i][1] == '_':
            continue
        print(names[i])
