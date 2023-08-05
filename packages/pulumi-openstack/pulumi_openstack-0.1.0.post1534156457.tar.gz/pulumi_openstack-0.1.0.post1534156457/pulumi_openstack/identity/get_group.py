# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import pulumi
import pulumi.runtime

class GetGroupResult(object):
    """
    A collection of values returned by getGroup.
    """
    def __init__(__self__, domain_id=None, region=None, id=None):
        if domain_id and not isinstance(domain_id, basestring):
            raise TypeError('Expected argument domain_id to be a basestring')
        __self__.domain_id = domain_id
        """
        See Argument Reference above.
        """
        if region and not isinstance(region, basestring):
            raise TypeError('Expected argument region to be a basestring')
        __self__.region = region
        """
        See Argument Reference above.
        """
        if id and not isinstance(id, basestring):
            raise TypeError('Expected argument id to be a basestring')
        __self__.id = id
        """
        id is the provider-assigned unique ID for this managed resource.
        """

def get_group(domain_id=None, name=None, region=None):
    """
    Use this data source to get the ID of an OpenStack group.
    
    Note: This usually requires admin privileges.
    """
    __args__ = dict()

    __args__['domainId'] = domain_id
    __args__['name'] = name
    __args__['region'] = region
    __ret__ = pulumi.runtime.invoke('openstack:identity/getGroup:getGroup', __args__)

    return GetGroupResult(
        domain_id=__ret__.get('domainId'),
        region=__ret__.get('region'),
        id=__ret__.get('id'))
