""" Logging """
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import tensorflow as tf

import functools


def log_parse_args(parse_args, argument_class='Arguments'):
    arg_dict = parse_args.__dict__
    arg_str = functools.reduce(lambda a, b: a + b, map(lambda (k, v): '{}: {}\n'.format(k, v), arg_dict.items()), '')
    tf.logging.info('{}: %s'.format(argument_class), arg_str)
