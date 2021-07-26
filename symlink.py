from argparse import ArgumentParser
from glob import glob
from os import makedirs, path, symlink

import tqdm


def parse_args():
    parser = ArgumentParser(
        prog="symlink", 
        description="This program receives one or more folders and " \
            "creates symbolic links to all containd items into an " \
            "output folder."
    )
    parser.add_argument(
        "input_folders", 
        type=str, 
        nargs="+", 
        help="One or more paths towards folders whose contained items "\
            "are to be linked"
    )
    parser.add_argument(
        "-o", "--output_folder",
        type=str,
        nargs=1,
        help="An output folder in which the links should be created. If " \
            "the folder does not exists, it is created."
    )

    args = parser.parse_args()
    if not path.exists(args.output_folder):
        makedirs(args.output_folder)

    return args


if __name__ == "__main__":
    args = parse_args()

    items = []
    for folder in args.input_folders:
        items.extend(list(sorted(glob(path.join(folder, "*")))))

    for item in tqdm.tqdm(items, desc="Creating symlinks"):
        item_name = item.split("/")[-1]
        symlink(item, path.join(args.output_folder, item_name), )

    