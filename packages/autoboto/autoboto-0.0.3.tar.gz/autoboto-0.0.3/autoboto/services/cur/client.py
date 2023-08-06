import datetime
import typing
import boto3
import autoboto
from . import shapes


class Client:
    def __init__(self, *args, **kwargs):
        self._boto_client = boto3.client("cur", *args, **kwargs)

    def delete_report_definition(
        self,
        _request: shapes.DeleteReportDefinitionRequest = None,
        *,
        report_name: str = autoboto.ShapeBase._NOT_SET,
    ) -> shapes.DeleteReportDefinitionResponse:
        """
        Delete a specified report definition
        """
        if _request is None:
            _params = {}
            if report_name is not autoboto.ShapeBase._NOT_SET:
                _params['report_name'] = report_name
            _request = shapes.DeleteReportDefinitionRequest(**_params)
        response = self._boto_client.delete_report_definition(
            **_request.to_boto_dict()
        )

        return shapes.DeleteReportDefinitionResponse.from_boto_dict(response)

    def describe_report_definitions(
        self,
        _request: shapes.DescribeReportDefinitionsRequest = None,
        *,
        max_results: int = autoboto.ShapeBase._NOT_SET,
        next_token: str = autoboto.ShapeBase._NOT_SET,
    ) -> shapes.DescribeReportDefinitionsResponse:
        """
        Describe a list of report definitions owned by the account
        """
        if _request is None:
            _params = {}
            if max_results is not autoboto.ShapeBase._NOT_SET:
                _params['max_results'] = max_results
            if next_token is not autoboto.ShapeBase._NOT_SET:
                _params['next_token'] = next_token
            _request = shapes.DescribeReportDefinitionsRequest(**_params)
        response = self._boto_client.describe_report_definitions(
            **_request.to_boto_dict()
        )

        return shapes.DescribeReportDefinitionsResponse.from_boto_dict(response)

    def put_report_definition(
        self,
        _request: shapes.PutReportDefinitionRequest = None,
        *,
        report_definition: shapes.ReportDefinition,
    ) -> shapes.PutReportDefinitionResponse:
        """
        Create a new report definition
        """
        if _request is None:
            _params = {}
            if report_definition is not autoboto.ShapeBase._NOT_SET:
                _params['report_definition'] = report_definition
            _request = shapes.PutReportDefinitionRequest(**_params)
        response = self._boto_client.put_report_definition(
            **_request.to_boto_dict()
        )

        return shapes.PutReportDefinitionResponse.from_boto_dict(response)
