#!/usr/bin/python3
# -*- coding: utf-8 -*-

from progress.spinner import PixelSpinner

from slpkg.configs import Configs
from slpkg.views.ascii import Ascii
from slpkg.queries import SBoQueries


class Dependees:
    """ Show which packages depend. """

    def __init__(self, packages: list, flags: list):
        self.packages = packages
        self.flags = flags
        self.configs = Configs
        self.ascii = Ascii()
        self.llc = self.ascii.lower_left_corner
        self.hl = self.ascii.horizontal_line
        self.var = self.ascii.vertical_and_right
        self.colors = self.configs.colour
        self.colors = self.configs.colour
        self.color = self.colors()
        self.bold = self.color['bold']
        self.violet = self.color['violet']
        self.cyan = self.color['cyan']
        self.grey = self.color['grey']
        self.yellow = self.color['yellow']
        self.bviolet = f'{self.bold}{self.violet}'
        self.endc = self.color['endc']

    def slackbuilds(self):
        """ Collecting the dependees. """
        print(f"The list below shows the "
              f"packages that dependees on '{', '.join([p for p in self.packages])}':\n")

        dependees = {}
        spinner = PixelSpinner(f'{self.endc}Collecting the data... {self.bviolet}')
        for package in self.packages:
            found = []  # Reset list every package
            sbos = SBoQueries('').sbos()

            for sbo in sbos:
                requires = SBoQueries(sbo).requires()
                spinner.next()

                if package in requires:
                    found.append(sbo)
                    dependees[package] = found

        last = f' {self.llc}{self.hl}'
        print('\n')
        if dependees:
            for key, value in dependees.items():
                print(f'{self.yellow}{key}{self.endc}')
                print(end=f'\r{last}')
                char = f' {self.var}{self.hl}'

                for i, v in enumerate(value, start=1):
                    if i == len(value):
                        char = last

                    if i == 1:
                        print(f'{self.cyan}{v}{self.endc}')
                    else:
                        print(f'{" " * 3}{self.cyan}{v}{self.endc}')

                    if '--full-reverse' in self.flags:
                        print(f'{" " * 4}{char} {" ".join([req for req in SBoQueries(v).requires()])}')

                print(f'\n{self.grey}{len(value)} dependees for {key}{self.endc}\n')
        else:
            print(f'{self.endc}No dependees found.\n')
