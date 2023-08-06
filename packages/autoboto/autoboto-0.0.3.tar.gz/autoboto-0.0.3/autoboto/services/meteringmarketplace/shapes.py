import datetime
import typing
import autoboto
from enum import Enum
import dataclasses


@dataclasses.dataclass
class BatchMeterUsageRequest(autoboto.ShapeBase):
    """
    A BatchMeterUsageRequest contains UsageRecords, which indicate quantities of
    usage within your application.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "usage_records",
                "UsageRecords",
                autoboto.TypeInfo(typing.List[UsageRecord]),
            ),
            (
                "product_code",
                "ProductCode",
                autoboto.TypeInfo(str),
            ),
        ]

    # The set of UsageRecords to submit. BatchMeterUsage accepts up to 25
    # UsageRecords at a time.
    usage_records: typing.List["UsageRecord"] = dataclasses.field(
        default_factory=list,
    )

    # Product code is used to uniquely identify a product in AWS Marketplace. The
    # product code should be the same as the one used during the publishing of a
    # new product.
    product_code: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class BatchMeterUsageResult(autoboto.ShapeBase):
    """
    Contains the UsageRecords processed by BatchMeterUsage and any records that have
    failed due to transient error.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "results",
                "Results",
                autoboto.TypeInfo(typing.List[UsageRecordResult]),
            ),
            (
                "unprocessed_records",
                "UnprocessedRecords",
                autoboto.TypeInfo(typing.List[UsageRecord]),
            ),
        ]

    # Contains all UsageRecords processed by BatchMeterUsage. These records were
    # either honored by AWS Marketplace Metering Service or were invalid.
    results: typing.List["UsageRecordResult"] = dataclasses.field(
        default_factory=list,
    )

    # Contains all UsageRecords that were not processed by BatchMeterUsage. This
    # is a list of UsageRecords. You can retry the failed request by making
    # another BatchMeterUsage call with this list as input in the
    # BatchMeterUsageRequest.
    unprocessed_records: typing.List["UsageRecord"] = dataclasses.field(
        default_factory=list,
    )


@dataclasses.dataclass
class DuplicateRequestException(autoboto.ShapeBase):
    """
    A metering record has already been emitted by the same EC2 instance for the
    given {usageDimension, timestamp} with a different usageQuantity.
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
class ExpiredTokenException(autoboto.ShapeBase):
    """
    The submitted registration token has expired. This can happen if the buyer's
    browser takes too long to redirect to your page, the buyer has resubmitted the
    registration token, or your application has held on to the registration token
    for too long. Your SaaS registration website should redeem this token as soon as
    it is submitted by the buyer's browser.
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
class InternalServiceErrorException(autoboto.ShapeBase):
    """
    An internal error has occurred. Retry your request. If the problem persists,
    post a message with details on the AWS forums.
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
class InvalidCustomerIdentifierException(autoboto.ShapeBase):
    """
    You have metered usage for a CustomerIdentifier that does not exist.
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
class InvalidEndpointRegionException(autoboto.ShapeBase):
    """
    The endpoint being called is in a region different from your EC2 instance. The
    region of the Metering service endpoint and the region of the EC2 instance must
    match.
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
class InvalidProductCodeException(autoboto.ShapeBase):
    """
    The product code passed does not match the product code used for publishing the
    product.
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
class InvalidTokenException(autoboto.ShapeBase):
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
class InvalidUsageDimensionException(autoboto.ShapeBase):
    """
    The usage dimension does not match one of the UsageDimensions associated with
    products.
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
class MeterUsageRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "product_code",
                "ProductCode",
                autoboto.TypeInfo(str),
            ),
            (
                "timestamp",
                "Timestamp",
                autoboto.TypeInfo(datetime.datetime),
            ),
            (
                "usage_dimension",
                "UsageDimension",
                autoboto.TypeInfo(str),
            ),
            (
                "usage_quantity",
                "UsageQuantity",
                autoboto.TypeInfo(int),
            ),
            (
                "dry_run",
                "DryRun",
                autoboto.TypeInfo(bool),
            ),
        ]

    # Product code is used to uniquely identify a product in AWS Marketplace. The
    # product code should be the same as the one used during the publishing of a
    # new product.
    product_code: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # Timestamp of the hour, recorded in UTC. The seconds and milliseconds
    # portions of the timestamp will be ignored.
    timestamp: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # It will be one of the fcp dimension name provided during the publishing of
    # the product.
    usage_dimension: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # Consumption value for the hour.
    usage_quantity: int = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # Checks whether you have the permissions required for the action, but does
    # not make the request. If you have the permissions, the request returns
    # DryRunOperation; otherwise, it returns UnauthorizedException.
    dry_run: bool = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class MeterUsageResult(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "metering_record_id",
                "MeteringRecordId",
                autoboto.TypeInfo(str),
            ),
        ]

    metering_record_id: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class ResolveCustomerRequest(autoboto.ShapeBase):
    """
    Contains input to the ResolveCustomer operation.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "registration_token",
                "RegistrationToken",
                autoboto.TypeInfo(str),
            ),
        ]

    # When a buyer visits your website during the registration process, the buyer
    # submits a registration token through the browser. The registration token is
    # resolved to obtain a CustomerIdentifier and product code.
    registration_token: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class ResolveCustomerResult(autoboto.ShapeBase):
    """
    The result of the ResolveCustomer operation. Contains the CustomerIdentifier and
    product code.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "customer_identifier",
                "CustomerIdentifier",
                autoboto.TypeInfo(str),
            ),
            (
                "product_code",
                "ProductCode",
                autoboto.TypeInfo(str),
            ),
        ]

    # The CustomerIdentifier is used to identify an individual customer in your
    # application. Calls to BatchMeterUsage require CustomerIdentifiers for each
    # UsageRecord.
    customer_identifier: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The product code is returned to confirm that the buyer is registering for
    # your product. Subsequent BatchMeterUsage calls should be made using this
    # product code.
    product_code: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class ThrottlingException(autoboto.ShapeBase):
    """
    The calls to the MeterUsage API are throttled.
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
class TimestampOutOfBoundsException(autoboto.ShapeBase):
    """
    The timestamp value passed in the meterUsage() is out of allowed range.
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
class UsageRecord(autoboto.ShapeBase):
    """
    A UsageRecord indicates a quantity of usage for a given product, customer,
    dimension and time.

    Multiple requests with the same UsageRecords as input will be deduplicated to
    prevent double charges.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "timestamp",
                "Timestamp",
                autoboto.TypeInfo(datetime.datetime),
            ),
            (
                "customer_identifier",
                "CustomerIdentifier",
                autoboto.TypeInfo(str),
            ),
            (
                "dimension",
                "Dimension",
                autoboto.TypeInfo(str),
            ),
            (
                "quantity",
                "Quantity",
                autoboto.TypeInfo(int),
            ),
        ]

    # Timestamp of the hour, recorded in UTC. The seconds and milliseconds
    # portions of the timestamp will be ignored.

    # Your application can meter usage for up to one hour in the past.
    timestamp: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The CustomerIdentifier is obtained through the ResolveCustomer operation
    # and represents an individual buyer in your application.
    customer_identifier: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # During the process of registering a product on AWS Marketplace, up to eight
    # dimensions are specified. These represent different units of value in your
    # application.
    dimension: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The quantity of usage consumed by the customer for the given dimension and
    # time.
    quantity: int = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class UsageRecordResult(autoboto.ShapeBase):
    """
    A UsageRecordResult indicates the status of a given UsageRecord processed by
    BatchMeterUsage.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "usage_record",
                "UsageRecord",
                autoboto.TypeInfo(UsageRecord),
            ),
            (
                "metering_record_id",
                "MeteringRecordId",
                autoboto.TypeInfo(str),
            ),
            (
                "status",
                "Status",
                autoboto.TypeInfo(UsageRecordResultStatus),
            ),
        ]

    # The UsageRecord that was part of the BatchMeterUsage request.
    usage_record: "UsageRecord" = dataclasses.field(default_factory=dict, )

    # The MeteringRecordId is a unique identifier for this metering event.
    metering_record_id: str = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The UsageRecordResult Status indicates the status of an individual
    # UsageRecord processed by BatchMeterUsage.

    #   * _Success_ \- The UsageRecord was accepted and honored by BatchMeterUsage.

    #   * _CustomerNotSubscribed_ \- The CustomerIdentifier specified is not subscribed to your product. The UsageRecord was not honored. Future UsageRecords for this customer will fail until the customer subscribes to your product.

    #   * _DuplicateRecord_ \- Indicates that the UsageRecord was invalid and not honored. A previously metered UsageRecord had the same customer, dimension, and time, but a different quantity.
    status: "UsageRecordResultStatus" = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


class UsageRecordResultStatus(Enum):
    Success = "Success"
    CustomerNotSubscribed = "CustomerNotSubscribed"
    DuplicateRecord = "DuplicateRecord"
