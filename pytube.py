#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os, sys, re


class PyTube(object):

    def __init__(self):
        self.file = open(sys.argv[1], 'r')
        self.links = []

    # Cria diretórios
    def makeDir(self):
        if not os.path.exists(r'Downloads'):
            os.makedirs(r'Downloads')

    # Parser de links
    def parser(self):
        self.file = self.file.read()
        self.links = re.findall('https://www.youtube.com/watch\?v=[a-zA-Z0-9-]{11}', self.file)
        print len(self.links)


    # Downloader dos videos
    def downloader(self):
        for link in self.links:
            os.system('cclive -f best {}'.format(link))


pytube = PyTube()
pytube.makeDir()
pytube.parser()
pytube.downloader()

