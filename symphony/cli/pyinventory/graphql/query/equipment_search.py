#!/usr/bin/env python3
# @generated AUTOGENERATED file. Do not Change!

from dataclasses import dataclass
from datetime import datetime
from gql.gql.datetime_utils import DATETIME_FIELD
from gql.gql.graphql_client import GraphqlClient
from gql.gql.client import OperationException
from gql.gql.reporter import FailedOperationException
from functools import partial
from numbers import Number
from typing import Any, Callable, List, Mapping, Optional
from time import perf_counter
from dataclasses_json import DataClassJsonMixin

from ..fragment.equipment import EquipmentFragment, QUERY as EquipmentFragmentQuery
from ..input.equipment_filter import EquipmentFilterInput


QUERY: List[str] = EquipmentFragmentQuery + ["""
query EquipmentSearchQuery($filters: [EquipmentFilterInput!]!, $limit: Int) {
  equipmentSearch(filters: $filters, limit: $limit) {
    equipment {
      ...EquipmentFragment
    }
    count
  }
}

"""]

@dataclass
class EquipmentSearchQuery(DataClassJsonMixin):
    @dataclass
    class EquipmentSearchQueryData(DataClassJsonMixin):
        @dataclass
        class EquipmentSearchResult(DataClassJsonMixin):
            @dataclass
            class Equipment(EquipmentFragment):
                pass

            equipment: List[Equipment]
            count: int

        equipmentSearch: EquipmentSearchResult

    data: EquipmentSearchQueryData

    @classmethod
    # fmt: off
    def execute(cls, client: GraphqlClient, filters: List[EquipmentFilterInput] = [], limit: Optional[int] = None) -> EquipmentSearchQueryData.EquipmentSearchResult:
        # fmt: off
        variables = {"filters": filters, "limit": limit}
        try:
            start_time = perf_counter()
            response_text = client.call(''.join(set(QUERY)), variables=variables)
            res = cls.from_json(response_text).data
            elapsed_time = perf_counter() - start_time
            client.reporter.log_successful_operation("EquipmentSearchQuery", variables, elapsed_time)
            return res.equipmentSearch
        except OperationException as e:
            raise FailedOperationException(
                client.reporter,
                e.err_msg,
                e.err_id,
                "EquipmentSearchQuery",
                variables,
            )