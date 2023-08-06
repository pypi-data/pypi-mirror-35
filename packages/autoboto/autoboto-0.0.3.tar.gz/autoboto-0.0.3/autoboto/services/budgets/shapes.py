import datetime
import typing
import autoboto
from enum import Enum
import dataclasses


@dataclasses.dataclass
class Budget(autoboto.ShapeBase):
    """
    Represents the output of the `CreateBudget` operation. The content consists of
    the detailed metadata and data file information, and the current status of the
    `budget`.

    The ARN pattern for a budget is:
    `arn:aws:budgetservice::AccountId:budget/budgetName`
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "budget_name",
                "BudgetName",
                autoboto.TypeInfo(str),
            ),
            (
                "time_unit",
                "TimeUnit",
                autoboto.TypeInfo(TimeUnit),
            ),
            (
                "budget_type",
                "BudgetType",
                autoboto.TypeInfo(BudgetType),
            ),
            (
                "budget_limit",
                "BudgetLimit",
                autoboto.TypeInfo(Spend),
            ),
            (
                "cost_filters",
                "CostFilters",
                autoboto.TypeInfo(typing.Dict[str, typing.List[str]]),
            ),
            (
                "cost_types",
                "CostTypes",
                autoboto.TypeInfo(CostTypes),
            ),
            (
                "time_period",
                "TimePeriod",
                autoboto.TypeInfo(TimePeriod),
            ),
            (
                "calculated_spend",
                "CalculatedSpend",
                autoboto.TypeInfo(CalculatedSpend),
            ),
        ]

    # The name of a budget. Unique within accounts. `:` and `\` characters are
    # not allowed in the `BudgetName`.
    budget_name: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The length of time until a budget resets the actual and forecasted spend.
    time_unit: "TimeUnit" = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # Whether this budget tracks monetary costs, usage, or RI utilization.
    budget_type: "BudgetType" = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The total amount of cost, usage, or RI utilization that you want to track
    # with your budget.

    # `BudgetLimit` is required for cost or usage budgets, but optional for RI
    # utilization budgets. RI utilization budgets default to the only valid value
    # for RI utilization budgets, which is `100`.
    budget_limit: "Spend" = dataclasses.field(default_factory=dict, )

    # The cost filters applied to a budget, such as service or region.
    cost_filters: typing.Dict[str, typing.List[str]] = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The types of costs included in this budget.
    cost_types: "CostTypes" = dataclasses.field(default_factory=dict, )

    # The period of time covered by a budget. Has a start date and an end date.
    # The start date must come before the end date. There are no restrictions on
    # the end date.

    # If you created your budget and didn't specify a start date, AWS defaults to
    # the start of your chosen time period (i.e. DAILY, MONTHLY, QUARTERLY,
    # ANNUALLY). For example, if you created your budget on January 24th 2018,
    # chose `DAILY`, and didn't set a start date, AWS set your start date to
    # `01/24/18 00:00 UTC`. If you chose `MONTHLY`, AWS set your start date to
    # `01/01/18 00:00 UTC`. If you didn't specify an end date, AWS set your end
    # date to `06/15/87 00:00 UTC`. The defaults are the same for the AWS Billing
    # and Cost Management console and the API.

    # You can change either date with the `UpdateBudget` operation.

    # After the end date, AWS deletes the budget and all associated notifications
    # and subscribers.
    time_period: "TimePeriod" = dataclasses.field(default_factory=dict, )

    # The actual and forecasted cost or usage being tracked by a budget.
    calculated_spend: "CalculatedSpend" = dataclasses.field(
        default_factory=dict,
    )


class BudgetType(Enum):
    """
    The type of a budget. It should be COST, USAGE, or RI_UTILIZATION.
    """
    USAGE = "USAGE"
    COST = "COST"
    RI_UTILIZATION = "RI_UTILIZATION"
    RI_COVERAGE = "RI_COVERAGE"


@dataclasses.dataclass
class CalculatedSpend(autoboto.ShapeBase):
    """
    The spend objects associated with this budget. The `actualSpend` tracks how much
    you've used, cost, usage, or RI units, and the `forecastedSpend` tracks how much
    you are predicted to spend if your current usage remains steady.

    For example, if it is the 20th of the month and you have spent `50` dollars on
    Amazon EC2, your `actualSpend` is `50 USD`, and your `forecastedSpend` is `75
    USD`.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "actual_spend",
                "ActualSpend",
                autoboto.TypeInfo(Spend),
            ),
            (
                "forecasted_spend",
                "ForecastedSpend",
                autoboto.TypeInfo(Spend),
            ),
        ]

    # The amount of cost, usage, or RI units that you have used.
    actual_spend: "Spend" = dataclasses.field(default_factory=dict, )

    # The amount of cost, usage, or RI units that you are forecasted to use.
    forecasted_spend: "Spend" = dataclasses.field(default_factory=dict, )


class ComparisonOperator(Enum):
    """
    The comparison operator of a notification. Currently we support less than, equal
    to and greater than.
    """
    GREATER_THAN = "GREATER_THAN"
    LESS_THAN = "LESS_THAN"
    EQUAL_TO = "EQUAL_TO"


@dataclasses.dataclass
class CostTypes(autoboto.ShapeBase):
    """
    The types of cost included in a budget, such as tax and subscriptions.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "include_tax",
                "IncludeTax",
                autoboto.TypeInfo(bool),
            ),
            (
                "include_subscription",
                "IncludeSubscription",
                autoboto.TypeInfo(bool),
            ),
            (
                "use_blended",
                "UseBlended",
                autoboto.TypeInfo(bool),
            ),
            (
                "include_refund",
                "IncludeRefund",
                autoboto.TypeInfo(bool),
            ),
            (
                "include_credit",
                "IncludeCredit",
                autoboto.TypeInfo(bool),
            ),
            (
                "include_upfront",
                "IncludeUpfront",
                autoboto.TypeInfo(bool),
            ),
            (
                "include_recurring",
                "IncludeRecurring",
                autoboto.TypeInfo(bool),
            ),
            (
                "include_other_subscription",
                "IncludeOtherSubscription",
                autoboto.TypeInfo(bool),
            ),
            (
                "include_support",
                "IncludeSupport",
                autoboto.TypeInfo(bool),
            ),
            (
                "include_discount",
                "IncludeDiscount",
                autoboto.TypeInfo(bool),
            ),
            (
                "use_amortized",
                "UseAmortized",
                autoboto.TypeInfo(bool),
            ),
        ]

    # Specifies whether a budget includes taxes.

    # The default value is `true`.
    include_tax: bool = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # Specifies whether a budget includes subscriptions.

    # The default value is `true`.
    include_subscription: bool = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # Specifies whether a budget uses blended rate.

    # The default value is `false`.
    use_blended: bool = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # Specifies whether a budget includes refunds.

    # The default value is `true`.
    include_refund: bool = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # Specifies whether a budget includes credits.

    # The default value is `true`.
    include_credit: bool = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # Specifies whether a budget includes upfront RI costs.

    # The default value is `true`.
    include_upfront: bool = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # Specifies whether a budget includes recurring fees such as monthly RI fees.

    # The default value is `true`.
    include_recurring: bool = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # Specifies whether a budget includes non-RI subscription costs.

    # The default value is `true`.
    include_other_subscription: bool = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # Specifies whether a budget includes support subscription fees.

    # The default value is `true`.
    include_support: bool = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # Specifies whether a budget includes discounts.

    # The default value is `true`.
    include_discount: bool = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # Specifies whether a budget uses the amortized rate.

    # The default value is `false`.
    use_amortized: bool = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


@dataclasses.dataclass
class CreateBudgetRequest(autoboto.ShapeBase):
    """
    Request of CreateBudget
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "account_id",
                "AccountId",
                autoboto.TypeInfo(str),
            ),
            (
                "budget",
                "Budget",
                autoboto.TypeInfo(Budget),
            ),
            (
                "notifications_with_subscribers",
                "NotificationsWithSubscribers",
                autoboto.TypeInfo(typing.List[NotificationWithSubscribers]),
            ),
        ]

    # The `accountId` that is associated with the budget.
    account_id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The budget object that you want to create.
    budget: "Budget" = dataclasses.field(default_factory=dict, )

    # A notification that you want to associate with a budget. A budget can have
    # up to five notifications, and each notification can have one SNS subscriber
    # and up to ten email subscribers. If you include notifications and
    # subscribers in your `CreateBudget` call, AWS creates the notifications and
    # subscribers for you.
    notifications_with_subscribers: typing.List["NotificationWithSubscribers"
                                               ] = dataclasses.field(
                                                   default_factory=list,
                                               )


@dataclasses.dataclass
class CreateBudgetResponse(autoboto.ShapeBase):
    """
    Response of CreateBudget
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class CreateNotificationRequest(autoboto.ShapeBase):
    """
    Request of CreateNotification
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "account_id",
                "AccountId",
                autoboto.TypeInfo(str),
            ),
            (
                "budget_name",
                "BudgetName",
                autoboto.TypeInfo(str),
            ),
            (
                "notification",
                "Notification",
                autoboto.TypeInfo(Notification),
            ),
            (
                "subscribers",
                "Subscribers",
                autoboto.TypeInfo(typing.List[Subscriber]),
            ),
        ]

    # The `accountId` that is associated with the budget that you want to create
    # a notification for.
    account_id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The name of the budget that you want AWS to notified you about. Budget
    # names must be unique within an account.
    budget_name: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The notification that you want to create.
    notification: "Notification" = dataclasses.field(default_factory=dict, )

    # A list of subscribers that you want to associate with the notification.
    # Each notification can have one SNS subscriber and up to ten email
    # subscribers.
    subscribers: typing.List["Subscriber"] = dataclasses.field(
        default_factory=list,
    )


@dataclasses.dataclass
class CreateNotificationResponse(autoboto.ShapeBase):
    """
    Response of CreateNotification
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class CreateSubscriberRequest(autoboto.ShapeBase):
    """
    Request of CreateSubscriber
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "account_id",
                "AccountId",
                autoboto.TypeInfo(str),
            ),
            (
                "budget_name",
                "BudgetName",
                autoboto.TypeInfo(str),
            ),
            (
                "notification",
                "Notification",
                autoboto.TypeInfo(Notification),
            ),
            (
                "subscriber",
                "Subscriber",
                autoboto.TypeInfo(Subscriber),
            ),
        ]

    # The `accountId` associated with the budget that you want to create a
    # subscriber for.
    account_id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The name of the budget that you want to subscribe to. Budget names must be
    # unique within an account.
    budget_name: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The notification that you want to create a subscriber for.
    notification: "Notification" = dataclasses.field(default_factory=dict, )

    # The subscriber that you want to associate with a budget notification.
    subscriber: "Subscriber" = dataclasses.field(default_factory=dict, )


@dataclasses.dataclass
class CreateSubscriberResponse(autoboto.ShapeBase):
    """
    Response of CreateSubscriber
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class CreationLimitExceededException(autoboto.ShapeBase):
    """
    You've exceeded the notification or subscriber limit.
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

    # The error message the exception carries.
    message: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class DeleteBudgetRequest(autoboto.ShapeBase):
    """
    Request of DeleteBudget
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "account_id",
                "AccountId",
                autoboto.TypeInfo(str),
            ),
            (
                "budget_name",
                "BudgetName",
                autoboto.TypeInfo(str),
            ),
        ]

    # The `accountId` that is associated with the budget that you want to delete.
    account_id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The name of the budget that you want to delete.
    budget_name: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class DeleteBudgetResponse(autoboto.ShapeBase):
    """
    Response of DeleteBudget
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class DeleteNotificationRequest(autoboto.ShapeBase):
    """
    Request of DeleteNotification
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "account_id",
                "AccountId",
                autoboto.TypeInfo(str),
            ),
            (
                "budget_name",
                "BudgetName",
                autoboto.TypeInfo(str),
            ),
            (
                "notification",
                "Notification",
                autoboto.TypeInfo(Notification),
            ),
        ]

    # The `accountId` that is associated with the budget whose notification you
    # want to delete.
    account_id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The name of the budget whose notification you want to delete.
    budget_name: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The notification that you want to delete.
    notification: "Notification" = dataclasses.field(default_factory=dict, )


@dataclasses.dataclass
class DeleteNotificationResponse(autoboto.ShapeBase):
    """
    Response of DeleteNotification
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class DeleteSubscriberRequest(autoboto.ShapeBase):
    """
    Request of DeleteSubscriber
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "account_id",
                "AccountId",
                autoboto.TypeInfo(str),
            ),
            (
                "budget_name",
                "BudgetName",
                autoboto.TypeInfo(str),
            ),
            (
                "notification",
                "Notification",
                autoboto.TypeInfo(Notification),
            ),
            (
                "subscriber",
                "Subscriber",
                autoboto.TypeInfo(Subscriber),
            ),
        ]

    # The `accountId` that is associated with the budget whose subscriber you
    # want to delete.
    account_id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The name of the budget whose subscriber you want to delete.
    budget_name: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The notification whose subscriber you want to delete.
    notification: "Notification" = dataclasses.field(default_factory=dict, )

    # The subscriber that you want to delete.
    subscriber: "Subscriber" = dataclasses.field(default_factory=dict, )


@dataclasses.dataclass
class DeleteSubscriberResponse(autoboto.ShapeBase):
    """
    Response of DeleteSubscriber
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class DescribeBudgetRequest(autoboto.ShapeBase):
    """
    Request of DescribeBudget
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "account_id",
                "AccountId",
                autoboto.TypeInfo(str),
            ),
            (
                "budget_name",
                "BudgetName",
                autoboto.TypeInfo(str),
            ),
        ]

    # The `accountId` that is associated with the budget that you want a
    # description of.
    account_id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The name of the budget that you want a description of.
    budget_name: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class DescribeBudgetResponse(autoboto.ShapeBase):
    """
    Response of DescribeBudget
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "budget",
                "Budget",
                autoboto.TypeInfo(Budget),
            ),
        ]

    # The description of the budget.
    budget: "Budget" = dataclasses.field(default_factory=dict, )


@dataclasses.dataclass
class DescribeBudgetsRequest(autoboto.ShapeBase):
    """
    Request of DescribeBudgets
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "account_id",
                "AccountId",
                autoboto.TypeInfo(str),
            ),
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

    # The `accountId` that is associated with the budgets that you want
    # descriptions of.
    account_id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # Optional integer. Specifies the maximum number of results to return in
    # response.
    max_results: int = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The pagination token that indicates the next set of results to retrieve.
    next_token: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class DescribeBudgetsResponse(autoboto.ShapeBase):
    """
    Response of DescribeBudgets
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "budgets",
                "Budgets",
                autoboto.TypeInfo(typing.List[Budget]),
            ),
            (
                "next_token",
                "NextToken",
                autoboto.TypeInfo(str),
            ),
        ]

    # A list of budgets.
    budgets: typing.List["Budget"] = dataclasses.field(default_factory=list, )

    # The pagination token that indicates the next set of results that you can
    # retrieve.
    next_token: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class DescribeNotificationsForBudgetRequest(autoboto.ShapeBase):
    """
    Request of DescribeNotificationsForBudget
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "account_id",
                "AccountId",
                autoboto.TypeInfo(str),
            ),
            (
                "budget_name",
                "BudgetName",
                autoboto.TypeInfo(str),
            ),
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

    # The `accountId` that is associated with the budget whose notifications you
    # want descriptions of.
    account_id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The name of the budget whose notifications you want descriptions of.
    budget_name: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # Optional integer. Specifies the maximum number of results to return in
    # response.
    max_results: int = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The pagination token that indicates the next set of results to retrieve.
    next_token: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class DescribeNotificationsForBudgetResponse(autoboto.ShapeBase):
    """
    Response of GetNotificationsForBudget
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "notifications",
                "Notifications",
                autoboto.TypeInfo(typing.List[Notification]),
            ),
            (
                "next_token",
                "NextToken",
                autoboto.TypeInfo(str),
            ),
        ]

    # A list of notifications associated with a budget.
    notifications: typing.List["Notification"] = dataclasses.field(
        default_factory=list,
    )

    # The pagination token that indicates the next set of results that you can
    # retrieve.
    next_token: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class DescribeSubscribersForNotificationRequest(autoboto.ShapeBase):
    """
    Request of DescribeSubscribersForNotification
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "account_id",
                "AccountId",
                autoboto.TypeInfo(str),
            ),
            (
                "budget_name",
                "BudgetName",
                autoboto.TypeInfo(str),
            ),
            (
                "notification",
                "Notification",
                autoboto.TypeInfo(Notification),
            ),
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

    # The `accountId` that is associated with the budget whose subscribers you
    # want descriptions of.
    account_id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The name of the budget whose subscribers you want descriptions of.
    budget_name: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The notification whose subscribers you want to list.
    notification: "Notification" = dataclasses.field(default_factory=dict, )

    # Optional integer. Specifies the maximum number of results to return in
    # response.
    max_results: int = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The pagination token that indicates the next set of results to retrieve.
    next_token: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class DescribeSubscribersForNotificationResponse(autoboto.ShapeBase):
    """
    Response of DescribeSubscribersForNotification
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "subscribers",
                "Subscribers",
                autoboto.TypeInfo(typing.List[Subscriber]),
            ),
            (
                "next_token",
                "NextToken",
                autoboto.TypeInfo(str),
            ),
        ]

    # A list of subscribers associated with a notification.
    subscribers: typing.List["Subscriber"] = dataclasses.field(
        default_factory=list,
    )

    # The pagination token that indicates the next set of results that you can
    # retrieve.
    next_token: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class DuplicateRecordException(autoboto.ShapeBase):
    """
    The budget name already exists. Budget names must be unique within an account.
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

    # The error message the exception carries.
    message: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class ExpiredNextTokenException(autoboto.ShapeBase):
    """
    The pagination token expired.
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

    # The error message the exception carries.
    message: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class InternalErrorException(autoboto.ShapeBase):
    """
    An error on the server occurred during the processing of your request. Try again
    later.
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

    # The error message the exception carries.
    message: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class InvalidNextTokenException(autoboto.ShapeBase):
    """
    The pagination token is invalid.
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

    # The error message the exception carries.
    message: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class InvalidParameterException(autoboto.ShapeBase):
    """
    An error on the client occurred. Typically, the cause is an invalid input value.
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

    # The error message the exception carries.
    message: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class NotFoundException(autoboto.ShapeBase):
    """
    We can’t locate the resource that you specified.
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

    # The error message the exception carries.
    message: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class Notification(autoboto.ShapeBase):
    """
    A notification associated with a budget. A budget can have up to five
    notifications.

    Each notification must have at least one subscriber. A notification can have one
    SNS subscriber and up to ten email subscribers, for a total of 11 subscribers.

    For example, if you have a budget for 200 dollars and you want to be notified
    when you go over 160 dollars, create a notification with the following
    parameters:

      * A notificationType of `ACTUAL`

      * A comparisonOperator of `GREATER_THAN`

      * A notification threshold of `80`
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "notification_type",
                "NotificationType",
                autoboto.TypeInfo(NotificationType),
            ),
            (
                "comparison_operator",
                "ComparisonOperator",
                autoboto.TypeInfo(ComparisonOperator),
            ),
            (
                "threshold",
                "Threshold",
                autoboto.TypeInfo(float),
            ),
            (
                "threshold_type",
                "ThresholdType",
                autoboto.TypeInfo(ThresholdType),
            ),
        ]

    # Whether the notification is for how much you have spent (`ACTUAL`) or for
    # how much you are forecasted to spend (`FORECASTED`).
    notification_type: "NotificationType" = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The comparison used for this notification.
    comparison_operator: "ComparisonOperator" = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The threshold associated with a notification. Thresholds are always a
    # percentage.
    threshold: float = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The type of threshold for a notification. For `ACTUAL` thresholds, AWS
    # notifies you when you go over the threshold, and for `FORECASTED`
    # thresholds AWS notifies you when you are forecasted to go over the
    # threshold.
    threshold_type: "ThresholdType" = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


class NotificationType(Enum):
    """
    The type of a notification. It should be ACTUAL or FORECASTED.
    """
    ACTUAL = "ACTUAL"
    FORECASTED = "FORECASTED"


@dataclasses.dataclass
class NotificationWithSubscribers(autoboto.ShapeBase):
    """
    A notification with subscribers. A notification can have one SNS subscriber and
    up to ten email subscribers, for a total of 11 subscribers.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "notification",
                "Notification",
                autoboto.TypeInfo(Notification),
            ),
            (
                "subscribers",
                "Subscribers",
                autoboto.TypeInfo(typing.List[Subscriber]),
            ),
        ]

    # The notification associated with a budget.
    notification: "Notification" = dataclasses.field(default_factory=dict, )

    # A list of subscribers who are subscribed to this notification.
    subscribers: typing.List["Subscriber"] = dataclasses.field(
        default_factory=list,
    )


@dataclasses.dataclass
class Spend(autoboto.ShapeBase):
    """
    The amount of cost or usage being measured for a budget.

    For example, a `Spend` for `3 GB` of S3 usage would have the following
    parameters:

      * An `Amount` of `3`

      * A `unit` of `GB`
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "amount",
                "Amount",
                autoboto.TypeInfo(str),
            ),
            (
                "unit",
                "Unit",
                autoboto.TypeInfo(str),
            ),
        ]

    # The cost or usage amount associated with a budget forecast, actual spend,
    # or budget threshold.
    amount: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The unit of measurement used for the budget forecast, actual spend, or
    # budget threshold, such as dollars or GB.
    unit: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


@dataclasses.dataclass
class Subscriber(autoboto.ShapeBase):
    """
    The subscriber to a budget notification. The subscriber consists of a
    subscription type and either an Amazon Simple Notification Service topic or an
    email address.

    For example, an email subscriber would have the following parameters:

      * A `subscriptionType` of `EMAIL`

      * An `address` of `example@example.com`
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "subscription_type",
                "SubscriptionType",
                autoboto.TypeInfo(SubscriptionType),
            ),
            (
                "address",
                "Address",
                autoboto.TypeInfo(str),
            ),
        ]

    # The type of notification that AWS sends to a subscriber.
    subscription_type: "SubscriptionType" = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The address that AWS sends budget notifications to, either an SNS topic or
    # an email.
    address: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )


class SubscriptionType(Enum):
    """
    The subscription type of the subscriber. It can be SMS or EMAIL.
    """
    SNS = "SNS"
    EMAIL = "EMAIL"


class ThresholdType(Enum):
    """
    The type of threshold for a notification. It can be PERCENTAGE or
    ABSOLUTE_VALUE.
    """
    PERCENTAGE = "PERCENTAGE"
    ABSOLUTE_VALUE = "ABSOLUTE_VALUE"


@dataclasses.dataclass
class TimePeriod(autoboto.ShapeBase):
    """
    The period of time covered by a budget. Has a start date and an end date. The
    start date must come before the end date. There are no restrictions on the end
    date.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "start",
                "Start",
                autoboto.TypeInfo(datetime.datetime),
            ),
            (
                "end",
                "End",
                autoboto.TypeInfo(datetime.datetime),
            ),
        ]

    # The start date for a budget. If you created your budget and didn't specify
    # a start date, AWS defaults to the start of your chosen time period (i.e.
    # DAILY, MONTHLY, QUARTERLY, ANNUALLY). For example, if you created your
    # budget on January 24th 2018, chose `DAILY`, and didn't set a start date,
    # AWS set your start date to `01/24/18 00:00 UTC`. If you chose `MONTHLY`,
    # AWS set your start date to `01/01/18 00:00 UTC`. The defaults are the same
    # for the AWS Billing and Cost Management console and the API.

    # You can change your start date with the `UpdateBudget` operation.
    start: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )

    # The end date for a budget. If you didn't specify an end date, AWS set your
    # end date to `06/15/87 00:00 UTC`. The defaults are the same for the AWS
    # Billing and Cost Management console and the API.

    # After the end date, AWS deletes the budget and all associated notifications
    # and subscribers. You can change your end date with the `UpdateBudget`
    # operation.
    end: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase._NOT_SET,
    )


class TimeUnit(Enum):
    """
    The time unit of the budget. e.g. MONTHLY, QUARTERLY, etc.
    """
    DAILY = "DAILY"
    MONTHLY = "MONTHLY"
    QUARTERLY = "QUARTERLY"
    ANNUALLY = "ANNUALLY"


@dataclasses.dataclass
class UpdateBudgetRequest(autoboto.ShapeBase):
    """
    Request of UpdateBudget
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "account_id",
                "AccountId",
                autoboto.TypeInfo(str),
            ),
            (
                "new_budget",
                "NewBudget",
                autoboto.TypeInfo(Budget),
            ),
        ]

    # The `accountId` that is associated with the budget that you want to update.
    account_id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The budget that you want to update your budget to.
    new_budget: "Budget" = dataclasses.field(default_factory=dict, )


@dataclasses.dataclass
class UpdateBudgetResponse(autoboto.ShapeBase):
    """
    Response of UpdateBudget
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class UpdateNotificationRequest(autoboto.ShapeBase):
    """
    Request of UpdateNotification
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "account_id",
                "AccountId",
                autoboto.TypeInfo(str),
            ),
            (
                "budget_name",
                "BudgetName",
                autoboto.TypeInfo(str),
            ),
            (
                "old_notification",
                "OldNotification",
                autoboto.TypeInfo(Notification),
            ),
            (
                "new_notification",
                "NewNotification",
                autoboto.TypeInfo(Notification),
            ),
        ]

    # The `accountId` that is associated with the budget whose notification you
    # want to update.
    account_id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The name of the budget whose notification you want to update.
    budget_name: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The previous notification associated with a budget.
    old_notification: "Notification" = dataclasses.field(default_factory=dict, )

    # The updated notification to be associated with a budget.
    new_notification: "Notification" = dataclasses.field(default_factory=dict, )


@dataclasses.dataclass
class UpdateNotificationResponse(autoboto.ShapeBase):
    """
    Response of UpdateNotification
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class UpdateSubscriberRequest(autoboto.ShapeBase):
    """
    Request of UpdateSubscriber
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "account_id",
                "AccountId",
                autoboto.TypeInfo(str),
            ),
            (
                "budget_name",
                "BudgetName",
                autoboto.TypeInfo(str),
            ),
            (
                "notification",
                "Notification",
                autoboto.TypeInfo(Notification),
            ),
            (
                "old_subscriber",
                "OldSubscriber",
                autoboto.TypeInfo(Subscriber),
            ),
            (
                "new_subscriber",
                "NewSubscriber",
                autoboto.TypeInfo(Subscriber),
            ),
        ]

    # The `accountId` that is associated with the budget whose subscriber you
    # want to update.
    account_id: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The name of the budget whose subscriber you want to update.
    budget_name: str = dataclasses.field(default=autoboto.ShapeBase._NOT_SET, )

    # The notification whose subscriber you want to update.
    notification: "Notification" = dataclasses.field(default_factory=dict, )

    # The previous subscriber associated with a budget notification.
    old_subscriber: "Subscriber" = dataclasses.field(default_factory=dict, )

    # The updated subscriber associated with a budget notification.
    new_subscriber: "Subscriber" = dataclasses.field(default_factory=dict, )


@dataclasses.dataclass
class UpdateSubscriberResponse(autoboto.ShapeBase):
    """
    Response of UpdateSubscriber
    """

    @classmethod
    def _get_boto_mapping(cls):
        return []
