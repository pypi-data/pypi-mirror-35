import sys


FULL_TO_HALF_TABLE = dict((i + 0xFEE0, i) for i in range(0x21, 0x7F))


def full_width_to_half_width(line: str) -> str:
    return line.translate(FULL_TO_HALF_TABLE)


def main():
    while True:
        line = sys.stdin.readline()
        if not line:
            break
        output = full_width_to_half_width(line.decode('utf-8'))
        sys.stdout.write(output.encode('utf-8'))


if __name__ == '__main__':
    main()
