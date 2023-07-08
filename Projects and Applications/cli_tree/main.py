import os
import argparse


def write_to_file(path, tree):
    file = open(path, "w")
    file.write(tree)

    file.close()
    return


def print_tree(path, level, hidden, depth, ignore):
    if not os.path.exists(path):
        raise Exception("Invalid path")

    tree = ""

    for file in os.listdir(path):
        if not hidden and file.startswith(".") or file in ignore:
            continue
        tree += "|  " * level + "|--" + file + "\n"
        if os.path.isdir(path + "/" + file) and file not in ignore:
            if depth == -1:
                print_tree(path + "/" + file, level + 1, hidden, depth, ignore)
                tree += print_tree(path + "/" + file, level + 1, hidden, depth, ignore)
            elif level < depth:
                print_tree(path + "/" + file, level + 1, hidden, depth, ignore)
                tree += print_tree(path + "/" + file, level + 1, hidden, depth, ignore)
    return tree


def main():
    parser = argparse.ArgumentParser(description="A CLI tool to see a tree of a directory.", prog="cli_tree", epilog="Made by: Caleb Han (https://github.com/calebyhan)")

    parser.add_argument("path", type=str, nargs=1,
                        metavar="path", help="Path to the directory")

    parser.add_argument("-w", "--write", type=str, nargs="?",
                        metavar="file_name", const="output.txt",
                        help="Writes content to a file (default output.txt)")

    parser.add_argument("-hi", "--hidden", type=bool, nargs=1,
                        metavar="hidden", default=False,
                        help="Shows hidden files (default False)")

    parser.add_argument("-d", "--depth", type=int, nargs=1,
                        metavar="depth", default=[-1],
                        help="Sets depth of the tree (default max)")

    parser.add_argument("-i", "--ignore", type=str, nargs="?",
                        metavar="ignore", default=[],
                        help="Ignores dirs with the given name (default None)")

    parser.add_argument("-v", "--version", action="version", version="%(prog)s 1.0")

    args = parser.parse_args()

    print(args)

    if args.hidden is None:
        args.hidden = False
    if args.depth is None:
        args.depth = [-1]
    if args.ignore is None:
        args.ignore = []

    tree = print_tree(args.path[0], 0, args.hidden, args.depth[0], args.ignore)

    if args.write is not None:
        write_to_file(args.write, tree)

    print(tree)

    return


if __name__ == "__main__":
    main()
