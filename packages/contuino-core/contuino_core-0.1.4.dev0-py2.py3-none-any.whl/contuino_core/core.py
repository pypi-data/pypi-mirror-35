# -*- coding: utf-8 -*-

import copy
import json

class Board:
    """Board class"""
    user_hash = None
    name = None
    message = None
    actions = []

    def __init__(self, user_hash=None, name=None, message=None, actions=[]):
        self.user_hash = user_hash
        self.name = name
        self.message = message
        for action in actions:
            self.add_action(action)

    def __str__(self):
        tmp_self_dict = copy.copy(self.__dict__)
        tmp_fixed_actions = []
        for action in self.actions:
            tmp_action = action.__dict__
            tmp_action['event'] = str(tmp_action['event'])
            tmp_action['sensor'] = str(tmp_action['sensor'])
            tmp_fixed_actions.append(tmp_action)
        tmp_self_dict['actions'] = tmp_fixed_actions
        return json.dumps(tmp_self_dict)

    def add_action(self, action):
        if isinstance(action, Action):
            self.actions.append(action)

class Action:
    """Action class"""
    event = None
    value = None
    sensor = None
    sensor_code = None

    def __init__(self, event=None, value=None, sensor=None, sensor_code=None):
        self.event = event
        self.value = value
        self.sensor = sensor
        self.sensor_code = sensor_code
