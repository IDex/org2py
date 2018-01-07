#!/bin/env python3
from collections import deque
import argparse


class OrgNode:
    def __init__(self, line='root', indent='    '):
        self.indent = indent
        self.level = self.count_level(line)
        self.children = []
        self.name = line.split()[-1]
        if self.level == 0:
            self.attributes = self.parse_attributes(line)
        else:
            self.attributes = []

    def add_child(self, node):
        self.children.append(node)

    def parse_attributes(self, line):
        return [attribute.strip() for attribute in line.split(',')]

    def is_class(self):
        return self.name[0].isupper()

    def to_string(self):
        if self.is_class():
            string = self.class_string()
        else:
            string = self.function_string()
        return string

    def class_string(self):
        return f"""{self.blank_lines()}{(self.level-1)*self.indent}class {self.name}:\n
{(self.level)*self.indent}def __init__(self, {', '.join(self.attributes)}):
{self.init_body()}"""

    def function_string(self):
        return f"""{self.blank_lines()}{(self.level-1)*self.indent}def {self.name}({', '.join(self.attributes)}):
{(self.level)*self.indent}pass"""

    def import_string(self):
        return '\n'.join(
            [f'import {attribute}' for attribute in self.attributes[1:]])

    def blank_lines(self):
        if self.level <= 1:
            return '\n\n'
        else:
            return '\n'

    def init_body(self):
        if self.attributes:
            return '\n'.join([
                f'{(self.level+1)*self.indent}self.{attribute} = {attribute}'
                for attribute in self.attributes
            ])
        else:
            return "{(self.level+1)*self.indent}pass"

    def count_level(self, line):
        return sum([1 for char in line if char == '*'])


class OrgTree:
    def __init__(self, fname):
        self.content = self.read(fname)
        self.code = []
        self.root = None

    def read(self, fname):
        with open(fname) as f:
            content = [l.strip() for l in f]
        return content

    def write(self, fname):
        if not self.code_is_parsed():
            self.construct()
            self.parse()
        with open(fname, 'w') as f:
            f.write(self.code)

    def code_is_parsed(self):
        return bool(self.code)

    def construct(self, indent='    '):
        self.root = OrgNode(indent=indent)
        parents_by_level = [self.root]
        previous_node = self.root
        for line in self.content:
            node = OrgNode(line, indent=indent)
            if node.level == 0:
                previous_node.attributes.extend(node.attributes)
                continue
            if parents_by_level[node.level -
                                1].is_class() and not node.is_class():
                node.attributes.append('self')
            parents_by_level[node.level - 1].add_child(node)
            parents_by_level.insert(node.level, node)
            previous_node = node

    def add_main(self):
        main = OrgNode('* main', indent=self.root.indent)
        self.code.append(main.to_string())
        self.code.append(f"""{self.root.blank_lines()}if __name__ == '__main__':
{self.root.indent*1}main()""")

    def add_imports(self):
        if len(self.root.attributes) > 1:
            self.code.append(self.root.import_string())

    def parse(self, main=False):
        self.add_imports()
        children = deque(self.root.children[::-1])
        while children:
            child = children.pop()
            self.code.append(child.to_string())
            children.extend(child.children[::-1])
        if main:
            self.add_main()
        self.code = '\n'.join(self.code)


def main():
    parser = argparse.ArgumentParser(
        description='Generates Python class/function stumps from an Org file.')
    parser.add_argument(
        'input', help='Org file to parse.')
        # '--input', default='outline.org', help='Org file to parse.')
    parser.add_argument(
        '-o',
        '--output',
        help='Output file for the generated code, by default STDOUT.')
    parser.add_argument(
        '-i',
        '--indent',
        default='    ',
        help='Indentation for generated code (e.g. "  "), by default 4 spaces.')
    parser.add_argument(
        '-m',
        '--main',
        action='store_true',
        help='Add "if __name__" boilerplate to the end, by default off.')
    args = parser.parse_args()
    tree = OrgTree(args.input)
    tree.construct(indent=args.indent)
    tree.parse(main=args.main)
    if args.output:
        tree.write(args.output)
    else:
        print(tree.code)


if __name__ == '__main__':
    main()
