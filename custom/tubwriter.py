#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from tub import Tub

class TubWriter(Tub):
    def __init__(self, *args, **kwargs):
        super(TubWriter, self).__init__(*args, **kwargs)

    def run(self, *args):
        print("TubWriter Running: ",len(args)," inputs: ",self.inputs)
        """
        Accepts values, pairs them with their input keys and saves them
        to disk.
        """
        assert len(self.inputs) == len(args)
        record = dict(zip(self.inputs, args))
        self.put_record(record)
