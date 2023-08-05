# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import pulumi
import pulumi.runtime

class IAMBinding(pulumi.CustomResource):
    """
    Allows creation and management of a single binding within IAM policy for
    an existing Google Cloud Platform folder.
    
    ~> **Note:** This resource _must not_ be used in conjunction with
       `google_folder_iam_policy` or they will fight over what your policy
       should be.
    """
    def __init__(__self__, __name__, __opts__=None, folder=None, members=None, role=None):
        """Create a IAMBinding resource with the given unique name, props, and options."""
        if not __name__:
            raise TypeError('Missing resource name argument (for URN creation)')
        if not isinstance(__name__, basestring):
            raise TypeError('Expected resource name to be a string')
        if __opts__ and not isinstance(__opts__, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')

        __props__ = dict()

        if not folder:
            raise TypeError('Missing required property folder')
        elif not isinstance(folder, basestring):
            raise TypeError('Expected property folder to be a basestring')
        __self__.folder = folder
        """
        The resource name of the folder the policy is attached to. Its format is folders/{folder_id}.
        """
        __props__['folder'] = folder

        if not members:
            raise TypeError('Missing required property members')
        elif not isinstance(members, list):
            raise TypeError('Expected property members to be a list')
        __self__.members = members
        """
        An array of identites that will be granted the privilege in the `role`.
        Each entry can have one of the following values:
        * **user:{emailid}**: An email address that represents a specific Google account. For example, alice@gmail.com or joe@example.com.
        * **serviceAccount:{emailid}**: An email address that represents a service account. For example, my-other-app@appspot.gserviceaccount.com.
        * **group:{emailid}**: An email address that represents a Google group. For example, admins@example.com.
        * **domain:{domain}**: A Google Apps domain name that represents all the users of that domain. For example, google.com or example.com.
        """
        __props__['members'] = members

        if not role:
            raise TypeError('Missing required property role')
        elif not isinstance(role, basestring):
            raise TypeError('Expected property role to be a basestring')
        __self__.role = role
        """
        The role that should be applied. Only one
        `google_folder_iam_binding` can be used per role. Note that custom roles must be of the format
        `[projects|organizations]/{parent-name}/roles/{role-name}`.
        """
        __props__['role'] = role

        __self__.etag = pulumi.runtime.UNKNOWN
        """
        (Computed) The etag of the folder's IAM policy.
        """

        super(IAMBinding, __self__).__init__(
            'gcp:folder/iAMBinding:IAMBinding',
            __name__,
            __props__,
            __opts__)

    def set_outputs(self, outs):
        if 'etag' in outs:
            self.etag = outs['etag']
        if 'folder' in outs:
            self.folder = outs['folder']
        if 'members' in outs:
            self.members = outs['members']
        if 'role' in outs:
            self.role = outs['role']
