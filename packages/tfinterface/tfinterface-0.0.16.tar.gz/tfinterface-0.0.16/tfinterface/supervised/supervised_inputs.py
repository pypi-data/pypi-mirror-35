#!/usr/bin/env python
# -*- coding: utf-8 -*-
# __coconut_hash__ = 0x60409b27

# Compiled with Coconut version 1.2.3 [Colonel]

# Coconut Header: --------------------------------------------------------

from __future__ import print_function, absolute_import, unicode_literals, division

import sys as _coconut_sys, os.path as _coconut_os_path
_coconut_file_path = _coconut_os_path.dirname(_coconut_os_path.abspath(__file__))
_coconut_sys.path.insert(0, _coconut_file_path)
from __coconut__ import _coconut, _coconut_MatchError, _coconut_tail_call, _coconut_tco, _coconut_igetitem, _coconut_compose, _coconut_pipe, _coconut_starpipe, _coconut_backpipe, _coconut_backstarpipe, _coconut_bool_and, _coconut_bool_or, _coconut_minus, _coconut_map, _coconut_partial
from __coconut__ import *
_coconut_sys.path.remove(_coconut_file_path)

# Compiled Coconut: ------------------------------------------------------

from tfinterface.utils import get_global_step
from tfinterface.base import GeneralInputs
import tensorflow as tf


class GeneralSupervisedInputs(GeneralInputs):

    def __init__(self, name, **kwargs):

        training = dict(shape=(), dtype=tf.bool, fit=True, predict=False)

        super(GeneralSupervisedInputs, self).__init__(name, training=training, global_step=get_global_step, **kwargs)

class SupervisedInputs(GeneralSupervisedInputs):

    def __init__(self, name, features, labels, **kwargs):

        super(SupervisedInputs, self).__init__(name, features=features, labels=labels, **kwargs)
