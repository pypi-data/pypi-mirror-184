#!/usr/bin/python3
# -*- coding: utf-8 -*-

import subprocess
from pathlib import Path
from typing import Union
from multiprocessing import Process

from slpkg.configs import Configs
from slpkg.progress_bar import ProgressBar


class Downloader:
    """ Wget downloader. """

    def __init__(self, path: Union[str, Path], url: str):
        self.path = path
        self.url = url
        self.filename = url.split('/')[-1]
        self.configs = Configs
        self.colors = self.configs.colour
        self.color = self.colors()
        self.green = self.color['green']
        self.yellow = self.color['yellow']
        self.endc = self.color['endc']
        self.progress = ProgressBar()
        self.stderr = None
        self.stdout = None

    def wget(self):
        """ Wget downloader. """
        subprocess.call(f'wget {self.configs.wget_options} --directory-prefix={self.path} {self.url}',
                        shell=True, stderr=self.stderr, stdout=self.stdout)

    def download(self):
        """ Starting multiprocessing download process. """
        if self.configs.view_mode == 'new':
            self.stderr = subprocess.DEVNULL
            self.stdout = subprocess.DEVNULL

            message = f'[{self.green}Downloading{self.endc}]'

            # Starting multiprocessing
            p1 = Process(target=self.wget)
            p2 = Process(target=self.progress.bar, args=(message, self.filename))

            p1.start()
            p2.start()

            # Wait until process 1 finish
            p1.join()

            # Terminate process 2 if process 1 finished
            if not p1.is_alive():
                print(f'{self.endc}{self.yellow} Done{self.endc}', end='')
                p2.terminate()

            # Wait until process 2 finish
            p2.join()

            # Restore the terminal cursor
            print('\x1b[?25h')
        else:
            self.wget()
