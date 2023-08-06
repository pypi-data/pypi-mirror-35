import datetime
import typing
import boto3
import autoboto
from . import shapes


class Client:
    def __init__(self, *args, **kwargs):
        self._boto_client = boto3.client("health", *args, **kwargs)

    def describe_affected_entities(
        self,
        _request: shapes.DescribeAffectedEntitiesRequest = None,
        *,
        filter: shapes.EntityFilter,
        locale: str = autoboto.ShapeBase._NOT_SET,
        next_token: str = autoboto.ShapeBase._NOT_SET,
        max_results: int = autoboto.ShapeBase._NOT_SET,
    ) -> shapes.DescribeAffectedEntitiesResponse:
        """
        Returns a list of entities that have been affected by the specified events,
        based on the specified filter criteria. Entities can refer to individual
        customer resources, groups of customer resources, or any other construct,
        depending on the AWS service. Events that have impact beyond that of the
        affected entities, or where the extent of impact is unknown, include at least
        one entity indicating this.

        At least one event ARN is required. Results are sorted by the `lastUpdatedTime`
        of the entity, starting with the most recent.
        """
        if _request is None:
            _params = {}
            if filter is not autoboto.ShapeBase._NOT_SET:
                _params['filter'] = filter
            if locale is not autoboto.ShapeBase._NOT_SET:
                _params['locale'] = locale
            if next_token is not autoboto.ShapeBase._NOT_SET:
                _params['next_token'] = next_token
            if max_results is not autoboto.ShapeBase._NOT_SET:
                _params['max_results'] = max_results
            _request = shapes.DescribeAffectedEntitiesRequest(**_params)
        response = self._boto_client.describe_affected_entities(
            **_request.to_boto_dict()
        )

        return shapes.DescribeAffectedEntitiesResponse.from_boto_dict(response)

    def describe_entity_aggregates(
        self,
        _request: shapes.DescribeEntityAggregatesRequest = None,
        *,
        event_arns: typing.List[str] = autoboto.ShapeBase._NOT_SET,
    ) -> shapes.DescribeEntityAggregatesResponse:
        """
        Returns the number of entities that are affected by each of the specified
        events. If no events are specified, the counts of all affected entities are
        returned.
        """
        if _request is None:
            _params = {}
            if event_arns is not autoboto.ShapeBase._NOT_SET:
                _params['event_arns'] = event_arns
            _request = shapes.DescribeEntityAggregatesRequest(**_params)
        response = self._boto_client.describe_entity_aggregates(
            **_request.to_boto_dict()
        )

        return shapes.DescribeEntityAggregatesResponse.from_boto_dict(response)

    def describe_event_aggregates(
        self,
        _request: shapes.DescribeEventAggregatesRequest = None,
        *,
        aggregate_field: shapes.eventAggregateField,
        filter: shapes.EventFilter = autoboto.ShapeBase._NOT_SET,
        max_results: int = autoboto.ShapeBase._NOT_SET,
        next_token: str = autoboto.ShapeBase._NOT_SET,
    ) -> shapes.DescribeEventAggregatesResponse:
        """
        Returns the number of events of each event type (issue, scheduled change, and
        account notification). If no filter is specified, the counts of all events in
        each category are returned.
        """
        if _request is None:
            _params = {}
            if aggregate_field is not autoboto.ShapeBase._NOT_SET:
                _params['aggregate_field'] = aggregate_field
            if filter is not autoboto.ShapeBase._NOT_SET:
                _params['filter'] = filter
            if max_results is not autoboto.ShapeBase._NOT_SET:
                _params['max_results'] = max_results
            if next_token is not autoboto.ShapeBase._NOT_SET:
                _params['next_token'] = next_token
            _request = shapes.DescribeEventAggregatesRequest(**_params)
        response = self._boto_client.describe_event_aggregates(
            **_request.to_boto_dict()
        )

        return shapes.DescribeEventAggregatesResponse.from_boto_dict(response)

    def describe_event_details(
        self,
        _request: shapes.DescribeEventDetailsRequest = None,
        *,
        event_arns: typing.List[str],
        locale: str = autoboto.ShapeBase._NOT_SET,
    ) -> shapes.DescribeEventDetailsResponse:
        """
        Returns detailed information about one or more specified events. Information
        includes standard event data (region, service, etc., as returned by
        DescribeEvents), a detailed event description, and possible additional metadata
        that depends upon the nature of the event. Affected entities are not included;
        to retrieve those, use the DescribeAffectedEntities operation.

        If a specified event cannot be retrieved, an error message is returned for that
        event.
        """
        if _request is None:
            _params = {}
            if event_arns is not autoboto.ShapeBase._NOT_SET:
                _params['event_arns'] = event_arns
            if locale is not autoboto.ShapeBase._NOT_SET:
                _params['locale'] = locale
            _request = shapes.DescribeEventDetailsRequest(**_params)
        response = self._boto_client.describe_event_details(
            **_request.to_boto_dict()
        )

        return shapes.DescribeEventDetailsResponse.from_boto_dict(response)

    def describe_event_types(
        self,
        _request: shapes.DescribeEventTypesRequest = None,
        *,
        filter: shapes.EventTypeFilter = autoboto.ShapeBase._NOT_SET,
        locale: str = autoboto.ShapeBase._NOT_SET,
        next_token: str = autoboto.ShapeBase._NOT_SET,
        max_results: int = autoboto.ShapeBase._NOT_SET,
    ) -> shapes.DescribeEventTypesResponse:
        """
        Returns the event types that meet the specified filter criteria. If no filter
        criteria are specified, all event types are returned, in no particular order.
        """
        if _request is None:
            _params = {}
            if filter is not autoboto.ShapeBase._NOT_SET:
                _params['filter'] = filter
            if locale is not autoboto.ShapeBase._NOT_SET:
                _params['locale'] = locale
            if next_token is not autoboto.ShapeBase._NOT_SET:
                _params['next_token'] = next_token
            if max_results is not autoboto.ShapeBase._NOT_SET:
                _params['max_results'] = max_results
            _request = shapes.DescribeEventTypesRequest(**_params)
        response = self._boto_client.describe_event_types(
            **_request.to_boto_dict()
        )

        return shapes.DescribeEventTypesResponse.from_boto_dict(response)

    def describe_events(
        self,
        _request: shapes.DescribeEventsRequest = None,
        *,
        filter: shapes.EventFilter = autoboto.ShapeBase._NOT_SET,
        next_token: str = autoboto.ShapeBase._NOT_SET,
        max_results: int = autoboto.ShapeBase._NOT_SET,
        locale: str = autoboto.ShapeBase._NOT_SET,
    ) -> shapes.DescribeEventsResponse:
        """
        Returns information about events that meet the specified filter criteria. Events
        are returned in a summary form and do not include the detailed description, any
        additional metadata that depends on the event type, or any affected resources.
        To retrieve that information, use the DescribeEventDetails and
        DescribeAffectedEntities operations.

        If no filter criteria are specified, all events are returned. Results are sorted
        by `lastModifiedTime`, starting with the most recent.
        """
        if _request is None:
            _params = {}
            if filter is not autoboto.ShapeBase._NOT_SET:
                _params['filter'] = filter
            if next_token is not autoboto.ShapeBase._NOT_SET:
                _params['next_token'] = next_token
            if max_results is not autoboto.ShapeBase._NOT_SET:
                _params['max_results'] = max_results
            if locale is not autoboto.ShapeBase._NOT_SET:
                _params['locale'] = locale
            _request = shapes.DescribeEventsRequest(**_params)
        response = self._boto_client.describe_events(**_request.to_boto_dict())

        return shapes.DescribeEventsResponse.from_boto_dict(response)
