# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import pulumi
import pulumi.runtime

class GetJobCollectionResult(object):
    """
    A collection of values returned by getJobCollection.
    """
    def __init__(__self__, location=None, quotas=None, sku=None, state=None, tags=None, id=None):
        if location and not isinstance(location, basestring):
            raise TypeError('Expected argument location to be a basestring')
        __self__.location = location
        """
        The Azure location where the resource exists. 
        """
        if quotas and not isinstance(quotas, list):
            raise TypeError('Expected argument quotas to be a list')
        __self__.quotas = quotas
        """
        The Job collection quotas as documented in the `quota` block below. 
        """
        if sku and not isinstance(sku, basestring):
            raise TypeError('Expected argument sku to be a basestring')
        __self__.sku = sku
        """
        The Job Collection's pricing level's SKU. 
        """
        if state and not isinstance(state, basestring):
            raise TypeError('Expected argument state to be a basestring')
        __self__.state = state
        """
        The Job Collection's state. 
        """
        if tags and not isinstance(tags, dict):
            raise TypeError('Expected argument tags to be a dict')
        __self__.tags = tags
        """
        A mapping of tags assigned to the resource.
        """
        if id and not isinstance(id, basestring):
            raise TypeError('Expected argument id to be a basestring')
        __self__.id = id
        """
        id is the provider-assigned unique ID for this managed resource.
        """

def get_job_collection(name=None, resource_group_name=None):
    """
    Use this data source to access the properties of an Azure scheduler job collection.
    """
    __args__ = dict()

    __args__['name'] = name
    __args__['resourceGroupName'] = resource_group_name
    __ret__ = pulumi.runtime.invoke('azure:scheduler/getJobCollection:getJobCollection', __args__)

    return GetJobCollectionResult(
        location=__ret__.get('location'),
        quotas=__ret__.get('quotas'),
        sku=__ret__.get('sku'),
        state=__ret__.get('state'),
        tags=__ret__.get('tags'),
        id=__ret__.get('id'))
