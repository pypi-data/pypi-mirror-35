"""Represents action to take in order to de-id a single field"""
from enum import Enum


class DeIdAction(Enum):
    """Enumeration of possible actions to take when de-identifying"""
    REMOVE = 'REMOVE'
    REPLACE = 'REPLACE'


class DeIdField(object):
    """Represents action to take to de-identify a single field"""
    def __init__(self, action, fieldname, value=None):
        """Create a new de-id field for action.

        Args:
            action (DeIdAction): The action to take
            fieldname (str): The fieldname
            value: The optional value (required for some actions)
        """
        if action not in DeIdAction:
            raise ValueError('Unknown de-identify action: {}'.format(action))

        self.action = action
        self.fieldname = fieldname
        self.value = value

    def to_config(self):
        """Convert to configuration dictionary"""
        result = {'name': self.fieldname}
        if self.action == DeIdAction.REMOVE:
            result['remove'] = True
        elif self.action == DeIdAction.REPLACE:
            result['replace-with'] = self.value
        return result

    @staticmethod
    def from_config(config):
        """Create a DeIdField from configuration"""
        fieldname = config['name']
        action = None
        value = None
        if 'remove' in config:
            action = DeIdAction.REMOVE
        elif 'replace-with' in config:
            action = DeIdAction.REPLACE
            value = config['replace-with']
        return DeIdField(action, fieldname, value=value)

    def deidentify(self, profile, state, record):
        """Perform this action for a given profile.

        Args:
            profile (FileProfile): The file profile object
            record: The record to de-identify
        """
        if self.action == DeIdAction.REMOVE:
            profile.remove_field(state, record, self.fieldname)
        elif self.action == DeIdAction.REPLACE:
            profile.replace_field(state, record, self.fieldname, self.value)
