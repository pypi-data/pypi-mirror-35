# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import pulumi
import pulumi.runtime

class Subnetwork(pulumi.CustomResource):
    def __init__(__self__, __name__, __opts__=None, description=None, enable_flow_logs=None, ip_cidr_range=None, name=None, network=None, private_ip_google_access=None, project=None, region=None, secondary_ip_ranges=None):
        """Create a Subnetwork resource with the given unique name, props, and options."""
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

        if enable_flow_logs and not isinstance(enable_flow_logs, bool):
            raise TypeError('Expected property enable_flow_logs to be a bool')
        __self__.enable_flow_logs = enable_flow_logs
        __props__['enableFlowLogs'] = enable_flow_logs

        if not ip_cidr_range:
            raise TypeError('Missing required property ip_cidr_range')
        elif not isinstance(ip_cidr_range, basestring):
            raise TypeError('Expected property ip_cidr_range to be a basestring')
        __self__.ip_cidr_range = ip_cidr_range
        __props__['ipCidrRange'] = ip_cidr_range

        if name and not isinstance(name, basestring):
            raise TypeError('Expected property name to be a basestring')
        __self__.name = name
        __props__['name'] = name

        if not network:
            raise TypeError('Missing required property network')
        elif not isinstance(network, basestring):
            raise TypeError('Expected property network to be a basestring')
        __self__.network = network
        __props__['network'] = network

        if private_ip_google_access and not isinstance(private_ip_google_access, bool):
            raise TypeError('Expected property private_ip_google_access to be a bool')
        __self__.private_ip_google_access = private_ip_google_access
        __props__['privateIpGoogleAccess'] = private_ip_google_access

        if project and not isinstance(project, basestring):
            raise TypeError('Expected property project to be a basestring')
        __self__.project = project
        """
        The ID of the project in which the resource belongs.
        If it is not provided, the provider project is used.
        """
        __props__['project'] = project

        if region and not isinstance(region, basestring):
            raise TypeError('Expected property region to be a basestring')
        __self__.region = region
        __props__['region'] = region

        if secondary_ip_ranges and not isinstance(secondary_ip_ranges, list):
            raise TypeError('Expected property secondary_ip_ranges to be a list')
        __self__.secondary_ip_ranges = secondary_ip_ranges
        __props__['secondaryIpRanges'] = secondary_ip_ranges

        __self__.creation_timestamp = pulumi.runtime.UNKNOWN
        __self__.fingerprint = pulumi.runtime.UNKNOWN
        __self__.gateway_address = pulumi.runtime.UNKNOWN
        __self__.self_link = pulumi.runtime.UNKNOWN
        """
        The URI of the created resource.
        """

        super(Subnetwork, __self__).__init__(
            'gcp:compute/subnetwork:Subnetwork',
            __name__,
            __props__,
            __opts__)

    def set_outputs(self, outs):
        if 'creationTimestamp' in outs:
            self.creation_timestamp = outs['creationTimestamp']
        if 'description' in outs:
            self.description = outs['description']
        if 'enableFlowLogs' in outs:
            self.enable_flow_logs = outs['enableFlowLogs']
        if 'fingerprint' in outs:
            self.fingerprint = outs['fingerprint']
        if 'gatewayAddress' in outs:
            self.gateway_address = outs['gatewayAddress']
        if 'ipCidrRange' in outs:
            self.ip_cidr_range = outs['ipCidrRange']
        if 'name' in outs:
            self.name = outs['name']
        if 'network' in outs:
            self.network = outs['network']
        if 'privateIpGoogleAccess' in outs:
            self.private_ip_google_access = outs['privateIpGoogleAccess']
        if 'project' in outs:
            self.project = outs['project']
        if 'region' in outs:
            self.region = outs['region']
        if 'secondaryIpRanges' in outs:
            self.secondary_ip_ranges = outs['secondaryIpRanges']
        if 'selfLink' in outs:
            self.self_link = outs['selfLink']
