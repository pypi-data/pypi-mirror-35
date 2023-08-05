# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import pulumi
import pulumi.runtime

class Trigger(pulumi.CustomResource):
    """
    Creates a new build trigger within GCR. For more information, see
    [the official documentation](https://cloud.google.com/container-builder/docs/running-builds/automate-builds)
    and
    [API](https://godoc.org/google.golang.org/api/cloudbuild/v1#BuildTrigger).
    """
    def __init__(__self__, __name__, __opts__=None, build=None, description=None, filename=None, project=None, trigger_template=None):
        """Create a Trigger resource with the given unique name, props, and options."""
        if not __name__:
            raise TypeError('Missing resource name argument (for URN creation)')
        if not isinstance(__name__, basestring):
            raise TypeError('Expected resource name to be a string')
        if __opts__ and not isinstance(__opts__, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')

        __props__ = dict()

        if build and not isinstance(build, dict):
            raise TypeError('Expected property build to be a dict')
        __self__.build = build
        """
        A build resource in the Container Builder API.
        Structure is documented below. At a high
        level, a `build` describes where to find source code, how to build it (for
        example, the builder image to run on the source), and where to store
        the built artifacts. Fields can include the following variables, which
        will be expanded when the build is created:
        * `$PROJECT_ID`: the project ID of the build.
        * `$BUILD_ID`: the autogenerated ID of the build.
        * `$REPO_NAME`: the source repository name specified by RepoSource.
        * `$BRANCH_NAME`: the branch name specified by RepoSource.
        * `$TAG_NAME`: the tag name specified by RepoSource.
        * `$REVISION_ID` or `$COMMIT_SHA`: the commit SHA specified by RepoSource
        or resolved from the specified branch or tag.
        * `$SHORT_SHA`: first 7 characters of `$REVISION_ID` or `$COMMIT_SHA`.
        """
        __props__['build'] = build

        if description and not isinstance(description, basestring):
            raise TypeError('Expected property description to be a basestring')
        __self__.description = description
        """
        A brief description of this resource.
        """
        __props__['description'] = description

        if filename and not isinstance(filename, basestring):
            raise TypeError('Expected property filename to be a basestring')
        __self__.filename = filename
        """
        Specify the path to a Cloud Build configuration file
        in the Git repo. This is mutually exclusive with `build`. This is typically
        `cloudbuild.yaml` however it can be specified by the user.
        """
        __props__['filename'] = filename

        if project and not isinstance(project, basestring):
            raise TypeError('Expected property project to be a basestring')
        __self__.project = project
        """
        ID of the project that owns the Cloud Source Repository.
        """
        __props__['project'] = project

        if trigger_template and not isinstance(trigger_template, dict):
            raise TypeError('Expected property trigger_template to be a dict')
        __self__.trigger_template = trigger_template
        """
        Location of the source in a Google
        Cloud Source Repository. Structure is documented below.
        """
        __props__['triggerTemplate'] = trigger_template

        super(Trigger, __self__).__init__(
            'gcp:cloudbuild/trigger:Trigger',
            __name__,
            __props__,
            __opts__)

    def set_outputs(self, outs):
        if 'build' in outs:
            self.build = outs['build']
        if 'description' in outs:
            self.description = outs['description']
        if 'filename' in outs:
            self.filename = outs['filename']
        if 'project' in outs:
            self.project = outs['project']
        if 'triggerTemplate' in outs:
            self.trigger_template = outs['triggerTemplate']
