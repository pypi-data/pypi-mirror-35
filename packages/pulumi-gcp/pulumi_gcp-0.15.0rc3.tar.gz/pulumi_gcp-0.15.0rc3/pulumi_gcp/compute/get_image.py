# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import pulumi
import pulumi.runtime

class GetImageResult(object):
    """
    A collection of values returned by getImage.
    """
    def __init__(__self__, archive_size_bytes=None, creation_timestamp=None, description=None, disk_size_gb=None, family=None, image_encryption_key_sha256=None, image_id=None, label_fingerprint=None, labels=None, licenses=None, name=None, project=None, self_link=None, source_disk=None, source_disk_encryption_key_sha256=None, source_disk_id=None, source_image_id=None, status=None, id=None):
        if archive_size_bytes and not isinstance(archive_size_bytes, int):
            raise TypeError('Expected argument archive_size_bytes to be a int')
        __self__.archive_size_bytes = archive_size_bytes
        """
        The size of the image tar.gz archive stored in Google Cloud Storage in bytes.
        """
        if creation_timestamp and not isinstance(creation_timestamp, basestring):
            raise TypeError('Expected argument creation_timestamp to be a basestring')
        __self__.creation_timestamp = creation_timestamp
        """
        The creation timestamp in RFC3339 text format.
        """
        if description and not isinstance(description, basestring):
            raise TypeError('Expected argument description to be a basestring')
        __self__.description = description
        """
        An optional description of this image.
        """
        if disk_size_gb and not isinstance(disk_size_gb, int):
            raise TypeError('Expected argument disk_size_gb to be a int')
        __self__.disk_size_gb = disk_size_gb
        """
        The size of the image when restored onto a persistent disk in gigabytes.
        """
        if family and not isinstance(family, basestring):
            raise TypeError('Expected argument family to be a basestring')
        __self__.family = family
        """
        The family name of the image.
        """
        if image_encryption_key_sha256 and not isinstance(image_encryption_key_sha256, basestring):
            raise TypeError('Expected argument image_encryption_key_sha256 to be a basestring')
        __self__.image_encryption_key_sha256 = image_encryption_key_sha256
        """
        The [RFC 4648 base64](https://tools.ietf.org/html/rfc4648#section-4)
        encoded SHA-256 hash of the [customer-supplied encryption key](https://cloud.google.com/compute/docs/disks/customer-supplied-encryption)
        that protects this image.
        """
        if image_id and not isinstance(image_id, basestring):
            raise TypeError('Expected argument image_id to be a basestring')
        __self__.image_id = image_id
        """
        The unique identifier for the image.
        """
        if label_fingerprint and not isinstance(label_fingerprint, basestring):
            raise TypeError('Expected argument label_fingerprint to be a basestring')
        __self__.label_fingerprint = label_fingerprint
        """
        A fingerprint for the labels being applied to this image.
        """
        if labels and not isinstance(labels, dict):
            raise TypeError('Expected argument labels to be a dict')
        __self__.labels = labels
        """
        A map of labels applied to this image.
        """
        if licenses and not isinstance(licenses, list):
            raise TypeError('Expected argument licenses to be a list')
        __self__.licenses = licenses
        """
        A list of applicable license URI.
        """
        if name and not isinstance(name, basestring):
            raise TypeError('Expected argument name to be a basestring')
        __self__.name = name
        """
        The name of the image.
        """
        if project and not isinstance(project, basestring):
            raise TypeError('Expected argument project to be a basestring')
        __self__.project = project
        if self_link and not isinstance(self_link, basestring):
            raise TypeError('Expected argument self_link to be a basestring')
        __self__.self_link = self_link
        """
        The URI of the image.
        """
        if source_disk and not isinstance(source_disk, basestring):
            raise TypeError('Expected argument source_disk to be a basestring')
        __self__.source_disk = source_disk
        """
        The URL of the source disk used to create this image.
        """
        if source_disk_encryption_key_sha256 and not isinstance(source_disk_encryption_key_sha256, basestring):
            raise TypeError('Expected argument source_disk_encryption_key_sha256 to be a basestring')
        __self__.source_disk_encryption_key_sha256 = source_disk_encryption_key_sha256
        """
        The [RFC 4648 base64](https://tools.ietf.org/html/rfc4648#section-4)
        encoded SHA-256 hash of the [customer-supplied encryption key](https://cloud.google.com/compute/docs/disks/customer-supplied-encryption)
        that protects this image.
        """
        if source_disk_id and not isinstance(source_disk_id, basestring):
            raise TypeError('Expected argument source_disk_id to be a basestring')
        __self__.source_disk_id = source_disk_id
        """
        The ID value of the disk used to create this image.
        """
        if source_image_id and not isinstance(source_image_id, basestring):
            raise TypeError('Expected argument source_image_id to be a basestring')
        __self__.source_image_id = source_image_id
        """
        The ID value of the image used to create this image.
        """
        if status and not isinstance(status, basestring):
            raise TypeError('Expected argument status to be a basestring')
        __self__.status = status
        """
        The status of the image. Possible values are **FAILED**, **PENDING**, or **READY**.
        """
        if id and not isinstance(id, basestring):
            raise TypeError('Expected argument id to be a basestring')
        __self__.id = id
        """
        id is the provider-assigned unique ID for this managed resource.
        """

def get_image(family=None, name=None, project=None):
    """
    Get information about a Google Compute Image. Check that your service account has the `compute.imageUser` role if you want to share [custom images](https://cloud.google.com/compute/docs/images/sharing-images-across-projects) from another project. If you want to use [public images][pubimg], do not forget to specify the dedicated project. For more information see
    [the official documentation](https://cloud.google.com/compute/docs/images) and its [API](https://cloud.google.com/compute/docs/reference/latest/images).
    """
    __args__ = dict()

    __args__['family'] = family
    __args__['name'] = name
    __args__['project'] = project
    __ret__ = pulumi.runtime.invoke('gcp:compute/getImage:getImage', __args__)

    return GetImageResult(
        archive_size_bytes=__ret__.get('archiveSizeBytes'),
        creation_timestamp=__ret__.get('creationTimestamp'),
        description=__ret__.get('description'),
        disk_size_gb=__ret__.get('diskSizeGb'),
        family=__ret__.get('family'),
        image_encryption_key_sha256=__ret__.get('imageEncryptionKeySha256'),
        image_id=__ret__.get('imageId'),
        label_fingerprint=__ret__.get('labelFingerprint'),
        labels=__ret__.get('labels'),
        licenses=__ret__.get('licenses'),
        name=__ret__.get('name'),
        project=__ret__.get('project'),
        self_link=__ret__.get('selfLink'),
        source_disk=__ret__.get('sourceDisk'),
        source_disk_encryption_key_sha256=__ret__.get('sourceDiskEncryptionKeySha256'),
        source_disk_id=__ret__.get('sourceDiskId'),
        source_image_id=__ret__.get('sourceImageId'),
        status=__ret__.get('status'),
        id=__ret__.get('id'))
