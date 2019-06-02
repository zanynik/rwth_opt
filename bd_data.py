#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun  1 11:21:40 2019

@author: luckshan
"""

from gurobi import *

drop_zones = ["DZ NRML-1", "DZ NRML-2", "DZ NML-1", "DZ CLD-1"]

break_down_zones = ["B BD NRML-1", "B BD NRML-2", "BD NML-1", "BD CLD-1", "BD NRML-1", "BD NML-2", "BD NRML-2",
                    "BD NRML-3", "BD CLD-2", "BD NML-3", "BD NRML-4", "BD CLD-4"]

time_to_dz_bd = tupledict({
	('B BD NRML-1', 'DZ NRML-1'): 0.25,
	('B BD NRML-2', 'DZ NRML-1'): 0.11,
	('BD NML-1', 'DZ NRML-1'): 0.19,
	('BD CLD-1', 'DZ NRML-1'): 0.24,
	('BD NRML-1', 'DZ NRML-1'): 0.05,
	('BD NML-2', 'DZ NRML-1'): 0.15,
	('BD NRML-2', 'DZ NRML-1'): 0.19,
	('BD NRML-3', 'DZ NRML-1'): 0.25,
	('BD CLD-2', 'DZ NRML-1'): 0.07,
	('BD NML-3', 'DZ NRML-1'): 0.25,
	('BD NRML-4', 'DZ NRML-1'): 0.20,
	('BD CLD-4', 'DZ NRML-1'): 0.21,
	('B BD NRML-1', 'DZ NRML-2'): 0.11,
	('B BD NRML-2', 'DZ NRML-2'): 0.17,
	('BD NML-1', 'DZ NRML-2'): 0.12,
	('BD CLD-1', 'DZ NRML-2'): 0.16,
	('BD NRML-1', 'DZ NRML-2'): 0.05,
	('BD NML-2', 'DZ NRML-2'): 0.03,
	('BD NRML-2', 'DZ NRML-2'): 0.24,
	('BD NRML-3', 'DZ NRML-2'): 0.06,
    ('BD CLD-2', 'DZ NRML-2'): 0.07,
	('BD NML-3', 'DZ NRML-2'): 0.15,
    ('BD NRML-4', 'DZ NRML-2'): 0.13,
	('BD CLD-4', 'DZ NRML-2'): 0.16,
    ('B BD NRML-1', 'DZ NML-1'): 0.26,
	('B BD NRML-2', 'DZ NML-1'): 0.08,
	('BD NML-1', 'DZ NML-1'): 0.28,
	('BD CLD-1', 'DZ NML-1'): 0.22,
	('BD NRML-1', 'DZ NML-1'): 0.02,
	('BD NML-2', 'DZ NML-1'): 0.26,
	('BD NRML-2', 'DZ NML-1'): 0.12,
	('BD NRML-3', 'DZ NML-1'): 0.25,
    ('BD CLD-2', 'DZ NML-1'): 0.17,
	('BD NML-3', 'DZ NML-1'): 0.11,
    ('BD NRML-4', 'DZ NML-1'): 0.18,
	('BD CLD-4', 'DZ NML-1'): 0.26
})


bd_handling = {"B BD NRML-1": 0.24, "B BD NRML-2": 0.24, "BD NML-1": 0.13, "BD CLD-1": 0.17, "BD NRML-1": 0.2,
               "BD NML-2": 0.13, "BD NRML-2": 0.2, "BD NRML-3": 0.2, "BD CLD-2": 0.17, "BD NML-3": 0.2,
               "BD NRML-4": 0.13, "BD CLD-4": 0.15}

bd_capacity = {"B BD NRML-1": 33, "B BD NRML-2": 10, "BD NML-1": 4, "BD CLD-1": 8, "BD NRML-1": 5,
               "BD NML-2": 3, "BD NRML-2": 6, "BD NRML-3": 3, "BD CLD-2": 5, "BD NML-3": 5,
               "BD NRML-4": 3, "BD CLD-4": 1}
