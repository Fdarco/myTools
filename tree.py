import os
import sys
import argparse
from pathlib import Path
from rich.tree import Tree
from rich.console import Console
from fileExtensions import fileColors, fileIcons, dirIgnore


console = Console()


class DirectionTree:
    def __init__(self, targetPath: str = '.', maxDepth: int = 3):
        self.targetPath = Path(targetPath)
        if self.targetPath.is_dir():
            self.rootTree = Tree(f'[#0ca0d8] {self.targetPath.name}')
        elif self.targetPath.is_file():
            raise ValueError('Please provide a directory path!')
        else:
            raise ValueError('Please provide a valid path!')
        self.maxDepth = maxDepth

    def generate_tree(self, tree: Tree, n: int = 0, originalPath: str = '.'):
        if n >= self.maxDepth:
            return
        if self.targetPath.is_file():
            fileExtention = '.' + self.targetPath.name.split('.')[-1]
            if fileExtention in fileIcons.keys():
                tree.add(
                    '{}{} {}'.format(
                        fileColors[fileExtention],
                        fileIcons[fileExtention],
                        self.targetPath.name
                    )
                )
            else:
                tree.add(f'󰈔 {self.targetPath.name}')
        elif self.targetPath.is_dir():
            if self.targetPath.name in dirIgnore:
                return
            if not self.targetPath.relative_to(self.targetPath.parent).name == originalPath:
                tree = tree.add(f'[#0ca0d8] {self.targetPath.name}')
            try:
                for cp in self.targetPath.iterdir():
                    self.targetPath = Path(cp)
                    self.generate_tree(tree, n + 1, originalPath)
            except PermissionError:
                pass


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='A simple tree generator')
    parser.add_argument(
        'path', type=str, help='The path to the directory'
    )
    parser.add_argument(
        '-d', '--depth', type=int,
        help='The depth of the tree, default 3.', default=3
    )
    args = parser.parse_args()

    dt = DirectionTree(args.path, args.depth+1)
    dt.generate_tree(dt.rootTree, 0, dt.targetPath.name)
    console.print(dt.rootTree)
