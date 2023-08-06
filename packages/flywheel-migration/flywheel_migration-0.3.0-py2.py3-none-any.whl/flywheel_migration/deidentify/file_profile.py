"""Individual file/packfile profile for de-identification"""

import fnmatch
from abc import ABCMeta, abstractmethod

import fs.copy

from .deid_field import DeIdField


class FileProfile:
    """Abstract class that represents a single file/packfile profile"""
    __metaclass__ = ABCMeta

    # NOTE: If you derive from this class, set a unique name for the factory method to use
    name = None
    log_fields = []

    def __init__(self, packfile_type=None, file_filter=None):
        """Initialize the file profile"""
        self.packfile_type = packfile_type
        self.file_filter = file_filter
        self.fields = []
        self.log = None

    def set_log(self, log):
        """Set the log instance"""
        self.log = log

    def get_log_fields(self):
        """Return the full set of fieldnames that should be logged"""
        result = list(self.log_fields)
        for field in self.fields:
            result.append(field.fieldname)
        return result

    @classmethod
    def factory(cls, name, config=None, log=None):
        """Create a new file profile instance for the given name.

        Arguments:
            name (str): The name of the profile type
            config (dict): The optional configuration dictionary
            log: The optional de-id log instance
        """
        result = None

        for subclass in cls.__subclasses__():
            if subclass.name == name:
                result = subclass()
                break

        if not result:
            raise ValueError('Unknown file profile: "{}"'.format(name))

        if config is not None:
            result.load_config(config)

        if log is not None:
            result.set_log(log)

        return result

    @classmethod
    def profile_names(cls):
        """Get the list of profile names"""
        result = []
        for subclass in cls.__subclasses__():
            if subclass.name is not None:
                result.append(subclass.name)
        return result

    def to_config(self):
        """Get configuration as a dictionary"""
        return {
            'fields': [field.to_config() for field in self.fields]
        }

    def load_config(self, config):
        """Read configuration from a dictionary"""
        for field in config.get('fields', []):
            self.fields.append(DeIdField.from_config(field))

    def matches_file(self, filename):
        """Check if this profile can process the given file"""
        return self.file_filter and fnmatch.fnmatch(self.file_filter, filename)

    def matches_packfile(self, packfile_type):
        """Check if this profile can process the given packfile"""
        return self.packfile_type and self.packfile_type == packfile_type

    def process_files(self, src_fs, dst_fs, files, callback=None):
        """Process all files in the file list, performing de-identification steps

        Args:
            src_fs: The source filesystem
            dst_fs: The destination filesystem
            files: The set of files in src_fs to process
            callback: Function to call after writing each file
        """
        state = self.create_file_state()

        for path in files:
            # Load file
            record = self.load_record(state, src_fs, path)

            # Record could be None if it should be skipped
            if not record:
                continue

            # Override destination path
            dst_path = self.get_dest_path(state, record, path)

            if self.fields:
                # Create before entry, if log is provided
                if self.log:
                    self.write_log_entry(path, 'before', state, record)

                # De-identify
                for field in self.fields:
                    field.deidentify(self, state, record)

                # Create after entry, if log is provided
                if self.log:
                    self.write_log_entry(path, 'after', state, record)

                # Save to dst_fs if we modified the record
                self.save_record(state, record, dst_fs, dst_path)
            else:
                # No fields to de-identify, just copy to dst
                fs.copy.copy_file(src_fs, path, dst_fs, dst_path)

            if callable(callback):
                callback(dst_fs, dst_path)

    def create_file_state(self):  # pylint: disable=no-self-use
        """Create state object for processing files"""
        return None

    def get_dest_path(self, state, record, path):  # pylint: disable=no-self-use, unused-argument
        """Get optional override for the destination path for record"""
        return path

    def write_log_entry(self, path, entry_type, state, record):
        """Write a single log entry of type for path"""
        log_entry = {'path': path, 'type': entry_type}
        for fieldname in self.get_log_fields():
            log_entry[fieldname] = self.read_field(state, record, fieldname)
        self.log.write_entry(log_entry)

    @abstractmethod
    def load_record(self, state, src_fs, path):
        """Load the record(file) at path, return None to ignore this file"""
        pass

    @abstractmethod
    def save_record(self, state, record, dst_fs, path):
        """Save the record to the destination path"""
        pass

    @abstractmethod
    def read_field(self, state, record, fieldname):
        """Read the named field as a string"""
        pass

    @abstractmethod
    def remove_field(self, state, record, fieldname):
        """Remove the named field from the record"""
        pass

    @abstractmethod
    def replace_field(self, state, record, fieldname, value):
        """Replace the named field with value in the record"""
        pass
