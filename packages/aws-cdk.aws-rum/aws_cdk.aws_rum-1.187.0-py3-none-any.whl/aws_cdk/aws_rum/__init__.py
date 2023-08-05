'''
# AWS::RUM Construct Library

<!--BEGIN STABILITY BANNER-->---


![cfn-resources: Stable](https://img.shields.io/badge/cfn--resources-stable-success.svg?style=for-the-badge)

> All classes with the `Cfn` prefix in this module ([CFN Resources](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) are always stable and safe to use.

---
<!--END STABILITY BANNER-->

This module is part of the [AWS Cloud Development Kit](https://github.com/aws/aws-cdk) project.

```python
import aws_cdk.aws_rum as rum
```

<!--BEGIN CFNONLY DISCLAIMER-->

There are no official hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet. Here are some suggestions on how to proceed:

* Search [Construct Hub for RUM construct libraries](https://constructs.dev/search?q=rum)
* Use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, in the same way you would use [the CloudFormation AWS::RUM resources](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_RUM.html) directly.

<!--BEGIN CFNONLY DISCLAIMER-->

There are no hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet.
However, you can still use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, and use this service exactly as you would using CloudFormation directly.

For more information on the resources and properties available for this service, see the [CloudFormation documentation for AWS::RUM](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_RUM.html).

(Read the [CDK Contributing Guide](https://github.com/aws/aws-cdk/blob/master/CONTRIBUTING.md) and submit an RFC if you are interested in contributing to this construct library.)

<!--END CFNONLY DISCLAIMER-->
'''
import abc
import builtins
import datetime
import enum
import typing

import jsii
import publication
import typing_extensions

from typeguard import check_type

from ._jsii import *

import aws_cdk.core as _aws_cdk_core_f4b25747


@jsii.implements(_aws_cdk_core_f4b25747.IInspectable)
class CfnAppMonitor(
    _aws_cdk_core_f4b25747.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/aws-rum.CfnAppMonitor",
):
    '''A CloudFormation ``AWS::RUM::AppMonitor``.

    Creates a CloudWatch RUM app monitor, which you can use to collect telemetry data from your application and send it to CloudWatch RUM. The data includes performance and reliability information such as page load time, client-side errors, and user behavior.

    After you create an app monitor, sign in to the CloudWatch RUM console to get the JavaScript code snippet to add to your web application. For more information, see `How do I find a code snippet that I've already generated? <https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-RUM-find-code-snippet.html>`_

    :cloudformationResource: AWS::RUM::AppMonitor
    :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rum-appmonitor.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        import aws_cdk.aws_rum as rum
        
        cfn_app_monitor = rum.CfnAppMonitor(self, "MyCfnAppMonitor",
            domain="domain",
            name="name",
        
            # the properties below are optional
            app_monitor_configuration=rum.CfnAppMonitor.AppMonitorConfigurationProperty(
                allow_cookies=False,
                enable_xRay=False,
                excluded_pages=["excludedPages"],
                favorite_pages=["favoritePages"],
                guest_role_arn="guestRoleArn",
                identity_pool_id="identityPoolId",
                included_pages=["includedPages"],
                metric_destinations=[rum.CfnAppMonitor.MetricDestinationProperty(
                    destination="destination",
        
                    # the properties below are optional
                    destination_arn="destinationArn",
                    iam_role_arn="iamRoleArn",
                    metric_definitions=[rum.CfnAppMonitor.MetricDefinitionProperty(
                        name="name",
        
                        # the properties below are optional
                        dimension_keys={
                            "dimension_keys_key": "dimensionKeys"
                        },
                        event_pattern="eventPattern",
                        unit_label="unitLabel",
                        value_key="valueKey"
                    )]
                )],
                session_sample_rate=123,
                telemetries=["telemetries"]
            ),
            cw_log_enabled=False,
            tags=[CfnTag(
                key="key",
                value="value"
            )]
        )
    '''

    def __init__(
        self,
        scope: _aws_cdk_core_f4b25747.Construct,
        id: builtins.str,
        *,
        domain: builtins.str,
        name: builtins.str,
        app_monitor_configuration: typing.Optional[typing.Union[typing.Union["CfnAppMonitor.AppMonitorConfigurationProperty", typing.Dict[builtins.str, typing.Any]], _aws_cdk_core_f4b25747.IResolvable]] = None,
        cw_log_enabled: typing.Optional[typing.Union[builtins.bool, _aws_cdk_core_f4b25747.IResolvable]] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_aws_cdk_core_f4b25747.CfnTag, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Create a new ``AWS::RUM::AppMonitor``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param domain: The top-level internet domain name for which your application has administrative authority. This parameter is required.
        :param name: A name for the app monitor. This parameter is required.
        :param app_monitor_configuration: A structure that contains much of the configuration data for the app monitor. If you are using Amazon Cognito for authorization, you must include this structure in your request, and it must include the ID of the Amazon Cognito identity pool to use for authorization. If you don't include ``AppMonitorConfiguration`` , you must set up your own authorization method. For more information, see `Authorize your application to send data to AWS <https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-RUM-get-started-authorization.html>`_ . If you omit this argument, the sample rate used for CloudWatch RUM is set to 10% of the user sessions.
        :param cw_log_enabled: Data collected by CloudWatch RUM is kept by RUM for 30 days and then deleted. This parameter specifies whether CloudWatch RUM sends a copy of this telemetry data to Amazon CloudWatch Logs in your account. This enables you to keep the telemetry data for more than 30 days, but it does incur Amazon CloudWatch Logs charges. If you omit this parameter, the default is ``false`` .
        :param tags: Assigns one or more tags (key-value pairs) to the app monitor. Tags can help you organize and categorize your resources. You can also use them to scope user permissions by granting a user permission to access or change only resources with certain tag values. Tags don't have any semantic meaning to AWS and are interpreted strictly as strings of characters. You can associate as many as 50 tags with an app monitor. For more information, see `Tagging AWS resources <https://docs.aws.amazon.com/general/latest/gr/aws_tagging.html>`_ .
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e4386a295d4af768eba5a9e5bbd1d1a922974f369e6c77a4d88d61ac86ee2db9)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnAppMonitorProps(
            domain=domain,
            name=name,
            app_monitor_configuration=app_monitor_configuration,
            cw_log_enabled=cw_log_enabled,
            tags=tags,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _aws_cdk_core_f4b25747.TreeInspector) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: - tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ccf08c4bb8358cb8bb84404f01c6b7914b25820b68d6607d900c269f204486b1)
            check_type(argname="argument inspector", value=inspector, expected_type=type_hints["inspector"])
        return typing.cast(None, jsii.invoke(self, "inspect", [inspector]))

    @jsii.member(jsii_name="renderProperties")
    def _render_properties(
        self,
        props: typing.Mapping[builtins.str, typing.Any],
    ) -> typing.Mapping[builtins.str, typing.Any]:
        '''
        :param props: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__48385f39d6f5e718818636993f5d959a8e2b5d8ba265038722f9927ea1976b53)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> _aws_cdk_core_f4b25747.TagManager:
        '''Assigns one or more tags (key-value pairs) to the app monitor.

        Tags can help you organize and categorize your resources. You can also use them to scope user permissions by granting a user permission to access or change only resources with certain tag values.

        Tags don't have any semantic meaning to AWS and are interpreted strictly as strings of characters.

        You can associate as many as 50 tags with an app monitor.

        For more information, see `Tagging AWS resources <https://docs.aws.amazon.com/general/latest/gr/aws_tagging.html>`_ .

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rum-appmonitor.html#cfn-rum-appmonitor-tags
        '''
        return typing.cast(_aws_cdk_core_f4b25747.TagManager, jsii.get(self, "tags"))

    @builtins.property
    @jsii.member(jsii_name="domain")
    def domain(self) -> builtins.str:
        '''The top-level internet domain name for which your application has administrative authority.

        This parameter is required.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rum-appmonitor.html#cfn-rum-appmonitor-domain
        '''
        return typing.cast(builtins.str, jsii.get(self, "domain"))

    @domain.setter
    def domain(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__77890539c9066a088dd1e2aad342cb5c3c84261be6434a5d77fde5d5be628a49)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "domain", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        '''A name for the app monitor.

        This parameter is required.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rum-appmonitor.html#cfn-rum-appmonitor-name
        '''
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__50808cb9b763105822ca8e31f852d6874fd49d79ee2bfc78a8e0b63ee0f27963)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="appMonitorConfiguration")
    def app_monitor_configuration(
        self,
    ) -> typing.Optional[typing.Union["CfnAppMonitor.AppMonitorConfigurationProperty", _aws_cdk_core_f4b25747.IResolvable]]:
        '''A structure that contains much of the configuration data for the app monitor.

        If you are using Amazon Cognito for authorization, you must include this structure in your request, and it must include the ID of the Amazon Cognito identity pool to use for authorization. If you don't include ``AppMonitorConfiguration`` , you must set up your own authorization method. For more information, see `Authorize your application to send data to AWS <https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-RUM-get-started-authorization.html>`_ .

        If you omit this argument, the sample rate used for CloudWatch RUM is set to 10% of the user sessions.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rum-appmonitor.html#cfn-rum-appmonitor-appmonitorconfiguration
        '''
        return typing.cast(typing.Optional[typing.Union["CfnAppMonitor.AppMonitorConfigurationProperty", _aws_cdk_core_f4b25747.IResolvable]], jsii.get(self, "appMonitorConfiguration"))

    @app_monitor_configuration.setter
    def app_monitor_configuration(
        self,
        value: typing.Optional[typing.Union["CfnAppMonitor.AppMonitorConfigurationProperty", _aws_cdk_core_f4b25747.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__955b53b1eba4ae379cfab72dd3df6364ab1c81abac78ae76b1b8a0b70dfe32fb)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "appMonitorConfiguration", value)

    @builtins.property
    @jsii.member(jsii_name="cwLogEnabled")
    def cw_log_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _aws_cdk_core_f4b25747.IResolvable]]:
        '''Data collected by CloudWatch RUM is kept by RUM for 30 days and then deleted.

        This parameter specifies whether CloudWatch RUM sends a copy of this telemetry data to Amazon CloudWatch Logs in your account. This enables you to keep the telemetry data for more than 30 days, but it does incur Amazon CloudWatch Logs charges.

        If you omit this parameter, the default is ``false`` .

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rum-appmonitor.html#cfn-rum-appmonitor-cwlogenabled
        '''
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _aws_cdk_core_f4b25747.IResolvable]], jsii.get(self, "cwLogEnabled"))

    @cw_log_enabled.setter
    def cw_log_enabled(
        self,
        value: typing.Optional[typing.Union[builtins.bool, _aws_cdk_core_f4b25747.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b572e85b4e463f057ce0f3733bc80e9d58aed2edf7d12de9302d20870d79f643)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "cwLogEnabled", value)

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-rum.CfnAppMonitor.AppMonitorConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "allow_cookies": "allowCookies",
            "enable_x_ray": "enableXRay",
            "excluded_pages": "excludedPages",
            "favorite_pages": "favoritePages",
            "guest_role_arn": "guestRoleArn",
            "identity_pool_id": "identityPoolId",
            "included_pages": "includedPages",
            "metric_destinations": "metricDestinations",
            "session_sample_rate": "sessionSampleRate",
            "telemetries": "telemetries",
        },
    )
    class AppMonitorConfigurationProperty:
        def __init__(
            self,
            *,
            allow_cookies: typing.Optional[typing.Union[builtins.bool, _aws_cdk_core_f4b25747.IResolvable]] = None,
            enable_x_ray: typing.Optional[typing.Union[builtins.bool, _aws_cdk_core_f4b25747.IResolvable]] = None,
            excluded_pages: typing.Optional[typing.Sequence[builtins.str]] = None,
            favorite_pages: typing.Optional[typing.Sequence[builtins.str]] = None,
            guest_role_arn: typing.Optional[builtins.str] = None,
            identity_pool_id: typing.Optional[builtins.str] = None,
            included_pages: typing.Optional[typing.Sequence[builtins.str]] = None,
            metric_destinations: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Sequence[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union["CfnAppMonitor.MetricDestinationProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
            session_sample_rate: typing.Optional[jsii.Number] = None,
            telemetries: typing.Optional[typing.Sequence[builtins.str]] = None,
        ) -> None:
            '''This structure contains much of the configuration data for the app monitor.

            :param allow_cookies: If you set this to ``true`` , the CloudWatch RUM web client sets two cookies, a session cookie and a user cookie. The cookies allow the CloudWatch RUM web client to collect data relating to the number of users an application has and the behavior of the application across a sequence of events. Cookies are stored in the top-level domain of the current page.
            :param enable_x_ray: If you set this to ``true`` , CloudWatch RUM sends client-side traces to X-Ray for each sampled session. You can then see traces and segments from these user sessions in the RUM dashboard and the CloudWatch ServiceLens console. For more information, see `What is AWS X-Ray ? <https://docs.aws.amazon.com/xray/latest/devguide/aws-xray.html>`_
            :param excluded_pages: A list of URLs in your website or application to exclude from RUM data collection. You can't include both ``ExcludedPages`` and ``IncludedPages`` in the same app monitor.
            :param favorite_pages: A list of pages in your application that are to be displayed with a "favorite" icon in the CloudWatch RUM console.
            :param guest_role_arn: The ARN of the guest IAM role that is attached to the Amazon Cognito identity pool that is used to authorize the sending of data to CloudWatch RUM.
            :param identity_pool_id: The ID of the Amazon Cognito identity pool that is used to authorize the sending of data to CloudWatch RUM.
            :param included_pages: If this app monitor is to collect data from only certain pages in your application, this structure lists those pages. You can't include both ``ExcludedPages`` and ``IncludedPages`` in the same app monitor.
            :param metric_destinations: An array of structures that each define a destination that this app monitor will send extended metrics to.
            :param session_sample_rate: Specifies the portion of user sessions to use for CloudWatch RUM data collection. Choosing a higher portion gives you more data but also incurs more costs. The range for this value is 0 to 1 inclusive. Setting this to 1 means that 100% of user sessions are sampled, and setting it to 0.1 means that 10% of user sessions are sampled. If you omit this parameter, the default of 0.1 is used, and 10% of sessions will be sampled.
            :param telemetries: An array that lists the types of telemetry data that this app monitor is to collect. - ``errors`` indicates that RUM collects data about unhandled JavaScript errors raised by your application. - ``performance`` indicates that RUM collects performance data about how your application and its resources are loaded and rendered. This includes Core Web Vitals. - ``http`` indicates that RUM collects data about HTTP errors thrown by your application.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-rum-appmonitor-appmonitorconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                import aws_cdk.aws_rum as rum
                
                app_monitor_configuration_property = rum.CfnAppMonitor.AppMonitorConfigurationProperty(
                    allow_cookies=False,
                    enable_xRay=False,
                    excluded_pages=["excludedPages"],
                    favorite_pages=["favoritePages"],
                    guest_role_arn="guestRoleArn",
                    identity_pool_id="identityPoolId",
                    included_pages=["includedPages"],
                    metric_destinations=[rum.CfnAppMonitor.MetricDestinationProperty(
                        destination="destination",
                
                        # the properties below are optional
                        destination_arn="destinationArn",
                        iam_role_arn="iamRoleArn",
                        metric_definitions=[rum.CfnAppMonitor.MetricDefinitionProperty(
                            name="name",
                
                            # the properties below are optional
                            dimension_keys={
                                "dimension_keys_key": "dimensionKeys"
                            },
                            event_pattern="eventPattern",
                            unit_label="unitLabel",
                            value_key="valueKey"
                        )]
                    )],
                    session_sample_rate=123,
                    telemetries=["telemetries"]
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__b85168633348525158847d17a686246f2b276774499d1b889efe70a6ee950e73)
                check_type(argname="argument allow_cookies", value=allow_cookies, expected_type=type_hints["allow_cookies"])
                check_type(argname="argument enable_x_ray", value=enable_x_ray, expected_type=type_hints["enable_x_ray"])
                check_type(argname="argument excluded_pages", value=excluded_pages, expected_type=type_hints["excluded_pages"])
                check_type(argname="argument favorite_pages", value=favorite_pages, expected_type=type_hints["favorite_pages"])
                check_type(argname="argument guest_role_arn", value=guest_role_arn, expected_type=type_hints["guest_role_arn"])
                check_type(argname="argument identity_pool_id", value=identity_pool_id, expected_type=type_hints["identity_pool_id"])
                check_type(argname="argument included_pages", value=included_pages, expected_type=type_hints["included_pages"])
                check_type(argname="argument metric_destinations", value=metric_destinations, expected_type=type_hints["metric_destinations"])
                check_type(argname="argument session_sample_rate", value=session_sample_rate, expected_type=type_hints["session_sample_rate"])
                check_type(argname="argument telemetries", value=telemetries, expected_type=type_hints["telemetries"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if allow_cookies is not None:
                self._values["allow_cookies"] = allow_cookies
            if enable_x_ray is not None:
                self._values["enable_x_ray"] = enable_x_ray
            if excluded_pages is not None:
                self._values["excluded_pages"] = excluded_pages
            if favorite_pages is not None:
                self._values["favorite_pages"] = favorite_pages
            if guest_role_arn is not None:
                self._values["guest_role_arn"] = guest_role_arn
            if identity_pool_id is not None:
                self._values["identity_pool_id"] = identity_pool_id
            if included_pages is not None:
                self._values["included_pages"] = included_pages
            if metric_destinations is not None:
                self._values["metric_destinations"] = metric_destinations
            if session_sample_rate is not None:
                self._values["session_sample_rate"] = session_sample_rate
            if telemetries is not None:
                self._values["telemetries"] = telemetries

        @builtins.property
        def allow_cookies(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _aws_cdk_core_f4b25747.IResolvable]]:
            '''If you set this to ``true`` , the CloudWatch RUM web client sets two cookies, a session cookie and a user cookie.

            The cookies allow the CloudWatch RUM web client to collect data relating to the number of users an application has and the behavior of the application across a sequence of events. Cookies are stored in the top-level domain of the current page.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-rum-appmonitor-appmonitorconfiguration.html#cfn-rum-appmonitor-appmonitorconfiguration-allowcookies
            '''
            result = self._values.get("allow_cookies")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _aws_cdk_core_f4b25747.IResolvable]], result)

        @builtins.property
        def enable_x_ray(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _aws_cdk_core_f4b25747.IResolvable]]:
            '''If you set this to ``true`` , CloudWatch RUM sends client-side traces to X-Ray for each sampled session.

            You can then see traces and segments from these user sessions in the RUM dashboard and the CloudWatch ServiceLens console. For more information, see `What is AWS X-Ray ? <https://docs.aws.amazon.com/xray/latest/devguide/aws-xray.html>`_

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-rum-appmonitor-appmonitorconfiguration.html#cfn-rum-appmonitor-appmonitorconfiguration-enablexray
            '''
            result = self._values.get("enable_x_ray")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _aws_cdk_core_f4b25747.IResolvable]], result)

        @builtins.property
        def excluded_pages(self) -> typing.Optional[typing.List[builtins.str]]:
            '''A list of URLs in your website or application to exclude from RUM data collection.

            You can't include both ``ExcludedPages`` and ``IncludedPages`` in the same app monitor.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-rum-appmonitor-appmonitorconfiguration.html#cfn-rum-appmonitor-appmonitorconfiguration-excludedpages
            '''
            result = self._values.get("excluded_pages")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        @builtins.property
        def favorite_pages(self) -> typing.Optional[typing.List[builtins.str]]:
            '''A list of pages in your application that are to be displayed with a "favorite" icon in the CloudWatch RUM console.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-rum-appmonitor-appmonitorconfiguration.html#cfn-rum-appmonitor-appmonitorconfiguration-favoritepages
            '''
            result = self._values.get("favorite_pages")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        @builtins.property
        def guest_role_arn(self) -> typing.Optional[builtins.str]:
            '''The ARN of the guest IAM role that is attached to the Amazon Cognito identity pool that is used to authorize the sending of data to CloudWatch RUM.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-rum-appmonitor-appmonitorconfiguration.html#cfn-rum-appmonitor-appmonitorconfiguration-guestrolearn
            '''
            result = self._values.get("guest_role_arn")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def identity_pool_id(self) -> typing.Optional[builtins.str]:
            '''The ID of the Amazon Cognito identity pool that is used to authorize the sending of data to CloudWatch RUM.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-rum-appmonitor-appmonitorconfiguration.html#cfn-rum-appmonitor-appmonitorconfiguration-identitypoolid
            '''
            result = self._values.get("identity_pool_id")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def included_pages(self) -> typing.Optional[typing.List[builtins.str]]:
            '''If this app monitor is to collect data from only certain pages in your application, this structure lists those pages.

            You can't include both ``ExcludedPages`` and ``IncludedPages`` in the same app monitor.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-rum-appmonitor-appmonitorconfiguration.html#cfn-rum-appmonitor-appmonitorconfiguration-includedpages
            '''
            result = self._values.get("included_pages")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        @builtins.property
        def metric_destinations(
            self,
        ) -> typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.List[typing.Union[_aws_cdk_core_f4b25747.IResolvable, "CfnAppMonitor.MetricDestinationProperty"]]]]:
            '''An array of structures that each define a destination that this app monitor will send extended metrics to.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-rum-appmonitor-appmonitorconfiguration.html#cfn-rum-appmonitor-appmonitorconfiguration-metricdestinations
            '''
            result = self._values.get("metric_destinations")
            return typing.cast(typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.List[typing.Union[_aws_cdk_core_f4b25747.IResolvable, "CfnAppMonitor.MetricDestinationProperty"]]]], result)

        @builtins.property
        def session_sample_rate(self) -> typing.Optional[jsii.Number]:
            '''Specifies the portion of user sessions to use for CloudWatch RUM data collection.

            Choosing a higher portion gives you more data but also incurs more costs.

            The range for this value is 0 to 1 inclusive. Setting this to 1 means that 100% of user sessions are sampled, and setting it to 0.1 means that 10% of user sessions are sampled.

            If you omit this parameter, the default of 0.1 is used, and 10% of sessions will be sampled.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-rum-appmonitor-appmonitorconfiguration.html#cfn-rum-appmonitor-appmonitorconfiguration-sessionsamplerate
            '''
            result = self._values.get("session_sample_rate")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def telemetries(self) -> typing.Optional[typing.List[builtins.str]]:
            '''An array that lists the types of telemetry data that this app monitor is to collect.

            - ``errors`` indicates that RUM collects data about unhandled JavaScript errors raised by your application.
            - ``performance`` indicates that RUM collects performance data about how your application and its resources are loaded and rendered. This includes Core Web Vitals.
            - ``http`` indicates that RUM collects data about HTTP errors thrown by your application.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-rum-appmonitor-appmonitorconfiguration.html#cfn-rum-appmonitor-appmonitorconfiguration-telemetries
            '''
            result = self._values.get("telemetries")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "AppMonitorConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-rum.CfnAppMonitor.MetricDefinitionProperty",
        jsii_struct_bases=[],
        name_mapping={
            "name": "name",
            "dimension_keys": "dimensionKeys",
            "event_pattern": "eventPattern",
            "unit_label": "unitLabel",
            "value_key": "valueKey",
        },
    )
    class MetricDefinitionProperty:
        def __init__(
            self,
            *,
            name: builtins.str,
            dimension_keys: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Mapping[builtins.str, builtins.str]]] = None,
            event_pattern: typing.Optional[builtins.str] = None,
            unit_label: typing.Optional[builtins.str] = None,
            value_key: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Specifies the extended metrics that you want the CloudWatch RUM app monitor to send to a destination.

            Valid destinations include CloudWatch and Evidently.

            By default, RUM app monitors send some metrics to CloudWatch . These default metrics are listed in `CloudWatch metrics that you can collect with CloudWatch RUM <https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-RUM-metrics.html>`_ .

            If you also send extended metrics, you can send metrics to Evidently as well as CloudWatch , and you can also optionally send the metrics with additional dimensions. The valid dimension names for the additional dimensions are ``BrowserName`` , ``CountryCode`` , ``DeviceType`` , ``FileType`` , ``OSName`` , and ``PageId`` . For more information, see `Extended metrics that you can send to CloudWatch and CloudWatch Evidently <https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-RUM-vended-metrics.html>`_ .

            The maximum number of metric definitions that one destination can contain is 2000.

            Extended metrics sent are charged as CloudWatch custom metrics. Each combination of additional dimension name and dimension value counts as a custom metric.

            If some metric definitions that you specify are not valid, then the operation will not modify any metric definitions even if other metric definitions specified are valid.

            :param name: The name of the metric that is defined in this structure.
            :param dimension_keys: This field is a map of field paths to dimension names. It defines the dimensions to associate with this metric in CloudWatch The value of this field is used only if the metric destination is ``CloudWatch`` . If the metric destination is ``Evidently`` , the value of ``DimensionKeys`` is ignored.
            :param event_pattern: The pattern that defines the metric. RUM checks events that happen in a user's session against the pattern, and events that match the pattern are sent to the metric destination. If the metrics destination is ``CloudWatch`` and the event also matches a value in ``DimensionKeys`` , then the metric is published with the specified dimensions.
            :param unit_label: Use this field only if you are sending this metric to CloudWatch . It defines the CloudWatch metric unit that this metric is measured in.
            :param value_key: The field within the event object that the metric value is sourced from.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-rum-appmonitor-metricdefinition.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                import aws_cdk.aws_rum as rum
                
                metric_definition_property = rum.CfnAppMonitor.MetricDefinitionProperty(
                    name="name",
                
                    # the properties below are optional
                    dimension_keys={
                        "dimension_keys_key": "dimensionKeys"
                    },
                    event_pattern="eventPattern",
                    unit_label="unitLabel",
                    value_key="valueKey"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__41574ad85a21ad764f5b732bea0d04f1d2e75f0ac75f7f90bafc937415623aa5)
                check_type(argname="argument name", value=name, expected_type=type_hints["name"])
                check_type(argname="argument dimension_keys", value=dimension_keys, expected_type=type_hints["dimension_keys"])
                check_type(argname="argument event_pattern", value=event_pattern, expected_type=type_hints["event_pattern"])
                check_type(argname="argument unit_label", value=unit_label, expected_type=type_hints["unit_label"])
                check_type(argname="argument value_key", value=value_key, expected_type=type_hints["value_key"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "name": name,
            }
            if dimension_keys is not None:
                self._values["dimension_keys"] = dimension_keys
            if event_pattern is not None:
                self._values["event_pattern"] = event_pattern
            if unit_label is not None:
                self._values["unit_label"] = unit_label
            if value_key is not None:
                self._values["value_key"] = value_key

        @builtins.property
        def name(self) -> builtins.str:
            '''The name of the metric that is defined in this structure.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-rum-appmonitor-metricdefinition.html#cfn-rum-appmonitor-metricdefinition-name
            '''
            result = self._values.get("name")
            assert result is not None, "Required property 'name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def dimension_keys(
            self,
        ) -> typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Mapping[builtins.str, builtins.str]]]:
            '''This field is a map of field paths to dimension names.

            It defines the dimensions to associate with this metric in CloudWatch The value of this field is used only if the metric destination is ``CloudWatch`` . If the metric destination is ``Evidently`` , the value of ``DimensionKeys`` is ignored.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-rum-appmonitor-metricdefinition.html#cfn-rum-appmonitor-metricdefinition-dimensionkeys
            '''
            result = self._values.get("dimension_keys")
            return typing.cast(typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Mapping[builtins.str, builtins.str]]], result)

        @builtins.property
        def event_pattern(self) -> typing.Optional[builtins.str]:
            '''The pattern that defines the metric.

            RUM checks events that happen in a user's session against the pattern, and events that match the pattern are sent to the metric destination.

            If the metrics destination is ``CloudWatch`` and the event also matches a value in ``DimensionKeys`` , then the metric is published with the specified dimensions.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-rum-appmonitor-metricdefinition.html#cfn-rum-appmonitor-metricdefinition-eventpattern
            '''
            result = self._values.get("event_pattern")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def unit_label(self) -> typing.Optional[builtins.str]:
            '''Use this field only if you are sending this metric to CloudWatch .

            It defines the CloudWatch metric unit that this metric is measured in.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-rum-appmonitor-metricdefinition.html#cfn-rum-appmonitor-metricdefinition-unitlabel
            '''
            result = self._values.get("unit_label")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def value_key(self) -> typing.Optional[builtins.str]:
            '''The field within the event object that the metric value is sourced from.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-rum-appmonitor-metricdefinition.html#cfn-rum-appmonitor-metricdefinition-valuekey
            '''
            result = self._values.get("value_key")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "MetricDefinitionProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="@aws-cdk/aws-rum.CfnAppMonitor.MetricDestinationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "destination": "destination",
            "destination_arn": "destinationArn",
            "iam_role_arn": "iamRoleArn",
            "metric_definitions": "metricDefinitions",
        },
    )
    class MetricDestinationProperty:
        def __init__(
            self,
            *,
            destination: builtins.str,
            destination_arn: typing.Optional[builtins.str] = None,
            iam_role_arn: typing.Optional[builtins.str] = None,
            metric_definitions: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Sequence[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union["CfnAppMonitor.MetricDefinitionProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
        ) -> None:
            '''Creates or updates a destination to receive extended metrics from CloudWatch RUM.

            You can send extended metrics to CloudWatch or to a CloudWatch Evidently experiment.

            For more information about extended metrics, see `Extended metrics that you can send to CloudWatch and CloudWatch Evidently <https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-RUM-vended-metrics.html>`_ .

            :param destination: Defines the destination to send the metrics to. Valid values are ``CloudWatch`` and ``Evidently`` . If you specify ``Evidently`` , you must also specify the ARN of the CloudWatch Evidently experiment that is to be the destination and an IAM role that has permission to write to the experiment.
            :param destination_arn: Use this parameter only if ``Destination`` is ``Evidently`` . This parameter specifies the ARN of the Evidently experiment that will receive the extended metrics.
            :param iam_role_arn: This parameter is required if ``Destination`` is ``Evidently`` . If ``Destination`` is ``CloudWatch`` , do not use this parameter. This parameter specifies the ARN of an IAM role that RUM will assume to write to the Evidently experiment that you are sending metrics to. This role must have permission to write to that experiment.
            :param metric_definitions: An array of structures which define the metrics that you want to send.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-rum-appmonitor-metricdestination.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                import aws_cdk.aws_rum as rum
                
                metric_destination_property = rum.CfnAppMonitor.MetricDestinationProperty(
                    destination="destination",
                
                    # the properties below are optional
                    destination_arn="destinationArn",
                    iam_role_arn="iamRoleArn",
                    metric_definitions=[rum.CfnAppMonitor.MetricDefinitionProperty(
                        name="name",
                
                        # the properties below are optional
                        dimension_keys={
                            "dimension_keys_key": "dimensionKeys"
                        },
                        event_pattern="eventPattern",
                        unit_label="unitLabel",
                        value_key="valueKey"
                    )]
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__67495da2d9456950b5545c72f398936caf478c4d2af1816d1b1ec34b7a34ed0e)
                check_type(argname="argument destination", value=destination, expected_type=type_hints["destination"])
                check_type(argname="argument destination_arn", value=destination_arn, expected_type=type_hints["destination_arn"])
                check_type(argname="argument iam_role_arn", value=iam_role_arn, expected_type=type_hints["iam_role_arn"])
                check_type(argname="argument metric_definitions", value=metric_definitions, expected_type=type_hints["metric_definitions"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "destination": destination,
            }
            if destination_arn is not None:
                self._values["destination_arn"] = destination_arn
            if iam_role_arn is not None:
                self._values["iam_role_arn"] = iam_role_arn
            if metric_definitions is not None:
                self._values["metric_definitions"] = metric_definitions

        @builtins.property
        def destination(self) -> builtins.str:
            '''Defines the destination to send the metrics to.

            Valid values are ``CloudWatch`` and ``Evidently`` . If you specify ``Evidently`` , you must also specify the ARN of the CloudWatch Evidently experiment that is to be the destination and an IAM role that has permission to write to the experiment.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-rum-appmonitor-metricdestination.html#cfn-rum-appmonitor-metricdestination-destination
            '''
            result = self._values.get("destination")
            assert result is not None, "Required property 'destination' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def destination_arn(self) -> typing.Optional[builtins.str]:
            '''Use this parameter only if ``Destination`` is ``Evidently`` .

            This parameter specifies the ARN of the Evidently experiment that will receive the extended metrics.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-rum-appmonitor-metricdestination.html#cfn-rum-appmonitor-metricdestination-destinationarn
            '''
            result = self._values.get("destination_arn")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def iam_role_arn(self) -> typing.Optional[builtins.str]:
            '''This parameter is required if ``Destination`` is ``Evidently`` . If ``Destination`` is ``CloudWatch`` , do not use this parameter.

            This parameter specifies the ARN of an IAM role that RUM will assume to write to the Evidently experiment that you are sending metrics to. This role must have permission to write to that experiment.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-rum-appmonitor-metricdestination.html#cfn-rum-appmonitor-metricdestination-iamrolearn
            '''
            result = self._values.get("iam_role_arn")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def metric_definitions(
            self,
        ) -> typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.List[typing.Union[_aws_cdk_core_f4b25747.IResolvable, "CfnAppMonitor.MetricDefinitionProperty"]]]]:
            '''An array of structures which define the metrics that you want to send.

            :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-rum-appmonitor-metricdestination.html#cfn-rum-appmonitor-metricdestination-metricdefinitions
            '''
            result = self._values.get("metric_definitions")
            return typing.cast(typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.List[typing.Union[_aws_cdk_core_f4b25747.IResolvable, "CfnAppMonitor.MetricDefinitionProperty"]]]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "MetricDestinationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="@aws-cdk/aws-rum.CfnAppMonitorProps",
    jsii_struct_bases=[],
    name_mapping={
        "domain": "domain",
        "name": "name",
        "app_monitor_configuration": "appMonitorConfiguration",
        "cw_log_enabled": "cwLogEnabled",
        "tags": "tags",
    },
)
class CfnAppMonitorProps:
    def __init__(
        self,
        *,
        domain: builtins.str,
        name: builtins.str,
        app_monitor_configuration: typing.Optional[typing.Union[typing.Union[CfnAppMonitor.AppMonitorConfigurationProperty, typing.Dict[builtins.str, typing.Any]], _aws_cdk_core_f4b25747.IResolvable]] = None,
        cw_log_enabled: typing.Optional[typing.Union[builtins.bool, _aws_cdk_core_f4b25747.IResolvable]] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_aws_cdk_core_f4b25747.CfnTag, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnAppMonitor``.

        :param domain: The top-level internet domain name for which your application has administrative authority. This parameter is required.
        :param name: A name for the app monitor. This parameter is required.
        :param app_monitor_configuration: A structure that contains much of the configuration data for the app monitor. If you are using Amazon Cognito for authorization, you must include this structure in your request, and it must include the ID of the Amazon Cognito identity pool to use for authorization. If you don't include ``AppMonitorConfiguration`` , you must set up your own authorization method. For more information, see `Authorize your application to send data to AWS <https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-RUM-get-started-authorization.html>`_ . If you omit this argument, the sample rate used for CloudWatch RUM is set to 10% of the user sessions.
        :param cw_log_enabled: Data collected by CloudWatch RUM is kept by RUM for 30 days and then deleted. This parameter specifies whether CloudWatch RUM sends a copy of this telemetry data to Amazon CloudWatch Logs in your account. This enables you to keep the telemetry data for more than 30 days, but it does incur Amazon CloudWatch Logs charges. If you omit this parameter, the default is ``false`` .
        :param tags: Assigns one or more tags (key-value pairs) to the app monitor. Tags can help you organize and categorize your resources. You can also use them to scope user permissions by granting a user permission to access or change only resources with certain tag values. Tags don't have any semantic meaning to AWS and are interpreted strictly as strings of characters. You can associate as many as 50 tags with an app monitor. For more information, see `Tagging AWS resources <https://docs.aws.amazon.com/general/latest/gr/aws_tagging.html>`_ .

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rum-appmonitor.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            import aws_cdk.aws_rum as rum
            
            cfn_app_monitor_props = rum.CfnAppMonitorProps(
                domain="domain",
                name="name",
            
                # the properties below are optional
                app_monitor_configuration=rum.CfnAppMonitor.AppMonitorConfigurationProperty(
                    allow_cookies=False,
                    enable_xRay=False,
                    excluded_pages=["excludedPages"],
                    favorite_pages=["favoritePages"],
                    guest_role_arn="guestRoleArn",
                    identity_pool_id="identityPoolId",
                    included_pages=["includedPages"],
                    metric_destinations=[rum.CfnAppMonitor.MetricDestinationProperty(
                        destination="destination",
            
                        # the properties below are optional
                        destination_arn="destinationArn",
                        iam_role_arn="iamRoleArn",
                        metric_definitions=[rum.CfnAppMonitor.MetricDefinitionProperty(
                            name="name",
            
                            # the properties below are optional
                            dimension_keys={
                                "dimension_keys_key": "dimensionKeys"
                            },
                            event_pattern="eventPattern",
                            unit_label="unitLabel",
                            value_key="valueKey"
                        )]
                    )],
                    session_sample_rate=123,
                    telemetries=["telemetries"]
                ),
                cw_log_enabled=False,
                tags=[CfnTag(
                    key="key",
                    value="value"
                )]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__489426512a46e7ce818e2601e927691ec10113c1ea0a3d7477e921958d72df0f)
            check_type(argname="argument domain", value=domain, expected_type=type_hints["domain"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument app_monitor_configuration", value=app_monitor_configuration, expected_type=type_hints["app_monitor_configuration"])
            check_type(argname="argument cw_log_enabled", value=cw_log_enabled, expected_type=type_hints["cw_log_enabled"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "domain": domain,
            "name": name,
        }
        if app_monitor_configuration is not None:
            self._values["app_monitor_configuration"] = app_monitor_configuration
        if cw_log_enabled is not None:
            self._values["cw_log_enabled"] = cw_log_enabled
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def domain(self) -> builtins.str:
        '''The top-level internet domain name for which your application has administrative authority.

        This parameter is required.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rum-appmonitor.html#cfn-rum-appmonitor-domain
        '''
        result = self._values.get("domain")
        assert result is not None, "Required property 'domain' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''A name for the app monitor.

        This parameter is required.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rum-appmonitor.html#cfn-rum-appmonitor-name
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def app_monitor_configuration(
        self,
    ) -> typing.Optional[typing.Union[CfnAppMonitor.AppMonitorConfigurationProperty, _aws_cdk_core_f4b25747.IResolvable]]:
        '''A structure that contains much of the configuration data for the app monitor.

        If you are using Amazon Cognito for authorization, you must include this structure in your request, and it must include the ID of the Amazon Cognito identity pool to use for authorization. If you don't include ``AppMonitorConfiguration`` , you must set up your own authorization method. For more information, see `Authorize your application to send data to AWS <https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-RUM-get-started-authorization.html>`_ .

        If you omit this argument, the sample rate used for CloudWatch RUM is set to 10% of the user sessions.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rum-appmonitor.html#cfn-rum-appmonitor-appmonitorconfiguration
        '''
        result = self._values.get("app_monitor_configuration")
        return typing.cast(typing.Optional[typing.Union[CfnAppMonitor.AppMonitorConfigurationProperty, _aws_cdk_core_f4b25747.IResolvable]], result)

    @builtins.property
    def cw_log_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _aws_cdk_core_f4b25747.IResolvable]]:
        '''Data collected by CloudWatch RUM is kept by RUM for 30 days and then deleted.

        This parameter specifies whether CloudWatch RUM sends a copy of this telemetry data to Amazon CloudWatch Logs in your account. This enables you to keep the telemetry data for more than 30 days, but it does incur Amazon CloudWatch Logs charges.

        If you omit this parameter, the default is ``false`` .

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rum-appmonitor.html#cfn-rum-appmonitor-cwlogenabled
        '''
        result = self._values.get("cw_log_enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _aws_cdk_core_f4b25747.IResolvable]], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_aws_cdk_core_f4b25747.CfnTag]]:
        '''Assigns one or more tags (key-value pairs) to the app monitor.

        Tags can help you organize and categorize your resources. You can also use them to scope user permissions by granting a user permission to access or change only resources with certain tag values.

        Tags don't have any semantic meaning to AWS and are interpreted strictly as strings of characters.

        You can associate as many as 50 tags with an app monitor.

        For more information, see `Tagging AWS resources <https://docs.aws.amazon.com/general/latest/gr/aws_tagging.html>`_ .

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rum-appmonitor.html#cfn-rum-appmonitor-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_aws_cdk_core_f4b25747.CfnTag]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnAppMonitorProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "CfnAppMonitor",
    "CfnAppMonitorProps",
]

publication.publish()

def _typecheckingstub__e4386a295d4af768eba5a9e5bbd1d1a922974f369e6c77a4d88d61ac86ee2db9(
    scope: _aws_cdk_core_f4b25747.Construct,
    id: builtins.str,
    *,
    domain: builtins.str,
    name: builtins.str,
    app_monitor_configuration: typing.Optional[typing.Union[typing.Union[CfnAppMonitor.AppMonitorConfigurationProperty, typing.Dict[builtins.str, typing.Any]], _aws_cdk_core_f4b25747.IResolvable]] = None,
    cw_log_enabled: typing.Optional[typing.Union[builtins.bool, _aws_cdk_core_f4b25747.IResolvable]] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_aws_cdk_core_f4b25747.CfnTag, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ccf08c4bb8358cb8bb84404f01c6b7914b25820b68d6607d900c269f204486b1(
    inspector: _aws_cdk_core_f4b25747.TreeInspector,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__48385f39d6f5e718818636993f5d959a8e2b5d8ba265038722f9927ea1976b53(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__77890539c9066a088dd1e2aad342cb5c3c84261be6434a5d77fde5d5be628a49(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__50808cb9b763105822ca8e31f852d6874fd49d79ee2bfc78a8e0b63ee0f27963(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__955b53b1eba4ae379cfab72dd3df6364ab1c81abac78ae76b1b8a0b70dfe32fb(
    value: typing.Optional[typing.Union[CfnAppMonitor.AppMonitorConfigurationProperty, _aws_cdk_core_f4b25747.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b572e85b4e463f057ce0f3733bc80e9d58aed2edf7d12de9302d20870d79f643(
    value: typing.Optional[typing.Union[builtins.bool, _aws_cdk_core_f4b25747.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b85168633348525158847d17a686246f2b276774499d1b889efe70a6ee950e73(
    *,
    allow_cookies: typing.Optional[typing.Union[builtins.bool, _aws_cdk_core_f4b25747.IResolvable]] = None,
    enable_x_ray: typing.Optional[typing.Union[builtins.bool, _aws_cdk_core_f4b25747.IResolvable]] = None,
    excluded_pages: typing.Optional[typing.Sequence[builtins.str]] = None,
    favorite_pages: typing.Optional[typing.Sequence[builtins.str]] = None,
    guest_role_arn: typing.Optional[builtins.str] = None,
    identity_pool_id: typing.Optional[builtins.str] = None,
    included_pages: typing.Optional[typing.Sequence[builtins.str]] = None,
    metric_destinations: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Sequence[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union[CfnAppMonitor.MetricDestinationProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    session_sample_rate: typing.Optional[jsii.Number] = None,
    telemetries: typing.Optional[typing.Sequence[builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__41574ad85a21ad764f5b732bea0d04f1d2e75f0ac75f7f90bafc937415623aa5(
    *,
    name: builtins.str,
    dimension_keys: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Mapping[builtins.str, builtins.str]]] = None,
    event_pattern: typing.Optional[builtins.str] = None,
    unit_label: typing.Optional[builtins.str] = None,
    value_key: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__67495da2d9456950b5545c72f398936caf478c4d2af1816d1b1ec34b7a34ed0e(
    *,
    destination: builtins.str,
    destination_arn: typing.Optional[builtins.str] = None,
    iam_role_arn: typing.Optional[builtins.str] = None,
    metric_definitions: typing.Optional[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Sequence[typing.Union[_aws_cdk_core_f4b25747.IResolvable, typing.Union[CfnAppMonitor.MetricDefinitionProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__489426512a46e7ce818e2601e927691ec10113c1ea0a3d7477e921958d72df0f(
    *,
    domain: builtins.str,
    name: builtins.str,
    app_monitor_configuration: typing.Optional[typing.Union[typing.Union[CfnAppMonitor.AppMonitorConfigurationProperty, typing.Dict[builtins.str, typing.Any]], _aws_cdk_core_f4b25747.IResolvable]] = None,
    cw_log_enabled: typing.Optional[typing.Union[builtins.bool, _aws_cdk_core_f4b25747.IResolvable]] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_aws_cdk_core_f4b25747.CfnTag, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass
