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
    from . import EdgeMetricsTopicEdgeMetricDisk
    from . import EdgeMetricsTopicEdgeMetricMemory
    from . import EdgeMetricsTopicEdgeMetricNetworks
    from . import EdgeMetricsTopicEdgeMetricProcessor
    from . import EdgeMetricsTopicEdgeMetricSubsystem
    from . import EdgeMetricsTopicUriReference

class EdgeMetricsTopicEdgeMetrics(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self) -> None:
        """
        EdgeMetricsTopicEdgeMetrics - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'edge': 'EdgeMetricsTopicUriReference',
            'event_time': 'datetime',
            'up_time_msec': 'int',
            'processors': 'list[EdgeMetricsTopicEdgeMetricProcessor]',
            'memory': 'list[EdgeMetricsTopicEdgeMetricMemory]',
            'disks': 'list[EdgeMetricsTopicEdgeMetricDisk]',
            'subsystems': 'list[EdgeMetricsTopicEdgeMetricSubsystem]',
            'networks': 'list[EdgeMetricsTopicEdgeMetricNetworks]'
        }

        self.attribute_map = {
            'edge': 'edge',
            'event_time': 'eventTime',
            'up_time_msec': 'upTimeMsec',
            'processors': 'processors',
            'memory': 'memory',
            'disks': 'disks',
            'subsystems': 'subsystems',
            'networks': 'networks'
        }

        self._edge = None
        self._event_time = None
        self._up_time_msec = None
        self._processors = None
        self._memory = None
        self._disks = None
        self._subsystems = None
        self._networks = None

    @property
    def edge(self) -> 'EdgeMetricsTopicUriReference':
        """
        Gets the edge of this EdgeMetricsTopicEdgeMetrics.


        :return: The edge of this EdgeMetricsTopicEdgeMetrics.
        :rtype: EdgeMetricsTopicUriReference
        """
        return self._edge

    @edge.setter
    def edge(self, edge: 'EdgeMetricsTopicUriReference') -> None:
        """
        Sets the edge of this EdgeMetricsTopicEdgeMetrics.


        :param edge: The edge of this EdgeMetricsTopicEdgeMetrics.
        :type: EdgeMetricsTopicUriReference
        """
        

        self._edge = edge

    @property
    def event_time(self) -> datetime:
        """
        Gets the event_time of this EdgeMetricsTopicEdgeMetrics.


        :return: The event_time of this EdgeMetricsTopicEdgeMetrics.
        :rtype: datetime
        """
        return self._event_time

    @event_time.setter
    def event_time(self, event_time: datetime) -> None:
        """
        Sets the event_time of this EdgeMetricsTopicEdgeMetrics.


        :param event_time: The event_time of this EdgeMetricsTopicEdgeMetrics.
        :type: datetime
        """
        

        self._event_time = event_time

    @property
    def up_time_msec(self) -> int:
        """
        Gets the up_time_msec of this EdgeMetricsTopicEdgeMetrics.


        :return: The up_time_msec of this EdgeMetricsTopicEdgeMetrics.
        :rtype: int
        """
        return self._up_time_msec

    @up_time_msec.setter
    def up_time_msec(self, up_time_msec: int) -> None:
        """
        Sets the up_time_msec of this EdgeMetricsTopicEdgeMetrics.


        :param up_time_msec: The up_time_msec of this EdgeMetricsTopicEdgeMetrics.
        :type: int
        """
        

        self._up_time_msec = up_time_msec

    @property
    def processors(self) -> List['EdgeMetricsTopicEdgeMetricProcessor']:
        """
        Gets the processors of this EdgeMetricsTopicEdgeMetrics.


        :return: The processors of this EdgeMetricsTopicEdgeMetrics.
        :rtype: list[EdgeMetricsTopicEdgeMetricProcessor]
        """
        return self._processors

    @processors.setter
    def processors(self, processors: List['EdgeMetricsTopicEdgeMetricProcessor']) -> None:
        """
        Sets the processors of this EdgeMetricsTopicEdgeMetrics.


        :param processors: The processors of this EdgeMetricsTopicEdgeMetrics.
        :type: list[EdgeMetricsTopicEdgeMetricProcessor]
        """
        

        self._processors = processors

    @property
    def memory(self) -> List['EdgeMetricsTopicEdgeMetricMemory']:
        """
        Gets the memory of this EdgeMetricsTopicEdgeMetrics.


        :return: The memory of this EdgeMetricsTopicEdgeMetrics.
        :rtype: list[EdgeMetricsTopicEdgeMetricMemory]
        """
        return self._memory

    @memory.setter
    def memory(self, memory: List['EdgeMetricsTopicEdgeMetricMemory']) -> None:
        """
        Sets the memory of this EdgeMetricsTopicEdgeMetrics.


        :param memory: The memory of this EdgeMetricsTopicEdgeMetrics.
        :type: list[EdgeMetricsTopicEdgeMetricMemory]
        """
        

        self._memory = memory

    @property
    def disks(self) -> List['EdgeMetricsTopicEdgeMetricDisk']:
        """
        Gets the disks of this EdgeMetricsTopicEdgeMetrics.


        :return: The disks of this EdgeMetricsTopicEdgeMetrics.
        :rtype: list[EdgeMetricsTopicEdgeMetricDisk]
        """
        return self._disks

    @disks.setter
    def disks(self, disks: List['EdgeMetricsTopicEdgeMetricDisk']) -> None:
        """
        Sets the disks of this EdgeMetricsTopicEdgeMetrics.


        :param disks: The disks of this EdgeMetricsTopicEdgeMetrics.
        :type: list[EdgeMetricsTopicEdgeMetricDisk]
        """
        

        self._disks = disks

    @property
    def subsystems(self) -> List['EdgeMetricsTopicEdgeMetricSubsystem']:
        """
        Gets the subsystems of this EdgeMetricsTopicEdgeMetrics.


        :return: The subsystems of this EdgeMetricsTopicEdgeMetrics.
        :rtype: list[EdgeMetricsTopicEdgeMetricSubsystem]
        """
        return self._subsystems

    @subsystems.setter
    def subsystems(self, subsystems: List['EdgeMetricsTopicEdgeMetricSubsystem']) -> None:
        """
        Sets the subsystems of this EdgeMetricsTopicEdgeMetrics.


        :param subsystems: The subsystems of this EdgeMetricsTopicEdgeMetrics.
        :type: list[EdgeMetricsTopicEdgeMetricSubsystem]
        """
        

        self._subsystems = subsystems

    @property
    def networks(self) -> List['EdgeMetricsTopicEdgeMetricNetworks']:
        """
        Gets the networks of this EdgeMetricsTopicEdgeMetrics.


        :return: The networks of this EdgeMetricsTopicEdgeMetrics.
        :rtype: list[EdgeMetricsTopicEdgeMetricNetworks]
        """
        return self._networks

    @networks.setter
    def networks(self, networks: List['EdgeMetricsTopicEdgeMetricNetworks']) -> None:
        """
        Sets the networks of this EdgeMetricsTopicEdgeMetrics.


        :param networks: The networks of this EdgeMetricsTopicEdgeMetrics.
        :type: list[EdgeMetricsTopicEdgeMetricNetworks]
        """
        

        self._networks = networks

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

