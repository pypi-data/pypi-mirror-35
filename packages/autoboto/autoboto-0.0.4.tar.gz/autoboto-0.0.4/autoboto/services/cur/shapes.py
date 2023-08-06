import datetime
import typing
import autoboto
from enum import Enum
import dataclasses


class AWSRegion(Enum):
    """
    Region of customer S3 bucket.
    """
    us_east_1 = "us-east-1"
    us_west_1 = "us-west-1"
    us_west_2 = "us-west-2"
    eu_central_1 = "eu-central-1"
    eu_west_1 = "eu-west-1"
    ap_southeast_1 = "ap-southeast-1"
    ap_southeast_2 = "ap-southeast-2"
    ap_northeast_1 = "ap-northeast-1"


class AdditionalArtifact(Enum):
    """
    Enable support for Redshift and/or QuickSight.
    """
    REDSHIFT = "REDSHIFT"
    QUICKSIGHT = "QUICKSIGHT"


class CompressionFormat(Enum):
    """
    Preferred compression format for report.
    """
    ZIP = "ZIP"
    GZIP = "GZIP"


@dataclasses.dataclass
class DeleteReportDefinitionRequest(autoboto.ShapeBase):
    """
    Request of DeleteReportDefinition
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "report_name",
                "ReportName",
                autoboto.TypeInfo(str),
            ),
        ]

    # Preferred name for a report, it has to be unique. Must starts with a
    # number/letter, case sensitive. Limited to 256 characters.
    report_name: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DeleteReportDefinitionResponse(autoboto.ShapeBase):
    """
    Response of DeleteReportDefinition
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "response_message",
                "ResponseMessage",
                autoboto.TypeInfo(str),
            ),
        ]

    # A message indicates if the deletion is successful.
    response_message: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class DescribeReportDefinitionsRequest(autoboto.ShapeBase):
    """
    Request of DescribeReportDefinitions
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "max_results",
                "MaxResults",
                autoboto.TypeInfo(int),
            ),
            (
                "next_token",
                "NextToken",
                autoboto.TypeInfo(str),
            ),
        ]

    # The max number of results returned by the operation.
    max_results: int = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # A generic string.
    next_token: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DescribeReportDefinitionsResponse(autoboto.ShapeBase):
    """
    Response of DescribeReportDefinitions
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "report_definitions",
                "ReportDefinitions",
                autoboto.TypeInfo(typing.List[ReportDefinition]),
            ),
            (
                "next_token",
                "NextToken",
                autoboto.TypeInfo(str),
            ),
        ]

    # A list of report definitions.
    report_definitions: typing.List["ReportDefinition"] = dataclasses.field(
        default_factory=list,
    )

    # A generic string.
    next_token: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DuplicateReportNameException(autoboto.ShapeBase):
    """
    This exception is thrown when putting a report preference with a name that
    already exists.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "message",
                "Message",
                autoboto.TypeInfo(str),
            ),
        ]

    # A message to show the detail of the exception.
    message: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class InternalErrorException(autoboto.ShapeBase):
    """
    This exception is thrown on a known dependency failure.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "message",
                "Message",
                autoboto.TypeInfo(str),
            ),
        ]

    # A message to show the detail of the exception.
    message: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class PutReportDefinitionRequest(autoboto.ShapeBase):
    """
    Request of PutReportDefinition
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "report_definition",
                "ReportDefinition",
                autoboto.TypeInfo(ReportDefinition),
            ),
        ]

    # The definition of AWS Cost and Usage Report. Customer can specify the
    # report name, time unit, report format, compression format, S3 bucket and
    # additional artifacts and schema elements in the definition.
    report_definition: "ReportDefinition" = dataclasses.field(
        default_factory=dict,
    )


@dataclasses.dataclass
class PutReportDefinitionResponse(autoboto.ShapeBase):
    """
    Response of PutReportDefinition
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class ReportDefinition(autoboto.ShapeBase):
    """
    The definition of AWS Cost and Usage Report. Customer can specify the report
    name, time unit, report format, compression format, S3 bucket and additional
    artifacts and schema elements in the definition.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "report_name",
                "ReportName",
                autoboto.TypeInfo(str),
            ),
            (
                "time_unit",
                "TimeUnit",
                autoboto.TypeInfo(TimeUnit),
            ),
            (
                "format",
                "Format",
                autoboto.TypeInfo(ReportFormat),
            ),
            (
                "compression",
                "Compression",
                autoboto.TypeInfo(CompressionFormat),
            ),
            (
                "additional_schema_elements",
                "AdditionalSchemaElements",
                autoboto.TypeInfo(typing.List[SchemaElement]),
            ),
            (
                "s3_bucket",
                "S3Bucket",
                autoboto.TypeInfo(str),
            ),
            (
                "s3_prefix",
                "S3Prefix",
                autoboto.TypeInfo(str),
            ),
            (
                "s3_region",
                "S3Region",
                autoboto.TypeInfo(AWSRegion),
            ),
            (
                "additional_artifacts",
                "AdditionalArtifacts",
                autoboto.TypeInfo(typing.List[AdditionalArtifact]),
            ),
        ]

    # Preferred name for a report, it has to be unique. Must starts with a
    # number/letter, case sensitive. Limited to 256 characters.
    report_name: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The frequency on which report data are measured and displayed.
    time_unit: "TimeUnit" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Preferred format for report.
    format: "ReportFormat" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Preferred compression format for report.
    compression: "CompressionFormat" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # A list of schema elements.
    additional_schema_elements: typing.List["SchemaElement"
                                           ] = dataclasses.field(
                                               default_factory=list,
                                           )

    # Name of customer S3 bucket.
    s3_bucket: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # Preferred report path prefix. Limited to 256 characters.
    s3_prefix: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # Region of customer S3 bucket.
    s3_region: "AWSRegion" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # A list of additional artifacts.
    additional_artifacts: typing.List["AdditionalArtifact"] = dataclasses.field(
        default_factory=list,
    )


class ReportFormat(Enum):
    """
    Preferred format for report.
    """
    textORcsv = "textORcsv"


@dataclasses.dataclass
class ReportLimitReachedException(autoboto.ShapeBase):
    """
    This exception is thrown when the number of report preference reaches max limit.
    The max number is 5.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "message",
                "Message",
                autoboto.TypeInfo(str),
            ),
        ]

    # A message to show the detail of the exception.
    message: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


class SchemaElement(Enum):
    """
    Preference of including Resource IDs. You can include additional details about
    individual resource IDs in your report.
    """
    RESOURCES = "RESOURCES"


class TimeUnit(Enum):
    """
    The frequency on which report data are measured and displayed.
    """
    HOURLY = "HOURLY"
    DAILY = "DAILY"


@dataclasses.dataclass
class ValidationException(autoboto.ShapeBase):
    """
    This exception is thrown when providing an invalid input. eg. Put a report
    preference with an invalid report name, or Delete a report preference with an
    empty report name.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "message",
                "Message",
                autoboto.TypeInfo(str),
            ),
        ]

    # A message to show the detail of the exception.
    message: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )
