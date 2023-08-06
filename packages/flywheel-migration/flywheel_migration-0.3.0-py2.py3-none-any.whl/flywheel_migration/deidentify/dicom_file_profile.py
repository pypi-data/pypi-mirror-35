"""File profile for de-identifying dicom files"""
import collections
import gzip
import logging
import os
import pydicom
import six

from .file_profile import FileProfile

log = logging.getLogger(__name__)


class DicomFileProfile(FileProfile):
    """Dicom implementation of load/save and remove/replace fields"""

    name = 'dicom'
    log_fields = ['StudyInstanceUID', 'SeriesInstanceUID', 'SOPInstanceUID']

    def __init__(self):
        super(DicomFileProfile, self).__init__(packfile_type='dicom')

    def create_file_state(self):
        """Create state object for processing files"""
        return {
            'series_uid': None,
            'session_uid': None,
            'sop_uids': set()
        }

    def get_dest_path(self, state, record, path):
        # Destination path is sop_uid.modality.dcm
        sop_uid = record.get('SOPInstanceUID')
        if not sop_uid:
            return path
        modality = record.get('Modality', 'NA')
        return u'{}.{}.dcm'.format(sop_uid, modality)

    def load_record(self, state, src_fs, path):
        try:
            with src_fs.open(path, 'rb') as f:
                # Extract gzipped dicoms
                _, ext = os.path.splitext(path)
                if ext.lower() == '.gz':
                    f = gzip.GzipFile(fileobj=f)

                # Read and decode the dicom
                dcm = pydicom.dcmread(f)
                dcm.decode()
        except (pydicom.errors.InvalidDicomError, ValueError):
            log.warning('IGNORING %s - it is not a DICOM file!', path)
            return None

        # Validate the series/session
        series_uid = dcm.get('SeriesInstanceUID')
        session_uid = dcm.get('StudyInstanceUID')

        if state['series_uid'] is not None:
            # Validate SeriesInstanceUID
            if series_uid != state['series_uid']:
                log.warning('DICOM %s has a different SeriesInstanceUID (%s) from the rest of the series: %s', path, series_uid, state['series_uid'])
            # Validate StudyInstanceUID
            elif session_uid != state['session_uid']:
                log.warning('DICOM %s has a different StudyInstanceUID (%s) from the rest of the series: %s', path, session_uid, state['session_uid'])
        else:
            state['series_uid'] = series_uid
            state['session_uid'] = session_uid

        # Validate SOPInstanceUID
        sop_uid = dcm.get('SOPInstanceUID')
        if sop_uid:
            if sop_uid in state['sop_uids']:
                log.error('DICOM %s re-uses SOPInstanceUID %s, and will be excluded!', path, sop_uid)
                return None
            state['sop_uids'].add(sop_uid)

        return dcm

    def save_record(self, state, record, dst_fs, path):
        with dst_fs.open(path, 'wb') as f:
            record.save_as(f)

    def read_field(self, state, record, fieldname):
        # Ensure that value is a string
        value = getattr(record, fieldname, None)
        if value is not None and not isinstance(value, six.string_types):
            if isinstance(value, collections.Sequence):
                value = ','.join([str(x) for x in value])
            else:  # Unknown value, just convert to string
                value = str(value)
        return value

    def remove_field(self, state, record, fieldname):
        if hasattr(record, fieldname):
            delattr(record, fieldname)

    def replace_field(self, state, record, fieldname, value):
        setattr(record, fieldname, value)
