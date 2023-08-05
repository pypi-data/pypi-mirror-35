# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import pulumi
import pulumi.runtime

class Schedule(pulumi.CustomResource):
    """
    Manages a Automation Schedule.
    """
    def __init__(__self__, __name__, __opts__=None, account_name=None, automation_account_name=None, description=None, expiry_time=None, frequency=None, interval=None, name=None, resource_group_name=None, start_time=None, timezone=None):
        """Create a Schedule resource with the given unique name, props, and options."""
        if not __name__:
            raise TypeError('Missing resource name argument (for URN creation)')
        if not isinstance(__name__, basestring):
            raise TypeError('Expected resource name to be a string')
        if __opts__ and not isinstance(__opts__, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')

        __props__ = dict()

        if account_name and not isinstance(account_name, basestring):
            raise TypeError('Expected property account_name to be a basestring')
        __self__.account_name = account_name
        __props__['accountName'] = account_name

        if automation_account_name and not isinstance(automation_account_name, basestring):
            raise TypeError('Expected property automation_account_name to be a basestring')
        __self__.automation_account_name = automation_account_name
        """
        The name of the automation account in which the Schedule is created. Changing this forces a new resource to be created.
        """
        __props__['automationAccountName'] = automation_account_name

        if description and not isinstance(description, basestring):
            raise TypeError('Expected property description to be a basestring')
        __self__.description = description
        """
        A description for this Schedule.
        """
        __props__['description'] = description

        if expiry_time and not isinstance(expiry_time, basestring):
            raise TypeError('Expected property expiry_time to be a basestring')
        __self__.expiry_time = expiry_time
        """
        The end time of the schedule.
        """
        __props__['expiryTime'] = expiry_time

        if not frequency:
            raise TypeError('Missing required property frequency')
        elif not isinstance(frequency, basestring):
            raise TypeError('Expected property frequency to be a basestring')
        __self__.frequency = frequency
        """
        The frequency of the schedule. - can be either `OneTime`, `Day`, `Hour`, `Week`, or `Month`.
        """
        __props__['frequency'] = frequency

        if interval and not isinstance(interval, int):
            raise TypeError('Expected property interval to be a int')
        __self__.interval = interval
        """
        The number of `frequency`s between runs. Only valid for `Day`, `Hour`, `Week`, or `Month` and defaults to `1`.
        """
        __props__['interval'] = interval

        if name and not isinstance(name, basestring):
            raise TypeError('Expected property name to be a basestring')
        __self__.name = name
        """
        Specifies the name of the Schedule. Changing this forces a new resource to be created.
        """
        __props__['name'] = name

        if not resource_group_name:
            raise TypeError('Missing required property resource_group_name')
        elif not isinstance(resource_group_name, basestring):
            raise TypeError('Expected property resource_group_name to be a basestring')
        __self__.resource_group_name = resource_group_name
        """
        The name of the resource group in which the Schedule is created. Changing this forces a new resource to be created.
        """
        __props__['resourceGroupName'] = resource_group_name

        if start_time and not isinstance(start_time, basestring):
            raise TypeError('Expected property start_time to be a basestring')
        __self__.start_time = start_time
        """
        Start time of the schedule. Must be at least five minutes in the future. Defaults to seven minutes in the future from the time the resource is created.
        """
        __props__['startTime'] = start_time

        if timezone and not isinstance(timezone, basestring):
            raise TypeError('Expected property timezone to be a basestring')
        __self__.timezone = timezone
        """
        The timezone of the start time. Defaults to `UTC`. For possible values see: https://msdn.microsoft.com/en-us/library/ms912391(v=winembedded.11).aspx
        """
        __props__['timezone'] = timezone

        super(Schedule, __self__).__init__(
            'azure:automation/schedule:Schedule',
            __name__,
            __props__,
            __opts__)

    def set_outputs(self, outs):
        if 'accountName' in outs:
            self.account_name = outs['accountName']
        if 'automationAccountName' in outs:
            self.automation_account_name = outs['automationAccountName']
        if 'description' in outs:
            self.description = outs['description']
        if 'expiryTime' in outs:
            self.expiry_time = outs['expiryTime']
        if 'frequency' in outs:
            self.frequency = outs['frequency']
        if 'interval' in outs:
            self.interval = outs['interval']
        if 'name' in outs:
            self.name = outs['name']
        if 'resourceGroupName' in outs:
            self.resource_group_name = outs['resourceGroupName']
        if 'startTime' in outs:
            self.start_time = outs['startTime']
        if 'timezone' in outs:
            self.timezone = outs['timezone']
