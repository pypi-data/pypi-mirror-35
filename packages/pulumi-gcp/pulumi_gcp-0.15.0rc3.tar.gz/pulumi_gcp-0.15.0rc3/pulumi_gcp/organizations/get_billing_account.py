# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import pulumi
import pulumi.runtime

class GetBillingAccountResult(object):
    """
    A collection of values returned by getBillingAccount.
    """
    def __init__(__self__, display_name=None, name=None, open=None, project_ids=None, id=None):
        if display_name and not isinstance(display_name, basestring):
            raise TypeError('Expected argument display_name to be a basestring')
        __self__.display_name = display_name
        if name and not isinstance(name, basestring):
            raise TypeError('Expected argument name to be a basestring')
        __self__.name = name
        """
        The resource name of the billing account in the form `billingAccounts/{billing_account_id}`.
        """
        if open and not isinstance(open, bool):
            raise TypeError('Expected argument open to be a bool')
        __self__.open = open
        if project_ids and not isinstance(project_ids, list):
            raise TypeError('Expected argument project_ids to be a list')
        __self__.project_ids = project_ids
        """
        The IDs of any projects associated with the billing account.
        """
        if id and not isinstance(id, basestring):
            raise TypeError('Expected argument id to be a basestring')
        __self__.id = id
        """
        id is the provider-assigned unique ID for this managed resource.
        """

def get_billing_account(billing_account=None, display_name=None, open=None):
    """
    Use this data source to get information about a Google Billing Account.
    
    ```hcl
    data "google_billing_account" "acct" {
      display_name = "My Billing Account"
      open         = true
    }
    
    resource "google_project" "my_project" {
      name       = "My Project"
      project_id = "your-project-id"
      org_id     = "1234567"
    
      billing_account = "${data.google_billing_account.acct.id}"
    }
    ```
    """
    __args__ = dict()

    __args__['billingAccount'] = billing_account
    __args__['displayName'] = display_name
    __args__['open'] = open
    __ret__ = pulumi.runtime.invoke('gcp:organizations/getBillingAccount:getBillingAccount', __args__)

    return GetBillingAccountResult(
        display_name=__ret__.get('displayName'),
        name=__ret__.get('name'),
        open=__ret__.get('open'),
        project_ids=__ret__.get('projectIds'),
        id=__ret__.get('id'))
