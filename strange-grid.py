def strange_grid():
    row, col = map(int, raw_input().strip().split(' '))
    if row % 2 == 1:
        print ((((((row/2 + 1) - 1) * 5) + col)-1)*2)
    else:
        print 1 + (((((row/2 - 1) * 5) + col)-1)*2)

def main():
    strange_grid()

if __name__ == "__main__":
    main()