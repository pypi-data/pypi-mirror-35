# -*- coding: utf-8 -*-

# Copyright 2018 ICON Foundation
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from typing import TYPE_CHECKING, List, Optional

from ..base.address import Address

if TYPE_CHECKING:
    from .icon_score_base2 import BaseType

INDEXED_ARGS_LIMIT = 3


class EventLog(object):
    """ A DataClass of a event log.
    """

    def __init__(
            self,
            score_address: 'Address',
            indexed: List['BaseType'] = None,
            data: List['BaseType'] = None) -> None:
        """
        Constructor

        :param score_address: an address of SCORE in which the event is invoked
        :param indexed: a list of indexed arguments including a event signature
        :param data: a list of normal arguments
        """
        self.score_address: 'Address' = score_address
        self.indexed: 'List[BaseType]' = indexed
        self.data: 'List[BaseType]' = data

    def __str__(self) -> str:
        return '\n'.join([f'{k}: {v}' for k, v in self.__dict__.items()])

    def to_dict(self, casing: Optional = None) -> dict:
        """
        Returns properties as `dict`
        :return: a dict
        """
        new_dict = {}
        for key, value in self.__dict__.items():
            if value is None:
                # Excludes properties which have `None` value
                continue

            new_dict[casing(key) if casing else key] = value

        return new_dict
