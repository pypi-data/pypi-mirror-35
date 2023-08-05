# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import pulumi
import pulumi.runtime

class GlobalAddress(pulumi.CustomResource):
    def __init__(__self__, __name__, __opts__=None, description=None, ip_version=None, name=None, project=None):
        """Create a GlobalAddress resource with the given unique name, props, and options."""
        if not __name__:
            raise TypeError('Missing resource name argument (for URN creation)')
        if not isinstance(__name__, basestring):
            raise TypeError('Expected resource name to be a string')
        if __opts__ and not isinstance(__opts__, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')

        __props__ = dict()

        if description and not isinstance(description, basestring):
            raise TypeError('Expected property description to be a basestring')
        __self__.description = description
        __props__['description'] = description

        if ip_version and not isinstance(ip_version, basestring):
            raise TypeError('Expected property ip_version to be a basestring')
        __self__.ip_version = ip_version
        __props__['ipVersion'] = ip_version

        if name and not isinstance(name, basestring):
            raise TypeError('Expected property name to be a basestring')
        __self__.name = name
        __props__['name'] = name

        if project and not isinstance(project, basestring):
            raise TypeError('Expected property project to be a basestring')
        __self__.project = project
        """
        The ID of the project in which the resource belongs.
        If it is not provided, the provider project is used.
        """
        __props__['project'] = project

        __self__.address = pulumi.runtime.UNKNOWN
        __self__.creation_timestamp = pulumi.runtime.UNKNOWN
        __self__.self_link = pulumi.runtime.UNKNOWN
        """
        The URI of the created resource.
        """

        super(GlobalAddress, __self__).__init__(
            'gcp:compute/globalAddress:GlobalAddress',
            __name__,
            __props__,
            __opts__)

    def set_outputs(self, outs):
        if 'address' in outs:
            self.address = outs['address']
        if 'creationTimestamp' in outs:
            self.creation_timestamp = outs['creationTimestamp']
        if 'description' in outs:
            self.description = outs['description']
        if 'ipVersion' in outs:
            self.ip_version = outs['ipVersion']
        if 'name' in outs:
            self.name = outs['name']
        if 'project' in outs:
            self.project = outs['project']
        if 'selfLink' in outs:
            self.self_link = outs['selfLink']
