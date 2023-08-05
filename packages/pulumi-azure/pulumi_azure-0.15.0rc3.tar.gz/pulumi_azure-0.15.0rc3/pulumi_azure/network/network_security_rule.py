# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import pulumi
import pulumi.runtime

class NetworkSecurityRule(pulumi.CustomResource):
    """
    Manages a Network Security Rule.
    
    ~> **NOTE on Network Security Groups and Network Security Rules:** Terraform currently
    provides both a standalone [Network Security Rule resource](network_security_rule.html), and allows for Network Security Rules to be defined in-line within the [Network Security Group resource](network_security_group.html).
    At this time you cannot use a Network Security Group with in-line Network Security Rules in conjunction with any Network Security Rule resources. Doing so will cause a conflict of rule settings and will overwrite rules.
    """
    def __init__(__self__, __name__, __opts__=None, access=None, description=None, destination_address_prefix=None, destination_address_prefixes=None, destination_application_security_group_ids=None, destination_port_range=None, destination_port_ranges=None, direction=None, name=None, network_security_group_name=None, priority=None, protocol=None, resource_group_name=None, source_address_prefix=None, source_address_prefixes=None, source_application_security_group_ids=None, source_port_range=None, source_port_ranges=None):
        """Create a NetworkSecurityRule resource with the given unique name, props, and options."""
        if not __name__:
            raise TypeError('Missing resource name argument (for URN creation)')
        if not isinstance(__name__, basestring):
            raise TypeError('Expected resource name to be a string')
        if __opts__ and not isinstance(__opts__, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')

        __props__ = dict()

        if not access:
            raise TypeError('Missing required property access')
        elif not isinstance(access, basestring):
            raise TypeError('Expected property access to be a basestring')
        __self__.access = access
        """
        Specifies whether network traffic is allowed or denied. Possible values are `Allow` and `Deny`.
        """
        __props__['access'] = access

        if description and not isinstance(description, basestring):
            raise TypeError('Expected property description to be a basestring')
        __self__.description = description
        """
        A description for this rule. Restricted to 140 characters.
        """
        __props__['description'] = description

        if destination_address_prefix and not isinstance(destination_address_prefix, basestring):
            raise TypeError('Expected property destination_address_prefix to be a basestring')
        __self__.destination_address_prefix = destination_address_prefix
        """
        CIDR or destination IP range or * to match any IP. Tags such as ‘VirtualNetwork’, ‘AzureLoadBalancer’ and ‘Internet’ can also be used. This is required if `destination_address_prefixes` is not specified.
        """
        __props__['destinationAddressPrefix'] = destination_address_prefix

        if destination_address_prefixes and not isinstance(destination_address_prefixes, list):
            raise TypeError('Expected property destination_address_prefixes to be a list')
        __self__.destination_address_prefixes = destination_address_prefixes
        """
        List of destination address prefixes. Tags may not be used. This is required if `destination_address_prefix` is not specified.
        """
        __props__['destinationAddressPrefixes'] = destination_address_prefixes

        if destination_application_security_group_ids and not isinstance(destination_application_security_group_ids, basestring):
            raise TypeError('Expected property destination_application_security_group_ids to be a basestring')
        __self__.destination_application_security_group_ids = destination_application_security_group_ids
        """
        A List of destination Application Security Group ID's
        """
        __props__['destinationApplicationSecurityGroupIds'] = destination_application_security_group_ids

        if destination_port_range and not isinstance(destination_port_range, basestring):
            raise TypeError('Expected property destination_port_range to be a basestring')
        __self__.destination_port_range = destination_port_range
        """
        Destination Port or Range. Integer or range between `0` and `65535` or `*` to match any. This is required if `destination_port_ranges` is not specified.
        """
        __props__['destinationPortRange'] = destination_port_range

        if destination_port_ranges and not isinstance(destination_port_ranges, list):
            raise TypeError('Expected property destination_port_ranges to be a list')
        __self__.destination_port_ranges = destination_port_ranges
        """
        List of destination ports or port ranges. This is required if `destination_port_range` is not specified.
        """
        __props__['destinationPortRanges'] = destination_port_ranges

        if not direction:
            raise TypeError('Missing required property direction')
        elif not isinstance(direction, basestring):
            raise TypeError('Expected property direction to be a basestring')
        __self__.direction = direction
        """
        The direction specifies if rule will be evaluated on incoming or outgoing traffic. Possible values are `Inbound` and `Outbound`.
        """
        __props__['direction'] = direction

        if name and not isinstance(name, basestring):
            raise TypeError('Expected property name to be a basestring')
        __self__.name = name
        """
        The name of the security rule. This needs to be unique across all Rules in the Network Security Group. Changing this forces a new resource to be created.
        """
        __props__['name'] = name

        if not network_security_group_name:
            raise TypeError('Missing required property network_security_group_name')
        elif not isinstance(network_security_group_name, basestring):
            raise TypeError('Expected property network_security_group_name to be a basestring')
        __self__.network_security_group_name = network_security_group_name
        """
        The name of the Network Security Group that we want to attach the rule to. Changing this forces a new resource to be created.
        """
        __props__['networkSecurityGroupName'] = network_security_group_name

        if not priority:
            raise TypeError('Missing required property priority')
        elif not isinstance(priority, int):
            raise TypeError('Expected property priority to be a int')
        __self__.priority = priority
        """
        Specifies the priority of the rule. The value can be between 100 and 4096. The priority number must be unique for each rule in the collection. The lower the priority number, the higher the priority of the rule.
        """
        __props__['priority'] = priority

        if not protocol:
            raise TypeError('Missing required property protocol')
        elif not isinstance(protocol, basestring):
            raise TypeError('Expected property protocol to be a basestring')
        __self__.protocol = protocol
        """
        Network protocol this rule applies to. Possible values include `Tcp`, `Udp` or `*` (which matches both).
        """
        __props__['protocol'] = protocol

        if not resource_group_name:
            raise TypeError('Missing required property resource_group_name')
        elif not isinstance(resource_group_name, basestring):
            raise TypeError('Expected property resource_group_name to be a basestring')
        __self__.resource_group_name = resource_group_name
        """
        The name of the resource group in which to create the Network Security Rule. Changing this forces a new resource to be created.
        """
        __props__['resourceGroupName'] = resource_group_name

        if source_address_prefix and not isinstance(source_address_prefix, basestring):
            raise TypeError('Expected property source_address_prefix to be a basestring')
        __self__.source_address_prefix = source_address_prefix
        """
        CIDR or source IP range or * to match any IP. Tags such as ‘VirtualNetwork’, ‘AzureLoadBalancer’ and ‘Internet’ can also be used. This is required if `source_address_prefixes` is not specified.
        """
        __props__['sourceAddressPrefix'] = source_address_prefix

        if source_address_prefixes and not isinstance(source_address_prefixes, list):
            raise TypeError('Expected property source_address_prefixes to be a list')
        __self__.source_address_prefixes = source_address_prefixes
        """
        List of source address prefixes. Tags may not be used. This is required if `source_address_prefix` is not specified.
        """
        __props__['sourceAddressPrefixes'] = source_address_prefixes

        if source_application_security_group_ids and not isinstance(source_application_security_group_ids, basestring):
            raise TypeError('Expected property source_application_security_group_ids to be a basestring')
        __self__.source_application_security_group_ids = source_application_security_group_ids
        """
        A List of source Application Security Group ID's
        """
        __props__['sourceApplicationSecurityGroupIds'] = source_application_security_group_ids

        if source_port_range and not isinstance(source_port_range, basestring):
            raise TypeError('Expected property source_port_range to be a basestring')
        __self__.source_port_range = source_port_range
        """
        Source Port or Range. Integer or range between `0` and `65535` or `*` to match any. This is required if `source_port_ranges` is not specified.
        """
        __props__['sourcePortRange'] = source_port_range

        if source_port_ranges and not isinstance(source_port_ranges, list):
            raise TypeError('Expected property source_port_ranges to be a list')
        __self__.source_port_ranges = source_port_ranges
        """
        List of source ports or port ranges. This is required if `source_port_range` is not specified.
        """
        __props__['sourcePortRanges'] = source_port_ranges

        super(NetworkSecurityRule, __self__).__init__(
            'azure:network/networkSecurityRule:NetworkSecurityRule',
            __name__,
            __props__,
            __opts__)

    def set_outputs(self, outs):
        if 'access' in outs:
            self.access = outs['access']
        if 'description' in outs:
            self.description = outs['description']
        if 'destinationAddressPrefix' in outs:
            self.destination_address_prefix = outs['destinationAddressPrefix']
        if 'destinationAddressPrefixes' in outs:
            self.destination_address_prefixes = outs['destinationAddressPrefixes']
        if 'destinationApplicationSecurityGroupIds' in outs:
            self.destination_application_security_group_ids = outs['destinationApplicationSecurityGroupIds']
        if 'destinationPortRange' in outs:
            self.destination_port_range = outs['destinationPortRange']
        if 'destinationPortRanges' in outs:
            self.destination_port_ranges = outs['destinationPortRanges']
        if 'direction' in outs:
            self.direction = outs['direction']
        if 'name' in outs:
            self.name = outs['name']
        if 'networkSecurityGroupName' in outs:
            self.network_security_group_name = outs['networkSecurityGroupName']
        if 'priority' in outs:
            self.priority = outs['priority']
        if 'protocol' in outs:
            self.protocol = outs['protocol']
        if 'resourceGroupName' in outs:
            self.resource_group_name = outs['resourceGroupName']
        if 'sourceAddressPrefix' in outs:
            self.source_address_prefix = outs['sourceAddressPrefix']
        if 'sourceAddressPrefixes' in outs:
            self.source_address_prefixes = outs['sourceAddressPrefixes']
        if 'sourceApplicationSecurityGroupIds' in outs:
            self.source_application_security_group_ids = outs['sourceApplicationSecurityGroupIds']
        if 'sourcePortRange' in outs:
            self.source_port_range = outs['sourcePortRange']
        if 'sourcePortRanges' in outs:
            self.source_port_ranges = outs['sourcePortRanges']
