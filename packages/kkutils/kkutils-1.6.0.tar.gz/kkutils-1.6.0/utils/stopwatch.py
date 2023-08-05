#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Author:   root
Created:  2022-11-16 21:18:34
"""

import time


class Stopwatch:

    def __init__(self, start=False):
        self.duration = 0.0
        self.begin = None
        if start:
            self.start()

    def start(self):
        self.begin = time.time()

    def stop(self):
        delta = time.time() - self.begin
        self.duration += delta
        self.start()
        return delta

    def reset(self):
        self.duration = 0.0
        self.start()
