import datetime
import typing
import autoboto
from enum import Enum
import dataclasses


@dataclasses.dataclass
class AccessDeniedException(autoboto.ShapeBase):
    """
    Lightsail throws this exception when the user cannot be authenticated or uses
    invalid credentials to access a resource.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "code",
                "code",
                autoboto.TypeInfo(str),
            ),
            (
                "docs",
                "docs",
                autoboto.TypeInfo(str),
            ),
            (
                "message",
                "message",
                autoboto.TypeInfo(str),
            ),
            (
                "tip",
                "tip",
                autoboto.TypeInfo(str),
            ),
        ]

    code: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )
    docs: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )
    message: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )
    tip: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


class AccessDirection(Enum):
    inbound = "inbound"
    outbound = "outbound"


@dataclasses.dataclass
class AccountSetupInProgressException(autoboto.ShapeBase):
    """
    Lightsail throws this exception when an account is still in the setup in
    progress state.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "code",
                "code",
                autoboto.TypeInfo(str),
            ),
            (
                "docs",
                "docs",
                autoboto.TypeInfo(str),
            ),
            (
                "message",
                "message",
                autoboto.TypeInfo(str),
            ),
            (
                "tip",
                "tip",
                autoboto.TypeInfo(str),
            ),
        ]

    code: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )
    docs: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )
    message: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )
    tip: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class AllocateStaticIpRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "static_ip_name",
                "staticIpName",
                autoboto.TypeInfo(str),
            ),
        ]

    # The name of the static IP address.
    static_ip_name: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class AllocateStaticIpResult(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "operations",
                "operations",
                autoboto.TypeInfo(typing.List[Operation]),
            ),
        ]

    # An array of key-value pairs containing information about the static IP
    # address you allocated.
    operations: typing.List["Operation"] = dataclasses.field(
        default_factory=list,
    )


@dataclasses.dataclass
class AttachDiskRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "disk_name",
                "diskName",
                autoboto.TypeInfo(str),
            ),
            (
                "instance_name",
                "instanceName",
                autoboto.TypeInfo(str),
            ),
            (
                "disk_path",
                "diskPath",
                autoboto.TypeInfo(str),
            ),
        ]

    # The unique Lightsail disk name (e.g., `my-disk`).
    disk_name: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The name of the Lightsail instance where you want to utilize the storage
    # disk.
    instance_name: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The disk path to expose to the instance (e.g., `/dev/xvdf`).
    disk_path: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class AttachDiskResult(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "operations",
                "operations",
                autoboto.TypeInfo(typing.List[Operation]),
            ),
        ]

    # An object describing the API operations.
    operations: typing.List["Operation"] = dataclasses.field(
        default_factory=list,
    )


@dataclasses.dataclass
class AttachInstancesToLoadBalancerRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "load_balancer_name",
                "loadBalancerName",
                autoboto.TypeInfo(str),
            ),
            (
                "instance_names",
                "instanceNames",
                autoboto.TypeInfo(typing.List[str]),
            ),
        ]

    # The name of the load balancer.
    load_balancer_name: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # An array of strings representing the instance name(s) you want to attach to
    # your load balancer.

    # An instance must be `running` before you can attach it to your load
    # balancer.

    # There are no additional limits on the number of instances you can attach to
    # your load balancer, aside from the limit of Lightsail instances you can
    # create in your account (20).
    instance_names: typing.List[str] = dataclasses.field(default_factory=list, )


@dataclasses.dataclass
class AttachInstancesToLoadBalancerResult(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "operations",
                "operations",
                autoboto.TypeInfo(typing.List[Operation]),
            ),
        ]

    # An object representing the API operations.
    operations: typing.List["Operation"] = dataclasses.field(
        default_factory=list,
    )


@dataclasses.dataclass
class AttachLoadBalancerTlsCertificateRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "load_balancer_name",
                "loadBalancerName",
                autoboto.TypeInfo(str),
            ),
            (
                "certificate_name",
                "certificateName",
                autoboto.TypeInfo(str),
            ),
        ]

    # The name of the load balancer to which you want to associate the SSL/TLS
    # certificate.
    load_balancer_name: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The name of your SSL/TLS certificate.
    certificate_name: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class AttachLoadBalancerTlsCertificateResult(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "operations",
                "operations",
                autoboto.TypeInfo(typing.List[Operation]),
            ),
        ]

    # An object representing the API operations.

    # These SSL/TLS certificates are only usable by Lightsail load balancers. You
    # can't get the certificate and use it for another purpose.
    operations: typing.List["Operation"] = dataclasses.field(
        default_factory=list,
    )


@dataclasses.dataclass
class AttachStaticIpRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "static_ip_name",
                "staticIpName",
                autoboto.TypeInfo(str),
            ),
            (
                "instance_name",
                "instanceName",
                autoboto.TypeInfo(str),
            ),
        ]

    # The name of the static IP.
    static_ip_name: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The instance name to which you want to attach the static IP address.
    instance_name: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class AttachStaticIpResult(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "operations",
                "operations",
                autoboto.TypeInfo(typing.List[Operation]),
            ),
        ]

    # An array of key-value pairs containing information about your API
    # operations.
    operations: typing.List["Operation"] = dataclasses.field(
        default_factory=list,
    )


@dataclasses.dataclass
class AvailabilityZone(autoboto.ShapeBase):
    """
    Describes an Availability Zone.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "zone_name",
                "zoneName",
                autoboto.TypeInfo(str),
            ),
            (
                "state",
                "state",
                autoboto.TypeInfo(str),
            ),
        ]

    # The name of the Availability Zone. The format is `us-east-2a` (case-
    # sensitive).
    zone_name: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The state of the Availability Zone.
    state: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class Blueprint(autoboto.ShapeBase):
    """
    Describes a blueprint (a virtual private server image).
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "blueprint_id",
                "blueprintId",
                autoboto.TypeInfo(str),
            ),
            (
                "name",
                "name",
                autoboto.TypeInfo(str),
            ),
            (
                "group",
                "group",
                autoboto.TypeInfo(str),
            ),
            (
                "type",
                "type",
                autoboto.TypeInfo(BlueprintType),
            ),
            (
                "description",
                "description",
                autoboto.TypeInfo(str),
            ),
            (
                "is_active",
                "isActive",
                autoboto.TypeInfo(bool),
            ),
            (
                "min_power",
                "minPower",
                autoboto.TypeInfo(int),
            ),
            (
                "version",
                "version",
                autoboto.TypeInfo(str),
            ),
            (
                "version_code",
                "versionCode",
                autoboto.TypeInfo(str),
            ),
            (
                "product_url",
                "productUrl",
                autoboto.TypeInfo(str),
            ),
            (
                "license_url",
                "licenseUrl",
                autoboto.TypeInfo(str),
            ),
            (
                "platform",
                "platform",
                autoboto.TypeInfo(InstancePlatform),
            ),
        ]

    # The ID for the virtual private server image (e.g., `app_wordpress_4_4` or
    # `app_lamp_7_0`).
    blueprint_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The friendly name of the blueprint (e.g., `Amazon Linux`).
    name: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The group name of the blueprint (e.g., `amazon-linux`).
    group: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The type of the blueprint (e.g., `os` or `app`).
    type: "BlueprintType" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The description of the blueprint.
    description: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # A Boolean value indicating whether the blueprint is active. When you update
    # your blueprints, you will inactivate old blueprints and keep the most
    # recent versions active.
    is_active: bool = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The minimum bundle power required to run this blueprint. For example, you
    # need a bundle with a power value of 500 or more to create an instance that
    # uses a blueprint with a minimum power value of 500. `0` indicates that the
    # blueprint runs on all instance sizes.
    min_power: int = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The version number of the operating system, application, or stack (e.g.,
    # `2016.03.0`).
    version: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The version code.
    version_code: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The product URL to learn more about the image or blueprint.
    product_url: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The end-user license agreement URL for the image or blueprint.
    license_url: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The operating system platform (either Linux/Unix-based or Windows Server-
    # based) of the blueprint.
    platform: "InstancePlatform" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


class BlueprintType(Enum):
    os = "os"
    app = "app"


@dataclasses.dataclass
class Bundle(autoboto.ShapeBase):
    """
    Describes a bundle, which is a set of specs describing your virtual private
    server (or _instance_ ).
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "price",
                "price",
                autoboto.TypeInfo(float),
            ),
            (
                "cpu_count",
                "cpuCount",
                autoboto.TypeInfo(int),
            ),
            (
                "disk_size_in_gb",
                "diskSizeInGb",
                autoboto.TypeInfo(int),
            ),
            (
                "bundle_id",
                "bundleId",
                autoboto.TypeInfo(str),
            ),
            (
                "instance_type",
                "instanceType",
                autoboto.TypeInfo(str),
            ),
            (
                "is_active",
                "isActive",
                autoboto.TypeInfo(bool),
            ),
            (
                "name",
                "name",
                autoboto.TypeInfo(str),
            ),
            (
                "power",
                "power",
                autoboto.TypeInfo(int),
            ),
            (
                "ram_size_in_gb",
                "ramSizeInGb",
                autoboto.TypeInfo(float),
            ),
            (
                "transfer_per_month_in_gb",
                "transferPerMonthInGb",
                autoboto.TypeInfo(int),
            ),
            (
                "supported_platforms",
                "supportedPlatforms",
                autoboto.TypeInfo(typing.List[InstancePlatform]),
            ),
        ]

    # The price in US dollars (e.g., `5.0`).
    price: float = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The number of vCPUs included in the bundle (e.g., `2`).
    cpu_count: int = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The size of the SSD (e.g., `30`).
    disk_size_in_gb: int = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The bundle ID (e.g., `micro_1_0`).
    bundle_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The Amazon EC2 instance type (e.g., `t2.micro`).
    instance_type: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # A Boolean value indicating whether the bundle is active.
    is_active: bool = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # A friendly name for the bundle (e.g., `Micro`).
    name: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # A numeric value that represents the power of the bundle (e.g., `500`). You
    # can use the bundle's power value in conjunction with a blueprint's minimum
    # power value to determine whether the blueprint will run on the bundle. For
    # example, you need a bundle with a power value of 500 or more to create an
    # instance that uses a blueprint with a minimum power value of 500.
    power: int = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The amount of RAM in GB (e.g., `2.0`).
    ram_size_in_gb: float = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The data transfer rate per month in GB (e.g., `2000`).
    transfer_per_month_in_gb: int = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The operating system platform (Linux/Unix-based or Windows Server-based)
    # that the bundle supports. You can only launch a `WINDOWS` bundle on a
    # blueprint that supports the `WINDOWS` platform. `LINUX_UNIX` blueprints
    # require a `LINUX_UNIX` bundle.
    supported_platforms: typing.List["InstancePlatform"] = dataclasses.field(
        default_factory=list,
    )


@dataclasses.dataclass
class CloseInstancePublicPortsRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "port_info",
                "portInfo",
                autoboto.TypeInfo(PortInfo),
            ),
            (
                "instance_name",
                "instanceName",
                autoboto.TypeInfo(str),
            ),
        ]

    # Information about the public port you are trying to close.
    port_info: "PortInfo" = dataclasses.field(default_factory=dict, )

    # The name of the instance on which you're attempting to close the public
    # ports.
    instance_name: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class CloseInstancePublicPortsResult(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "operation",
                "operation",
                autoboto.TypeInfo(Operation),
            ),
        ]

    # An array of key-value pairs that contains information about the operation.
    operation: "Operation" = dataclasses.field(default_factory=dict, )


@dataclasses.dataclass
class CreateDiskFromSnapshotRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "disk_name",
                "diskName",
                autoboto.TypeInfo(str),
            ),
            (
                "disk_snapshot_name",
                "diskSnapshotName",
                autoboto.TypeInfo(str),
            ),
            (
                "availability_zone",
                "availabilityZone",
                autoboto.TypeInfo(str),
            ),
            (
                "size_in_gb",
                "sizeInGb",
                autoboto.TypeInfo(int),
            ),
        ]

    # The unique Lightsail disk name (e.g., `my-disk`).
    disk_name: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The name of the disk snapshot (e.g., `my-snapshot`) from which to create
    # the new storage disk.
    disk_snapshot_name: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The Availability Zone where you want to create the disk (e.g., `us-
    # east-2a`). Choose the same Availability Zone as the Lightsail instance
    # where you want to create the disk.

    # Use the GetRegions operation to list the Availability Zones where Lightsail
    # is currently available.
    availability_zone: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The size of the disk in GB (e.g., `32`).
    size_in_gb: int = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class CreateDiskFromSnapshotResult(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "operations",
                "operations",
                autoboto.TypeInfo(typing.List[Operation]),
            ),
        ]

    # An object describing the API operations.
    operations: typing.List["Operation"] = dataclasses.field(
        default_factory=list,
    )


@dataclasses.dataclass
class CreateDiskRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "disk_name",
                "diskName",
                autoboto.TypeInfo(str),
            ),
            (
                "availability_zone",
                "availabilityZone",
                autoboto.TypeInfo(str),
            ),
            (
                "size_in_gb",
                "sizeInGb",
                autoboto.TypeInfo(int),
            ),
        ]

    # The unique Lightsail disk name (e.g., `my-disk`).
    disk_name: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The Availability Zone where you want to create the disk (e.g., `us-
    # east-2a`). Choose the same Availability Zone as the Lightsail instance
    # where you want to create the disk.

    # Use the GetRegions operation to list the Availability Zones where Lightsail
    # is currently available.
    availability_zone: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The size of the disk in GB (e.g., `32`).
    size_in_gb: int = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class CreateDiskResult(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "operations",
                "operations",
                autoboto.TypeInfo(typing.List[Operation]),
            ),
        ]

    # An object describing the API operations.
    operations: typing.List["Operation"] = dataclasses.field(
        default_factory=list,
    )


@dataclasses.dataclass
class CreateDiskSnapshotRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "disk_name",
                "diskName",
                autoboto.TypeInfo(str),
            ),
            (
                "disk_snapshot_name",
                "diskSnapshotName",
                autoboto.TypeInfo(str),
            ),
        ]

    # The unique name of the source disk (e.g., `my-source-disk`).
    disk_name: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The name of the destination disk snapshot (e.g., `my-disk-snapshot`) based
    # on the source disk.
    disk_snapshot_name: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class CreateDiskSnapshotResult(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "operations",
                "operations",
                autoboto.TypeInfo(typing.List[Operation]),
            ),
        ]

    # An object describing the API operations.
    operations: typing.List["Operation"] = dataclasses.field(
        default_factory=list,
    )


@dataclasses.dataclass
class CreateDomainEntryRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "domain_name",
                "domainName",
                autoboto.TypeInfo(str),
            ),
            (
                "domain_entry",
                "domainEntry",
                autoboto.TypeInfo(DomainEntry),
            ),
        ]

    # The domain name (e.g., `example.com`) for which you want to create the
    # domain entry.
    domain_name: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # An array of key-value pairs containing information about the domain entry
    # request.
    domain_entry: "DomainEntry" = dataclasses.field(default_factory=dict, )


@dataclasses.dataclass
class CreateDomainEntryResult(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "operation",
                "operation",
                autoboto.TypeInfo(Operation),
            ),
        ]

    # An array of key-value pairs containing information about the operation.
    operation: "Operation" = dataclasses.field(default_factory=dict, )


@dataclasses.dataclass
class CreateDomainRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "domain_name",
                "domainName",
                autoboto.TypeInfo(str),
            ),
        ]

    # The domain name to manage (e.g., `example.com`).

    # You cannot register a new domain name using Lightsail. You must register a
    # domain name using Amazon Route 53 or another domain name registrar. If you
    # have already registered your domain, you can enter its name in this
    # parameter to manage the DNS records for that domain.
    domain_name: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class CreateDomainResult(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "operation",
                "operation",
                autoboto.TypeInfo(Operation),
            ),
        ]

    # An array of key-value pairs containing information about the domain
    # resource you created.
    operation: "Operation" = dataclasses.field(default_factory=dict, )


@dataclasses.dataclass
class CreateInstanceSnapshotRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "instance_snapshot_name",
                "instanceSnapshotName",
                autoboto.TypeInfo(str),
            ),
            (
                "instance_name",
                "instanceName",
                autoboto.TypeInfo(str),
            ),
        ]

    # The name for your new snapshot.
    instance_snapshot_name: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The Lightsail instance on which to base your snapshot.
    instance_name: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class CreateInstanceSnapshotResult(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "operations",
                "operations",
                autoboto.TypeInfo(typing.List[Operation]),
            ),
        ]

    # An array of key-value pairs containing information about the results of
    # your create instances snapshot request.
    operations: typing.List["Operation"] = dataclasses.field(
        default_factory=list,
    )


@dataclasses.dataclass
class CreateInstancesFromSnapshotRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "instance_names",
                "instanceNames",
                autoboto.TypeInfo(typing.List[str]),
            ),
            (
                "availability_zone",
                "availabilityZone",
                autoboto.TypeInfo(str),
            ),
            (
                "instance_snapshot_name",
                "instanceSnapshotName",
                autoboto.TypeInfo(str),
            ),
            (
                "bundle_id",
                "bundleId",
                autoboto.TypeInfo(str),
            ),
            (
                "attached_disk_mapping",
                "attachedDiskMapping",
                autoboto.TypeInfo(typing.Dict[str, typing.List[DiskMap]]),
            ),
            (
                "user_data",
                "userData",
                autoboto.TypeInfo(str),
            ),
            (
                "key_pair_name",
                "keyPairName",
                autoboto.TypeInfo(str),
            ),
        ]

    # The names for your new instances.
    instance_names: typing.List[str] = dataclasses.field(default_factory=list, )

    # The Availability Zone where you want to create your instances. Use the
    # following formatting: `us-east-2a` (case sensitive). You can get a list of
    # availability zones by using the [get
    # regions](http://docs.aws.amazon.com/lightsail/2016-11-28/api-
    # reference/API_GetRegions.html) operation. Be sure to add the `include
    # availability zones` parameter to your request.
    availability_zone: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The name of the instance snapshot on which you are basing your new
    # instances. Use the get instance snapshots operation to return information
    # about your existing snapshots.
    instance_snapshot_name: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The bundle of specification information for your virtual private server (or
    # _instance_ ), including the pricing plan (e.g., `micro_1_0`).
    bundle_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # An object containing information about one or more disk mappings.
    attached_disk_mapping: typing.Dict[str, typing.List["DiskMap"]
                                      ] = dataclasses.field(
                                          default=autoboto.ShapeBase.NOT_SET,
                                      )

    # You can create a launch script that configures a server with additional
    # user data. For example, `apt-get -y update`.

    # Depending on the machine image you choose, the command to get software on
    # your instance varies. Amazon Linux and CentOS use `yum`, Debian and Ubuntu
    # use `apt-get`, and FreeBSD uses `pkg`. For a complete list, see the [Dev
    # Guide](http://lightsail.aws.amazon.com/ls/docs/getting-
    # started/articles/pre-installed-apps).
    user_data: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The name for your key pair.
    key_pair_name: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class CreateInstancesFromSnapshotResult(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "operations",
                "operations",
                autoboto.TypeInfo(typing.List[Operation]),
            ),
        ]

    # An array of key-value pairs containing information about the results of
    # your create instances from snapshot request.
    operations: typing.List["Operation"] = dataclasses.field(
        default_factory=list,
    )


@dataclasses.dataclass
class CreateInstancesRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "instance_names",
                "instanceNames",
                autoboto.TypeInfo(typing.List[str]),
            ),
            (
                "availability_zone",
                "availabilityZone",
                autoboto.TypeInfo(str),
            ),
            (
                "blueprint_id",
                "blueprintId",
                autoboto.TypeInfo(str),
            ),
            (
                "bundle_id",
                "bundleId",
                autoboto.TypeInfo(str),
            ),
            (
                "custom_image_name",
                "customImageName",
                autoboto.TypeInfo(str),
            ),
            (
                "user_data",
                "userData",
                autoboto.TypeInfo(str),
            ),
            (
                "key_pair_name",
                "keyPairName",
                autoboto.TypeInfo(str),
            ),
        ]

    # The names to use for your new Lightsail instances. Separate multiple values
    # using quotation marks and commas, for example:
    # `["MyFirstInstance","MySecondInstance"]`
    instance_names: typing.List[str] = dataclasses.field(default_factory=list, )

    # The Availability Zone in which to create your instance. Use the following
    # format: `us-east-2a` (case sensitive). You can get a list of availability
    # zones by using the [get
    # regions](http://docs.aws.amazon.com/lightsail/2016-11-28/api-
    # reference/API_GetRegions.html) operation. Be sure to add the `include
    # availability zones` parameter to your request.
    availability_zone: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The ID for a virtual private server image (e.g., `app_wordpress_4_4` or
    # `app_lamp_7_0`). Use the get blueprints operation to return a list of
    # available images (or _blueprints_ ).
    blueprint_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The bundle of specification information for your virtual private server (or
    # _instance_ ), including the pricing plan (e.g., `micro_1_0`).
    bundle_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # (Deprecated) The name for your custom image.

    # In releases prior to June 12, 2017, this parameter was ignored by the API.
    # It is now deprecated.
    custom_image_name: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # A launch script you can create that configures a server with additional
    # user data. For example, you might want to run `apt-get -y update`.

    # Depending on the machine image you choose, the command to get software on
    # your instance varies. Amazon Linux and CentOS use `yum`, Debian and Ubuntu
    # use `apt-get`, and FreeBSD uses `pkg`. For a complete list, see the [Dev
    # Guide](https://lightsail.aws.amazon.com/ls/docs/getting-
    # started/article/compare-options-choose-lightsail-instance-image).
    user_data: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The name of your key pair.
    key_pair_name: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class CreateInstancesResult(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "operations",
                "operations",
                autoboto.TypeInfo(typing.List[Operation]),
            ),
        ]

    # An array of key-value pairs containing information about the results of
    # your create instances request.
    operations: typing.List["Operation"] = dataclasses.field(
        default_factory=list,
    )


@dataclasses.dataclass
class CreateKeyPairRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "key_pair_name",
                "keyPairName",
                autoboto.TypeInfo(str),
            ),
        ]

    # The name for your new key pair.
    key_pair_name: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class CreateKeyPairResult(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "key_pair",
                "keyPair",
                autoboto.TypeInfo(KeyPair),
            ),
            (
                "public_key_base64",
                "publicKeyBase64",
                autoboto.TypeInfo(str),
            ),
            (
                "private_key_base64",
                "privateKeyBase64",
                autoboto.TypeInfo(str),
            ),
            (
                "operation",
                "operation",
                autoboto.TypeInfo(Operation),
            ),
        ]

    # An array of key-value pairs containing information about the new key pair
    # you just created.
    key_pair: "KeyPair" = dataclasses.field(default_factory=dict, )

    # A base64-encoded public key of the `ssh-rsa` type.
    public_key_base64: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # A base64-encoded RSA private key.
    private_key_base64: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # An array of key-value pairs containing information about the results of
    # your create key pair request.
    operation: "Operation" = dataclasses.field(default_factory=dict, )


@dataclasses.dataclass
class CreateLoadBalancerRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "load_balancer_name",
                "loadBalancerName",
                autoboto.TypeInfo(str),
            ),
            (
                "instance_port",
                "instancePort",
                autoboto.TypeInfo(int),
            ),
            (
                "health_check_path",
                "healthCheckPath",
                autoboto.TypeInfo(str),
            ),
            (
                "certificate_name",
                "certificateName",
                autoboto.TypeInfo(str),
            ),
            (
                "certificate_domain_name",
                "certificateDomainName",
                autoboto.TypeInfo(str),
            ),
            (
                "certificate_alternative_names",
                "certificateAlternativeNames",
                autoboto.TypeInfo(typing.List[str]),
            ),
        ]

    # The name of your load balancer.
    load_balancer_name: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The instance port where you're creating your load balancer.
    instance_port: int = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The path you provided to perform the load balancer health check. If you
    # didn't specify a health check path, Lightsail uses the root path of your
    # website (e.g., `"/"`).

    # You may want to specify a custom health check path other than the root of
    # your application if your home page loads slowly or has a lot of media or
    # scripting on it.
    health_check_path: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The name of the SSL/TLS certificate.

    # If you specify `certificateName`, then `certificateDomainName` is required
    # (and vice-versa).
    certificate_name: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The domain name with which your certificate is associated (e.g.,
    # `example.com`).

    # If you specify `certificateDomainName`, then `certificateName` is required
    # (and vice-versa).
    certificate_domain_name: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The optional alternative domains and subdomains to use with your SSL/TLS
    # certificate (e.g., `www.example.com`, `example.com`, `m.example.com`,
    # `blog.example.com`).
    certificate_alternative_names: typing.List[str] = dataclasses.field(
        default_factory=list,
    )


@dataclasses.dataclass
class CreateLoadBalancerResult(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "operations",
                "operations",
                autoboto.TypeInfo(typing.List[Operation]),
            ),
        ]

    # An object containing information about the API operations.
    operations: typing.List["Operation"] = dataclasses.field(
        default_factory=list,
    )


@dataclasses.dataclass
class CreateLoadBalancerTlsCertificateRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "load_balancer_name",
                "loadBalancerName",
                autoboto.TypeInfo(str),
            ),
            (
                "certificate_name",
                "certificateName",
                autoboto.TypeInfo(str),
            ),
            (
                "certificate_domain_name",
                "certificateDomainName",
                autoboto.TypeInfo(str),
            ),
            (
                "certificate_alternative_names",
                "certificateAlternativeNames",
                autoboto.TypeInfo(typing.List[str]),
            ),
        ]

    # The load balancer name where you want to create the SSL/TLS certificate.
    load_balancer_name: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The SSL/TLS certificate name.

    # You can have up to 10 certificates in your account at one time. Each
    # Lightsail load balancer can have up to 2 certificates associated with it at
    # one time. There is also an overall limit to the number of certificates that
    # can be issue in a 365-day period. For more information, see
    # [Limits](http://docs.aws.amazon.com/acm/latest/userguide/acm-limits.html).
    certificate_name: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The domain name (e.g., `example.com`) for your SSL/TLS certificate.
    certificate_domain_name: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # An array of strings listing alternative domains and subdomains for your
    # SSL/TLS certificate. Lightsail will de-dupe the names for you. You can have
    # a maximum of 9 alternative names (in addition to the 1 primary domain). We
    # do not support wildcards (e.g., `*.example.com`).
    certificate_alternative_names: typing.List[str] = dataclasses.field(
        default_factory=list,
    )


@dataclasses.dataclass
class CreateLoadBalancerTlsCertificateResult(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "operations",
                "operations",
                autoboto.TypeInfo(typing.List[Operation]),
            ),
        ]

    # An object containing information about the API operations.
    operations: typing.List["Operation"] = dataclasses.field(
        default_factory=list,
    )


@dataclasses.dataclass
class DeleteDiskRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "disk_name",
                "diskName",
                autoboto.TypeInfo(str),
            ),
        ]

    # The unique name of the disk you want to delete (e.g., `my-disk`).
    disk_name: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DeleteDiskResult(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "operations",
                "operations",
                autoboto.TypeInfo(typing.List[Operation]),
            ),
        ]

    # An object describing the API operations.
    operations: typing.List["Operation"] = dataclasses.field(
        default_factory=list,
    )


@dataclasses.dataclass
class DeleteDiskSnapshotRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "disk_snapshot_name",
                "diskSnapshotName",
                autoboto.TypeInfo(str),
            ),
        ]

    # The name of the disk snapshot you want to delete (e.g., `my-disk-
    # snapshot`).
    disk_snapshot_name: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class DeleteDiskSnapshotResult(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "operations",
                "operations",
                autoboto.TypeInfo(typing.List[Operation]),
            ),
        ]

    # An object describing the API operations.
    operations: typing.List["Operation"] = dataclasses.field(
        default_factory=list,
    )


@dataclasses.dataclass
class DeleteDomainEntryRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "domain_name",
                "domainName",
                autoboto.TypeInfo(str),
            ),
            (
                "domain_entry",
                "domainEntry",
                autoboto.TypeInfo(DomainEntry),
            ),
        ]

    # The name of the domain entry to delete.
    domain_name: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # An array of key-value pairs containing information about your domain
    # entries.
    domain_entry: "DomainEntry" = dataclasses.field(default_factory=dict, )


@dataclasses.dataclass
class DeleteDomainEntryResult(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "operation",
                "operation",
                autoboto.TypeInfo(Operation),
            ),
        ]

    # An array of key-value pairs containing information about the results of
    # your delete domain entry request.
    operation: "Operation" = dataclasses.field(default_factory=dict, )


@dataclasses.dataclass
class DeleteDomainRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "domain_name",
                "domainName",
                autoboto.TypeInfo(str),
            ),
        ]

    # The specific domain name to delete.
    domain_name: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DeleteDomainResult(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "operation",
                "operation",
                autoboto.TypeInfo(Operation),
            ),
        ]

    # An array of key-value pairs containing information about the results of
    # your delete domain request.
    operation: "Operation" = dataclasses.field(default_factory=dict, )


@dataclasses.dataclass
class DeleteInstanceRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "instance_name",
                "instanceName",
                autoboto.TypeInfo(str),
            ),
        ]

    # The name of the instance to delete.
    instance_name: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DeleteInstanceResult(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "operations",
                "operations",
                autoboto.TypeInfo(typing.List[Operation]),
            ),
        ]

    # An array of key-value pairs containing information about the results of
    # your delete instance request.
    operations: typing.List["Operation"] = dataclasses.field(
        default_factory=list,
    )


@dataclasses.dataclass
class DeleteInstanceSnapshotRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "instance_snapshot_name",
                "instanceSnapshotName",
                autoboto.TypeInfo(str),
            ),
        ]

    # The name of the snapshot to delete.
    instance_snapshot_name: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class DeleteInstanceSnapshotResult(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "operations",
                "operations",
                autoboto.TypeInfo(typing.List[Operation]),
            ),
        ]

    # An array of key-value pairs containing information about the results of
    # your delete instance snapshot request.
    operations: typing.List["Operation"] = dataclasses.field(
        default_factory=list,
    )


@dataclasses.dataclass
class DeleteKeyPairRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "key_pair_name",
                "keyPairName",
                autoboto.TypeInfo(str),
            ),
        ]

    # The name of the key pair to delete.
    key_pair_name: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DeleteKeyPairResult(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "operation",
                "operation",
                autoboto.TypeInfo(Operation),
            ),
        ]

    # An array of key-value pairs containing information about the results of
    # your delete key pair request.
    operation: "Operation" = dataclasses.field(default_factory=dict, )


@dataclasses.dataclass
class DeleteLoadBalancerRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "load_balancer_name",
                "loadBalancerName",
                autoboto.TypeInfo(str),
            ),
        ]

    # The name of the load balancer you want to delete.
    load_balancer_name: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class DeleteLoadBalancerResult(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "operations",
                "operations",
                autoboto.TypeInfo(typing.List[Operation]),
            ),
        ]

    # An object describing the API operations.
    operations: typing.List["Operation"] = dataclasses.field(
        default_factory=list,
    )


@dataclasses.dataclass
class DeleteLoadBalancerTlsCertificateRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "load_balancer_name",
                "loadBalancerName",
                autoboto.TypeInfo(str),
            ),
            (
                "certificate_name",
                "certificateName",
                autoboto.TypeInfo(str),
            ),
            (
                "force",
                "force",
                autoboto.TypeInfo(bool),
            ),
        ]

    # The load balancer name.
    load_balancer_name: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The SSL/TLS certificate name.
    certificate_name: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # When `true`, forces the deletion of an SSL/TLS certificate.

    # There can be two certificates associated with a Lightsail load balancer:
    # the primary and the backup. The force parameter is required when the
    # primary SSL/TLS certificate is in use by an instance attached to the load
    # balancer.
    force: bool = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DeleteLoadBalancerTlsCertificateResult(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "operations",
                "operations",
                autoboto.TypeInfo(typing.List[Operation]),
            ),
        ]

    # An object describing the API operations.
    operations: typing.List["Operation"] = dataclasses.field(
        default_factory=list,
    )


@dataclasses.dataclass
class DetachDiskRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "disk_name",
                "diskName",
                autoboto.TypeInfo(str),
            ),
        ]

    # The unique name of the disk you want to detach from your instance (e.g.,
    # `my-disk`).
    disk_name: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DetachDiskResult(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "operations",
                "operations",
                autoboto.TypeInfo(typing.List[Operation]),
            ),
        ]

    # An object describing the API operations.
    operations: typing.List["Operation"] = dataclasses.field(
        default_factory=list,
    )


@dataclasses.dataclass
class DetachInstancesFromLoadBalancerRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "load_balancer_name",
                "loadBalancerName",
                autoboto.TypeInfo(str),
            ),
            (
                "instance_names",
                "instanceNames",
                autoboto.TypeInfo(typing.List[str]),
            ),
        ]

    # The name of the Lightsail load balancer.
    load_balancer_name: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # An array of strings containing the names of the instances you want to
    # detach from the load balancer.
    instance_names: typing.List[str] = dataclasses.field(default_factory=list, )


@dataclasses.dataclass
class DetachInstancesFromLoadBalancerResult(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "operations",
                "operations",
                autoboto.TypeInfo(typing.List[Operation]),
            ),
        ]

    # An object describing the API operations.
    operations: typing.List["Operation"] = dataclasses.field(
        default_factory=list,
    )


@dataclasses.dataclass
class DetachStaticIpRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "static_ip_name",
                "staticIpName",
                autoboto.TypeInfo(str),
            ),
        ]

    # The name of the static IP to detach from the instance.
    static_ip_name: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class DetachStaticIpResult(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "operations",
                "operations",
                autoboto.TypeInfo(typing.List[Operation]),
            ),
        ]

    # An array of key-value pairs containing information about the results of
    # your detach static IP request.
    operations: typing.List["Operation"] = dataclasses.field(
        default_factory=list,
    )


@dataclasses.dataclass
class Disk(autoboto.ShapeBase):
    """
    Describes a system disk or an block storage disk.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "name",
                "name",
                autoboto.TypeInfo(str),
            ),
            (
                "arn",
                "arn",
                autoboto.TypeInfo(str),
            ),
            (
                "support_code",
                "supportCode",
                autoboto.TypeInfo(str),
            ),
            (
                "created_at",
                "createdAt",
                autoboto.TypeInfo(datetime.datetime),
            ),
            (
                "location",
                "location",
                autoboto.TypeInfo(ResourceLocation),
            ),
            (
                "resource_type",
                "resourceType",
                autoboto.TypeInfo(ResourceType),
            ),
            (
                "size_in_gb",
                "sizeInGb",
                autoboto.TypeInfo(int),
            ),
            (
                "is_system_disk",
                "isSystemDisk",
                autoboto.TypeInfo(bool),
            ),
            (
                "iops",
                "iops",
                autoboto.TypeInfo(int),
            ),
            (
                "path",
                "path",
                autoboto.TypeInfo(str),
            ),
            (
                "state",
                "state",
                autoboto.TypeInfo(DiskState),
            ),
            (
                "attached_to",
                "attachedTo",
                autoboto.TypeInfo(str),
            ),
            (
                "is_attached",
                "isAttached",
                autoboto.TypeInfo(bool),
            ),
            (
                "attachment_state",
                "attachmentState",
                autoboto.TypeInfo(str),
            ),
            (
                "gb_in_use",
                "gbInUse",
                autoboto.TypeInfo(int),
            ),
        ]

    # The unique name of the disk.
    name: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The Amazon Resource Name (ARN) of the disk.
    arn: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The support code. Include this code in your email to support when you have
    # questions about an instance or another resource in Lightsail. This code
    # enables our support team to look up your Lightsail information more easily.
    support_code: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The date when the disk was created.
    created_at: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The AWS Region and Availability Zone where the disk is located.
    location: "ResourceLocation" = dataclasses.field(default_factory=dict, )

    # The Lightsail resource type (e.g., `Disk`).
    resource_type: "ResourceType" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The size of the disk in GB.
    size_in_gb: int = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # A Boolean value indicating whether this disk is a system disk (has an
    # operating system loaded on it).
    is_system_disk: bool = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The input/output operations per second (IOPS) of the disk.
    iops: int = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The disk path.
    path: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # Describes the status of the disk.
    state: "DiskState" = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The resources to which the disk is attached.
    attached_to: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # A Boolean value indicating whether the disk is attached.
    is_attached: bool = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # (Deprecated) The attachment state of the disk.

    # In releases prior to November 14, 2017, this parameter returned `attached`
    # for system disks in the API response. It is now deprecated, but still
    # included in the response. Use `isAttached` instead.
    attachment_state: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # (Deprecated) The number of GB in use by the disk.

    # In releases prior to November 14, 2017, this parameter was not included in
    # the API response. It is now deprecated.
    gb_in_use: int = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DiskMap(autoboto.ShapeBase):
    """
    Describes a block storage disk mapping.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "original_disk_path",
                "originalDiskPath",
                autoboto.TypeInfo(str),
            ),
            (
                "new_disk_name",
                "newDiskName",
                autoboto.TypeInfo(str),
            ),
        ]

    # The original disk path exposed to the instance (for example, `/dev/sdh`).
    original_disk_path: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The new disk name (e.g., `my-new-disk`).
    new_disk_name: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class DiskSnapshot(autoboto.ShapeBase):
    """
    Describes a block storage disk snapshot.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "name",
                "name",
                autoboto.TypeInfo(str),
            ),
            (
                "arn",
                "arn",
                autoboto.TypeInfo(str),
            ),
            (
                "support_code",
                "supportCode",
                autoboto.TypeInfo(str),
            ),
            (
                "created_at",
                "createdAt",
                autoboto.TypeInfo(datetime.datetime),
            ),
            (
                "location",
                "location",
                autoboto.TypeInfo(ResourceLocation),
            ),
            (
                "resource_type",
                "resourceType",
                autoboto.TypeInfo(ResourceType),
            ),
            (
                "size_in_gb",
                "sizeInGb",
                autoboto.TypeInfo(int),
            ),
            (
                "state",
                "state",
                autoboto.TypeInfo(DiskSnapshotState),
            ),
            (
                "progress",
                "progress",
                autoboto.TypeInfo(str),
            ),
            (
                "from_disk_name",
                "fromDiskName",
                autoboto.TypeInfo(str),
            ),
            (
                "from_disk_arn",
                "fromDiskArn",
                autoboto.TypeInfo(str),
            ),
        ]

    # The name of the disk snapshot (e.g., `my-disk-snapshot`).
    name: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The Amazon Resource Name (ARN) of the disk snapshot.
    arn: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The support code. Include this code in your email to support when you have
    # questions about an instance or another resource in Lightsail. This code
    # enables our support team to look up your Lightsail information more easily.
    support_code: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The date when the disk snapshot was created.
    created_at: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The AWS Region and Availability Zone where the disk snapshot was created.
    location: "ResourceLocation" = dataclasses.field(default_factory=dict, )

    # The Lightsail resource type (e.g., `DiskSnapshot`).
    resource_type: "ResourceType" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The size of the disk in GB.
    size_in_gb: int = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The status of the disk snapshot operation.
    state: "DiskSnapshotState" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The progress of the disk snapshot operation.
    progress: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The unique name of the source disk from which you are creating the disk
    # snapshot.
    from_disk_name: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The Amazon Resource Name (ARN) of the source disk from which you are
    # creating the disk snapshot.
    from_disk_arn: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


class DiskSnapshotState(Enum):
    pending = "pending"
    completed = "completed"
    error = "error"
    unknown = "unknown"


class DiskState(Enum):
    pending = "pending"
    error = "error"
    available = "available"
    in_use = "in-use"
    unknown = "unknown"


@dataclasses.dataclass
class Domain(autoboto.ShapeBase):
    """
    Describes a domain where you are storing recordsets in Lightsail.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "name",
                "name",
                autoboto.TypeInfo(str),
            ),
            (
                "arn",
                "arn",
                autoboto.TypeInfo(str),
            ),
            (
                "support_code",
                "supportCode",
                autoboto.TypeInfo(str),
            ),
            (
                "created_at",
                "createdAt",
                autoboto.TypeInfo(datetime.datetime),
            ),
            (
                "location",
                "location",
                autoboto.TypeInfo(ResourceLocation),
            ),
            (
                "resource_type",
                "resourceType",
                autoboto.TypeInfo(ResourceType),
            ),
            (
                "domain_entries",
                "domainEntries",
                autoboto.TypeInfo(typing.List[DomainEntry]),
            ),
        ]

    # The name of the domain.
    name: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The Amazon Resource Name (ARN) of the domain recordset (e.g.,
    # `arn:aws:lightsail:global:123456789101:Domain/824cede0-abc7-4f84-8dbc-12345EXAMPLE`).
    arn: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The support code. Include this code in your email to support when you have
    # questions about an instance or another resource in Lightsail. This code
    # enables our support team to look up your Lightsail information more easily.
    support_code: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The date when the domain recordset was created.
    created_at: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The AWS Region and Availability Zones where the domain recordset was
    # created.
    location: "ResourceLocation" = dataclasses.field(default_factory=dict, )

    # The resource type.
    resource_type: "ResourceType" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # An array of key-value pairs containing information about the domain
    # entries.
    domain_entries: typing.List["DomainEntry"] = dataclasses.field(
        default_factory=list,
    )


@dataclasses.dataclass
class DomainEntry(autoboto.ShapeBase):
    """
    Describes a domain recordset entry.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "id",
                "id",
                autoboto.TypeInfo(str),
            ),
            (
                "name",
                "name",
                autoboto.TypeInfo(str),
            ),
            (
                "target",
                "target",
                autoboto.TypeInfo(str),
            ),
            (
                "is_alias",
                "isAlias",
                autoboto.TypeInfo(bool),
            ),
            (
                "type",
                "type",
                autoboto.TypeInfo(str),
            ),
            (
                "options",
                "options",
                autoboto.TypeInfo(typing.Dict[str, str]),
            ),
        ]

    # The ID of the domain recordset entry.
    id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The name of the domain.
    name: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The target AWS name server (e.g., `ns-111.awsdns-22.com.`).

    # For Lightsail load balancers, the value looks like
    # `ab1234c56789c6b86aba6fb203d443bc-123456789.us-east-2.elb.amazonaws.com`.
    # Be sure to also set `isAlias` to `true` when setting up an A record for a
    # load balancer.
    target: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # When `true`, specifies whether the domain entry is an alias used by the
    # Lightsail load balancer. You can include an alias (A type) record in your
    # request, which points to a load balancer DNS name and routes traffic to
    # your load balancer
    is_alias: bool = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The type of domain entry (e.g., `SOA` or `NS`).
    type: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # (Deprecated) The options for the domain entry.

    # In releases prior to November 29, 2017, this parameter was not included in
    # the API response. It is now deprecated.
    options: typing.Dict[str, str] = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class DownloadDefaultKeyPairRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class DownloadDefaultKeyPairResult(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "public_key_base64",
                "publicKeyBase64",
                autoboto.TypeInfo(str),
            ),
            (
                "private_key_base64",
                "privateKeyBase64",
                autoboto.TypeInfo(str),
            ),
        ]

    # A base64-encoded public key of the `ssh-rsa` type.
    public_key_base64: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # A base64-encoded RSA private key.
    private_key_base64: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class GetActiveNamesRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "page_token",
                "pageToken",
                autoboto.TypeInfo(str),
            ),
        ]

    # A token used for paginating results from your get active names request.
    page_token: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetActiveNamesResult(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "active_names",
                "activeNames",
                autoboto.TypeInfo(typing.List[str]),
            ),
            (
                "next_page_token",
                "nextPageToken",
                autoboto.TypeInfo(str),
            ),
        ]

    # The list of active names returned by the get active names request.
    active_names: typing.List[str] = dataclasses.field(default_factory=list, )

    # A token used for advancing to the next page of results from your get active
    # names request.
    next_page_token: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class GetBlueprintsRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "include_inactive",
                "includeInactive",
                autoboto.TypeInfo(bool),
            ),
            (
                "page_token",
                "pageToken",
                autoboto.TypeInfo(str),
            ),
        ]

    # A Boolean value indicating whether to include inactive results in your
    # request.
    include_inactive: bool = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # A token used for advancing to the next page of results from your get
    # blueprints request.
    page_token: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetBlueprintsResult(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "blueprints",
                "blueprints",
                autoboto.TypeInfo(typing.List[Blueprint]),
            ),
            (
                "next_page_token",
                "nextPageToken",
                autoboto.TypeInfo(str),
            ),
        ]

    # An array of key-value pairs that contains information about the available
    # blueprints.
    blueprints: typing.List["Blueprint"] = dataclasses.field(
        default_factory=list,
    )

    # A token used for advancing to the next page of results from your get
    # blueprints request.
    next_page_token: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class GetBundlesRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "include_inactive",
                "includeInactive",
                autoboto.TypeInfo(bool),
            ),
            (
                "page_token",
                "pageToken",
                autoboto.TypeInfo(str),
            ),
        ]

    # A Boolean value that indicates whether to include inactive bundle results
    # in your request.
    include_inactive: bool = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # A token used for advancing to the next page of results from your get
    # bundles request.
    page_token: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetBundlesResult(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "bundles",
                "bundles",
                autoboto.TypeInfo(typing.List[Bundle]),
            ),
            (
                "next_page_token",
                "nextPageToken",
                autoboto.TypeInfo(str),
            ),
        ]

    # An array of key-value pairs that contains information about the available
    # bundles.
    bundles: typing.List["Bundle"] = dataclasses.field(default_factory=list, )

    # A token used for advancing to the next page of results from your get active
    # names request.
    next_page_token: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class GetDiskRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "disk_name",
                "diskName",
                autoboto.TypeInfo(str),
            ),
        ]

    # The name of the disk (e.g., `my-disk`).
    disk_name: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetDiskResult(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "disk",
                "disk",
                autoboto.TypeInfo(Disk),
            ),
        ]

    # An object containing information about the disk.
    disk: "Disk" = dataclasses.field(default_factory=dict, )


@dataclasses.dataclass
class GetDiskSnapshotRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "disk_snapshot_name",
                "diskSnapshotName",
                autoboto.TypeInfo(str),
            ),
        ]

    # The name of the disk snapshot (e.g., `my-disk-snapshot`).
    disk_snapshot_name: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class GetDiskSnapshotResult(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "disk_snapshot",
                "diskSnapshot",
                autoboto.TypeInfo(DiskSnapshot),
            ),
        ]

    # An object containing information about the disk snapshot.
    disk_snapshot: "DiskSnapshot" = dataclasses.field(default_factory=dict, )


@dataclasses.dataclass
class GetDiskSnapshotsRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "page_token",
                "pageToken",
                autoboto.TypeInfo(str),
            ),
        ]

    # A token used for advancing to the next page of results from your
    # GetDiskSnapshots request.
    page_token: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetDiskSnapshotsResult(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "disk_snapshots",
                "diskSnapshots",
                autoboto.TypeInfo(typing.List[DiskSnapshot]),
            ),
            (
                "next_page_token",
                "nextPageToken",
                autoboto.TypeInfo(str),
            ),
        ]

    # An array of objects containing information about all block storage disk
    # snapshots.
    disk_snapshots: typing.List["DiskSnapshot"] = dataclasses.field(
        default_factory=list,
    )

    # A token used for advancing to the next page of results from your
    # GetDiskSnapshots request.
    next_page_token: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class GetDisksRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "page_token",
                "pageToken",
                autoboto.TypeInfo(str),
            ),
        ]

    # A token used for advancing to the next page of results from your GetDisks
    # request.
    page_token: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetDisksResult(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "disks",
                "disks",
                autoboto.TypeInfo(typing.List[Disk]),
            ),
            (
                "next_page_token",
                "nextPageToken",
                autoboto.TypeInfo(str),
            ),
        ]

    # An array of objects containing information about all block storage disks.
    disks: typing.List["Disk"] = dataclasses.field(default_factory=list, )

    # A token used for advancing to the next page of results from your GetDisks
    # request.
    next_page_token: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class GetDomainRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "domain_name",
                "domainName",
                autoboto.TypeInfo(str),
            ),
        ]

    # The domain name for which your want to return information about.
    domain_name: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetDomainResult(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "domain",
                "domain",
                autoboto.TypeInfo(Domain),
            ),
        ]

    # An array of key-value pairs containing information about your get domain
    # request.
    domain: "Domain" = dataclasses.field(default_factory=dict, )


@dataclasses.dataclass
class GetDomainsRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "page_token",
                "pageToken",
                autoboto.TypeInfo(str),
            ),
        ]

    # A token used for advancing to the next page of results from your get
    # domains request.
    page_token: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetDomainsResult(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "domains",
                "domains",
                autoboto.TypeInfo(typing.List[Domain]),
            ),
            (
                "next_page_token",
                "nextPageToken",
                autoboto.TypeInfo(str),
            ),
        ]

    # An array of key-value pairs containing information about each of the domain
    # entries in the user's account.
    domains: typing.List["Domain"] = dataclasses.field(default_factory=list, )

    # A token used for advancing to the next page of results from your get active
    # names request.
    next_page_token: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class GetInstanceAccessDetailsRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "instance_name",
                "instanceName",
                autoboto.TypeInfo(str),
            ),
            (
                "protocol",
                "protocol",
                autoboto.TypeInfo(InstanceAccessProtocol),
            ),
        ]

    # The name of the instance to access.
    instance_name: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The protocol to use to connect to your instance. Defaults to `ssh`.
    protocol: "InstanceAccessProtocol" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class GetInstanceAccessDetailsResult(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "access_details",
                "accessDetails",
                autoboto.TypeInfo(InstanceAccessDetails),
            ),
        ]

    # An array of key-value pairs containing information about a get instance
    # access request.
    access_details: "InstanceAccessDetails" = dataclasses.field(
        default_factory=dict,
    )


@dataclasses.dataclass
class GetInstanceMetricDataRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "instance_name",
                "instanceName",
                autoboto.TypeInfo(str),
            ),
            (
                "metric_name",
                "metricName",
                autoboto.TypeInfo(InstanceMetricName),
            ),
            (
                "period",
                "period",
                autoboto.TypeInfo(int),
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
                "unit",
                "unit",
                autoboto.TypeInfo(MetricUnit),
            ),
            (
                "statistics",
                "statistics",
                autoboto.TypeInfo(typing.List[MetricStatistic]),
            ),
        ]

    # The name of the instance for which you want to get metrics data.
    instance_name: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The metric name to get data about.
    metric_name: "InstanceMetricName" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The time period for which you are requesting data.
    period: int = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The start time of the time period.
    start_time: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The end time of the time period.
    end_time: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The unit. The list of valid values is below.
    unit: "MetricUnit" = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The instance statistics.
    statistics: typing.List["MetricStatistic"] = dataclasses.field(
        default_factory=list,
    )


@dataclasses.dataclass
class GetInstanceMetricDataResult(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "metric_name",
                "metricName",
                autoboto.TypeInfo(InstanceMetricName),
            ),
            (
                "metric_data",
                "metricData",
                autoboto.TypeInfo(typing.List[MetricDatapoint]),
            ),
        ]

    # The metric name to return data for.
    metric_name: "InstanceMetricName" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # An array of key-value pairs containing information about the results of
    # your get instance metric data request.
    metric_data: typing.List["MetricDatapoint"] = dataclasses.field(
        default_factory=list,
    )


@dataclasses.dataclass
class GetInstancePortStatesRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "instance_name",
                "instanceName",
                autoboto.TypeInfo(str),
            ),
        ]

    # The name of the instance.
    instance_name: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetInstancePortStatesResult(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "port_states",
                "portStates",
                autoboto.TypeInfo(typing.List[InstancePortState]),
            ),
        ]

    # Information about the port states resulting from your request.
    port_states: typing.List["InstancePortState"] = dataclasses.field(
        default_factory=list,
    )


@dataclasses.dataclass
class GetInstanceRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "instance_name",
                "instanceName",
                autoboto.TypeInfo(str),
            ),
        ]

    # The name of the instance.
    instance_name: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetInstanceResult(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "instance",
                "instance",
                autoboto.TypeInfo(Instance),
            ),
        ]

    # An array of key-value pairs containing information about the specified
    # instance.
    instance: "Instance" = dataclasses.field(default_factory=dict, )


@dataclasses.dataclass
class GetInstanceSnapshotRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "instance_snapshot_name",
                "instanceSnapshotName",
                autoboto.TypeInfo(str),
            ),
        ]

    # The name of the snapshot for which you are requesting information.
    instance_snapshot_name: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class GetInstanceSnapshotResult(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "instance_snapshot",
                "instanceSnapshot",
                autoboto.TypeInfo(InstanceSnapshot),
            ),
        ]

    # An array of key-value pairs containing information about the results of
    # your get instance snapshot request.
    instance_snapshot: "InstanceSnapshot" = dataclasses.field(
        default_factory=dict,
    )


@dataclasses.dataclass
class GetInstanceSnapshotsRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "page_token",
                "pageToken",
                autoboto.TypeInfo(str),
            ),
        ]

    # A token used for advancing to the next page of results from your get
    # instance snapshots request.
    page_token: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetInstanceSnapshotsResult(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "instance_snapshots",
                "instanceSnapshots",
                autoboto.TypeInfo(typing.List[InstanceSnapshot]),
            ),
            (
                "next_page_token",
                "nextPageToken",
                autoboto.TypeInfo(str),
            ),
        ]

    # An array of key-value pairs containing information about the results of
    # your get instance snapshots request.
    instance_snapshots: typing.List["InstanceSnapshot"] = dataclasses.field(
        default_factory=list,
    )

    # A token used for advancing to the next page of results from your get
    # instance snapshots request.
    next_page_token: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class GetInstanceStateRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "instance_name",
                "instanceName",
                autoboto.TypeInfo(str),
            ),
        ]

    # The name of the instance to get state information about.
    instance_name: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetInstanceStateResult(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "state",
                "state",
                autoboto.TypeInfo(InstanceState),
            ),
        ]

    # The state of the instance.
    state: "InstanceState" = dataclasses.field(default_factory=dict, )


@dataclasses.dataclass
class GetInstancesRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "page_token",
                "pageToken",
                autoboto.TypeInfo(str),
            ),
        ]

    # A token used for advancing to the next page of results from your get
    # instances request.
    page_token: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetInstancesResult(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "instances",
                "instances",
                autoboto.TypeInfo(typing.List[Instance]),
            ),
            (
                "next_page_token",
                "nextPageToken",
                autoboto.TypeInfo(str),
            ),
        ]

    # An array of key-value pairs containing information about your instances.
    instances: typing.List["Instance"] = dataclasses.field(
        default_factory=list,
    )

    # A token used for advancing to the next page of results from your get
    # instances request.
    next_page_token: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class GetKeyPairRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "key_pair_name",
                "keyPairName",
                autoboto.TypeInfo(str),
            ),
        ]

    # The name of the key pair for which you are requesting information.
    key_pair_name: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetKeyPairResult(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "key_pair",
                "keyPair",
                autoboto.TypeInfo(KeyPair),
            ),
        ]

    # An array of key-value pairs containing information about the key pair.
    key_pair: "KeyPair" = dataclasses.field(default_factory=dict, )


@dataclasses.dataclass
class GetKeyPairsRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "page_token",
                "pageToken",
                autoboto.TypeInfo(str),
            ),
        ]

    # A token used for advancing to the next page of results from your get key
    # pairs request.
    page_token: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetKeyPairsResult(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "key_pairs",
                "keyPairs",
                autoboto.TypeInfo(typing.List[KeyPair]),
            ),
            (
                "next_page_token",
                "nextPageToken",
                autoboto.TypeInfo(str),
            ),
        ]

    # An array of key-value pairs containing information about the key pairs.
    key_pairs: typing.List["KeyPair"] = dataclasses.field(
        default_factory=list,
    )

    # A token used for advancing to the next page of results from your get key
    # pairs request.
    next_page_token: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class GetLoadBalancerMetricDataRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "load_balancer_name",
                "loadBalancerName",
                autoboto.TypeInfo(str),
            ),
            (
                "metric_name",
                "metricName",
                autoboto.TypeInfo(LoadBalancerMetricName),
            ),
            (
                "period",
                "period",
                autoboto.TypeInfo(int),
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
                "unit",
                "unit",
                autoboto.TypeInfo(MetricUnit),
            ),
            (
                "statistics",
                "statistics",
                autoboto.TypeInfo(typing.List[MetricStatistic]),
            ),
        ]

    # The name of the load balancer.
    load_balancer_name: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The metric about which you want to return information. Valid values are
    # listed below, along with the most useful `statistics` to include in your
    # request.

    #   * **`ClientTLSNegotiationErrorCount` ** \- The number of TLS connections initiated by the client that did not establish a session with the load balancer. Possible causes include a mismatch of ciphers or protocols.

    # `Statistics`: The most useful statistic is `Sum`.

    #   * **`HealthyHostCount` ** \- The number of target instances that are considered healthy.

    # `Statistics`: The most useful statistic are `Average`, `Minimum`, and
    # `Maximum`.

    #   * **`UnhealthyHostCount` ** \- The number of target instances that are considered unhealthy.

    # `Statistics`: The most useful statistic are `Average`, `Minimum`, and
    # `Maximum`.

    #   * **`HTTPCode_LB_4XX_Count` ** \- The number of HTTP 4XX client error codes that originate from the load balancer. Client errors are generated when requests are malformed or incomplete. These requests have not been received by the target instance. This count does not include any response codes generated by the target instances.

    # `Statistics`: The most useful statistic is `Sum`. Note that `Minimum`,
    # `Maximum`, and `Average` all return `1`.

    #   * **`HTTPCode_LB_5XX_Count` ** \- The number of HTTP 5XX server error codes that originate from the load balancer. This count does not include any response codes generated by the target instances.

    # `Statistics`: The most useful statistic is `Sum`. Note that `Minimum`,
    # `Maximum`, and `Average` all return `1`. Note that `Minimum`, `Maximum`,
    # and `Average` all return `1`.

    #   * **`HTTPCode_Instance_2XX_Count` ** \- The number of HTTP response codes generated by the target instances. This does not include any response codes generated by the load balancer.

    # `Statistics`: The most useful statistic is `Sum`. Note that `Minimum`,
    # `Maximum`, and `Average` all return `1`.

    #   * **`HTTPCode_Instance_3XX_Count` ** \- The number of HTTP response codes generated by the target instances. This does not include any response codes generated by the load balancer.

    # `Statistics`: The most useful statistic is `Sum`. Note that `Minimum`,
    # `Maximum`, and `Average` all return `1`.

    #   * **`HTTPCode_Instance_4XX_Count` ** \- The number of HTTP response codes generated by the target instances. This does not include any response codes generated by the load balancer.

    # `Statistics`: The most useful statistic is `Sum`. Note that `Minimum`,
    # `Maximum`, and `Average` all return `1`.

    #   * **`HTTPCode_Instance_5XX_Count` ** \- The number of HTTP response codes generated by the target instances. This does not include any response codes generated by the load balancer.

    # `Statistics`: The most useful statistic is `Sum`. Note that `Minimum`,
    # `Maximum`, and `Average` all return `1`.

    #   * **`InstanceResponseTime` ** \- The time elapsed, in seconds, after the request leaves the load balancer until a response from the target instance is received.

    # `Statistics`: The most useful statistic is `Average`.

    #   * **`RejectedConnectionCount` ** \- The number of connections that were rejected because the load balancer had reached its maximum number of connections.

    # `Statistics`: The most useful statistic is `Sum`.

    #   * **`RequestCount` ** \- The number of requests processed over IPv4. This count includes only the requests with a response generated by a target instance of the load balancer.

    # `Statistics`: The most useful statistic is `Sum`. Note that `Minimum`,
    # `Maximum`, and `Average` all return `1`.
    metric_name: "LoadBalancerMetricName" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The time period duration for your health data request.
    period: int = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The start time of the period.
    start_time: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The end time of the period.
    end_time: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The unit for the time period request. Valid values are listed below.
    unit: "MetricUnit" = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # An array of statistics that you want to request metrics for. Valid values
    # are listed below.

    #   * **`SampleCount` ** \- The count (number) of data points used for the statistical calculation.

    #   * **`Average` ** \- The value of Sum / SampleCount during the specified period. By comparing this statistic with the Minimum and Maximum, you can determine the full scope of a metric and how close the average use is to the Minimum and Maximum. This comparison helps you to know when to increase or decrease your resources as needed.

    #   * **`Sum` ** \- All values submitted for the matching metric added together. This statistic can be useful for determining the total volume of a metric.

    #   * **`Minimum` ** \- The lowest value observed during the specified period. You can use this value to determine low volumes of activity for your application.

    #   * **`Maximum` ** \- The highest value observed during the specified period. You can use this value to determine high volumes of activity for your application.
    statistics: typing.List["MetricStatistic"] = dataclasses.field(
        default_factory=list,
    )


@dataclasses.dataclass
class GetLoadBalancerMetricDataResult(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "metric_name",
                "metricName",
                autoboto.TypeInfo(LoadBalancerMetricName),
            ),
            (
                "metric_data",
                "metricData",
                autoboto.TypeInfo(typing.List[MetricDatapoint]),
            ),
        ]

    # The metric about which you are receiving information. Valid values are
    # listed below, along with the most useful `statistics` to include in your
    # request.

    #   * **`ClientTLSNegotiationErrorCount` ** \- The number of TLS connections initiated by the client that did not establish a session with the load balancer. Possible causes include a mismatch of ciphers or protocols.

    # `Statistics`: The most useful statistic is `Sum`.

    #   * **`HealthyHostCount` ** \- The number of target instances that are considered healthy.

    # `Statistics`: The most useful statistic are `Average`, `Minimum`, and
    # `Maximum`.

    #   * **`UnhealthyHostCount` ** \- The number of target instances that are considered unhealthy.

    # `Statistics`: The most useful statistic are `Average`, `Minimum`, and
    # `Maximum`.

    #   * **`HTTPCode_LB_4XX_Count` ** \- The number of HTTP 4XX client error codes that originate from the load balancer. Client errors are generated when requests are malformed or incomplete. These requests have not been received by the target instance. This count does not include any response codes generated by the target instances.

    # `Statistics`: The most useful statistic is `Sum`. Note that `Minimum`,
    # `Maximum`, and `Average` all return `1`.

    #   * **`HTTPCode_LB_5XX_Count` ** \- The number of HTTP 5XX server error codes that originate from the load balancer. This count does not include any response codes generated by the target instances.

    # `Statistics`: The most useful statistic is `Sum`. Note that `Minimum`,
    # `Maximum`, and `Average` all return `1`. Note that `Minimum`, `Maximum`,
    # and `Average` all return `1`.

    #   * **`HTTPCode_Instance_2XX_Count` ** \- The number of HTTP response codes generated by the target instances. This does not include any response codes generated by the load balancer.

    # `Statistics`: The most useful statistic is `Sum`. Note that `Minimum`,
    # `Maximum`, and `Average` all return `1`.

    #   * **`HTTPCode_Instance_3XX_Count` ** \- The number of HTTP response codes generated by the target instances. This does not include any response codes generated by the load balancer.

    # `Statistics`: The most useful statistic is `Sum`. Note that `Minimum`,
    # `Maximum`, and `Average` all return `1`.

    #   * **`HTTPCode_Instance_4XX_Count` ** \- The number of HTTP response codes generated by the target instances. This does not include any response codes generated by the load balancer.

    # `Statistics`: The most useful statistic is `Sum`. Note that `Minimum`,
    # `Maximum`, and `Average` all return `1`.

    #   * **`HTTPCode_Instance_5XX_Count` ** \- The number of HTTP response codes generated by the target instances. This does not include any response codes generated by the load balancer.

    # `Statistics`: The most useful statistic is `Sum`. Note that `Minimum`,
    # `Maximum`, and `Average` all return `1`.

    #   * **`InstanceResponseTime` ** \- The time elapsed, in seconds, after the request leaves the load balancer until a response from the target instance is received.

    # `Statistics`: The most useful statistic is `Average`.

    #   * **`RejectedConnectionCount` ** \- The number of connections that were rejected because the load balancer had reached its maximum number of connections.

    # `Statistics`: The most useful statistic is `Sum`.

    #   * **`RequestCount` ** \- The number of requests processed over IPv4. This count includes only the requests with a response generated by a target instance of the load balancer.

    # `Statistics`: The most useful statistic is `Sum`. Note that `Minimum`,
    # `Maximum`, and `Average` all return `1`.
    metric_name: "LoadBalancerMetricName" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # An array of metric datapoint objects.
    metric_data: typing.List["MetricDatapoint"] = dataclasses.field(
        default_factory=list,
    )


@dataclasses.dataclass
class GetLoadBalancerRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "load_balancer_name",
                "loadBalancerName",
                autoboto.TypeInfo(str),
            ),
        ]

    # The name of the load balancer.
    load_balancer_name: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class GetLoadBalancerResult(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "load_balancer",
                "loadBalancer",
                autoboto.TypeInfo(LoadBalancer),
            ),
        ]

    # An object containing information about your load balancer.
    load_balancer: "LoadBalancer" = dataclasses.field(default_factory=dict, )


@dataclasses.dataclass
class GetLoadBalancerTlsCertificatesRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "load_balancer_name",
                "loadBalancerName",
                autoboto.TypeInfo(str),
            ),
        ]

    # The name of the load balancer you associated with your SSL/TLS certificate.
    load_balancer_name: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class GetLoadBalancerTlsCertificatesResult(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "tls_certificates",
                "tlsCertificates",
                autoboto.TypeInfo(typing.List[LoadBalancerTlsCertificate]),
            ),
        ]

    # An array of LoadBalancerTlsCertificate objects describing your SSL/TLS
    # certificates.
    tls_certificates: typing.List["LoadBalancerTlsCertificate"
                                 ] = dataclasses.field(
                                     default_factory=list,
                                 )


@dataclasses.dataclass
class GetLoadBalancersRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "page_token",
                "pageToken",
                autoboto.TypeInfo(str),
            ),
        ]

    # A token used for paginating the results from your GetLoadBalancers request.
    page_token: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetLoadBalancersResult(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "load_balancers",
                "loadBalancers",
                autoboto.TypeInfo(typing.List[LoadBalancer]),
            ),
            (
                "next_page_token",
                "nextPageToken",
                autoboto.TypeInfo(str),
            ),
        ]

    # An array of LoadBalancer objects describing your load balancers.
    load_balancers: typing.List["LoadBalancer"] = dataclasses.field(
        default_factory=list,
    )

    # A token used for advancing to the next page of results from your
    # GetLoadBalancers request.
    next_page_token: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class GetOperationRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "operation_id",
                "operationId",
                autoboto.TypeInfo(str),
            ),
        ]

    # A GUID used to identify the operation.
    operation_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetOperationResult(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "operation",
                "operation",
                autoboto.TypeInfo(Operation),
            ),
        ]

    # An array of key-value pairs containing information about the results of
    # your get operation request.
    operation: "Operation" = dataclasses.field(default_factory=dict, )


@dataclasses.dataclass
class GetOperationsForResourceRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "resource_name",
                "resourceName",
                autoboto.TypeInfo(str),
            ),
            (
                "page_token",
                "pageToken",
                autoboto.TypeInfo(str),
            ),
        ]

    # The name of the resource for which you are requesting information.
    resource_name: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # A token used for advancing to the next page of results from your get
    # operations for resource request.
    page_token: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetOperationsForResourceResult(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "operations",
                "operations",
                autoboto.TypeInfo(typing.List[Operation]),
            ),
            (
                "next_page_count",
                "nextPageCount",
                autoboto.TypeInfo(str),
            ),
            (
                "next_page_token",
                "nextPageToken",
                autoboto.TypeInfo(str),
            ),
        ]

    # An array of key-value pairs containing information about the results of
    # your get operations for resource request.
    operations: typing.List["Operation"] = dataclasses.field(
        default_factory=list,
    )

    # (Deprecated) Returns the number of pages of results that remain.

    # In releases prior to June 12, 2017, this parameter returned `null` by the
    # API. It is now deprecated, and the API returns the `nextPageToken`
    # parameter instead.
    next_page_count: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # An identifier that was returned from the previous call to this operation,
    # which can be used to return the next set of items in the list.
    next_page_token: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class GetOperationsRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "page_token",
                "pageToken",
                autoboto.TypeInfo(str),
            ),
        ]

    # A token used for advancing to the next page of results from your get
    # operations request.
    page_token: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetOperationsResult(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "operations",
                "operations",
                autoboto.TypeInfo(typing.List[Operation]),
            ),
            (
                "next_page_token",
                "nextPageToken",
                autoboto.TypeInfo(str),
            ),
        ]

    # An array of key-value pairs containing information about the results of
    # your get operations request.
    operations: typing.List["Operation"] = dataclasses.field(
        default_factory=list,
    )

    # A token used for advancing to the next page of results from your get
    # operations request.
    next_page_token: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class GetRegionsRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "include_availability_zones",
                "includeAvailabilityZones",
                autoboto.TypeInfo(bool),
            ),
        ]

    # A Boolean value indicating whether to also include Availability Zones in
    # your get regions request. Availability Zones are indicated with a letter:
    # e.g., `us-east-2a`.
    include_availability_zones: bool = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class GetRegionsResult(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "regions",
                "regions",
                autoboto.TypeInfo(typing.List[Region]),
            ),
        ]

    # An array of key-value pairs containing information about your get regions
    # request.
    regions: typing.List["Region"] = dataclasses.field(default_factory=list, )


@dataclasses.dataclass
class GetStaticIpRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "static_ip_name",
                "staticIpName",
                autoboto.TypeInfo(str),
            ),
        ]

    # The name of the static IP in Lightsail.
    static_ip_name: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class GetStaticIpResult(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "static_ip",
                "staticIp",
                autoboto.TypeInfo(StaticIp),
            ),
        ]

    # An array of key-value pairs containing information about the requested
    # static IP.
    static_ip: "StaticIp" = dataclasses.field(default_factory=dict, )


@dataclasses.dataclass
class GetStaticIpsRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "page_token",
                "pageToken",
                autoboto.TypeInfo(str),
            ),
        ]

    # A token used for advancing to the next page of results from your get static
    # IPs request.
    page_token: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class GetStaticIpsResult(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "static_ips",
                "staticIps",
                autoboto.TypeInfo(typing.List[StaticIp]),
            ),
            (
                "next_page_token",
                "nextPageToken",
                autoboto.TypeInfo(str),
            ),
        ]

    # An array of key-value pairs containing information about your get static
    # IPs request.
    static_ips: typing.List["StaticIp"] = dataclasses.field(
        default_factory=list,
    )

    # A token used for advancing to the next page of results from your get static
    # IPs request.
    next_page_token: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class ImportKeyPairRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "key_pair_name",
                "keyPairName",
                autoboto.TypeInfo(str),
            ),
            (
                "public_key_base64",
                "publicKeyBase64",
                autoboto.TypeInfo(str),
            ),
        ]

    # The name of the key pair for which you want to import the public key.
    key_pair_name: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # A base64-encoded public key of the `ssh-rsa` type.
    public_key_base64: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class ImportKeyPairResult(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "operation",
                "operation",
                autoboto.TypeInfo(Operation),
            ),
        ]

    # An array of key-value pairs containing information about the request
    # operation.
    operation: "Operation" = dataclasses.field(default_factory=dict, )


@dataclasses.dataclass
class Instance(autoboto.ShapeBase):
    """
    Describes an instance (a virtual private server).
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "name",
                "name",
                autoboto.TypeInfo(str),
            ),
            (
                "arn",
                "arn",
                autoboto.TypeInfo(str),
            ),
            (
                "support_code",
                "supportCode",
                autoboto.TypeInfo(str),
            ),
            (
                "created_at",
                "createdAt",
                autoboto.TypeInfo(datetime.datetime),
            ),
            (
                "location",
                "location",
                autoboto.TypeInfo(ResourceLocation),
            ),
            (
                "resource_type",
                "resourceType",
                autoboto.TypeInfo(ResourceType),
            ),
            (
                "blueprint_id",
                "blueprintId",
                autoboto.TypeInfo(str),
            ),
            (
                "blueprint_name",
                "blueprintName",
                autoboto.TypeInfo(str),
            ),
            (
                "bundle_id",
                "bundleId",
                autoboto.TypeInfo(str),
            ),
            (
                "is_static_ip",
                "isStaticIp",
                autoboto.TypeInfo(bool),
            ),
            (
                "private_ip_address",
                "privateIpAddress",
                autoboto.TypeInfo(str),
            ),
            (
                "public_ip_address",
                "publicIpAddress",
                autoboto.TypeInfo(str),
            ),
            (
                "ipv6_address",
                "ipv6Address",
                autoboto.TypeInfo(str),
            ),
            (
                "hardware",
                "hardware",
                autoboto.TypeInfo(InstanceHardware),
            ),
            (
                "networking",
                "networking",
                autoboto.TypeInfo(InstanceNetworking),
            ),
            (
                "state",
                "state",
                autoboto.TypeInfo(InstanceState),
            ),
            (
                "username",
                "username",
                autoboto.TypeInfo(str),
            ),
            (
                "ssh_key_name",
                "sshKeyName",
                autoboto.TypeInfo(str),
            ),
        ]

    # The name the user gave the instance (e.g., `Amazon_Linux-1GB-Ohio-1`).
    name: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The Amazon Resource Name (ARN) of the instance (e.g.,
    # `arn:aws:lightsail:us-
    # east-2:123456789101:Instance/244ad76f-8aad-4741-809f-12345EXAMPLE`).
    arn: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The support code. Include this code in your email to support when you have
    # questions about an instance or another resource in Lightsail. This code
    # enables our support team to look up your Lightsail information more easily.
    support_code: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The timestamp when the instance was created (e.g., `1479734909.17`).
    created_at: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The region name and availability zone where the instance is located.
    location: "ResourceLocation" = dataclasses.field(default_factory=dict, )

    # The type of resource (usually `Instance`).
    resource_type: "ResourceType" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The blueprint ID (e.g., `os_amlinux_2016_03`).
    blueprint_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The friendly name of the blueprint (e.g., `Amazon Linux`).
    blueprint_name: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The bundle for the instance (e.g., `micro_1_0`).
    bundle_id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # A Boolean value indicating whether this instance has a static IP assigned
    # to it.
    is_static_ip: bool = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The private IP address of the instance.
    private_ip_address: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The public IP address of the instance.
    public_ip_address: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The IPv6 address of the instance.
    ipv6_address: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The size of the vCPU and the amount of RAM for the instance.
    hardware: "InstanceHardware" = dataclasses.field(default_factory=dict, )

    # Information about the public ports and monthly data transfer rates for the
    # instance.
    networking: "InstanceNetworking" = dataclasses.field(default_factory=dict, )

    # The status code and the state (e.g., `running`) for the instance.
    state: "InstanceState" = dataclasses.field(default_factory=dict, )

    # The user name for connecting to the instance (e.g., `ec2-user`).
    username: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The name of the SSH key being used to connect to the instance (e.g.,
    # `LightsailDefaultKeyPair`).
    ssh_key_name: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class InstanceAccessDetails(autoboto.ShapeBase):
    """
    The parameters for gaining temporary access to one of your Amazon Lightsail
    instances.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "cert_key",
                "certKey",
                autoboto.TypeInfo(str),
            ),
            (
                "expires_at",
                "expiresAt",
                autoboto.TypeInfo(datetime.datetime),
            ),
            (
                "ip_address",
                "ipAddress",
                autoboto.TypeInfo(str),
            ),
            (
                "password",
                "password",
                autoboto.TypeInfo(str),
            ),
            (
                "password_data",
                "passwordData",
                autoboto.TypeInfo(PasswordData),
            ),
            (
                "private_key",
                "privateKey",
                autoboto.TypeInfo(str),
            ),
            (
                "protocol",
                "protocol",
                autoboto.TypeInfo(InstanceAccessProtocol),
            ),
            (
                "instance_name",
                "instanceName",
                autoboto.TypeInfo(str),
            ),
            (
                "username",
                "username",
                autoboto.TypeInfo(str),
            ),
        ]

    # For SSH access, the public key to use when accessing your instance For
    # OpenSSH clients (e.g., command line SSH), you should save this value to
    # `tempkey-cert.pub`.
    cert_key: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # For SSH access, the date on which the temporary keys expire.
    expires_at: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The public IP address of the Amazon Lightsail instance.
    ip_address: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # For RDP access, the password for your Amazon Lightsail instance. Password
    # will be an empty string if the password for your new instance is not ready
    # yet. When you create an instance, it can take up to 15 minutes for the
    # instance to be ready.

    # If you create an instance using any key pair other than the default
    # (`LightsailDefaultKeyPair`), `password` will always be an empty string.

    # If you change the Administrator password on the instance, Lightsail will
    # continue to return the original password value. When accessing the instance
    # using RDP, you need to manually enter the Administrator password after
    # changing it from the default.
    password: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # For a Windows Server-based instance, an object with the data you can use to
    # retrieve your password. This is only needed if `password` is empty and the
    # instance is not new (and therefore the password is not ready yet). When you
    # create an instance, it can take up to 15 minutes for the instance to be
    # ready.
    password_data: "PasswordData" = dataclasses.field(default_factory=dict, )

    # For SSH access, the temporary private key. For OpenSSH clients (e.g.,
    # command line SSH), you should save this value to `tempkey`).
    private_key: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The protocol for these Amazon Lightsail instance access details.
    protocol: "InstanceAccessProtocol" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The name of this Amazon Lightsail instance.
    instance_name: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The user name to use when logging in to the Amazon Lightsail instance.
    username: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


class InstanceAccessProtocol(Enum):
    ssh = "ssh"
    rdp = "rdp"


@dataclasses.dataclass
class InstanceHardware(autoboto.ShapeBase):
    """
    Describes the hardware for the instance.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "cpu_count",
                "cpuCount",
                autoboto.TypeInfo(int),
            ),
            (
                "disks",
                "disks",
                autoboto.TypeInfo(typing.List[Disk]),
            ),
            (
                "ram_size_in_gb",
                "ramSizeInGb",
                autoboto.TypeInfo(float),
            ),
        ]

    # The number of vCPUs the instance has.
    cpu_count: int = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The disks attached to the instance.
    disks: typing.List["Disk"] = dataclasses.field(default_factory=list, )

    # The amount of RAM in GB on the instance (e.g., `1.0`).
    ram_size_in_gb: float = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


class InstanceHealthReason(Enum):
    Lb_RegistrationInProgress = "Lb.RegistrationInProgress"
    Lb_InitialHealthChecking = "Lb.InitialHealthChecking"
    Lb_InternalError = "Lb.InternalError"
    Instance_ResponseCodeMismatch = "Instance.ResponseCodeMismatch"
    Instance_Timeout = "Instance.Timeout"
    Instance_FailedHealthChecks = "Instance.FailedHealthChecks"
    Instance_NotRegistered = "Instance.NotRegistered"
    Instance_NotInUse = "Instance.NotInUse"
    Instance_DeregistrationInProgress = "Instance.DeregistrationInProgress"
    Instance_InvalidState = "Instance.InvalidState"
    Instance_IpUnusable = "Instance.IpUnusable"


class InstanceHealthState(Enum):
    initial = "initial"
    healthy = "healthy"
    unhealthy = "unhealthy"
    unused = "unused"
    draining = "draining"
    unavailable = "unavailable"


@dataclasses.dataclass
class InstanceHealthSummary(autoboto.ShapeBase):
    """
    Describes information about the health of the instance.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "instance_name",
                "instanceName",
                autoboto.TypeInfo(str),
            ),
            (
                "instance_health",
                "instanceHealth",
                autoboto.TypeInfo(InstanceHealthState),
            ),
            (
                "instance_health_reason",
                "instanceHealthReason",
                autoboto.TypeInfo(InstanceHealthReason),
            ),
        ]

    # The name of the Lightsail instance for which you are requesting health
    # check data.
    instance_name: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # Describes the overall instance health. Valid values are below.
    instance_health: "InstanceHealthState" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # More information about the instance health. If the `instanceHealth` is
    # `healthy`, then an `instanceHealthReason` value is not provided.

    # If **`instanceHealth` ** is `initial`, the **`instanceHealthReason` **
    # value can be one of the following:

    #   * **`Lb.RegistrationInProgress` ** \- The target instance is in the process of being registered with the load balancer.

    #   * **`Lb.InitialHealthChecking` ** \- The Lightsail load balancer is still sending the target instance the minimum number of health checks required to determine its health status.

    # If **`instanceHealth` ** is `unhealthy`, the **`instanceHealthReason` **
    # value can be one of the following:

    #   * **`Instance.ResponseCodeMismatch` ** \- The health checks did not return an expected HTTP code.

    #   * **`Instance.Timeout` ** \- The health check requests timed out.

    #   * **`Instance.FailedHealthChecks` ** \- The health checks failed because the connection to the target instance timed out, the target instance response was malformed, or the target instance failed the health check for an unknown reason.

    #   * **`Lb.InternalError` ** \- The health checks failed due to an internal error.

    # If **`instanceHealth` ** is `unused`, the **`instanceHealthReason` ** value
    # can be one of the following:

    #   * **`Instance.NotRegistered` ** \- The target instance is not registered with the target group.

    #   * **`Instance.NotInUse` ** \- The target group is not used by any load balancer, or the target instance is in an Availability Zone that is not enabled for its load balancer.

    #   * **`Instance.IpUnusable` ** \- The target IP address is reserved for use by a Lightsail load balancer.

    #   * **`Instance.InvalidState` ** \- The target is in the stopped or terminated state.

    # If **`instanceHealth` ** is `draining`, the **`instanceHealthReason` **
    # value can be one of the following:

    #   * **`Instance.DeregistrationInProgress` ** \- The target instance is in the process of being deregistered and the deregistration delay period has not expired.
    instance_health_reason: "InstanceHealthReason" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


class InstanceMetricName(Enum):
    CPUUtilization = "CPUUtilization"
    NetworkIn = "NetworkIn"
    NetworkOut = "NetworkOut"
    StatusCheckFailed = "StatusCheckFailed"
    StatusCheckFailed_Instance = "StatusCheckFailed_Instance"
    StatusCheckFailed_System = "StatusCheckFailed_System"


@dataclasses.dataclass
class InstanceNetworking(autoboto.ShapeBase):
    """
    Describes monthly data transfer rates and port information for an instance.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "monthly_transfer",
                "monthlyTransfer",
                autoboto.TypeInfo(MonthlyTransfer),
            ),
            (
                "ports",
                "ports",
                autoboto.TypeInfo(typing.List[InstancePortInfo]),
            ),
        ]

    # The amount of data in GB allocated for monthly data transfers.
    monthly_transfer: "MonthlyTransfer" = dataclasses.field(
        default_factory=dict,
    )

    # An array of key-value pairs containing information about the ports on the
    # instance.
    ports: typing.List["InstancePortInfo"] = dataclasses.field(
        default_factory=list,
    )


class InstancePlatform(Enum):
    LINUX_UNIX = "LINUX_UNIX"
    WINDOWS = "WINDOWS"


@dataclasses.dataclass
class InstancePortInfo(autoboto.ShapeBase):
    """
    Describes information about the instance ports.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "from_port",
                "fromPort",
                autoboto.TypeInfo(int),
            ),
            (
                "to_port",
                "toPort",
                autoboto.TypeInfo(int),
            ),
            (
                "protocol",
                "protocol",
                autoboto.TypeInfo(NetworkProtocol),
            ),
            (
                "access_from",
                "accessFrom",
                autoboto.TypeInfo(str),
            ),
            (
                "access_type",
                "accessType",
                autoboto.TypeInfo(PortAccessType),
            ),
            (
                "common_name",
                "commonName",
                autoboto.TypeInfo(str),
            ),
            (
                "access_direction",
                "accessDirection",
                autoboto.TypeInfo(AccessDirection),
            ),
        ]

    # The first port in the range.
    from_port: int = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The last port in the range.
    to_port: int = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The protocol being used. Can be one of the following.

    #   * `tcp` \- Transmission Control Protocol (TCP) provides reliable, ordered, and error-checked delivery of streamed data between applications running on hosts communicating by an IP network. If you have an application that doesn't require reliable data stream service, use UDP instead.

    #   * `all` \- All transport layer protocol types. For more general information, see [Transport layer](https://en.wikipedia.org/wiki/Transport_layer) on Wikipedia.

    #   * `udp` \- With User Datagram Protocol (UDP), computer applications can send messages (or datagrams) to other hosts on an Internet Protocol (IP) network. Prior communications are not required to set up transmission channels or data paths. Applications that don't require reliable data stream service can use UDP, which provides a connectionless datagram service that emphasizes reduced latency over reliability. If you do require reliable data stream service, use TCP instead.
    protocol: "NetworkProtocol" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The location from which access is allowed (e.g., `Anywhere (0.0.0.0/0)`).
    access_from: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The type of access (`Public` or `Private`).
    access_type: "PortAccessType" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The common name.
    common_name: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The access direction (`inbound` or `outbound`).
    access_direction: "AccessDirection" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class InstancePortState(autoboto.ShapeBase):
    """
    Describes the port state.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "from_port",
                "fromPort",
                autoboto.TypeInfo(int),
            ),
            (
                "to_port",
                "toPort",
                autoboto.TypeInfo(int),
            ),
            (
                "protocol",
                "protocol",
                autoboto.TypeInfo(NetworkProtocol),
            ),
            (
                "state",
                "state",
                autoboto.TypeInfo(PortState),
            ),
        ]

    # The first port in the range.
    from_port: int = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The last port in the range.
    to_port: int = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The protocol being used. Can be one of the following.

    #   * `tcp` \- Transmission Control Protocol (TCP) provides reliable, ordered, and error-checked delivery of streamed data between applications running on hosts communicating by an IP network. If you have an application that doesn't require reliable data stream service, use UDP instead.

    #   * `all` \- All transport layer protocol types. For more general information, see [Transport layer](https://en.wikipedia.org/wiki/Transport_layer) on Wikipedia.

    #   * `udp` \- With User Datagram Protocol (UDP), computer applications can send messages (or datagrams) to other hosts on an Internet Protocol (IP) network. Prior communications are not required to set up transmission channels or data paths. Applications that don't require reliable data stream service can use UDP, which provides a connectionless datagram service that emphasizes reduced latency over reliability. If you do require reliable data stream service, use TCP instead.
    protocol: "NetworkProtocol" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Specifies whether the instance port is `open` or `closed`.
    state: "PortState" = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class InstanceSnapshot(autoboto.ShapeBase):
    """
    Describes the snapshot of the virtual private server, or _instance_.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "name",
                "name",
                autoboto.TypeInfo(str),
            ),
            (
                "arn",
                "arn",
                autoboto.TypeInfo(str),
            ),
            (
                "support_code",
                "supportCode",
                autoboto.TypeInfo(str),
            ),
            (
                "created_at",
                "createdAt",
                autoboto.TypeInfo(datetime.datetime),
            ),
            (
                "location",
                "location",
                autoboto.TypeInfo(ResourceLocation),
            ),
            (
                "resource_type",
                "resourceType",
                autoboto.TypeInfo(ResourceType),
            ),
            (
                "state",
                "state",
                autoboto.TypeInfo(InstanceSnapshotState),
            ),
            (
                "progress",
                "progress",
                autoboto.TypeInfo(str),
            ),
            (
                "from_attached_disks",
                "fromAttachedDisks",
                autoboto.TypeInfo(typing.List[Disk]),
            ),
            (
                "from_instance_name",
                "fromInstanceName",
                autoboto.TypeInfo(str),
            ),
            (
                "from_instance_arn",
                "fromInstanceArn",
                autoboto.TypeInfo(str),
            ),
            (
                "from_blueprint_id",
                "fromBlueprintId",
                autoboto.TypeInfo(str),
            ),
            (
                "from_bundle_id",
                "fromBundleId",
                autoboto.TypeInfo(str),
            ),
            (
                "size_in_gb",
                "sizeInGb",
                autoboto.TypeInfo(int),
            ),
        ]

    # The name of the snapshot.
    name: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The Amazon Resource Name (ARN) of the snapshot (e.g.,
    # `arn:aws:lightsail:us-
    # east-2:123456789101:InstanceSnapshot/d23b5706-3322-4d83-81e5-12345EXAMPLE`).
    arn: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The support code. Include this code in your email to support when you have
    # questions about an instance or another resource in Lightsail. This code
    # enables our support team to look up your Lightsail information more easily.
    support_code: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The timestamp when the snapshot was created (e.g., `1479907467.024`).
    created_at: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The region name and availability zone where you created the snapshot.
    location: "ResourceLocation" = dataclasses.field(default_factory=dict, )

    # The type of resource (usually `InstanceSnapshot`).
    resource_type: "ResourceType" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The state the snapshot is in.
    state: "InstanceSnapshotState" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The progress of the snapshot.
    progress: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # An array of disk objects containing information about all block storage
    # disks.
    from_attached_disks: typing.List["Disk"] = dataclasses.field(
        default_factory=list,
    )

    # The instance from which the snapshot was created.
    from_instance_name: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The Amazon Resource Name (ARN) of the instance from which the snapshot was
    # created (e.g., `arn:aws:lightsail:us-
    # east-2:123456789101:Instance/64b8404c-ccb1-430b-8daf-12345EXAMPLE`).
    from_instance_arn: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The blueprint ID from which you created the snapshot (e.g.,
    # `os_debian_8_3`). A blueprint is a virtual private server (or _instance_ )
    # image used to create instances quickly.
    from_blueprint_id: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The bundle ID from which you created the snapshot (e.g., `micro_1_0`).
    from_bundle_id: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The size in GB of the SSD.
    size_in_gb: int = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


class InstanceSnapshotState(Enum):
    pending = "pending"
    error = "error"
    available = "available"


@dataclasses.dataclass
class InstanceState(autoboto.ShapeBase):
    """
    Describes the virtual private server (or _instance_ ) status.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "code",
                "code",
                autoboto.TypeInfo(int),
            ),
            (
                "name",
                "name",
                autoboto.TypeInfo(str),
            ),
        ]

    # The status code for the instance.
    code: int = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The state of the instance (e.g., `running` or `pending`).
    name: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class InvalidInputException(autoboto.ShapeBase):
    """
    Lightsail throws this exception when user input does not conform to the
    validation rules of an input field.

    Domain-related APIs are only available in the N. Virginia (us-east-1) Region.
    Please set your AWS Region configuration to us-east-1 to create, view, or edit
    these resources.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "code",
                "code",
                autoboto.TypeInfo(str),
            ),
            (
                "docs",
                "docs",
                autoboto.TypeInfo(str),
            ),
            (
                "message",
                "message",
                autoboto.TypeInfo(str),
            ),
            (
                "tip",
                "tip",
                autoboto.TypeInfo(str),
            ),
        ]

    code: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )
    docs: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )
    message: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )
    tip: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class IsVpcPeeredRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class IsVpcPeeredResult(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "is_peered",
                "isPeered",
                autoboto.TypeInfo(bool),
            ),
        ]

    # Returns `true` if the Lightsail VPC is peered; otherwise, `false`.
    is_peered: bool = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class KeyPair(autoboto.ShapeBase):
    """
    Describes the SSH key pair.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "name",
                "name",
                autoboto.TypeInfo(str),
            ),
            (
                "arn",
                "arn",
                autoboto.TypeInfo(str),
            ),
            (
                "support_code",
                "supportCode",
                autoboto.TypeInfo(str),
            ),
            (
                "created_at",
                "createdAt",
                autoboto.TypeInfo(datetime.datetime),
            ),
            (
                "location",
                "location",
                autoboto.TypeInfo(ResourceLocation),
            ),
            (
                "resource_type",
                "resourceType",
                autoboto.TypeInfo(ResourceType),
            ),
            (
                "fingerprint",
                "fingerprint",
                autoboto.TypeInfo(str),
            ),
        ]

    # The friendly name of the SSH key pair.
    name: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The Amazon Resource Name (ARN) of the key pair (e.g.,
    # `arn:aws:lightsail:us-
    # east-2:123456789101:KeyPair/05859e3d-331d-48ba-9034-12345EXAMPLE`).
    arn: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The support code. Include this code in your email to support when you have
    # questions about an instance or another resource in Lightsail. This code
    # enables our support team to look up your Lightsail information more easily.
    support_code: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The timestamp when the key pair was created (e.g., `1479816991.349`).
    created_at: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The region name and Availability Zone where the key pair was created.
    location: "ResourceLocation" = dataclasses.field(default_factory=dict, )

    # The resource type (usually `KeyPair`).
    resource_type: "ResourceType" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The RSA fingerprint of the key pair.
    fingerprint: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class LoadBalancer(autoboto.ShapeBase):
    """
    Describes the Lightsail load balancer.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "name",
                "name",
                autoboto.TypeInfo(str),
            ),
            (
                "arn",
                "arn",
                autoboto.TypeInfo(str),
            ),
            (
                "support_code",
                "supportCode",
                autoboto.TypeInfo(str),
            ),
            (
                "created_at",
                "createdAt",
                autoboto.TypeInfo(datetime.datetime),
            ),
            (
                "location",
                "location",
                autoboto.TypeInfo(ResourceLocation),
            ),
            (
                "resource_type",
                "resourceType",
                autoboto.TypeInfo(ResourceType),
            ),
            (
                "dns_name",
                "dnsName",
                autoboto.TypeInfo(str),
            ),
            (
                "state",
                "state",
                autoboto.TypeInfo(LoadBalancerState),
            ),
            (
                "protocol",
                "protocol",
                autoboto.TypeInfo(LoadBalancerProtocol),
            ),
            (
                "public_ports",
                "publicPorts",
                autoboto.TypeInfo(typing.List[int]),
            ),
            (
                "health_check_path",
                "healthCheckPath",
                autoboto.TypeInfo(str),
            ),
            (
                "instance_port",
                "instancePort",
                autoboto.TypeInfo(int),
            ),
            (
                "instance_health_summary",
                "instanceHealthSummary",
                autoboto.TypeInfo(typing.List[InstanceHealthSummary]),
            ),
            (
                "tls_certificate_summaries",
                "tlsCertificateSummaries",
                autoboto.TypeInfo(
                    typing.List[LoadBalancerTlsCertificateSummary]
                ),
            ),
            (
                "configuration_options",
                "configurationOptions",
                autoboto.TypeInfo(typing.Dict[LoadBalancerAttributeName, str]),
            ),
        ]

    # The name of the load balancer (e.g., `my-load-balancer`).
    name: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The Amazon Resource Name (ARN) of the load balancer.
    arn: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The support code. Include this code in your email to support when you have
    # questions about your Lightsail load balancer. This code enables our support
    # team to look up your Lightsail information more easily.
    support_code: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The date when your load balancer was created.
    created_at: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The AWS Region where your load balancer was created (e.g., `us-east-2a`).
    # Lightsail automatically creates your load balancer across Availability
    # Zones.
    location: "ResourceLocation" = dataclasses.field(default_factory=dict, )

    # The resource type (e.g., `LoadBalancer`.
    resource_type: "ResourceType" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The DNS name of your Lightsail load balancer.
    dns_name: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The status of your load balancer. Valid values are below.
    state: "LoadBalancerState" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The protocol you have enabled for your load balancer. Valid values are
    # below.

    # You can't just have `HTTP_HTTPS`, but you can have just `HTTP`.
    protocol: "LoadBalancerProtocol" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # An array of public port settings for your load balancer. For HTTP, use port
    # 80. For HTTPS, use port 443.
    public_ports: typing.List[int] = dataclasses.field(default_factory=list, )

    # The path you specified to perform your health checks. If no path is
    # specified, the load balancer tries to make a request to the default (root)
    # page.
    health_check_path: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The port where the load balancer will direct traffic to your Lightsail
    # instances. For HTTP traffic, it's port 80. For HTTPS traffic, it's port
    # 443.
    instance_port: int = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # An array of InstanceHealthSummary objects describing the health of the load
    # balancer.
    instance_health_summary: typing.List["InstanceHealthSummary"
                                        ] = dataclasses.field(
                                            default_factory=list,
                                        )

    # An array of LoadBalancerTlsCertificateSummary objects that provide
    # additional information about the SSL/TLS certificates. For example, if
    # `true`, the certificate is attached to the load balancer.
    tls_certificate_summaries: typing.List["LoadBalancerTlsCertificateSummary"
                                          ] = dataclasses.field(
                                              default_factory=list,
                                          )

    # A string to string map of the configuration options for your load balancer.
    # Valid values are listed below.
    configuration_options: typing.Dict["LoadBalancerAttributeName", str
                                      ] = dataclasses.field(
                                          default=autoboto.ShapeBase.NOT_SET,
                                      )


class LoadBalancerAttributeName(Enum):
    HealthCheckPath = "HealthCheckPath"
    SessionStickinessEnabled = "SessionStickinessEnabled"
    SessionStickiness_LB_CookieDurationSeconds = "SessionStickiness_LB_CookieDurationSeconds"


class LoadBalancerMetricName(Enum):
    ClientTLSNegotiationErrorCount = "ClientTLSNegotiationErrorCount"
    HealthyHostCount = "HealthyHostCount"
    UnhealthyHostCount = "UnhealthyHostCount"
    HTTPCode_LB_4XX_Count = "HTTPCode_LB_4XX_Count"
    HTTPCode_LB_5XX_Count = "HTTPCode_LB_5XX_Count"
    HTTPCode_Instance_2XX_Count = "HTTPCode_Instance_2XX_Count"
    HTTPCode_Instance_3XX_Count = "HTTPCode_Instance_3XX_Count"
    HTTPCode_Instance_4XX_Count = "HTTPCode_Instance_4XX_Count"
    HTTPCode_Instance_5XX_Count = "HTTPCode_Instance_5XX_Count"
    InstanceResponseTime = "InstanceResponseTime"
    RejectedConnectionCount = "RejectedConnectionCount"
    RequestCount = "RequestCount"


class LoadBalancerProtocol(Enum):
    HTTP_HTTPS = "HTTP_HTTPS"
    HTTP = "HTTP"


class LoadBalancerState(Enum):
    active = "active"
    provisioning = "provisioning"
    active_impaired = "active_impaired"
    failed = "failed"
    unknown = "unknown"


@dataclasses.dataclass
class LoadBalancerTlsCertificate(autoboto.ShapeBase):
    """
    Describes a load balancer SSL/TLS certificate.

    TLS is just an updated, more secure version of Secure Socket Layer (SSL).
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "name",
                "name",
                autoboto.TypeInfo(str),
            ),
            (
                "arn",
                "arn",
                autoboto.TypeInfo(str),
            ),
            (
                "support_code",
                "supportCode",
                autoboto.TypeInfo(str),
            ),
            (
                "created_at",
                "createdAt",
                autoboto.TypeInfo(datetime.datetime),
            ),
            (
                "location",
                "location",
                autoboto.TypeInfo(ResourceLocation),
            ),
            (
                "resource_type",
                "resourceType",
                autoboto.TypeInfo(ResourceType),
            ),
            (
                "load_balancer_name",
                "loadBalancerName",
                autoboto.TypeInfo(str),
            ),
            (
                "is_attached",
                "isAttached",
                autoboto.TypeInfo(bool),
            ),
            (
                "status",
                "status",
                autoboto.TypeInfo(LoadBalancerTlsCertificateStatus),
            ),
            (
                "domain_name",
                "domainName",
                autoboto.TypeInfo(str),
            ),
            (
                "domain_validation_records",
                "domainValidationRecords",
                autoboto.TypeInfo(
                    typing.List[LoadBalancerTlsCertificateDomainValidationRecord
                               ]
                ),
            ),
            (
                "failure_reason",
                "failureReason",
                autoboto.TypeInfo(LoadBalancerTlsCertificateFailureReason),
            ),
            (
                "issued_at",
                "issuedAt",
                autoboto.TypeInfo(datetime.datetime),
            ),
            (
                "issuer",
                "issuer",
                autoboto.TypeInfo(str),
            ),
            (
                "key_algorithm",
                "keyAlgorithm",
                autoboto.TypeInfo(str),
            ),
            (
                "not_after",
                "notAfter",
                autoboto.TypeInfo(datetime.datetime),
            ),
            (
                "not_before",
                "notBefore",
                autoboto.TypeInfo(datetime.datetime),
            ),
            (
                "renewal_summary",
                "renewalSummary",
                autoboto.TypeInfo(LoadBalancerTlsCertificateRenewalSummary),
            ),
            (
                "revocation_reason",
                "revocationReason",
                autoboto.TypeInfo(LoadBalancerTlsCertificateRevocationReason),
            ),
            (
                "revoked_at",
                "revokedAt",
                autoboto.TypeInfo(datetime.datetime),
            ),
            (
                "serial",
                "serial",
                autoboto.TypeInfo(str),
            ),
            (
                "signature_algorithm",
                "signatureAlgorithm",
                autoboto.TypeInfo(str),
            ),
            (
                "subject",
                "subject",
                autoboto.TypeInfo(str),
            ),
            (
                "subject_alternative_names",
                "subjectAlternativeNames",
                autoboto.TypeInfo(typing.List[str]),
            ),
        ]

    # The name of the SSL/TLS certificate (e.g., `my-certificate`).
    name: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The Amazon Resource Name (ARN) of the SSL/TLS certificate.
    arn: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The support code. Include this code in your email to support when you have
    # questions about your Lightsail load balancer or SSL/TLS certificate. This
    # code enables our support team to look up your Lightsail information more
    # easily.
    support_code: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The time when you created your SSL/TLS certificate.
    created_at: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The AWS Region and Availability Zone where you created your certificate.
    location: "ResourceLocation" = dataclasses.field(default_factory=dict, )

    # The resource type (e.g., `LoadBalancerTlsCertificate`).

    #   * **`Instance` ** \- A Lightsail instance (a virtual private server)

    #   * **`StaticIp` ** \- A static IP address

    #   * **`KeyPair` ** \- The key pair used to connect to a Lightsail instance

    #   * **`InstanceSnapshot` ** \- A Lightsail instance snapshot

    #   * **`Domain` ** \- A DNS zone

    #   * **`PeeredVpc` ** \- A peered VPC

    #   * **`LoadBalancer` ** \- A Lightsail load balancer

    #   * **`LoadBalancerTlsCertificate` ** \- An SSL/TLS certificate associated with a Lightsail load balancer

    #   * **`Disk` ** \- A Lightsail block storage disk

    #   * **`DiskSnapshot` ** \- A block storage disk snapshot
    resource_type: "ResourceType" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The load balancer name where your SSL/TLS certificate is attached.
    load_balancer_name: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # When `true`, the SSL/TLS certificate is attached to the Lightsail load
    # balancer.
    is_attached: bool = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The status of the SSL/TLS certificate. Valid values are below.
    status: "LoadBalancerTlsCertificateStatus" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The domain name for your SSL/TLS certificate.
    domain_name: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # An array of LoadBalancerTlsCertificateDomainValidationRecord objects
    # describing the records.
    domain_validation_records: typing.List[
        "LoadBalancerTlsCertificateDomainValidationRecord"
    ] = dataclasses.field(
        default_factory=list,
    )

    # The reason for the SSL/TLS certificate validation failure.
    failure_reason: "LoadBalancerTlsCertificateFailureReason" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The time when the SSL/TLS certificate was issued.
    issued_at: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The issuer of the certificate.
    issuer: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The algorithm that was used to generate the key pair (the public and
    # private key).
    key_algorithm: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The timestamp when the SSL/TLS certificate expires.
    not_after: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The timestamp when the SSL/TLS certificate is first valid.
    not_before: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # An object containing information about the status of Lightsail's managed
    # renewal for the certificate.
    renewal_summary: "LoadBalancerTlsCertificateRenewalSummary" = dataclasses.field(
        default_factory=dict,
    )

    # The reason the certificate was revoked. Valid values are below.
    revocation_reason: "LoadBalancerTlsCertificateRevocationReason" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The timestamp when the SSL/TLS certificate was revoked.
    revoked_at: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The serial number of the certificate.
    serial: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The algorithm that was used to sign the certificate.
    signature_algorithm: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The name of the entity that is associated with the public key contained in
    # the certificate.
    subject: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # One or more domains or subdomains included in the certificate. This list
    # contains the domain names that are bound to the public key that is
    # contained in the certificate. The subject alternative names include the
    # canonical domain name (CNAME) of the certificate and additional domain
    # names that can be used to connect to the website, such as `example.com`,
    # `www.example.com`, or `m.example.com`.
    subject_alternative_names: typing.List[str] = dataclasses.field(
        default_factory=list,
    )


class LoadBalancerTlsCertificateDomainStatus(Enum):
    PENDING_VALIDATION = "PENDING_VALIDATION"
    FAILED = "FAILED"
    SUCCESS = "SUCCESS"


@dataclasses.dataclass
class LoadBalancerTlsCertificateDomainValidationOption(autoboto.ShapeBase):
    """
    Contains information about the domain names on an SSL/TLS certificate that you
    will use to validate domain ownership.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "domain_name",
                "domainName",
                autoboto.TypeInfo(str),
            ),
            (
                "validation_status",
                "validationStatus",
                autoboto.TypeInfo(LoadBalancerTlsCertificateDomainStatus),
            ),
        ]

    # The fully qualified domain name in the certificate request.
    domain_name: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The status of the domain validation. Valid values are listed below.
    validation_status: "LoadBalancerTlsCertificateDomainStatus" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class LoadBalancerTlsCertificateDomainValidationRecord(autoboto.ShapeBase):
    """
    Describes the validation record of each domain name in the SSL/TLS certificate.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "name",
                "name",
                autoboto.TypeInfo(str),
            ),
            (
                "type",
                "type",
                autoboto.TypeInfo(str),
            ),
            (
                "value",
                "value",
                autoboto.TypeInfo(str),
            ),
            (
                "validation_status",
                "validationStatus",
                autoboto.TypeInfo(LoadBalancerTlsCertificateDomainStatus),
            ),
            (
                "domain_name",
                "domainName",
                autoboto.TypeInfo(str),
            ),
        ]

    # A fully qualified domain name in the certificate. For example,
    # `example.com`.
    name: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The type of validation record. For example, `CNAME` for domain validation.
    type: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The value for that type.
    value: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The validation status. Valid values are listed below.
    validation_status: "LoadBalancerTlsCertificateDomainStatus" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The domain name against which your SSL/TLS certificate was validated.
    domain_name: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


class LoadBalancerTlsCertificateFailureReason(Enum):
    NO_AVAILABLE_CONTACTS = "NO_AVAILABLE_CONTACTS"
    ADDITIONAL_VERIFICATION_REQUIRED = "ADDITIONAL_VERIFICATION_REQUIRED"
    DOMAIN_NOT_ALLOWED = "DOMAIN_NOT_ALLOWED"
    INVALID_PUBLIC_DOMAIN = "INVALID_PUBLIC_DOMAIN"
    OTHER = "OTHER"


class LoadBalancerTlsCertificateRenewalStatus(Enum):
    PENDING_AUTO_RENEWAL = "PENDING_AUTO_RENEWAL"
    PENDING_VALIDATION = "PENDING_VALIDATION"
    SUCCESS = "SUCCESS"
    FAILED = "FAILED"


@dataclasses.dataclass
class LoadBalancerTlsCertificateRenewalSummary(autoboto.ShapeBase):
    """
    Contains information about the status of Lightsail's managed renewal for the
    certificate.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "renewal_status",
                "renewalStatus",
                autoboto.TypeInfo(LoadBalancerTlsCertificateRenewalStatus),
            ),
            (
                "domain_validation_options",
                "domainValidationOptions",
                autoboto.TypeInfo(
                    typing.List[LoadBalancerTlsCertificateDomainValidationOption
                               ]
                ),
            ),
        ]

    # The status of Lightsail's managed renewal of the certificate. Valid values
    # are listed below.
    renewal_status: "LoadBalancerTlsCertificateRenewalStatus" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # Contains information about the validation of each domain name in the
    # certificate, as it pertains to Lightsail's managed renewal. This is
    # different from the initial validation that occurs as a result of the
    # RequestCertificate request.
    domain_validation_options: typing.List[
        "LoadBalancerTlsCertificateDomainValidationOption"
    ] = dataclasses.field(
        default_factory=list,
    )


class LoadBalancerTlsCertificateRevocationReason(Enum):
    UNSPECIFIED = "UNSPECIFIED"
    KEY_COMPROMISE = "KEY_COMPROMISE"
    CA_COMPROMISE = "CA_COMPROMISE"
    AFFILIATION_CHANGED = "AFFILIATION_CHANGED"
    SUPERCEDED = "SUPERCEDED"
    CESSATION_OF_OPERATION = "CESSATION_OF_OPERATION"
    CERTIFICATE_HOLD = "CERTIFICATE_HOLD"
    REMOVE_FROM_CRL = "REMOVE_FROM_CRL"
    PRIVILEGE_WITHDRAWN = "PRIVILEGE_WITHDRAWN"
    A_A_COMPROMISE = "A_A_COMPROMISE"


class LoadBalancerTlsCertificateStatus(Enum):
    PENDING_VALIDATION = "PENDING_VALIDATION"
    ISSUED = "ISSUED"
    INACTIVE = "INACTIVE"
    EXPIRED = "EXPIRED"
    VALIDATION_TIMED_OUT = "VALIDATION_TIMED_OUT"
    REVOKED = "REVOKED"
    FAILED = "FAILED"
    UNKNOWN = "UNKNOWN"


@dataclasses.dataclass
class LoadBalancerTlsCertificateSummary(autoboto.ShapeBase):
    """
    Provides a summary of SSL/TLS certificate metadata.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "name",
                "name",
                autoboto.TypeInfo(str),
            ),
            (
                "is_attached",
                "isAttached",
                autoboto.TypeInfo(bool),
            ),
        ]

    # The name of the SSL/TLS certificate.
    name: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # When `true`, the SSL/TLS certificate is attached to the Lightsail load
    # balancer.
    is_attached: bool = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class MetricDatapoint(autoboto.ShapeBase):
    """
    Describes the metric data point.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "average",
                "average",
                autoboto.TypeInfo(float),
            ),
            (
                "maximum",
                "maximum",
                autoboto.TypeInfo(float),
            ),
            (
                "minimum",
                "minimum",
                autoboto.TypeInfo(float),
            ),
            (
                "sample_count",
                "sampleCount",
                autoboto.TypeInfo(float),
            ),
            (
                "sum",
                "sum",
                autoboto.TypeInfo(float),
            ),
            (
                "timestamp",
                "timestamp",
                autoboto.TypeInfo(datetime.datetime),
            ),
            (
                "unit",
                "unit",
                autoboto.TypeInfo(MetricUnit),
            ),
        ]

    # The average.
    average: float = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The maximum.
    maximum: float = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The minimum.
    minimum: float = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The sample count.
    sample_count: float = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The sum.
    sum: float = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The timestamp (e.g., `1479816991.349`).
    timestamp: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The unit.
    unit: "MetricUnit" = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


class MetricStatistic(Enum):
    Minimum = "Minimum"
    Maximum = "Maximum"
    Sum = "Sum"
    Average = "Average"
    SampleCount = "SampleCount"


class MetricUnit(Enum):
    SECONDS = "Seconds"
    MICROSECONDS = "Microseconds"
    MILLISECONDS = "Milliseconds"
    BYTES = "Bytes"
    KILOBYTES = "Kilobytes"
    MEGABYTES = "Megabytes"
    GIGABYTES = "Gigabytes"
    TERABYTES = "Terabytes"
    BITS = "Bits"
    KILOBITS = "Kilobits"
    MEGABITS = "Megabits"
    GIGABITS = "Gigabits"
    TERABITS = "Terabits"
    PERCENT = "Percent"
    COUNT = "Count"
    BYTES_SECOND = "Bytes/Second"
    KILOBYTES_SECOND = "Kilobytes/Second"
    MEGABYTES_SECOND = "Megabytes/Second"
    GIGABYTES_SECOND = "Gigabytes/Second"
    TERABYTES_SECOND = "Terabytes/Second"
    BITS_SECOND = "Bits/Second"
    KILOBITS_SECOND = "Kilobits/Second"
    MEGABITS_SECOND = "Megabits/Second"
    GIGABITS_SECOND = "Gigabits/Second"
    TERABITS_SECOND = "Terabits/Second"
    COUNT_SECOND = "Count/Second"
    NONE = "None"


@dataclasses.dataclass
class MonthlyTransfer(autoboto.ShapeBase):
    """
    Describes the monthly data transfer in and out of your virtual private server
    (or _instance_ ).
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "gb_per_month_allocated",
                "gbPerMonthAllocated",
                autoboto.TypeInfo(int),
            ),
        ]

    # The amount allocated per month (in GB).
    gb_per_month_allocated: int = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


class NetworkProtocol(Enum):
    tcp = "tcp"
    all = "all"
    udp = "udp"


@dataclasses.dataclass
class NotFoundException(autoboto.ShapeBase):
    """
    Lightsail throws this exception when it cannot find a resource.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "code",
                "code",
                autoboto.TypeInfo(str),
            ),
            (
                "docs",
                "docs",
                autoboto.TypeInfo(str),
            ),
            (
                "message",
                "message",
                autoboto.TypeInfo(str),
            ),
            (
                "tip",
                "tip",
                autoboto.TypeInfo(str),
            ),
        ]

    code: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )
    docs: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )
    message: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )
    tip: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class OpenInstancePublicPortsRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "port_info",
                "portInfo",
                autoboto.TypeInfo(PortInfo),
            ),
            (
                "instance_name",
                "instanceName",
                autoboto.TypeInfo(str),
            ),
        ]

    # An array of key-value pairs containing information about the port mappings.
    port_info: "PortInfo" = dataclasses.field(default_factory=dict, )

    # The name of the instance for which you want to open the public ports.
    instance_name: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class OpenInstancePublicPortsResult(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "operation",
                "operation",
                autoboto.TypeInfo(Operation),
            ),
        ]

    # An array of key-value pairs containing information about the request
    # operation.
    operation: "Operation" = dataclasses.field(default_factory=dict, )


@dataclasses.dataclass
class Operation(autoboto.ShapeBase):
    """
    Describes the API operation.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "id",
                "id",
                autoboto.TypeInfo(str),
            ),
            (
                "resource_name",
                "resourceName",
                autoboto.TypeInfo(str),
            ),
            (
                "resource_type",
                "resourceType",
                autoboto.TypeInfo(ResourceType),
            ),
            (
                "created_at",
                "createdAt",
                autoboto.TypeInfo(datetime.datetime),
            ),
            (
                "location",
                "location",
                autoboto.TypeInfo(ResourceLocation),
            ),
            (
                "is_terminal",
                "isTerminal",
                autoboto.TypeInfo(bool),
            ),
            (
                "operation_details",
                "operationDetails",
                autoboto.TypeInfo(str),
            ),
            (
                "operation_type",
                "operationType",
                autoboto.TypeInfo(OperationType),
            ),
            (
                "status",
                "status",
                autoboto.TypeInfo(OperationStatus),
            ),
            (
                "status_changed_at",
                "statusChangedAt",
                autoboto.TypeInfo(datetime.datetime),
            ),
            (
                "error_code",
                "errorCode",
                autoboto.TypeInfo(str),
            ),
            (
                "error_details",
                "errorDetails",
                autoboto.TypeInfo(str),
            ),
        ]

    # The ID of the operation.
    id: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The resource name.
    resource_name: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The resource type.
    resource_type: "ResourceType" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The timestamp when the operation was initialized (e.g., `1479816991.349`).
    created_at: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The region and Availability Zone.
    location: "ResourceLocation" = dataclasses.field(default_factory=dict, )

    # A Boolean value indicating whether the operation is terminal.
    is_terminal: bool = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # Details about the operation (e.g., `Debian-1GB-Ohio-1`).
    operation_details: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The type of operation.
    operation_type: "OperationType" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The status of the operation.
    status: "OperationStatus" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The timestamp when the status was changed (e.g., `1479816991.349`).
    status_changed_at: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The error code.
    error_code: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The error details.
    error_details: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class OperationFailureException(autoboto.ShapeBase):
    """
    Lightsail throws this exception when an operation fails to execute.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "code",
                "code",
                autoboto.TypeInfo(str),
            ),
            (
                "docs",
                "docs",
                autoboto.TypeInfo(str),
            ),
            (
                "message",
                "message",
                autoboto.TypeInfo(str),
            ),
            (
                "tip",
                "tip",
                autoboto.TypeInfo(str),
            ),
        ]

    code: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )
    docs: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )
    message: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )
    tip: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


class OperationStatus(Enum):
    NotStarted = "NotStarted"
    Started = "Started"
    Failed = "Failed"
    Completed = "Completed"
    Succeeded = "Succeeded"


class OperationType(Enum):
    DeleteInstance = "DeleteInstance"
    CreateInstance = "CreateInstance"
    StopInstance = "StopInstance"
    StartInstance = "StartInstance"
    RebootInstance = "RebootInstance"
    OpenInstancePublicPorts = "OpenInstancePublicPorts"
    PutInstancePublicPorts = "PutInstancePublicPorts"
    CloseInstancePublicPorts = "CloseInstancePublicPorts"
    AllocateStaticIp = "AllocateStaticIp"
    ReleaseStaticIp = "ReleaseStaticIp"
    AttachStaticIp = "AttachStaticIp"
    DetachStaticIp = "DetachStaticIp"
    UpdateDomainEntry = "UpdateDomainEntry"
    DeleteDomainEntry = "DeleteDomainEntry"
    CreateDomain = "CreateDomain"
    DeleteDomain = "DeleteDomain"
    CreateInstanceSnapshot = "CreateInstanceSnapshot"
    DeleteInstanceSnapshot = "DeleteInstanceSnapshot"
    CreateInstancesFromSnapshot = "CreateInstancesFromSnapshot"
    CreateLoadBalancer = "CreateLoadBalancer"
    DeleteLoadBalancer = "DeleteLoadBalancer"
    AttachInstancesToLoadBalancer = "AttachInstancesToLoadBalancer"
    DetachInstancesFromLoadBalancer = "DetachInstancesFromLoadBalancer"
    UpdateLoadBalancerAttribute = "UpdateLoadBalancerAttribute"
    CreateLoadBalancerTlsCertificate = "CreateLoadBalancerTlsCertificate"
    DeleteLoadBalancerTlsCertificate = "DeleteLoadBalancerTlsCertificate"
    AttachLoadBalancerTlsCertificate = "AttachLoadBalancerTlsCertificate"
    CreateDisk = "CreateDisk"
    DeleteDisk = "DeleteDisk"
    AttachDisk = "AttachDisk"
    DetachDisk = "DetachDisk"
    CreateDiskSnapshot = "CreateDiskSnapshot"
    DeleteDiskSnapshot = "DeleteDiskSnapshot"
    CreateDiskFromSnapshot = "CreateDiskFromSnapshot"


@dataclasses.dataclass
class PasswordData(autoboto.ShapeBase):
    """
    The password data for the Windows Server-based instance, including the
    ciphertext and the key pair name.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "ciphertext",
                "ciphertext",
                autoboto.TypeInfo(str),
            ),
            (
                "key_pair_name",
                "keyPairName",
                autoboto.TypeInfo(str),
            ),
        ]

    # The encrypted password. Ciphertext will be an empty string if access to
    # your new instance is not ready yet. When you create an instance, it can
    # take up to 15 minutes for the instance to be ready.

    # If you use the default key pair (`LightsailDefaultKeyPair`), the decrypted
    # password will be available in the password field.

    # If you are using a custom key pair, you need to use your own means of
    # decryption.

    # If you change the Administrator password on the instance, Lightsail will
    # continue to return the original ciphertext value. When accessing the
    # instance using RDP, you need to manually enter the Administrator password
    # after changing it from the default.
    ciphertext: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The name of the key pair that you used when creating your instance. If no
    # key pair name was specified when creating the instance, Lightsail uses the
    # default key pair (`LightsailDefaultKeyPair`).

    # If you are using a custom key pair, you need to use your own means of
    # decrypting your password using the `ciphertext`. Lightsail creates the
    # ciphertext by encrypting your password with the public key part of this key
    # pair.
    key_pair_name: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class PeerVpcRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class PeerVpcResult(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "operation",
                "operation",
                autoboto.TypeInfo(Operation),
            ),
        ]

    # An array of key-value pairs containing information about the request
    # operation.
    operation: "Operation" = dataclasses.field(default_factory=dict, )


class PortAccessType(Enum):
    Public = "Public"
    Private = "Private"


@dataclasses.dataclass
class PortInfo(autoboto.ShapeBase):
    """
    Describes information about the ports on your virtual private server (or
    _instance_ ).
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "from_port",
                "fromPort",
                autoboto.TypeInfo(int),
            ),
            (
                "to_port",
                "toPort",
                autoboto.TypeInfo(int),
            ),
            (
                "protocol",
                "protocol",
                autoboto.TypeInfo(NetworkProtocol),
            ),
        ]

    # The first port in the range.
    from_port: int = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The last port in the range.
    to_port: int = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The protocol.
    protocol: "NetworkProtocol" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


class PortState(Enum):
    open = "open"
    closed = "closed"


@dataclasses.dataclass
class PutInstancePublicPortsRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "port_infos",
                "portInfos",
                autoboto.TypeInfo(typing.List[PortInfo]),
            ),
            (
                "instance_name",
                "instanceName",
                autoboto.TypeInfo(str),
            ),
        ]

    # Specifies information about the public port(s).
    port_infos: typing.List["PortInfo"] = dataclasses.field(
        default_factory=list,
    )

    # The Lightsail instance name of the public port(s) you are setting.
    instance_name: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class PutInstancePublicPortsResult(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "operation",
                "operation",
                autoboto.TypeInfo(Operation),
            ),
        ]

    # Describes metadata about the operation you just executed.
    operation: "Operation" = dataclasses.field(default_factory=dict, )


@dataclasses.dataclass
class RebootInstanceRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "instance_name",
                "instanceName",
                autoboto.TypeInfo(str),
            ),
        ]

    # The name of the instance to reboot.
    instance_name: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class RebootInstanceResult(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "operations",
                "operations",
                autoboto.TypeInfo(typing.List[Operation]),
            ),
        ]

    # An array of key-value pairs containing information about the request
    # operations.
    operations: typing.List["Operation"] = dataclasses.field(
        default_factory=list,
    )


@dataclasses.dataclass
class Region(autoboto.ShapeBase):
    """
    Describes the AWS Region.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "continent_code",
                "continentCode",
                autoboto.TypeInfo(str),
            ),
            (
                "description",
                "description",
                autoboto.TypeInfo(str),
            ),
            (
                "display_name",
                "displayName",
                autoboto.TypeInfo(str),
            ),
            (
                "name",
                "name",
                autoboto.TypeInfo(RegionName),
            ),
            (
                "availability_zones",
                "availabilityZones",
                autoboto.TypeInfo(typing.List[AvailabilityZone]),
            ),
        ]

    # The continent code (e.g., `NA`, meaning North America).
    continent_code: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The description of the AWS Region (e.g., `This region is recommended to
    # serve users in the eastern United States and eastern Canada`).
    description: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The display name (e.g., `Ohio`).
    display_name: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The region name (e.g., `us-east-2`).
    name: "RegionName" = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The Availability Zones. Follows the format `us-east-2a` (case-sensitive).
    availability_zones: typing.List["AvailabilityZone"] = dataclasses.field(
        default_factory=list,
    )


class RegionName(Enum):
    us_east_1 = "us-east-1"
    us_east_2 = "us-east-2"
    us_west_1 = "us-west-1"
    us_west_2 = "us-west-2"
    eu_central_1 = "eu-central-1"
    eu_west_1 = "eu-west-1"
    eu_west_2 = "eu-west-2"
    ap_south_1 = "ap-south-1"
    ap_southeast_1 = "ap-southeast-1"
    ap_southeast_2 = "ap-southeast-2"
    ap_northeast_1 = "ap-northeast-1"
    ap_northeast_2 = "ap-northeast-2"


@dataclasses.dataclass
class ReleaseStaticIpRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "static_ip_name",
                "staticIpName",
                autoboto.TypeInfo(str),
            ),
        ]

    # The name of the static IP to delete.
    static_ip_name: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class ReleaseStaticIpResult(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "operations",
                "operations",
                autoboto.TypeInfo(typing.List[Operation]),
            ),
        ]

    # An array of key-value pairs containing information about the request
    # operation.
    operations: typing.List["Operation"] = dataclasses.field(
        default_factory=list,
    )


@dataclasses.dataclass
class ResourceLocation(autoboto.ShapeBase):
    """
    Describes the resource location.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "availability_zone",
                "availabilityZone",
                autoboto.TypeInfo(str),
            ),
            (
                "region_name",
                "regionName",
                autoboto.TypeInfo(RegionName),
            ),
        ]

    # The Availability Zone. Follows the format `us-east-2a` (case-sensitive).
    availability_zone: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The AWS Region name.
    region_name: "RegionName" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


class ResourceType(Enum):
    Instance = "Instance"
    StaticIp = "StaticIp"
    KeyPair = "KeyPair"
    InstanceSnapshot = "InstanceSnapshot"
    Domain = "Domain"
    PeeredVpc = "PeeredVpc"
    LoadBalancer = "LoadBalancer"
    LoadBalancerTlsCertificate = "LoadBalancerTlsCertificate"
    Disk = "Disk"
    DiskSnapshot = "DiskSnapshot"


@dataclasses.dataclass
class ServiceException(autoboto.ShapeBase):
    """
    A general service exception.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "code",
                "code",
                autoboto.TypeInfo(str),
            ),
            (
                "docs",
                "docs",
                autoboto.TypeInfo(str),
            ),
            (
                "message",
                "message",
                autoboto.TypeInfo(str),
            ),
            (
                "tip",
                "tip",
                autoboto.TypeInfo(str),
            ),
        ]

    code: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )
    docs: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )
    message: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )
    tip: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class StartInstanceRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "instance_name",
                "instanceName",
                autoboto.TypeInfo(str),
            ),
        ]

    # The name of the instance (a virtual private server) to start.
    instance_name: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class StartInstanceResult(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "operations",
                "operations",
                autoboto.TypeInfo(typing.List[Operation]),
            ),
        ]

    # An array of key-value pairs containing information about the request
    # operation.
    operations: typing.List["Operation"] = dataclasses.field(
        default_factory=list,
    )


@dataclasses.dataclass
class StaticIp(autoboto.ShapeBase):
    """
    Describes the static IP.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "name",
                "name",
                autoboto.TypeInfo(str),
            ),
            (
                "arn",
                "arn",
                autoboto.TypeInfo(str),
            ),
            (
                "support_code",
                "supportCode",
                autoboto.TypeInfo(str),
            ),
            (
                "created_at",
                "createdAt",
                autoboto.TypeInfo(datetime.datetime),
            ),
            (
                "location",
                "location",
                autoboto.TypeInfo(ResourceLocation),
            ),
            (
                "resource_type",
                "resourceType",
                autoboto.TypeInfo(ResourceType),
            ),
            (
                "ip_address",
                "ipAddress",
                autoboto.TypeInfo(str),
            ),
            (
                "attached_to",
                "attachedTo",
                autoboto.TypeInfo(str),
            ),
            (
                "is_attached",
                "isAttached",
                autoboto.TypeInfo(bool),
            ),
        ]

    # The name of the static IP (e.g., `StaticIP-Ohio-EXAMPLE`).
    name: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The Amazon Resource Name (ARN) of the static IP (e.g.,
    # `arn:aws:lightsail:us-
    # east-2:123456789101:StaticIp/9cbb4a9e-f8e3-4dfe-b57e-12345EXAMPLE`).
    arn: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The support code. Include this code in your email to support when you have
    # questions about an instance or another resource in Lightsail. This code
    # enables our support team to look up your Lightsail information more easily.
    support_code: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The timestamp when the static IP was created (e.g., `1479735304.222`).
    created_at: datetime.datetime = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The region and Availability Zone where the static IP was created.
    location: "ResourceLocation" = dataclasses.field(default_factory=dict, )

    # The resource type (usually `StaticIp`).
    resource_type: "ResourceType" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The static IP address.
    ip_address: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # The instance where the static IP is attached (e.g., `Amazon_Linux-1GB-
    # Ohio-1`).
    attached_to: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # A Boolean value indicating whether the static IP is attached.
    is_attached: bool = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class StopInstanceRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "instance_name",
                "instanceName",
                autoboto.TypeInfo(str),
            ),
            (
                "force",
                "force",
                autoboto.TypeInfo(bool),
            ),
        ]

    # The name of the instance (a virtual private server) to stop.
    instance_name: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # When set to `True`, forces a Lightsail instance that is stuck in a
    # `stopping` state to stop.

    # Only use the `force` parameter if your instance is stuck in the `stopping`
    # state. In any other state, your instance should stop normally without
    # adding this parameter to your API request.
    force: bool = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class StopInstanceResult(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "operations",
                "operations",
                autoboto.TypeInfo(typing.List[Operation]),
            ),
        ]

    # An array of key-value pairs containing information about the request
    # operation.
    operations: typing.List["Operation"] = dataclasses.field(
        default_factory=list,
    )


@dataclasses.dataclass
class UnauthenticatedException(autoboto.ShapeBase):
    """
    Lightsail throws this exception when the user has not been authenticated.
    """

    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "code",
                "code",
                autoboto.TypeInfo(str),
            ),
            (
                "docs",
                "docs",
                autoboto.TypeInfo(str),
            ),
            (
                "message",
                "message",
                autoboto.TypeInfo(str),
            ),
            (
                "tip",
                "tip",
                autoboto.TypeInfo(str),
            ),
        ]

    code: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )
    docs: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )
    message: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )
    tip: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )


@dataclasses.dataclass
class UnpeerVpcRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return []


@dataclasses.dataclass
class UnpeerVpcResult(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "operation",
                "operation",
                autoboto.TypeInfo(Operation),
            ),
        ]

    # An array of key-value pairs containing information about the request
    # operation.
    operation: "Operation" = dataclasses.field(default_factory=dict, )


@dataclasses.dataclass
class UpdateDomainEntryRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "domain_name",
                "domainName",
                autoboto.TypeInfo(str),
            ),
            (
                "domain_entry",
                "domainEntry",
                autoboto.TypeInfo(DomainEntry),
            ),
        ]

    # The name of the domain recordset to update.
    domain_name: str = dataclasses.field(default=autoboto.ShapeBase.NOT_SET, )

    # An array of key-value pairs containing information about the domain entry.
    domain_entry: "DomainEntry" = dataclasses.field(default_factory=dict, )


@dataclasses.dataclass
class UpdateDomainEntryResult(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "operations",
                "operations",
                autoboto.TypeInfo(typing.List[Operation]),
            ),
        ]

    # An array of key-value pairs containing information about the request
    # operation.
    operations: typing.List["Operation"] = dataclasses.field(
        default_factory=list,
    )


@dataclasses.dataclass
class UpdateLoadBalancerAttributeRequest(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "load_balancer_name",
                "loadBalancerName",
                autoboto.TypeInfo(str),
            ),
            (
                "attribute_name",
                "attributeName",
                autoboto.TypeInfo(LoadBalancerAttributeName),
            ),
            (
                "attribute_value",
                "attributeValue",
                autoboto.TypeInfo(str),
            ),
        ]

    # The name of the load balancer that you want to modify (e.g., `my-load-
    # balancer`.
    load_balancer_name: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The name of the attribute you want to update. Valid values are below.
    attribute_name: "LoadBalancerAttributeName" = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )

    # The value that you want to specify for the attribute name.
    attribute_value: str = dataclasses.field(
        default=autoboto.ShapeBase.NOT_SET,
    )


@dataclasses.dataclass
class UpdateLoadBalancerAttributeResult(autoboto.ShapeBase):
    @classmethod
    def _get_boto_mapping(cls):
        return [
            (
                "operations",
                "operations",
                autoboto.TypeInfo(typing.List[Operation]),
            ),
        ]

    # An object describing the API operations.
    operations: typing.List["Operation"] = dataclasses.field(
        default_factory=list,
    )
