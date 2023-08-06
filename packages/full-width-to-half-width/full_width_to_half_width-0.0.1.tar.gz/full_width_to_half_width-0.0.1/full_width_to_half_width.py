import unicodedata


def full_width_to_half_width(line: str) -> str:
    return unicodedata.normalize('NFKC', line)


def main():
    while True:
        try:
            print(full_width_to_half_width(input()))
        except EOFError:
            break


if __name__ == '__main__':
    main()
