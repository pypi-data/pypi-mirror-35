# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import pulumi
import pulumi.runtime

class CryptoKey(pulumi.CustomResource):
    """
    Allows creation of a Google Cloud Platform KMS CryptoKey. For more information see
    [the official documentation](https://cloud.google.com/kms/docs/object-hierarchy#cryptokey)
    and
    [API](https://cloud.google.com/kms/docs/reference/rest/v1/projects.locations.keyRings.cryptoKeys).
    
    A CryptoKey is an interface to key material which can be used to encrypt and decrypt data. A CryptoKey belongs to a
    Google Cloud KMS KeyRing.
    
    ~> Note: CryptoKeys cannot be deleted from Google Cloud Platform. Destroying a Terraform-managed CryptoKey will remove it
    from state and delete all CryptoKeyVersions, rendering the key unusable, but **will not delete the resource on the server**.
    """
    def __init__(__self__, __name__, __opts__=None, key_ring=None, name=None, rotation_period=None):
        """Create a CryptoKey resource with the given unique name, props, and options."""
        if not __name__:
            raise TypeError('Missing resource name argument (for URN creation)')
        if not isinstance(__name__, basestring):
            raise TypeError('Expected resource name to be a string')
        if __opts__ and not isinstance(__opts__, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')

        __props__ = dict()

        if not key_ring:
            raise TypeError('Missing required property key_ring')
        elif not isinstance(key_ring, basestring):
            raise TypeError('Expected property key_ring to be a basestring')
        __self__.key_ring = key_ring
        """
        The id of the Google Cloud Platform KeyRing to which the key shall belong.
        """
        __props__['keyRing'] = key_ring

        if name and not isinstance(name, basestring):
            raise TypeError('Expected property name to be a basestring')
        __self__.name = name
        """
        The CryptoKey's name.
        A CryptoKey’s name must be unique within a location and match the regular expression `[a-zA-Z0-9_-]{1,63}`
        """
        __props__['name'] = name

        if rotation_period and not isinstance(rotation_period, basestring):
            raise TypeError('Expected property rotation_period to be a basestring')
        __self__.rotation_period = rotation_period
        """
        Every time this period passes, generate a new CryptoKeyVersion and set it as
        the primary. The first rotation will take place after the specified period. The rotation period has the format
        of a decimal number with up to 9 fractional digits, followed by the letter s (seconds). It must be greater than
        a day (ie, 83400).
        """
        __props__['rotationPeriod'] = rotation_period

        super(CryptoKey, __self__).__init__(
            'gcp:kms/cryptoKey:CryptoKey',
            __name__,
            __props__,
            __opts__)

    def set_outputs(self, outs):
        if 'keyRing' in outs:
            self.key_ring = outs['keyRing']
        if 'name' in outs:
            self.name = outs['name']
        if 'rotationPeriod' in outs:
            self.rotation_period = outs['rotationPeriod']
