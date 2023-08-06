import datetime
import typing
import autoboto
from enum import Enum
import dataclasses


@dataclasses.dataclass
class AffectedEntity(autoboto.ShapeBase):
    """
    Information about an entity that is affected by a Health event.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "entity_arn",
                "entityArn",
                autoboto.TypeInfo(str),
            ),
            (
                "event_arn",
                "eventArn",
                autoboto.TypeInfo(str),
            ),
            (
                "entity_value",
                "entityValue",
                autoboto.TypeInfo(str),
            ),
            (
                "aws_account_id",
                "awsAccountId",
                autoboto.TypeInfo(str),
            ),
            (
                "last_updated_time",
                "lastUpdatedTime",
                autoboto.TypeInfo(datetime.datetime),
            ),
            (
                "status_code",
                "statusCode",
                autoboto.TypeInfo(entityStatusCode),
            ),
            (
                "tags",
                "tags",
                autoboto.TypeInfo(typing.Dict[str, str]),
            ),
        ]

    # The unique identifier for the entity. Format: `arn:aws:health: _entity-
    # region_ : _aws-account_ :entity/ _entity-id_ `. Example:
    # `arn:aws:health:us-east-1:111222333444:entity/AVh5GGT7ul1arKr1sE1K`
    entity_arn: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The unique identifier for the event. Format: `arn:aws:health: _event-
    # region_ ::event/ _SERVICE_ / _EVENT_TYPE_CODE_ / _EVENT_TYPE_PLUS_ID_ `.
    # Example: `Example: arn:aws:health:us-
    # east-1::event/EC2/EC2_INSTANCE_RETIREMENT_SCHEDULED/EC2_INSTANCE_RETIREMENT_SCHEDULED_ABC123-DEF456`
    event_arn: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The ID of the affected entity.
    entity_value: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The 12-digit AWS account number that contains the affected entity.
    aws_account_id: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The most recent time that the entity was updated.
    last_updated_time: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The most recent status of the entity affected by the event. The possible
    # values are `IMPAIRED`, `UNIMPAIRED`, and `UNKNOWN`.
    status_code: "entityStatusCode" = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # A map of entity tags attached to the affected entity.
    tags: typing.Dict[str, str] = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class DateTimeRange(autoboto.ShapeBase):
    """
    A range of dates and times that is used by the EventFilter and EntityFilter
    objects. If `from` is set and `to` is set: match items where the timestamp
    (`startTime`, `endTime`, or `lastUpdatedTime`) is between `from` and `to`
    inclusive. If `from` is set and `to` is not set: match items where the timestamp
    value is equal to or after `from`. If `from` is not set and `to` is set: match
    items where the timestamp value is equal to or before `to`.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "from_",
                "from",
                autoboto.TypeInfo(datetime.datetime),
            ),
            (
                "to",
                "to",
                autoboto.TypeInfo(datetime.datetime),
            ),
        ]

    # The starting date and time of a time range.
    from_: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The ending date and time of a time range.
    to: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class DescribeAffectedEntitiesRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "filter",
                "filter",
                autoboto.TypeInfo(EntityFilter),
            ),
            (
                "locale",
                "locale",
                autoboto.TypeInfo(str),
            ),
            (
                "next_token",
                "nextToken",
                autoboto.TypeInfo(str),
            ),
            (
                "max_results",
                "maxResults",
                autoboto.TypeInfo(int),
            ),
        ]

    # Values to narrow the results returned. At least one event ARN is required.
    filter: "EntityFilter" = dataclasses.field(default_factory=dict, )

    # The locale (language) to return information in. English (en) is the default
    # and the only supported value at this time.
    locale: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # If the results of a search are large, only a portion of the results are
    # returned, and a `nextToken` pagination token is returned in the response.
    # To retrieve the next batch of results, reissue the search request and
    # include the returned token. When all results have been returned, the
    # response does not contain a pagination token value.
    next_token: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The maximum number of items to return in one batch, between 10 and 100,
    # inclusive.
    max_results: int = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class DescribeAffectedEntitiesResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "entities",
                "entities",
                autoboto.TypeInfo(typing.List[AffectedEntity]),
            ),
            (
                "next_token",
                "nextToken",
                autoboto.TypeInfo(str),
            ),
        ]

    # The entities that match the filter criteria.
    entities: typing.List["AffectedEntity"] = dataclasses.field(
        default_factory=list,
    )

    # If the results of a search are large, only a portion of the results are
    # returned, and a `nextToken` pagination token is returned in the response.
    # To retrieve the next batch of results, reissue the search request and
    # include the returned token. When all results have been returned, the
    # response does not contain a pagination token value.
    next_token: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class DescribeEntityAggregatesRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "event_arns",
                "eventArns",
                autoboto.TypeInfo(typing.List[str]),
            ),
        ]

    # A list of event ARNs (unique identifiers). For example:
    # `"arn:aws:health:us-
    # east-1::event/EC2/EC2_INSTANCE_RETIREMENT_SCHEDULED/EC2_INSTANCE_RETIREMENT_SCHEDULED_ABC123-CDE456",
    # "arn:aws:health:us-
    # west-1::event/EBS/AWS_EBS_LOST_VOLUME/AWS_EBS_LOST_VOLUME_CHI789_JKL101"`
    event_arns: typing.List[str] = dataclasses.field(default_factory=list, )


@dataclasses.dataclass
class DescribeEntityAggregatesResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "entity_aggregates",
                "entityAggregates",
                autoboto.TypeInfo(typing.List[EntityAggregate]),
            ),
        ]

    # The number of entities that are affected by each of the specified events.
    entity_aggregates: typing.List["EntityAggregate"] = dataclasses.field(
        default_factory=list,
    )


@dataclasses.dataclass
class DescribeEventAggregatesRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "aggregate_field",
                "aggregateField",
                autoboto.TypeInfo(eventAggregateField),
            ),
            (
                "filter",
                "filter",
                autoboto.TypeInfo(EventFilter),
            ),
            (
                "max_results",
                "maxResults",
                autoboto.TypeInfo(int),
            ),
            (
                "next_token",
                "nextToken",
                autoboto.TypeInfo(str),
            ),
        ]

    # The only currently supported value is `eventTypeCategory`.
    aggregate_field: "eventAggregateField" = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # Values to narrow the results returned.
    filter: "EventFilter" = dataclasses.field(default_factory=dict, )

    # The maximum number of items to return in one batch, between 10 and 100,
    # inclusive.
    max_results: int = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # If the results of a search are large, only a portion of the results are
    # returned, and a `nextToken` pagination token is returned in the response.
    # To retrieve the next batch of results, reissue the search request and
    # include the returned token. When all results have been returned, the
    # response does not contain a pagination token value.
    next_token: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class DescribeEventAggregatesResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "event_aggregates",
                "eventAggregates",
                autoboto.TypeInfo(typing.List[EventAggregate]),
            ),
            (
                "next_token",
                "nextToken",
                autoboto.TypeInfo(str),
            ),
        ]

    # The number of events in each category that meet the optional filter
    # criteria.
    event_aggregates: typing.List["EventAggregate"] = dataclasses.field(
        default_factory=list,
    )

    # If the results of a search are large, only a portion of the results are
    # returned, and a `nextToken` pagination token is returned in the response.
    # To retrieve the next batch of results, reissue the search request and
    # include the returned token. When all results have been returned, the
    # response does not contain a pagination token value.
    next_token: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class DescribeEventDetailsRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "event_arns",
                "eventArns",
                autoboto.TypeInfo(typing.List[str]),
            ),
            (
                "locale",
                "locale",
                autoboto.TypeInfo(str),
            ),
        ]

    # A list of event ARNs (unique identifiers). For example:
    # `"arn:aws:health:us-
    # east-1::event/EC2/EC2_INSTANCE_RETIREMENT_SCHEDULED/EC2_INSTANCE_RETIREMENT_SCHEDULED_ABC123-CDE456",
    # "arn:aws:health:us-
    # west-1::event/EBS/AWS_EBS_LOST_VOLUME/AWS_EBS_LOST_VOLUME_CHI789_JKL101"`
    event_arns: typing.List[str] = dataclasses.field(default_factory=list, )

    # The locale (language) to return information in. English (en) is the default
    # and the only supported value at this time.
    locale: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class DescribeEventDetailsResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "successful_set",
                "successfulSet",
                autoboto.TypeInfo(typing.List[EventDetails]),
            ),
            (
                "failed_set",
                "failedSet",
                autoboto.TypeInfo(typing.List[EventDetailsErrorItem]),
            ),
        ]

    # Information about the events that could be retrieved.
    successful_set: typing.List["EventDetails"] = dataclasses.field(
        default_factory=list,
    )

    # Error messages for any events that could not be retrieved.
    failed_set: typing.List["EventDetailsErrorItem"] = dataclasses.field(
        default_factory=list,
    )


@dataclasses.dataclass
class DescribeEventTypesRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "filter",
                "filter",
                autoboto.TypeInfo(EventTypeFilter),
            ),
            (
                "locale",
                "locale",
                autoboto.TypeInfo(str),
            ),
            (
                "next_token",
                "nextToken",
                autoboto.TypeInfo(str),
            ),
            (
                "max_results",
                "maxResults",
                autoboto.TypeInfo(int),
            ),
        ]

    # Values to narrow the results returned.
    filter: "EventTypeFilter" = dataclasses.field(default_factory=dict, )

    # The locale (language) to return information in. English (en) is the default
    # and the only supported value at this time.
    locale: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # If the results of a search are large, only a portion of the results are
    # returned, and a `nextToken` pagination token is returned in the response.
    # To retrieve the next batch of results, reissue the search request and
    # include the returned token. When all results have been returned, the
    # response does not contain a pagination token value.
    next_token: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The maximum number of items to return in one batch, between 10 and 100,
    # inclusive.
    max_results: int = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class DescribeEventTypesResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "event_types",
                "eventTypes",
                autoboto.TypeInfo(typing.List[EventType]),
            ),
            (
                "next_token",
                "nextToken",
                autoboto.TypeInfo(str),
            ),
        ]

    # A list of event types that match the filter criteria. Event types have a
    # category (`issue`, `accountNotification`, or `scheduledChange`), a service
    # (for example, `EC2`, `RDS`, `DATAPIPELINE`, `BILLING`), and a code (in the
    # format `AWS_ _SERVICE_ _ _DESCRIPTION_ `; for example,
    # `AWS_EC2_SYSTEM_MAINTENANCE_EVENT`).
    event_types: typing.List["EventType"] = dataclasses.field(
        default_factory=list,
    )

    # If the results of a search are large, only a portion of the results are
    # returned, and a `nextToken` pagination token is returned in the response.
    # To retrieve the next batch of results, reissue the search request and
    # include the returned token. When all results have been returned, the
    # response does not contain a pagination token value.
    next_token: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class DescribeEventsRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "filter",
                "filter",
                autoboto.TypeInfo(EventFilter),
            ),
            (
                "next_token",
                "nextToken",
                autoboto.TypeInfo(str),
            ),
            (
                "max_results",
                "maxResults",
                autoboto.TypeInfo(int),
            ),
            (
                "locale",
                "locale",
                autoboto.TypeInfo(str),
            ),
        ]

    # Values to narrow the results returned.
    filter: "EventFilter" = dataclasses.field(default_factory=dict, )

    # If the results of a search are large, only a portion of the results are
    # returned, and a `nextToken` pagination token is returned in the response.
    # To retrieve the next batch of results, reissue the search request and
    # include the returned token. When all results have been returned, the
    # response does not contain a pagination token value.
    next_token: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The maximum number of items to return in one batch, between 10 and 100,
    # inclusive.
    max_results: int = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The locale (language) to return information in. English (en) is the default
    # and the only supported value at this time.
    locale: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class DescribeEventsResponse(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "events",
                "events",
                autoboto.TypeInfo(typing.List[Event]),
            ),
            (
                "next_token",
                "nextToken",
                autoboto.TypeInfo(str),
            ),
        ]

    # The events that match the specified filter criteria.
    events: typing.List["Event"] = dataclasses.field(default_factory=list, )

    # If the results of a search are large, only a portion of the results are
    # returned, and a `nextToken` pagination token is returned in the response.
    # To retrieve the next batch of results, reissue the search request and
    # include the returned token. When all results have been returned, the
    # response does not contain a pagination token value.
    next_token: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class EntityAggregate(autoboto.ShapeBase):
    """
    The number of entities that are affected by one or more events. Returned by the
    DescribeEntityAggregates operation.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "event_arn",
                "eventArn",
                autoboto.TypeInfo(str),
            ),
            (
                "count",
                "count",
                autoboto.TypeInfo(int),
            ),
        ]

    # The unique identifier for the event. Format: `arn:aws:health: _event-
    # region_ ::event/ _SERVICE_ / _EVENT_TYPE_CODE_ / _EVENT_TYPE_PLUS_ID_ `.
    # Example: `Example: arn:aws:health:us-
    # east-1::event/EC2/EC2_INSTANCE_RETIREMENT_SCHEDULED/EC2_INSTANCE_RETIREMENT_SCHEDULED_ABC123-DEF456`
    event_arn: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The number entities that match the criteria for the specified events.
    count: int = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class EntityFilter(autoboto.ShapeBase):
    """
    The values to use to filter results from the DescribeAffectedEntities operation.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "event_arns",
                "eventArns",
                autoboto.TypeInfo(typing.List[str]),
            ),
            (
                "entity_arns",
                "entityArns",
                autoboto.TypeInfo(typing.List[str]),
            ),
            (
                "entity_values",
                "entityValues",
                autoboto.TypeInfo(typing.List[str]),
            ),
            (
                "last_updated_times",
                "lastUpdatedTimes",
                autoboto.TypeInfo(typing.List[DateTimeRange]),
            ),
            (
                "tags",
                "tags",
                autoboto.TypeInfo(typing.List[typing.Dict[str, str]]),
            ),
            (
                "status_codes",
                "statusCodes",
                autoboto.TypeInfo(typing.List[entityStatusCode]),
            ),
        ]

    # A list of event ARNs (unique identifiers). For example:
    # `"arn:aws:health:us-
    # east-1::event/EC2/EC2_INSTANCE_RETIREMENT_SCHEDULED/EC2_INSTANCE_RETIREMENT_SCHEDULED_ABC123-CDE456",
    # "arn:aws:health:us-
    # west-1::event/EBS/AWS_EBS_LOST_VOLUME/AWS_EBS_LOST_VOLUME_CHI789_JKL101"`
    event_arns: typing.List[str] = dataclasses.field(default_factory=list, )

    # A list of entity ARNs (unique identifiers).
    entity_arns: typing.List[str] = dataclasses.field(default_factory=list, )

    # A list of IDs for affected entities.
    entity_values: typing.List[str] = dataclasses.field(default_factory=list, )

    # A list of the most recent dates and times that the entity was updated.
    last_updated_times: typing.List["DateTimeRange"] = dataclasses.field(
        default_factory=list,
    )

    # A map of entity tags attached to the affected entity.
    tags: typing.List[typing.Dict[str, str]] = dataclasses.field(
        default_factory=list,
    )

    # A list of entity status codes (`IMPAIRED`, `UNIMPAIRED`, or `UNKNOWN`).
    status_codes: typing.List["entityStatusCode"] = dataclasses.field(
        default_factory=list,
    )


@dataclasses.dataclass
class Event(autoboto.ShapeBase):
    """
    Summary information about an event, returned by the DescribeEvents operation.
    The DescribeEventDetails operation also returns this information, as well as the
    EventDescription and additional event metadata.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "arn",
                "arn",
                autoboto.TypeInfo(str),
            ),
            (
                "service",
                "service",
                autoboto.TypeInfo(str),
            ),
            (
                "event_type_code",
                "eventTypeCode",
                autoboto.TypeInfo(str),
            ),
            (
                "event_type_category",
                "eventTypeCategory",
                autoboto.TypeInfo(eventTypeCategory),
            ),
            (
                "region",
                "region",
                autoboto.TypeInfo(str),
            ),
            (
                "availability_zone",
                "availabilityZone",
                autoboto.TypeInfo(str),
            ),
            (
                "start_time",
                "startTime",
                autoboto.TypeInfo(datetime.datetime),
            ),
            (
                "end_time",
                "endTime",
                autoboto.TypeInfo(datetime.datetime),
            ),
            (
                "last_updated_time",
                "lastUpdatedTime",
                autoboto.TypeInfo(datetime.datetime),
            ),
            (
                "status_code",
                "statusCode",
                autoboto.TypeInfo(eventStatusCode),
            ),
        ]

    # The unique identifier for the event. Format: `arn:aws:health: _event-
    # region_ ::event/ _SERVICE_ / _EVENT_TYPE_CODE_ / _EVENT_TYPE_PLUS_ID_ `.
    # Example: `Example: arn:aws:health:us-
    # east-1::event/EC2/EC2_INSTANCE_RETIREMENT_SCHEDULED/EC2_INSTANCE_RETIREMENT_SCHEDULED_ABC123-DEF456`
    arn: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The AWS service that is affected by the event. For example, `EC2`, `RDS`.
    service: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The unique identifier for the event type. The format is `AWS_ _SERVICE_ _
    # _DESCRIPTION_ `; for example, `AWS_EC2_SYSTEM_MAINTENANCE_EVENT`.
    event_type_code: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The category of the event. Possible values are `issue`, `scheduledChange`,
    # and `accountNotification`.
    event_type_category: "eventTypeCategory" = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The AWS region name of the event.
    region: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The AWS Availability Zone of the event. For example, us-east-1a.
    availability_zone: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The date and time that the event began.
    start_time: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The date and time that the event ended.
    end_time: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The most recent date and time that the event was updated.
    last_updated_time: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The most recent status of the event. Possible values are `open`, `closed`,
    # and `upcoming`.
    status_code: "eventStatusCode" = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class EventAggregate(autoboto.ShapeBase):
    """
    The number of events of each issue type. Returned by the DescribeEventAggregates
    operation.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "aggregate_value",
                "aggregateValue",
                autoboto.TypeInfo(str),
            ),
            (
                "count",
                "count",
                autoboto.TypeInfo(int),
            ),
        ]

    # The issue type for the associated count.
    aggregate_value: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The number of events of the associated issue type.
    count: int = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class EventDescription(autoboto.ShapeBase):
    """
    The detailed description of the event. Included in the information returned by
    the DescribeEventDetails operation.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "latest_description",
                "latestDescription",
                autoboto.TypeInfo(str),
            ),
        ]

    # The most recent description of the event.
    latest_description: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class EventDetails(autoboto.ShapeBase):
    """
    Detailed information about an event. A combination of an Event object, an
    EventDescription object, and additional metadata about the event. Returned by
    the DescribeEventDetails operation.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "event",
                "event",
                autoboto.TypeInfo(Event),
            ),
            (
                "event_description",
                "eventDescription",
                autoboto.TypeInfo(EventDescription),
            ),
            (
                "event_metadata",
                "eventMetadata",
                autoboto.TypeInfo(typing.Dict[str, str]),
            ),
        ]

    # Summary information about the event.
    event: "Event" = dataclasses.field(default_factory=dict, )

    # The most recent description of the event.
    event_description: "EventDescription" = dataclasses.field(
        default_factory=dict,
    )

    # Additional metadata about the event.
    event_metadata: typing.Dict[str, str] = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class EventDetailsErrorItem(autoboto.ShapeBase):
    """
    Error information returned when a DescribeEventDetails operation cannot find a
    specified event.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "event_arn",
                "eventArn",
                autoboto.TypeInfo(str),
            ),
            (
                "error_name",
                "errorName",
                autoboto.TypeInfo(str),
            ),
            (
                "error_message",
                "errorMessage",
                autoboto.TypeInfo(str),
            ),
        ]

    # The unique identifier for the event. Format: `arn:aws:health: _event-
    # region_ ::event/ _SERVICE_ / _EVENT_TYPE_CODE_ / _EVENT_TYPE_PLUS_ID_ `.
    # Example: `Example: arn:aws:health:us-
    # east-1::event/EC2/EC2_INSTANCE_RETIREMENT_SCHEDULED/EC2_INSTANCE_RETIREMENT_SCHEDULED_ABC123-DEF456`
    event_arn: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The name of the error.
    error_name: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # A message that describes the error.
    error_message: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class EventFilter(autoboto.ShapeBase):
    """
    The values to use to filter results from the DescribeEvents and
    DescribeEventAggregates operations.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "event_arns",
                "eventArns",
                autoboto.TypeInfo(typing.List[str]),
            ),
            (
                "event_type_codes",
                "eventTypeCodes",
                autoboto.TypeInfo(typing.List[str]),
            ),
            (
                "services",
                "services",
                autoboto.TypeInfo(typing.List[str]),
            ),
            (
                "regions",
                "regions",
                autoboto.TypeInfo(typing.List[str]),
            ),
            (
                "availability_zones",
                "availabilityZones",
                autoboto.TypeInfo(typing.List[str]),
            ),
            (
                "start_times",
                "startTimes",
                autoboto.TypeInfo(typing.List[DateTimeRange]),
            ),
            (
                "end_times",
                "endTimes",
                autoboto.TypeInfo(typing.List[DateTimeRange]),
            ),
            (
                "last_updated_times",
                "lastUpdatedTimes",
                autoboto.TypeInfo(typing.List[DateTimeRange]),
            ),
            (
                "entity_arns",
                "entityArns",
                autoboto.TypeInfo(typing.List[str]),
            ),
            (
                "entity_values",
                "entityValues",
                autoboto.TypeInfo(typing.List[str]),
            ),
            (
                "event_type_categories",
                "eventTypeCategories",
                autoboto.TypeInfo(typing.List[eventTypeCategory]),
            ),
            (
                "tags",
                "tags",
                autoboto.TypeInfo(typing.List[typing.Dict[str, str]]),
            ),
            (
                "event_status_codes",
                "eventStatusCodes",
                autoboto.TypeInfo(typing.List[eventStatusCode]),
            ),
        ]

    # A list of event ARNs (unique identifiers). For example:
    # `"arn:aws:health:us-
    # east-1::event/EC2/EC2_INSTANCE_RETIREMENT_SCHEDULED/EC2_INSTANCE_RETIREMENT_SCHEDULED_ABC123-CDE456",
    # "arn:aws:health:us-
    # west-1::event/EBS/AWS_EBS_LOST_VOLUME/AWS_EBS_LOST_VOLUME_CHI789_JKL101"`
    event_arns: typing.List[str] = dataclasses.field(default_factory=list, )

    # A list of unique identifiers for event types. For example,
    # `"AWS_EC2_SYSTEM_MAINTENANCE_EVENT","AWS_RDS_MAINTENANCE_SCHEDULED"`
    event_type_codes: typing.List[str] = dataclasses.field(
        default_factory=list,
    )

    # The AWS services associated with the event. For example, `EC2`, `RDS`.
    services: typing.List[str] = dataclasses.field(default_factory=list, )

    # A list of AWS regions.
    regions: typing.List[str] = dataclasses.field(default_factory=list, )

    # A list of AWS availability zones.
    availability_zones: typing.List[str] = dataclasses.field(
        default_factory=list,
    )

    # A list of dates and times that the event began.
    start_times: typing.List["DateTimeRange"] = dataclasses.field(
        default_factory=list,
    )

    # A list of dates and times that the event ended.
    end_times: typing.List["DateTimeRange"] = dataclasses.field(
        default_factory=list,
    )

    # A list of dates and times that the event was last updated.
    last_updated_times: typing.List["DateTimeRange"] = dataclasses.field(
        default_factory=list,
    )

    # A list of entity ARNs (unique identifiers).
    entity_arns: typing.List[str] = dataclasses.field(default_factory=list, )

    # A list of entity identifiers, such as EC2 instance IDs (`i-34ab692e`) or
    # EBS volumes (`vol-426ab23e`).
    entity_values: typing.List[str] = dataclasses.field(default_factory=list, )

    # A list of event type category codes (`issue`, `scheduledChange`, or
    # `accountNotification`).
    event_type_categories: typing.List["eventTypeCategory"] = dataclasses.field(
        default_factory=list,
    )

    # A map of entity tags attached to the affected entity.
    tags: typing.List[typing.Dict[str, str]] = dataclasses.field(
        default_factory=list,
    )

    # A list of event status codes.
    event_status_codes: typing.List["eventStatusCode"] = dataclasses.field(
        default_factory=list,
    )


@dataclasses.dataclass
class EventType(autoboto.ShapeBase):
    """
    Metadata about a type of event that is reported by AWS Health. Data consists of
    the category (for example, `issue`), the service (for example, `EC2`), and the
    event type code (for example, `AWS_EC2_SYSTEM_MAINTENANCE_EVENT`).
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "service",
                "service",
                autoboto.TypeInfo(str),
            ),
            (
                "code",
                "code",
                autoboto.TypeInfo(str),
            ),
            (
                "category",
                "category",
                autoboto.TypeInfo(eventTypeCategory),
            ),
        ]

    # The AWS service that is affected by the event. For example, `EC2`, `RDS`.
    service: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The unique identifier for the event type. The format is `AWS_ _SERVICE_ _
    # _DESCRIPTION_ `; for example, `AWS_EC2_SYSTEM_MAINTENANCE_EVENT`.
    code: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # A list of event type category codes (`issue`, `scheduledChange`, or
    # `accountNotification`).
    category: "eventTypeCategory" = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class EventTypeFilter(autoboto.ShapeBase):
    """
    The values to use to filter results from the DescribeEventTypes operation.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "event_type_codes",
                "eventTypeCodes",
                autoboto.TypeInfo(typing.List[str]),
            ),
            (
                "services",
                "services",
                autoboto.TypeInfo(typing.List[str]),
            ),
            (
                "event_type_categories",
                "eventTypeCategories",
                autoboto.TypeInfo(typing.List[eventTypeCategory]),
            ),
        ]

    # A list of event type codes.
    event_type_codes: typing.List[str] = dataclasses.field(
        default_factory=list,
    )

    # The AWS services associated with the event. For example, `EC2`, `RDS`.
    services: typing.List[str] = dataclasses.field(default_factory=list, )

    # A list of event type category codes (`issue`, `scheduledChange`, or
    # `accountNotification`).
    event_type_categories: typing.List["eventTypeCategory"] = dataclasses.field(
        default_factory=list,
    )


@dataclasses.dataclass
class InvalidPaginationToken(autoboto.ShapeBase):
    """
    The specified pagination token (`nextToken`) is not valid.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "message",
                "message",
                autoboto.TypeInfo(str),
            ),
        ]

    message: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class UnsupportedLocale(autoboto.ShapeBase):
    """
    The specified locale is not supported.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "message",
                "message",
                autoboto.TypeInfo(str),
            ),
        ]

    message: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


class entityStatusCode(Enum):
    IMPAIRED = "IMPAIRED"
    UNIMPAIRED = "UNIMPAIRED"
    UNKNOWN = "UNKNOWN"


class eventAggregateField(Enum):
    eventTypeCategory = "eventTypeCategory"


class eventStatusCode(Enum):
    open = "open"
    closed = "closed"
    upcoming = "upcoming"


class eventTypeCategory(Enum):
    issue = "issue"
    accountNotification = "accountNotification"
    scheduledChange = "scheduledChange"
