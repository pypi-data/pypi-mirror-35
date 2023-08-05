# -*- coding: utf-8 -*-

import json
import copy

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
            tmp_fixed_actions.append(action.__dict__)
        tmp_self_dict['actions'] = tmp_fixed_actions
        return str(tmp_self_dict)

    def add_action(self, action):
        if isinstance(action, Action):
            self.actions.append(action)

    # def jsonify(self):
    #     # No actions cause crash
    #     return {'user_hash': str(self.user_hash), 'name': str(self.name), 'message': str(self.message), 'actions': list(action.jsonify() for action in self.actions)}


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

    # def jsonify(self):
    #     return {'event': str(self.event), 'sensor': str(self.sensor), 'sensor_code': str(self.sensor_code), 'value': str(self.value)}