# coding: utf-8

"""
Copyright 2016 SmartBear Software

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.

    Ref: https://github.com/swagger-api/swagger-codegen
"""

from datetime import datetime
from datetime import date
from pprint import pformat
import re
import json

from ..utils import sanitize_for_serialization

# type hinting support
from typing import TYPE_CHECKING
from typing import List
from typing import Dict

if TYPE_CHECKING:
    from . import Conversation
    from . import Group
    from . import Queue
    from . import User
    from . import VoicemailCopyRecord
    from . import VoicemailRetentionPolicy

class VoicemailMessage(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self) -> None:
        """
        VoicemailMessage - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id': 'str',
            'conversation': 'Conversation',
            'read': 'bool',
            'audio_recording_duration_seconds': 'int',
            'audio_recording_size_bytes': 'int',
            'transcription': 'str',
            'created_date': 'datetime',
            'modified_date': 'datetime',
            'deleted_date': 'datetime',
            'caller_address': 'str',
            'caller_name': 'str',
            'caller_user': 'User',
            'deleted': 'bool',
            'note': 'str',
            'user': 'User',
            'group': 'Group',
            'queue': 'Queue',
            'copied_from': 'VoicemailCopyRecord',
            'copied_to': 'list[VoicemailCopyRecord]',
            'delete_retention_policy': 'VoicemailRetentionPolicy',
            'self_uri': 'str'
        }

        self.attribute_map = {
            'id': 'id',
            'conversation': 'conversation',
            'read': 'read',
            'audio_recording_duration_seconds': 'audioRecordingDurationSeconds',
            'audio_recording_size_bytes': 'audioRecordingSizeBytes',
            'transcription': 'transcription',
            'created_date': 'createdDate',
            'modified_date': 'modifiedDate',
            'deleted_date': 'deletedDate',
            'caller_address': 'callerAddress',
            'caller_name': 'callerName',
            'caller_user': 'callerUser',
            'deleted': 'deleted',
            'note': 'note',
            'user': 'user',
            'group': 'group',
            'queue': 'queue',
            'copied_from': 'copiedFrom',
            'copied_to': 'copiedTo',
            'delete_retention_policy': 'deleteRetentionPolicy',
            'self_uri': 'selfUri'
        }

        self._id = None
        self._conversation = None
        self._read = None
        self._audio_recording_duration_seconds = None
        self._audio_recording_size_bytes = None
        self._transcription = None
        self._created_date = None
        self._modified_date = None
        self._deleted_date = None
        self._caller_address = None
        self._caller_name = None
        self._caller_user = None
        self._deleted = None
        self._note = None
        self._user = None
        self._group = None
        self._queue = None
        self._copied_from = None
        self._copied_to = None
        self._delete_retention_policy = None
        self._self_uri = None

    @property
    def id(self) -> str:
        """
        Gets the id of this VoicemailMessage.
        The globally unique identifier for the object.

        :return: The id of this VoicemailMessage.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id: str) -> None:
        """
        Sets the id of this VoicemailMessage.
        The globally unique identifier for the object.

        :param id: The id of this VoicemailMessage.
        :type: str
        """
        

        self._id = id

    @property
    def conversation(self) -> 'Conversation':
        """
        Gets the conversation of this VoicemailMessage.
        The conversation that the voicemail message is associated with

        :return: The conversation of this VoicemailMessage.
        :rtype: Conversation
        """
        return self._conversation

    @conversation.setter
    def conversation(self, conversation: 'Conversation') -> None:
        """
        Sets the conversation of this VoicemailMessage.
        The conversation that the voicemail message is associated with

        :param conversation: The conversation of this VoicemailMessage.
        :type: Conversation
        """
        

        self._conversation = conversation

    @property
    def read(self) -> bool:
        """
        Gets the read of this VoicemailMessage.
        Whether the voicemail message is marked as read

        :return: The read of this VoicemailMessage.
        :rtype: bool
        """
        return self._read

    @read.setter
    def read(self, read: bool) -> None:
        """
        Sets the read of this VoicemailMessage.
        Whether the voicemail message is marked as read

        :param read: The read of this VoicemailMessage.
        :type: bool
        """
        

        self._read = read

    @property
    def audio_recording_duration_seconds(self) -> int:
        """
        Gets the audio_recording_duration_seconds of this VoicemailMessage.
        The voicemail message's audio recording duration in seconds

        :return: The audio_recording_duration_seconds of this VoicemailMessage.
        :rtype: int
        """
        return self._audio_recording_duration_seconds

    @audio_recording_duration_seconds.setter
    def audio_recording_duration_seconds(self, audio_recording_duration_seconds: int) -> None:
        """
        Sets the audio_recording_duration_seconds of this VoicemailMessage.
        The voicemail message's audio recording duration in seconds

        :param audio_recording_duration_seconds: The audio_recording_duration_seconds of this VoicemailMessage.
        :type: int
        """
        

        self._audio_recording_duration_seconds = audio_recording_duration_seconds

    @property
    def audio_recording_size_bytes(self) -> int:
        """
        Gets the audio_recording_size_bytes of this VoicemailMessage.
        The voicemail message's audio recording size in bytes

        :return: The audio_recording_size_bytes of this VoicemailMessage.
        :rtype: int
        """
        return self._audio_recording_size_bytes

    @audio_recording_size_bytes.setter
    def audio_recording_size_bytes(self, audio_recording_size_bytes: int) -> None:
        """
        Sets the audio_recording_size_bytes of this VoicemailMessage.
        The voicemail message's audio recording size in bytes

        :param audio_recording_size_bytes: The audio_recording_size_bytes of this VoicemailMessage.
        :type: int
        """
        

        self._audio_recording_size_bytes = audio_recording_size_bytes

    @property
    def transcription(self) -> str:
        """
        Gets the transcription of this VoicemailMessage.
        The transcription of the voicemail's audio

        :return: The transcription of this VoicemailMessage.
        :rtype: str
        """
        return self._transcription

    @transcription.setter
    def transcription(self, transcription: str) -> None:
        """
        Sets the transcription of this VoicemailMessage.
        The transcription of the voicemail's audio

        :param transcription: The transcription of this VoicemailMessage.
        :type: str
        """
        

        self._transcription = transcription

    @property
    def created_date(self) -> datetime:
        """
        Gets the created_date of this VoicemailMessage.
        The date the voicemail message was created. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z

        :return: The created_date of this VoicemailMessage.
        :rtype: datetime
        """
        return self._created_date

    @created_date.setter
    def created_date(self, created_date: datetime) -> None:
        """
        Sets the created_date of this VoicemailMessage.
        The date the voicemail message was created. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z

        :param created_date: The created_date of this VoicemailMessage.
        :type: datetime
        """
        

        self._created_date = created_date

    @property
    def modified_date(self) -> datetime:
        """
        Gets the modified_date of this VoicemailMessage.
        The date the voicemail message was last modified. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z

        :return: The modified_date of this VoicemailMessage.
        :rtype: datetime
        """
        return self._modified_date

    @modified_date.setter
    def modified_date(self, modified_date: datetime) -> None:
        """
        Sets the modified_date of this VoicemailMessage.
        The date the voicemail message was last modified. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z

        :param modified_date: The modified_date of this VoicemailMessage.
        :type: datetime
        """
        

        self._modified_date = modified_date

    @property
    def deleted_date(self) -> datetime:
        """
        Gets the deleted_date of this VoicemailMessage.
        The date the voicemail message deleted property was set to true. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z

        :return: The deleted_date of this VoicemailMessage.
        :rtype: datetime
        """
        return self._deleted_date

    @deleted_date.setter
    def deleted_date(self, deleted_date: datetime) -> None:
        """
        Sets the deleted_date of this VoicemailMessage.
        The date the voicemail message deleted property was set to true. Date time is represented as an ISO-8601 string. For example: yyyy-MM-ddTHH:mm:ss[.mmm]Z

        :param deleted_date: The deleted_date of this VoicemailMessage.
        :type: datetime
        """
        

        self._deleted_date = deleted_date

    @property
    def caller_address(self) -> str:
        """
        Gets the caller_address of this VoicemailMessage.
        The caller address

        :return: The caller_address of this VoicemailMessage.
        :rtype: str
        """
        return self._caller_address

    @caller_address.setter
    def caller_address(self, caller_address: str) -> None:
        """
        Sets the caller_address of this VoicemailMessage.
        The caller address

        :param caller_address: The caller_address of this VoicemailMessage.
        :type: str
        """
        

        self._caller_address = caller_address

    @property
    def caller_name(self) -> str:
        """
        Gets the caller_name of this VoicemailMessage.
        Optionally the name of the caller that left the voicemail message if the caller was a known user

        :return: The caller_name of this VoicemailMessage.
        :rtype: str
        """
        return self._caller_name

    @caller_name.setter
    def caller_name(self, caller_name: str) -> None:
        """
        Sets the caller_name of this VoicemailMessage.
        Optionally the name of the caller that left the voicemail message if the caller was a known user

        :param caller_name: The caller_name of this VoicemailMessage.
        :type: str
        """
        

        self._caller_name = caller_name

    @property
    def caller_user(self) -> 'User':
        """
        Gets the caller_user of this VoicemailMessage.
        Optionally the user that left the voicemail message if the caller was a known user

        :return: The caller_user of this VoicemailMessage.
        :rtype: User
        """
        return self._caller_user

    @caller_user.setter
    def caller_user(self, caller_user: 'User') -> None:
        """
        Sets the caller_user of this VoicemailMessage.
        Optionally the user that left the voicemail message if the caller was a known user

        :param caller_user: The caller_user of this VoicemailMessage.
        :type: User
        """
        

        self._caller_user = caller_user

    @property
    def deleted(self) -> bool:
        """
        Gets the deleted of this VoicemailMessage.
        Whether the voicemail message has been marked as deleted

        :return: The deleted of this VoicemailMessage.
        :rtype: bool
        """
        return self._deleted

    @deleted.setter
    def deleted(self, deleted: bool) -> None:
        """
        Sets the deleted of this VoicemailMessage.
        Whether the voicemail message has been marked as deleted

        :param deleted: The deleted of this VoicemailMessage.
        :type: bool
        """
        

        self._deleted = deleted

    @property
    def note(self) -> str:
        """
        Gets the note of this VoicemailMessage.
        An optional note

        :return: The note of this VoicemailMessage.
        :rtype: str
        """
        return self._note

    @note.setter
    def note(self, note: str) -> None:
        """
        Sets the note of this VoicemailMessage.
        An optional note

        :param note: The note of this VoicemailMessage.
        :type: str
        """
        

        self._note = note

    @property
    def user(self) -> 'User':
        """
        Gets the user of this VoicemailMessage.
        The user that the voicemail message belongs to or null which means the voicemail message belongs to a group or queue

        :return: The user of this VoicemailMessage.
        :rtype: User
        """
        return self._user

    @user.setter
    def user(self, user: 'User') -> None:
        """
        Sets the user of this VoicemailMessage.
        The user that the voicemail message belongs to or null which means the voicemail message belongs to a group or queue

        :param user: The user of this VoicemailMessage.
        :type: User
        """
        

        self._user = user

    @property
    def group(self) -> 'Group':
        """
        Gets the group of this VoicemailMessage.
        The group that the voicemail message belongs to or null which means the voicemail message belongs to a user or queue

        :return: The group of this VoicemailMessage.
        :rtype: Group
        """
        return self._group

    @group.setter
    def group(self, group: 'Group') -> None:
        """
        Sets the group of this VoicemailMessage.
        The group that the voicemail message belongs to or null which means the voicemail message belongs to a user or queue

        :param group: The group of this VoicemailMessage.
        :type: Group
        """
        

        self._group = group

    @property
    def queue(self) -> 'Queue':
        """
        Gets the queue of this VoicemailMessage.
        The queue that the voicemail message belongs to or null which means the voicemail message belongs to a user or group

        :return: The queue of this VoicemailMessage.
        :rtype: Queue
        """
        return self._queue

    @queue.setter
    def queue(self, queue: 'Queue') -> None:
        """
        Sets the queue of this VoicemailMessage.
        The queue that the voicemail message belongs to or null which means the voicemail message belongs to a user or group

        :param queue: The queue of this VoicemailMessage.
        :type: Queue
        """
        

        self._queue = queue

    @property
    def copied_from(self) -> 'VoicemailCopyRecord':
        """
        Gets the copied_from of this VoicemailMessage.
        Represents where this voicemail message was copied from

        :return: The copied_from of this VoicemailMessage.
        :rtype: VoicemailCopyRecord
        """
        return self._copied_from

    @copied_from.setter
    def copied_from(self, copied_from: 'VoicemailCopyRecord') -> None:
        """
        Sets the copied_from of this VoicemailMessage.
        Represents where this voicemail message was copied from

        :param copied_from: The copied_from of this VoicemailMessage.
        :type: VoicemailCopyRecord
        """
        

        self._copied_from = copied_from

    @property
    def copied_to(self) -> List['VoicemailCopyRecord']:
        """
        Gets the copied_to of this VoicemailMessage.
        Represents where this voicemail has been copied to

        :return: The copied_to of this VoicemailMessage.
        :rtype: list[VoicemailCopyRecord]
        """
        return self._copied_to

    @copied_to.setter
    def copied_to(self, copied_to: List['VoicemailCopyRecord']) -> None:
        """
        Sets the copied_to of this VoicemailMessage.
        Represents where this voicemail has been copied to

        :param copied_to: The copied_to of this VoicemailMessage.
        :type: list[VoicemailCopyRecord]
        """
        

        self._copied_to = copied_to

    @property
    def delete_retention_policy(self) -> 'VoicemailRetentionPolicy':
        """
        Gets the delete_retention_policy of this VoicemailMessage.
        The retention policy for this voicemail when deleted is set to true

        :return: The delete_retention_policy of this VoicemailMessage.
        :rtype: VoicemailRetentionPolicy
        """
        return self._delete_retention_policy

    @delete_retention_policy.setter
    def delete_retention_policy(self, delete_retention_policy: 'VoicemailRetentionPolicy') -> None:
        """
        Sets the delete_retention_policy of this VoicemailMessage.
        The retention policy for this voicemail when deleted is set to true

        :param delete_retention_policy: The delete_retention_policy of this VoicemailMessage.
        :type: VoicemailRetentionPolicy
        """
        

        self._delete_retention_policy = delete_retention_policy

    @property
    def self_uri(self) -> str:
        """
        Gets the self_uri of this VoicemailMessage.
        The URI for this object

        :return: The self_uri of this VoicemailMessage.
        :rtype: str
        """
        return self._self_uri

    @self_uri.setter
    def self_uri(self, self_uri: str) -> None:
        """
        Sets the self_uri of this VoicemailMessage.
        The URI for this object

        :param self_uri: The self_uri of this VoicemailMessage.
        :type: str
        """
        

        self._self_uri = self_uri

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in self.swagger_types.items():
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_json(self):
        """
        Returns the model as raw JSON
        """
        return json.dumps(sanitize_for_serialization(self.to_dict()))

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other

