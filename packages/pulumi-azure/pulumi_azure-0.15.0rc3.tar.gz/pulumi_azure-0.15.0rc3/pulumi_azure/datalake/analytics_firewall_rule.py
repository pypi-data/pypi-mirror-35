# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import pulumi
import pulumi.runtime

class AnalyticsFirewallRule(pulumi.CustomResource):
    """
    Manage a Azure Data Lake Analytics Firewall Rule.
    """
    def __init__(__self__, __name__, __opts__=None, account_name=None, end_ip_address=None, name=None, resource_group_name=None, start_ip_address=None):
        """Create a AnalyticsFirewallRule resource with the given unique name, props, and options."""
        if not __name__:
            raise TypeError('Missing resource name argument (for URN creation)')
        if not isinstance(__name__, basestring):
            raise TypeError('Expected resource name to be a string')
        if __opts__ and not isinstance(__opts__, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')

        __props__ = dict()

        if not account_name:
            raise TypeError('Missing required property account_name')
        elif not isinstance(account_name, basestring):
            raise TypeError('Expected property account_name to be a basestring')
        __self__.account_name = account_name
        """
        Specifies the name of the Data Lake Analytics for which the Firewall Rule should take effect.
        """
        __props__['accountName'] = account_name

        if not end_ip_address:
            raise TypeError('Missing required property end_ip_address')
        elif not isinstance(end_ip_address, basestring):
            raise TypeError('Expected property end_ip_address to be a basestring')
        __self__.end_ip_address = end_ip_address
        """
        The End IP Address for the firewall rule.
        """
        __props__['endIpAddress'] = end_ip_address

        if name and not isinstance(name, basestring):
            raise TypeError('Expected property name to be a basestring')
        __self__.name = name
        """
        Specifies the name of the Data Lake Analytics. Changing this forces a new resource to be created. Has to be between 3 to 24 characters.
        """
        __props__['name'] = name

        if not resource_group_name:
            raise TypeError('Missing required property resource_group_name')
        elif not isinstance(resource_group_name, basestring):
            raise TypeError('Expected property resource_group_name to be a basestring')
        __self__.resource_group_name = resource_group_name
        """
        The name of the resource group in which to create the Data Lake Analytics.
        """
        __props__['resourceGroupName'] = resource_group_name

        if not start_ip_address:
            raise TypeError('Missing required property start_ip_address')
        elif not isinstance(start_ip_address, basestring):
            raise TypeError('Expected property start_ip_address to be a basestring')
        __self__.start_ip_address = start_ip_address
        """
        The Start IP address for the firewall rule.
        """
        __props__['startIpAddress'] = start_ip_address

        super(AnalyticsFirewallRule, __self__).__init__(
            'azure:datalake/analyticsFirewallRule:AnalyticsFirewallRule',
            __name__,
            __props__,
            __opts__)

    def set_outputs(self, outs):
        if 'accountName' in outs:
            self.account_name = outs['accountName']
        if 'endIpAddress' in outs:
            self.end_ip_address = outs['endIpAddress']
        if 'name' in outs:
            self.name = outs['name']
        if 'resourceGroupName' in outs:
            self.resource_group_name = outs['resourceGroupName']
        if 'startIpAddress' in outs:
            self.start_ip_address = outs['startIpAddress']
