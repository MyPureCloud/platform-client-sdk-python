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
    from . import WorkitemsAttributeChangeBoolean
    from . import WorkitemsAttributeChangeInstant
    from . import WorkitemsAttributeChangeInteger
    from . import WorkitemsAttributeChangeList
    from . import WorkitemsAttributeChangeListWorkitemScoredAgentDelta
    from . import WorkitemsAttributeChangeMap
    from . import WorkitemsAttributeChangeString
    from . import WorkitemsAttributeChangeWorkitemStatusCategory
    from . import WorkitemsAttributeChangeWrapupDelta

class WorkitemDelta(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self) -> None:
        """
        WorkitemDelta - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'name': 'WorkitemsAttributeChangeString',
            'description': 'WorkitemsAttributeChangeString',
            'language_id': 'WorkitemsAttributeChangeString',
            'utilization_label_id': 'WorkitemsAttributeChangeString',
            'priority': 'WorkitemsAttributeChangeInteger',
            'skill_ids': 'WorkitemsAttributeChangeList',
            'preferred_agent_ids': 'WorkitemsAttributeChangeList',
            'date_due': 'WorkitemsAttributeChangeInstant',
            'date_expires': 'WorkitemsAttributeChangeInstant',
            'duration_seconds': 'WorkitemsAttributeChangeInteger',
            'status_id': 'WorkitemsAttributeChangeString',
            'reporter_id': 'WorkitemsAttributeChangeString',
            'external_contact_id': 'WorkitemsAttributeChangeString',
            'assignee_id': 'WorkitemsAttributeChangeString',
            'workbin_id': 'WorkitemsAttributeChangeString',
            'queue_id': 'WorkitemsAttributeChangeString',
            'external_tag': 'WorkitemsAttributeChangeString',
            'wrapup_id': 'WorkitemsAttributeChangeString',
            'wrapup': 'WorkitemsAttributeChangeWrapupDelta',
            'ttl': 'WorkitemsAttributeChangeInteger',
            'date_closed': 'WorkitemsAttributeChangeInstant',
            'assignment_state': 'WorkitemsAttributeChangeString',
            'auto_status_transition': 'WorkitemsAttributeChangeBoolean',
            'custom_fields': 'WorkitemsAttributeChangeMap',
            'date_modified': 'WorkitemsAttributeChangeInstant',
            'modified_by': 'WorkitemsAttributeChangeString',
            'status_category': 'WorkitemsAttributeChangeWorkitemStatusCategory',
            'script_id': 'WorkitemsAttributeChangeString',
            'date_assignment_state_changed': 'WorkitemsAttributeChangeInstant',
            'alert_timeout_seconds': 'WorkitemsAttributeChangeInteger',
            'scored_agents': 'WorkitemsAttributeChangeListWorkitemScoredAgentDelta'
        }

        self.attribute_map = {
            'name': 'name',
            'description': 'description',
            'language_id': 'languageId',
            'utilization_label_id': 'utilizationLabelId',
            'priority': 'priority',
            'skill_ids': 'skillIds',
            'preferred_agent_ids': 'preferredAgentIds',
            'date_due': 'dateDue',
            'date_expires': 'dateExpires',
            'duration_seconds': 'durationSeconds',
            'status_id': 'statusId',
            'reporter_id': 'reporterId',
            'external_contact_id': 'externalContactId',
            'assignee_id': 'assigneeId',
            'workbin_id': 'workbinId',
            'queue_id': 'queueId',
            'external_tag': 'externalTag',
            'wrapup_id': 'wrapupId',
            'wrapup': 'wrapup',
            'ttl': 'ttl',
            'date_closed': 'dateClosed',
            'assignment_state': 'assignmentState',
            'auto_status_transition': 'autoStatusTransition',
            'custom_fields': 'customFields',
            'date_modified': 'dateModified',
            'modified_by': 'modifiedBy',
            'status_category': 'statusCategory',
            'script_id': 'scriptId',
            'date_assignment_state_changed': 'dateAssignmentStateChanged',
            'alert_timeout_seconds': 'alertTimeoutSeconds',
            'scored_agents': 'scoredAgents'
        }

        self._name = None
        self._description = None
        self._language_id = None
        self._utilization_label_id = None
        self._priority = None
        self._skill_ids = None
        self._preferred_agent_ids = None
        self._date_due = None
        self._date_expires = None
        self._duration_seconds = None
        self._status_id = None
        self._reporter_id = None
        self._external_contact_id = None
        self._assignee_id = None
        self._workbin_id = None
        self._queue_id = None
        self._external_tag = None
        self._wrapup_id = None
        self._wrapup = None
        self._ttl = None
        self._date_closed = None
        self._assignment_state = None
        self._auto_status_transition = None
        self._custom_fields = None
        self._date_modified = None
        self._modified_by = None
        self._status_category = None
        self._script_id = None
        self._date_assignment_state_changed = None
        self._alert_timeout_seconds = None
        self._scored_agents = None

    @property
    def name(self) -> 'WorkitemsAttributeChangeString':
        """
        Gets the name of this WorkitemDelta.


        :return: The name of this WorkitemDelta.
        :rtype: WorkitemsAttributeChangeString
        """
        return self._name

    @name.setter
    def name(self, name: 'WorkitemsAttributeChangeString') -> None:
        """
        Sets the name of this WorkitemDelta.


        :param name: The name of this WorkitemDelta.
        :type: WorkitemsAttributeChangeString
        """
        

        self._name = name

    @property
    def description(self) -> 'WorkitemsAttributeChangeString':
        """
        Gets the description of this WorkitemDelta.


        :return: The description of this WorkitemDelta.
        :rtype: WorkitemsAttributeChangeString
        """
        return self._description

    @description.setter
    def description(self, description: 'WorkitemsAttributeChangeString') -> None:
        """
        Sets the description of this WorkitemDelta.


        :param description: The description of this WorkitemDelta.
        :type: WorkitemsAttributeChangeString
        """
        

        self._description = description

    @property
    def language_id(self) -> 'WorkitemsAttributeChangeString':
        """
        Gets the language_id of this WorkitemDelta.


        :return: The language_id of this WorkitemDelta.
        :rtype: WorkitemsAttributeChangeString
        """
        return self._language_id

    @language_id.setter
    def language_id(self, language_id: 'WorkitemsAttributeChangeString') -> None:
        """
        Sets the language_id of this WorkitemDelta.


        :param language_id: The language_id of this WorkitemDelta.
        :type: WorkitemsAttributeChangeString
        """
        

        self._language_id = language_id

    @property
    def utilization_label_id(self) -> 'WorkitemsAttributeChangeString':
        """
        Gets the utilization_label_id of this WorkitemDelta.


        :return: The utilization_label_id of this WorkitemDelta.
        :rtype: WorkitemsAttributeChangeString
        """
        return self._utilization_label_id

    @utilization_label_id.setter
    def utilization_label_id(self, utilization_label_id: 'WorkitemsAttributeChangeString') -> None:
        """
        Sets the utilization_label_id of this WorkitemDelta.


        :param utilization_label_id: The utilization_label_id of this WorkitemDelta.
        :type: WorkitemsAttributeChangeString
        """
        

        self._utilization_label_id = utilization_label_id

    @property
    def priority(self) -> 'WorkitemsAttributeChangeInteger':
        """
        Gets the priority of this WorkitemDelta.


        :return: The priority of this WorkitemDelta.
        :rtype: WorkitemsAttributeChangeInteger
        """
        return self._priority

    @priority.setter
    def priority(self, priority: 'WorkitemsAttributeChangeInteger') -> None:
        """
        Sets the priority of this WorkitemDelta.


        :param priority: The priority of this WorkitemDelta.
        :type: WorkitemsAttributeChangeInteger
        """
        

        self._priority = priority

    @property
    def skill_ids(self) -> 'WorkitemsAttributeChangeList':
        """
        Gets the skill_ids of this WorkitemDelta.


        :return: The skill_ids of this WorkitemDelta.
        :rtype: WorkitemsAttributeChangeList
        """
        return self._skill_ids

    @skill_ids.setter
    def skill_ids(self, skill_ids: 'WorkitemsAttributeChangeList') -> None:
        """
        Sets the skill_ids of this WorkitemDelta.


        :param skill_ids: The skill_ids of this WorkitemDelta.
        :type: WorkitemsAttributeChangeList
        """
        

        self._skill_ids = skill_ids

    @property
    def preferred_agent_ids(self) -> 'WorkitemsAttributeChangeList':
        """
        Gets the preferred_agent_ids of this WorkitemDelta.


        :return: The preferred_agent_ids of this WorkitemDelta.
        :rtype: WorkitemsAttributeChangeList
        """
        return self._preferred_agent_ids

    @preferred_agent_ids.setter
    def preferred_agent_ids(self, preferred_agent_ids: 'WorkitemsAttributeChangeList') -> None:
        """
        Sets the preferred_agent_ids of this WorkitemDelta.


        :param preferred_agent_ids: The preferred_agent_ids of this WorkitemDelta.
        :type: WorkitemsAttributeChangeList
        """
        

        self._preferred_agent_ids = preferred_agent_ids

    @property
    def date_due(self) -> 'WorkitemsAttributeChangeInstant':
        """
        Gets the date_due of this WorkitemDelta.


        :return: The date_due of this WorkitemDelta.
        :rtype: WorkitemsAttributeChangeInstant
        """
        return self._date_due

    @date_due.setter
    def date_due(self, date_due: 'WorkitemsAttributeChangeInstant') -> None:
        """
        Sets the date_due of this WorkitemDelta.


        :param date_due: The date_due of this WorkitemDelta.
        :type: WorkitemsAttributeChangeInstant
        """
        

        self._date_due = date_due

    @property
    def date_expires(self) -> 'WorkitemsAttributeChangeInstant':
        """
        Gets the date_expires of this WorkitemDelta.


        :return: The date_expires of this WorkitemDelta.
        :rtype: WorkitemsAttributeChangeInstant
        """
        return self._date_expires

    @date_expires.setter
    def date_expires(self, date_expires: 'WorkitemsAttributeChangeInstant') -> None:
        """
        Sets the date_expires of this WorkitemDelta.


        :param date_expires: The date_expires of this WorkitemDelta.
        :type: WorkitemsAttributeChangeInstant
        """
        

        self._date_expires = date_expires

    @property
    def duration_seconds(self) -> 'WorkitemsAttributeChangeInteger':
        """
        Gets the duration_seconds of this WorkitemDelta.


        :return: The duration_seconds of this WorkitemDelta.
        :rtype: WorkitemsAttributeChangeInteger
        """
        return self._duration_seconds

    @duration_seconds.setter
    def duration_seconds(self, duration_seconds: 'WorkitemsAttributeChangeInteger') -> None:
        """
        Sets the duration_seconds of this WorkitemDelta.


        :param duration_seconds: The duration_seconds of this WorkitemDelta.
        :type: WorkitemsAttributeChangeInteger
        """
        

        self._duration_seconds = duration_seconds

    @property
    def status_id(self) -> 'WorkitemsAttributeChangeString':
        """
        Gets the status_id of this WorkitemDelta.


        :return: The status_id of this WorkitemDelta.
        :rtype: WorkitemsAttributeChangeString
        """
        return self._status_id

    @status_id.setter
    def status_id(self, status_id: 'WorkitemsAttributeChangeString') -> None:
        """
        Sets the status_id of this WorkitemDelta.


        :param status_id: The status_id of this WorkitemDelta.
        :type: WorkitemsAttributeChangeString
        """
        

        self._status_id = status_id

    @property
    def reporter_id(self) -> 'WorkitemsAttributeChangeString':
        """
        Gets the reporter_id of this WorkitemDelta.


        :return: The reporter_id of this WorkitemDelta.
        :rtype: WorkitemsAttributeChangeString
        """
        return self._reporter_id

    @reporter_id.setter
    def reporter_id(self, reporter_id: 'WorkitemsAttributeChangeString') -> None:
        """
        Sets the reporter_id of this WorkitemDelta.


        :param reporter_id: The reporter_id of this WorkitemDelta.
        :type: WorkitemsAttributeChangeString
        """
        

        self._reporter_id = reporter_id

    @property
    def external_contact_id(self) -> 'WorkitemsAttributeChangeString':
        """
        Gets the external_contact_id of this WorkitemDelta.


        :return: The external_contact_id of this WorkitemDelta.
        :rtype: WorkitemsAttributeChangeString
        """
        return self._external_contact_id

    @external_contact_id.setter
    def external_contact_id(self, external_contact_id: 'WorkitemsAttributeChangeString') -> None:
        """
        Sets the external_contact_id of this WorkitemDelta.


        :param external_contact_id: The external_contact_id of this WorkitemDelta.
        :type: WorkitemsAttributeChangeString
        """
        

        self._external_contact_id = external_contact_id

    @property
    def assignee_id(self) -> 'WorkitemsAttributeChangeString':
        """
        Gets the assignee_id of this WorkitemDelta.


        :return: The assignee_id of this WorkitemDelta.
        :rtype: WorkitemsAttributeChangeString
        """
        return self._assignee_id

    @assignee_id.setter
    def assignee_id(self, assignee_id: 'WorkitemsAttributeChangeString') -> None:
        """
        Sets the assignee_id of this WorkitemDelta.


        :param assignee_id: The assignee_id of this WorkitemDelta.
        :type: WorkitemsAttributeChangeString
        """
        

        self._assignee_id = assignee_id

    @property
    def workbin_id(self) -> 'WorkitemsAttributeChangeString':
        """
        Gets the workbin_id of this WorkitemDelta.


        :return: The workbin_id of this WorkitemDelta.
        :rtype: WorkitemsAttributeChangeString
        """
        return self._workbin_id

    @workbin_id.setter
    def workbin_id(self, workbin_id: 'WorkitemsAttributeChangeString') -> None:
        """
        Sets the workbin_id of this WorkitemDelta.


        :param workbin_id: The workbin_id of this WorkitemDelta.
        :type: WorkitemsAttributeChangeString
        """
        

        self._workbin_id = workbin_id

    @property
    def queue_id(self) -> 'WorkitemsAttributeChangeString':
        """
        Gets the queue_id of this WorkitemDelta.


        :return: The queue_id of this WorkitemDelta.
        :rtype: WorkitemsAttributeChangeString
        """
        return self._queue_id

    @queue_id.setter
    def queue_id(self, queue_id: 'WorkitemsAttributeChangeString') -> None:
        """
        Sets the queue_id of this WorkitemDelta.


        :param queue_id: The queue_id of this WorkitemDelta.
        :type: WorkitemsAttributeChangeString
        """
        

        self._queue_id = queue_id

    @property
    def external_tag(self) -> 'WorkitemsAttributeChangeString':
        """
        Gets the external_tag of this WorkitemDelta.


        :return: The external_tag of this WorkitemDelta.
        :rtype: WorkitemsAttributeChangeString
        """
        return self._external_tag

    @external_tag.setter
    def external_tag(self, external_tag: 'WorkitemsAttributeChangeString') -> None:
        """
        Sets the external_tag of this WorkitemDelta.


        :param external_tag: The external_tag of this WorkitemDelta.
        :type: WorkitemsAttributeChangeString
        """
        

        self._external_tag = external_tag

    @property
    def wrapup_id(self) -> 'WorkitemsAttributeChangeString':
        """
        Gets the wrapup_id of this WorkitemDelta.


        :return: The wrapup_id of this WorkitemDelta.
        :rtype: WorkitemsAttributeChangeString
        """
        return self._wrapup_id

    @wrapup_id.setter
    def wrapup_id(self, wrapup_id: 'WorkitemsAttributeChangeString') -> None:
        """
        Sets the wrapup_id of this WorkitemDelta.


        :param wrapup_id: The wrapup_id of this WorkitemDelta.
        :type: WorkitemsAttributeChangeString
        """
        

        self._wrapup_id = wrapup_id

    @property
    def wrapup(self) -> 'WorkitemsAttributeChangeWrapupDelta':
        """
        Gets the wrapup of this WorkitemDelta.


        :return: The wrapup of this WorkitemDelta.
        :rtype: WorkitemsAttributeChangeWrapupDelta
        """
        return self._wrapup

    @wrapup.setter
    def wrapup(self, wrapup: 'WorkitemsAttributeChangeWrapupDelta') -> None:
        """
        Sets the wrapup of this WorkitemDelta.


        :param wrapup: The wrapup of this WorkitemDelta.
        :type: WorkitemsAttributeChangeWrapupDelta
        """
        

        self._wrapup = wrapup

    @property
    def ttl(self) -> 'WorkitemsAttributeChangeInteger':
        """
        Gets the ttl of this WorkitemDelta.


        :return: The ttl of this WorkitemDelta.
        :rtype: WorkitemsAttributeChangeInteger
        """
        return self._ttl

    @ttl.setter
    def ttl(self, ttl: 'WorkitemsAttributeChangeInteger') -> None:
        """
        Sets the ttl of this WorkitemDelta.


        :param ttl: The ttl of this WorkitemDelta.
        :type: WorkitemsAttributeChangeInteger
        """
        

        self._ttl = ttl

    @property
    def date_closed(self) -> 'WorkitemsAttributeChangeInstant':
        """
        Gets the date_closed of this WorkitemDelta.


        :return: The date_closed of this WorkitemDelta.
        :rtype: WorkitemsAttributeChangeInstant
        """
        return self._date_closed

    @date_closed.setter
    def date_closed(self, date_closed: 'WorkitemsAttributeChangeInstant') -> None:
        """
        Sets the date_closed of this WorkitemDelta.


        :param date_closed: The date_closed of this WorkitemDelta.
        :type: WorkitemsAttributeChangeInstant
        """
        

        self._date_closed = date_closed

    @property
    def assignment_state(self) -> 'WorkitemsAttributeChangeString':
        """
        Gets the assignment_state of this WorkitemDelta.


        :return: The assignment_state of this WorkitemDelta.
        :rtype: WorkitemsAttributeChangeString
        """
        return self._assignment_state

    @assignment_state.setter
    def assignment_state(self, assignment_state: 'WorkitemsAttributeChangeString') -> None:
        """
        Sets the assignment_state of this WorkitemDelta.


        :param assignment_state: The assignment_state of this WorkitemDelta.
        :type: WorkitemsAttributeChangeString
        """
        

        self._assignment_state = assignment_state

    @property
    def auto_status_transition(self) -> 'WorkitemsAttributeChangeBoolean':
        """
        Gets the auto_status_transition of this WorkitemDelta.


        :return: The auto_status_transition of this WorkitemDelta.
        :rtype: WorkitemsAttributeChangeBoolean
        """
        return self._auto_status_transition

    @auto_status_transition.setter
    def auto_status_transition(self, auto_status_transition: 'WorkitemsAttributeChangeBoolean') -> None:
        """
        Sets the auto_status_transition of this WorkitemDelta.


        :param auto_status_transition: The auto_status_transition of this WorkitemDelta.
        :type: WorkitemsAttributeChangeBoolean
        """
        

        self._auto_status_transition = auto_status_transition

    @property
    def custom_fields(self) -> 'WorkitemsAttributeChangeMap':
        """
        Gets the custom_fields of this WorkitemDelta.


        :return: The custom_fields of this WorkitemDelta.
        :rtype: WorkitemsAttributeChangeMap
        """
        return self._custom_fields

    @custom_fields.setter
    def custom_fields(self, custom_fields: 'WorkitemsAttributeChangeMap') -> None:
        """
        Sets the custom_fields of this WorkitemDelta.


        :param custom_fields: The custom_fields of this WorkitemDelta.
        :type: WorkitemsAttributeChangeMap
        """
        

        self._custom_fields = custom_fields

    @property
    def date_modified(self) -> 'WorkitemsAttributeChangeInstant':
        """
        Gets the date_modified of this WorkitemDelta.


        :return: The date_modified of this WorkitemDelta.
        :rtype: WorkitemsAttributeChangeInstant
        """
        return self._date_modified

    @date_modified.setter
    def date_modified(self, date_modified: 'WorkitemsAttributeChangeInstant') -> None:
        """
        Sets the date_modified of this WorkitemDelta.


        :param date_modified: The date_modified of this WorkitemDelta.
        :type: WorkitemsAttributeChangeInstant
        """
        

        self._date_modified = date_modified

    @property
    def modified_by(self) -> 'WorkitemsAttributeChangeString':
        """
        Gets the modified_by of this WorkitemDelta.


        :return: The modified_by of this WorkitemDelta.
        :rtype: WorkitemsAttributeChangeString
        """
        return self._modified_by

    @modified_by.setter
    def modified_by(self, modified_by: 'WorkitemsAttributeChangeString') -> None:
        """
        Sets the modified_by of this WorkitemDelta.


        :param modified_by: The modified_by of this WorkitemDelta.
        :type: WorkitemsAttributeChangeString
        """
        

        self._modified_by = modified_by

    @property
    def status_category(self) -> 'WorkitemsAttributeChangeWorkitemStatusCategory':
        """
        Gets the status_category of this WorkitemDelta.


        :return: The status_category of this WorkitemDelta.
        :rtype: WorkitemsAttributeChangeWorkitemStatusCategory
        """
        return self._status_category

    @status_category.setter
    def status_category(self, status_category: 'WorkitemsAttributeChangeWorkitemStatusCategory') -> None:
        """
        Sets the status_category of this WorkitemDelta.


        :param status_category: The status_category of this WorkitemDelta.
        :type: WorkitemsAttributeChangeWorkitemStatusCategory
        """
        

        self._status_category = status_category

    @property
    def script_id(self) -> 'WorkitemsAttributeChangeString':
        """
        Gets the script_id of this WorkitemDelta.


        :return: The script_id of this WorkitemDelta.
        :rtype: WorkitemsAttributeChangeString
        """
        return self._script_id

    @script_id.setter
    def script_id(self, script_id: 'WorkitemsAttributeChangeString') -> None:
        """
        Sets the script_id of this WorkitemDelta.


        :param script_id: The script_id of this WorkitemDelta.
        :type: WorkitemsAttributeChangeString
        """
        

        self._script_id = script_id

    @property
    def date_assignment_state_changed(self) -> 'WorkitemsAttributeChangeInstant':
        """
        Gets the date_assignment_state_changed of this WorkitemDelta.


        :return: The date_assignment_state_changed of this WorkitemDelta.
        :rtype: WorkitemsAttributeChangeInstant
        """
        return self._date_assignment_state_changed

    @date_assignment_state_changed.setter
    def date_assignment_state_changed(self, date_assignment_state_changed: 'WorkitemsAttributeChangeInstant') -> None:
        """
        Sets the date_assignment_state_changed of this WorkitemDelta.


        :param date_assignment_state_changed: The date_assignment_state_changed of this WorkitemDelta.
        :type: WorkitemsAttributeChangeInstant
        """
        

        self._date_assignment_state_changed = date_assignment_state_changed

    @property
    def alert_timeout_seconds(self) -> 'WorkitemsAttributeChangeInteger':
        """
        Gets the alert_timeout_seconds of this WorkitemDelta.


        :return: The alert_timeout_seconds of this WorkitemDelta.
        :rtype: WorkitemsAttributeChangeInteger
        """
        return self._alert_timeout_seconds

    @alert_timeout_seconds.setter
    def alert_timeout_seconds(self, alert_timeout_seconds: 'WorkitemsAttributeChangeInteger') -> None:
        """
        Sets the alert_timeout_seconds of this WorkitemDelta.


        :param alert_timeout_seconds: The alert_timeout_seconds of this WorkitemDelta.
        :type: WorkitemsAttributeChangeInteger
        """
        

        self._alert_timeout_seconds = alert_timeout_seconds

    @property
    def scored_agents(self) -> 'WorkitemsAttributeChangeListWorkitemScoredAgentDelta':
        """
        Gets the scored_agents of this WorkitemDelta.


        :return: The scored_agents of this WorkitemDelta.
        :rtype: WorkitemsAttributeChangeListWorkitemScoredAgentDelta
        """
        return self._scored_agents

    @scored_agents.setter
    def scored_agents(self, scored_agents: 'WorkitemsAttributeChangeListWorkitemScoredAgentDelta') -> None:
        """
        Sets the scored_agents of this WorkitemDelta.


        :param scored_agents: The scored_agents of this WorkitemDelta.
        :type: WorkitemsAttributeChangeListWorkitemScoredAgentDelta
        """
        

        self._scored_agents = scored_agents

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

