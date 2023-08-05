# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import pulumi
import pulumi.runtime

class ActionCustom(pulumi.CustomResource):
    """
    Manages a Custom Action within a Logic App Workflow
    """
    def __init__(__self__, __name__, __opts__=None, body=None, logic_app_id=None, name=None):
        """Create a ActionCustom resource with the given unique name, props, and options."""
        if not __name__:
            raise TypeError('Missing resource name argument (for URN creation)')
        if not isinstance(__name__, basestring):
            raise TypeError('Expected resource name to be a string')
        if __opts__ and not isinstance(__opts__, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')

        __props__ = dict()

        if not body:
            raise TypeError('Missing required property body')
        elif not isinstance(body, basestring):
            raise TypeError('Expected property body to be a basestring')
        __self__.body = body
        """
        Specifies the JSON Blob defining the Body of this Custom Action.
        """
        __props__['body'] = body

        if not logic_app_id:
            raise TypeError('Missing required property logic_app_id')
        elif not isinstance(logic_app_id, basestring):
            raise TypeError('Expected property logic_app_id to be a basestring')
        __self__.logic_app_id = logic_app_id
        """
        Specifies the ID of the Logic App Workflow. Changing this forces a new resource to be created.
        """
        __props__['logicAppId'] = logic_app_id

        if name and not isinstance(name, basestring):
            raise TypeError('Expected property name to be a basestring')
        __self__.name = name
        """
        Specifies the name of the HTTP Action to be created within the Logic App Workflow. Changing this forces a new resource to be created.
        """
        __props__['name'] = name

        super(ActionCustom, __self__).__init__(
            'azure:logicapps/actionCustom:ActionCustom',
            __name__,
            __props__,
            __opts__)

    def set_outputs(self, outs):
        if 'body' in outs:
            self.body = outs['body']
        if 'logicAppId' in outs:
            self.logic_app_id = outs['logicAppId']
        if 'name' in outs:
            self.name = outs['name']
