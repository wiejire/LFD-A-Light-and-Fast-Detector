# -*- coding: utf-8 -*-
# author: Yonghao He
# description: base hook class

from enum import Enum


class Priority(Enum):
    """Hook priority levels.

    +------------+------------+
    | Level      | Value      |
    +============+============+
    | HIGHEST    | 0          |
    +------------+------------+
    | VERY_HIGH  | 10         |
    +------------+------------+
    | HIGH       | 30         |
    +------------+------------+
    | NORMAL     | 50         |
    +------------+------------+
    | LOW        | 70         |
    +------------+------------+
    | VERY_LOW   | 90         |
    +------------+------------+
    | LOWEST     | 100        |
    +------------+------------+
    """

    HIGHEST = 0
    VERY_HIGH = 10
    HIGH = 30
    NORMAL = 50
    LOW = 70
    VERY_LOW = 90
    LOWEST = 100


def get_priority(priority):
    """Get priority value.

    Args:
        priority (int or str or :obj:`Priority`): Priority.

    Returns:
        int: The priority value.
    """
    if isinstance(priority, int):
        if priority < 0 or priority > 100:
            raise ValueError('priority must be between 0 and 100')
        return priority
    elif isinstance(priority, Priority):
        return priority.value
    elif isinstance(priority, str):
        return Priority[priority.upper()].value
    else:
        raise TypeError('priority must be an integer or Priority enum value')


class Hook(object):

    def before_run(self, executor):
        pass

    def after_run(self, executor):
        pass

    def before_epoch(self, executor):
        pass

    def after_epoch(self, executor):
        pass

    def before_iter(self, executor):
        pass

    def after_iter(self, executor):
        pass

    def before_train_epoch(self, executor):
        self.before_epoch(executor)

    def before_val_epoch(self, executor):
        self.before_epoch(executor)

    def after_train_epoch(self, executor):
        self.after_epoch(executor)

    def after_val_epoch(self, executor):
        self.after_epoch(executor)

    def before_train_iter(self, executor):
        self.before_iter(executor)

    def before_val_iter(self, executor):
        self.before_iter(executor)

    def after_train_iter(self, executor):
        self.after_iter(executor)

    def after_val_iter(self, executor):
        self.after_iter(executor)

