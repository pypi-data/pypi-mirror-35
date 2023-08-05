# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import pulumi
import pulumi.runtime

class Image(pulumi.CustomResource):
    """
    Creates a bootable VM image resource for Google Compute Engine from an existing
    tarball. For more information see [the official documentation](https://cloud.google.com/compute/docs/images) and
    [API](https://cloud.google.com/compute/docs/reference/latest/images).
    
    """
    def __init__(__self__, __name__, __opts__=None, create_timeout=None, description=None, family=None, labels=None, licenses=None, name=None, project=None, raw_disk=None, source_disk=None):
        """Create a Image resource with the given unique name, props, and options."""
        if not __name__:
            raise TypeError('Missing resource name argument (for URN creation)')
        if not isinstance(__name__, basestring):
            raise TypeError('Expected resource name to be a string')
        if __opts__ and not isinstance(__opts__, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')

        __props__ = dict()

        if create_timeout and not isinstance(create_timeout, int):
            raise TypeError('Expected property create_timeout to be a int')
        __self__.create_timeout = create_timeout
        """
        Configurable timeout in minutes for creating images. Default is 4 minutes.
        """
        __props__['createTimeout'] = create_timeout

        if description and not isinstance(description, basestring):
            raise TypeError('Expected property description to be a basestring')
        __self__.description = description
        """
        The description of the image to be created
        """
        __props__['description'] = description

        if family and not isinstance(family, basestring):
            raise TypeError('Expected property family to be a basestring')
        __self__.family = family
        """
        The name of the image family to which this image belongs.
        """
        __props__['family'] = family

        if labels and not isinstance(labels, dict):
            raise TypeError('Expected property labels to be a dict')
        __self__.labels = labels
        """
        A set of key/value label pairs to assign to the image.
        """
        __props__['labels'] = labels

        if licenses and not isinstance(licenses, list):
            raise TypeError('Expected property licenses to be a list')
        __self__.licenses = licenses
        """
        A list of license URIs to apply to this image. Changing this
        forces a new resource to be created.
        """
        __props__['licenses'] = licenses

        if name and not isinstance(name, basestring):
            raise TypeError('Expected property name to be a basestring')
        __self__.name = name
        """
        A unique name for the resource, required by GCE.
        Changing this forces a new resource to be created.
        """
        __props__['name'] = name

        if project and not isinstance(project, basestring):
            raise TypeError('Expected property project to be a basestring')
        __self__.project = project
        """
        The ID of the project in which the resource belongs. If it
        is not provided, the provider project is used.
        """
        __props__['project'] = project

        if raw_disk and not isinstance(raw_disk, dict):
            raise TypeError('Expected property raw_disk to be a dict')
        __self__.raw_disk = raw_disk
        """
        The raw disk that will be used as the source of the image.
        Changing this forces a new resource to be created. Structure is documented
        below.
        """
        __props__['rawDisk'] = raw_disk

        if source_disk and not isinstance(source_disk, basestring):
            raise TypeError('Expected property source_disk to be a basestring')
        __self__.source_disk = source_disk
        """
        The URL of a disk that will be used as the source of the
        image. Changing this forces a new resource to be created.
        """
        __props__['sourceDisk'] = source_disk

        __self__.label_fingerprint = pulumi.runtime.UNKNOWN
        """
        The fingerprint of the assigned labels.
        """
        __self__.self_link = pulumi.runtime.UNKNOWN
        """
        The URI of the created resource.
        """

        super(Image, __self__).__init__(
            'gcp:compute/image:Image',
            __name__,
            __props__,
            __opts__)

    def set_outputs(self, outs):
        if 'createTimeout' in outs:
            self.create_timeout = outs['createTimeout']
        if 'description' in outs:
            self.description = outs['description']
        if 'family' in outs:
            self.family = outs['family']
        if 'labelFingerprint' in outs:
            self.label_fingerprint = outs['labelFingerprint']
        if 'labels' in outs:
            self.labels = outs['labels']
        if 'licenses' in outs:
            self.licenses = outs['licenses']
        if 'name' in outs:
            self.name = outs['name']
        if 'project' in outs:
            self.project = outs['project']
        if 'rawDisk' in outs:
            self.raw_disk = outs['rawDisk']
        if 'selfLink' in outs:
            self.self_link = outs['selfLink']
        if 'sourceDisk' in outs:
            self.source_disk = outs['sourceDisk']
