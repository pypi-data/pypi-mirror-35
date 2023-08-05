# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import pulumi
import pulumi.runtime

class AnalyticsAccount(pulumi.CustomResource):
    """
    Manage an Azure Data Lake Analytics Account.
    """
    def __init__(__self__, __name__, __opts__=None, default_store_account_name=None, location=None, name=None, resource_group_name=None, tags=None, tier=None):
        """Create a AnalyticsAccount resource with the given unique name, props, and options."""
        if not __name__:
            raise TypeError('Missing resource name argument (for URN creation)')
        if not isinstance(__name__, basestring):
            raise TypeError('Expected resource name to be a string')
        if __opts__ and not isinstance(__opts__, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')

        __props__ = dict()

        if not default_store_account_name:
            raise TypeError('Missing required property default_store_account_name')
        elif not isinstance(default_store_account_name, basestring):
            raise TypeError('Expected property default_store_account_name to be a basestring')
        __self__.default_store_account_name = default_store_account_name
        """
        Specifies the data lake store to use by default. Changing this forces a new resource to be created.
        """
        __props__['defaultStoreAccountName'] = default_store_account_name

        if not location:
            raise TypeError('Missing required property location')
        elif not isinstance(location, basestring):
            raise TypeError('Expected property location to be a basestring')
        __self__.location = location
        """
        Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.
        """
        __props__['location'] = location

        if name and not isinstance(name, basestring):
            raise TypeError('Expected property name to be a basestring')
        __self__.name = name
        """
        Specifies the name of the Data Lake Analytics Account. Changing this forces a new resource to be created. Has to be between 3 to 24 characters.
        """
        __props__['name'] = name

        if not resource_group_name:
            raise TypeError('Missing required property resource_group_name')
        elif not isinstance(resource_group_name, basestring):
            raise TypeError('Expected property resource_group_name to be a basestring')
        __self__.resource_group_name = resource_group_name
        """
        The name of the resource group in which to create the Data Lake Analytics Account.
        """
        __props__['resourceGroupName'] = resource_group_name

        if tags and not isinstance(tags, dict):
            raise TypeError('Expected property tags to be a dict')
        __self__.tags = tags
        """
        A mapping of tags to assign to the resource.
        """
        __props__['tags'] = tags

        if tier and not isinstance(tier, basestring):
            raise TypeError('Expected property tier to be a basestring')
        __self__.tier = tier
        """
        The monthly commitment tier for Data Lake Analytics Account. Accepted values are `Consumption`, `Commitment_100000AUHours`, `Commitment_10000AUHours`, `Commitment_1000AUHours`, `Commitment_100AUHours`, `Commitment_500000AUHours`, `Commitment_50000AUHours`, `Commitment_5000AUHours`, or `Commitment_500AUHours`.
        """
        __props__['tier'] = tier

        super(AnalyticsAccount, __self__).__init__(
            'azure:datalake/analyticsAccount:AnalyticsAccount',
            __name__,
            __props__,
            __opts__)

    def set_outputs(self, outs):
        if 'defaultStoreAccountName' in outs:
            self.default_store_account_name = outs['defaultStoreAccountName']
        if 'location' in outs:
            self.location = outs['location']
        if 'name' in outs:
            self.name = outs['name']
        if 'resourceGroupName' in outs:
            self.resource_group_name = outs['resourceGroupName']
        if 'tags' in outs:
            self.tags = outs['tags']
        if 'tier' in outs:
            self.tier = outs['tier']
