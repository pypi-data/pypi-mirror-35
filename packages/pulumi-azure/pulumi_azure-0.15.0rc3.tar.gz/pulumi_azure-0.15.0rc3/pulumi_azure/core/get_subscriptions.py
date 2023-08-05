# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import pulumi
import pulumi.runtime

class GetSubscriptionsResult(object):
    """
    A collection of values returned by getSubscriptions.
    """
    def __init__(__self__, subscriptions=None, id=None):
        if subscriptions and not isinstance(subscriptions, list):
            raise TypeError('Expected argument subscriptions to be a list')
        __self__.subscriptions = subscriptions
        """
        One or more `subscription` blocks as defined below.
        """
        if id and not isinstance(id, basestring):
            raise TypeError('Expected argument id to be a basestring')
        __self__.id = id
        """
        id is the provider-assigned unique ID for this managed resource.
        """

def get_subscriptions():
    """
    Use this data source to access a list of all Azure subscriptions currently available.
    """
    __args__ = dict()

    __ret__ = pulumi.runtime.invoke('azure:core/getSubscriptions:getSubscriptions', __args__)

    return GetSubscriptionsResult(
        subscriptions=__ret__.get('subscriptions'),
        id=__ret__.get('id'))
