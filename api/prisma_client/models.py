# -*- coding: utf-8 -*-
# code generated by Prisma. DO NOT EDIT.
# pyright: reportUnusedImport=false
# fmt: off

# global imports for type checking
from builtins import bool as _bool
from builtins import int as _int
from builtins import float as _float
from builtins import str as _str
import sys
import decimal
import datetime
from typing import (
    TYPE_CHECKING,
    Optional,
    Iterable,
    Iterator,
    Sequence,
    Callable,
    ClassVar,
    NoReturn,
    TypeVar,
    Generic,
    Mapping,
    Tuple,
    Union,
    List,
    Dict,
    Type,
    Any,
    Set,
    overload,
    cast,
)
from typing_extensions import TypedDict, Literal


LiteralString = str
# -- template models.py.jinja --
import os
import logging
import inspect
import warnings
from collections import OrderedDict

from pydantic import BaseModel, Field

from . import types, enums, errors, fields, bases
from ._types import FuncType
from ._compat import model_rebuild, field_validator
from ._builder import serialize_base64
from .generator import partial_models_ctx, PartialModelField


log: logging.Logger = logging.getLogger(__name__)
_created_partial_types: Set[str] = set()

class Application_logs(bases.BaseApplication_logs):
    """Represents a Application_logs record"""

    id: _int
    session_id: _str
    user_query: _str
    gpt_response: _str
    model: _str
    created_at: datetime.datetime

    # take *args and **kwargs so that other metaclasses can define arguments
    def __init_subclass__(
        cls,
        *args: Any,
        warn_subclass: Optional[bool] = None,
        **kwargs: Any,
    ) -> None:
        super().__init_subclass__()
        if warn_subclass is not None:
            warnings.warn(
                'The `warn_subclass` argument is deprecated as it is no longer necessary and will be removed in the next release',
                DeprecationWarning,
                stacklevel=3,
            )


    @staticmethod
    def create_partial(
        name: str,
        include: Optional[Iterable['types.Application_logsKeys']] = None,
        exclude: Optional[Iterable['types.Application_logsKeys']] = None,
        required: Optional[Iterable['types.Application_logsKeys']] = None,
        optional: Optional[Iterable['types.Application_logsKeys']] = None,
        relations: Optional[Mapping['types.Application_logsRelationalFieldKeys', str]] = None,
        exclude_relational_fields: bool = False,
    ) -> None:
        if not os.environ.get('PRISMA_GENERATOR_INVOCATION'):
            raise RuntimeError(
                'Attempted to create a partial type outside of client generation.'
            )

        if name in _created_partial_types:
            raise ValueError(f'Partial type "{name}" has already been created.')

        if include is not None:
            if exclude is not None:
                raise TypeError('Exclude and include are mutually exclusive.')
            if exclude_relational_fields is True:
                raise TypeError('Include and exclude_relational_fields=True are mutually exclusive.')

        if required and optional:
            shared = set(required) & set(optional)
            if shared:
                raise ValueError(f'Cannot make the same field(s) required and optional {shared}')

        if exclude_relational_fields and relations:
            raise ValueError(
                'exclude_relational_fields and relations are mutually exclusive'
            )

        fields: Dict['types.Application_logsKeys', PartialModelField] = OrderedDict()

        try:
            if include:
                for field in include:
                    fields[field] = _Application_logs_fields[field].copy()
            elif exclude:
                for field in exclude:
                    if field not in _Application_logs_fields:
                        raise KeyError(field)

                fields = {
                    key: data.copy()
                    for key, data in _Application_logs_fields.items()
                    if key not in exclude
                }
            else:
                fields = {
                    key: data.copy()
                    for key, data in _Application_logs_fields.items()
                }

            if required:
                for field in required:
                    fields[field]['optional'] = False

            if optional:
                for field in optional:
                    fields[field]['optional'] = True


            if relations:
                raise ValueError('Model: "Application_logs" has no relational fields.')
        except KeyError as exc:
            raise ValueError(
                f'{exc.args[0]} is not a valid Application_logs / {name} field.'
            ) from None

        models = partial_models_ctx.get()
        models.append(
            {
                'name': name,
                'fields': cast(Mapping[str, PartialModelField], fields),
                'from_model': 'Application_logs',
            }
        )
        _created_partial_types.add(name)


class Document_store(bases.BaseDocument_store):
    """Represents a Document_store record"""

    id: _int
    filename: _str
    upload_timestamp: datetime.datetime

    # take *args and **kwargs so that other metaclasses can define arguments
    def __init_subclass__(
        cls,
        *args: Any,
        warn_subclass: Optional[bool] = None,
        **kwargs: Any,
    ) -> None:
        super().__init_subclass__()
        if warn_subclass is not None:
            warnings.warn(
                'The `warn_subclass` argument is deprecated as it is no longer necessary and will be removed in the next release',
                DeprecationWarning,
                stacklevel=3,
            )


    @staticmethod
    def create_partial(
        name: str,
        include: Optional[Iterable['types.Document_storeKeys']] = None,
        exclude: Optional[Iterable['types.Document_storeKeys']] = None,
        required: Optional[Iterable['types.Document_storeKeys']] = None,
        optional: Optional[Iterable['types.Document_storeKeys']] = None,
        relations: Optional[Mapping['types.Document_storeRelationalFieldKeys', str]] = None,
        exclude_relational_fields: bool = False,
    ) -> None:
        if not os.environ.get('PRISMA_GENERATOR_INVOCATION'):
            raise RuntimeError(
                'Attempted to create a partial type outside of client generation.'
            )

        if name in _created_partial_types:
            raise ValueError(f'Partial type "{name}" has already been created.')

        if include is not None:
            if exclude is not None:
                raise TypeError('Exclude and include are mutually exclusive.')
            if exclude_relational_fields is True:
                raise TypeError('Include and exclude_relational_fields=True are mutually exclusive.')

        if required and optional:
            shared = set(required) & set(optional)
            if shared:
                raise ValueError(f'Cannot make the same field(s) required and optional {shared}')

        if exclude_relational_fields and relations:
            raise ValueError(
                'exclude_relational_fields and relations are mutually exclusive'
            )

        fields: Dict['types.Document_storeKeys', PartialModelField] = OrderedDict()

        try:
            if include:
                for field in include:
                    fields[field] = _Document_store_fields[field].copy()
            elif exclude:
                for field in exclude:
                    if field not in _Document_store_fields:
                        raise KeyError(field)

                fields = {
                    key: data.copy()
                    for key, data in _Document_store_fields.items()
                    if key not in exclude
                }
            else:
                fields = {
                    key: data.copy()
                    for key, data in _Document_store_fields.items()
                }

            if required:
                for field in required:
                    fields[field]['optional'] = False

            if optional:
                for field in optional:
                    fields[field]['optional'] = True


            if relations:
                raise ValueError('Model: "Document_store" has no relational fields.')
        except KeyError as exc:
            raise ValueError(
                f'{exc.args[0]} is not a valid Document_store / {name} field.'
            ) from None

        models = partial_models_ctx.get()
        models.append(
            {
                'name': name,
                'fields': cast(Mapping[str, PartialModelField], fields),
                'from_model': 'Document_store',
            }
        )
        _created_partial_types.add(name)



_Application_logs_relational_fields: Set[str] = set()  # pyright: ignore[reportUnusedVariable]
_Application_logs_fields: Dict['types.Application_logsKeys', PartialModelField] = OrderedDict(
    [
        ('id', {
            'name': 'id',
            'is_list': False,
            'optional': False,
            'type': '_int',
            'is_relational': False,
            'documentation': None,
        }),
        ('session_id', {
            'name': 'session_id',
            'is_list': False,
            'optional': False,
            'type': '_str',
            'is_relational': False,
            'documentation': None,
        }),
        ('user_query', {
            'name': 'user_query',
            'is_list': False,
            'optional': False,
            'type': '_str',
            'is_relational': False,
            'documentation': None,
        }),
        ('gpt_response', {
            'name': 'gpt_response',
            'is_list': False,
            'optional': False,
            'type': '_str',
            'is_relational': False,
            'documentation': None,
        }),
        ('model', {
            'name': 'model',
            'is_list': False,
            'optional': False,
            'type': '_str',
            'is_relational': False,
            'documentation': None,
        }),
        ('created_at', {
            'name': 'created_at',
            'is_list': False,
            'optional': False,
            'type': 'datetime.datetime',
            'is_relational': False,
            'documentation': None,
        }),
    ],
)

_Document_store_relational_fields: Set[str] = set()  # pyright: ignore[reportUnusedVariable]
_Document_store_fields: Dict['types.Document_storeKeys', PartialModelField] = OrderedDict(
    [
        ('id', {
            'name': 'id',
            'is_list': False,
            'optional': False,
            'type': '_int',
            'is_relational': False,
            'documentation': None,
        }),
        ('filename', {
            'name': 'filename',
            'is_list': False,
            'optional': False,
            'type': '_str',
            'is_relational': False,
            'documentation': None,
        }),
        ('upload_timestamp', {
            'name': 'upload_timestamp',
            'is_list': False,
            'optional': False,
            'type': 'datetime.datetime',
            'is_relational': False,
            'documentation': None,
        }),
    ],
)



# we have to import ourselves as relation types are namespaced to models
# e.g. models.Post
from . import models, actions

# required to support relationships between models
model_rebuild(Application_logs)
model_rebuild(Document_store)