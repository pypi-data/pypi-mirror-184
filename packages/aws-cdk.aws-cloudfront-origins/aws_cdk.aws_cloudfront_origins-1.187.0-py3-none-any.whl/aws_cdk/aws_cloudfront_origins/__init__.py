'''
# CloudFront Origins for the CDK CloudFront Library

<!--BEGIN STABILITY BANNER-->---


![cdk-constructs: Stable](https://img.shields.io/badge/cdk--constructs-stable-success.svg?style=for-the-badge)

---
<!--END STABILITY BANNER-->

This library contains convenience methods for defining origins for a CloudFront distribution. You can use this library to create origins from
S3 buckets, Elastic Load Balancing v2 load balancers, or any other domain name.

## S3 Bucket

An S3 bucket can be added as an origin. If the bucket is configured as a website endpoint, the distribution can use S3 redirects and S3 custom error
documents.

```python
my_bucket = s3.Bucket(self, "myBucket")
cloudfront.Distribution(self, "myDist",
    default_behavior=cloudfront.BehaviorOptions(origin=origins.S3Origin(my_bucket))
)
```

The above will treat the bucket differently based on if `IBucket.isWebsite` is set or not. If the bucket is configured as a website, the bucket is
treated as an HTTP origin, and the built-in S3 redirects and error pages can be used. Otherwise, the bucket is handled as a bucket origin and
CloudFront's redirect and error handling will be used. In the latter case, the Origin will create an origin access identity and grant it access to the
underlying bucket. This can be used in conjunction with a bucket that is not public to require that your users access your content using CloudFront
URLs and not S3 URLs directly. Alternatively, a custom origin access identity can be passed to the S3 origin in the properties.

### Adding Custom Headers

You can configure CloudFront to add custom headers to the requests that it sends to your origin. These custom headers enable you to send and gather information from your origin that you don’t get with typical viewer requests. These headers can even be customized for each origin. CloudFront supports custom headers for both for custom and Amazon S3 origins.

```python
my_bucket = s3.Bucket(self, "myBucket")
cloudfront.Distribution(self, "myDist",
    default_behavior=cloudfront.BehaviorOptions(origin=origins.S3Origin(my_bucket,
        custom_headers={
            "Foo": "bar"
        }
    ))
)
```

## ELBv2 Load Balancer

An Elastic Load Balancing (ELB) v2 load balancer may be used as an origin. In order for a load balancer to serve as an origin, it must be publicly
accessible (`internetFacing` is true). Both Application and Network load balancers are supported.

```python
import aws_cdk.aws_ec2 as ec2
import aws_cdk.aws_elasticloadbalancingv2 as elbv2

# vpc: ec2.Vpc

# Create an application load balancer in a VPC. 'internetFacing' must be 'true'
# for CloudFront to access the load balancer and use it as an origin.
lb = elbv2.ApplicationLoadBalancer(self, "LB",
    vpc=vpc,
    internet_facing=True
)
cloudfront.Distribution(self, "myDist",
    default_behavior=cloudfront.BehaviorOptions(origin=origins.LoadBalancerV2Origin(lb))
)
```

The origin can also be customized to respond on different ports, have different connection properties, etc.

```python
import aws_cdk.aws_elasticloadbalancingv2 as elbv2

# load_balancer: elbv2.ApplicationLoadBalancer

origin = origins.LoadBalancerV2Origin(load_balancer,
    connection_attempts=3,
    connection_timeout=Duration.seconds(5),
    read_timeout=Duration.seconds(45),
    keepalive_timeout=Duration.seconds(45),
    protocol_policy=cloudfront.OriginProtocolPolicy.MATCH_VIEWER
)
```

Note that the `readTimeout` and `keepaliveTimeout` properties can extend their values over 60 seconds only if a limit increase request for CloudFront origin response timeout
quota has been approved in the target account; otherwise, values over 60 seconds will produce an error at deploy time. Consider that this value is
still limited to a maximum value of 180 seconds, which is a hard limit for that quota.

## From an HTTP endpoint

Origins can also be created from any other HTTP endpoint, given the domain name, and optionally, other origin properties.

```python
cloudfront.Distribution(self, "myDist",
    default_behavior=cloudfront.BehaviorOptions(origin=origins.HttpOrigin("www.example.com"))
)
```

See the documentation of `@aws-cdk/aws-cloudfront` for more information.

## Failover Origins (Origin Groups)

You can set up CloudFront with origin failover for scenarios that require high availability.
To get started, you create an origin group with two origins: a primary and a secondary.
If the primary origin is unavailable, or returns specific HTTP response status codes that indicate a failure,
CloudFront automatically switches to the secondary origin.
You achieve that behavior in the CDK using the `OriginGroup` class:

```python
my_bucket = s3.Bucket(self, "myBucket")
cloudfront.Distribution(self, "myDist",
    default_behavior=cloudfront.BehaviorOptions(
        origin=origins.OriginGroup(
            primary_origin=origins.S3Origin(my_bucket),
            fallback_origin=origins.HttpOrigin("www.example.com"),
            # optional, defaults to: 500, 502, 503 and 504
            fallback_status_codes=[404]
        )
    )
)
```

## From an API Gateway REST API

Origins can be created from an API Gateway REST API. It is recommended to use a
[regional API](https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-api-endpoint-types.html) in this case.

```python
# api: apigateway.RestApi

cloudfront.Distribution(self, "Distribution",
    default_behavior=cloudfront.BehaviorOptions(origin=origins.RestApiOrigin(api))
)
```

The origin path will automatically be set as the stage name.
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

import aws_cdk.aws_apigateway as _aws_cdk_aws_apigateway_f01c2838
import aws_cdk.aws_cloudfront as _aws_cdk_aws_cloudfront_d69ac3eb
import aws_cdk.aws_elasticloadbalancingv2 as _aws_cdk_aws_elasticloadbalancingv2_e93c784f
import aws_cdk.aws_s3 as _aws_cdk_aws_s3_55f001a5
import aws_cdk.core as _aws_cdk_core_f4b25747


class HttpOrigin(
    _aws_cdk_aws_cloudfront_d69ac3eb.OriginBase,
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/aws-cloudfront-origins.HttpOrigin",
):
    '''An Origin for an HTTP server or S3 bucket configured for website hosting.

    :exampleMetadata: infused

    Example::

        my_bucket = s3.Bucket(self, "myBucket")
        cloudfront.Distribution(self, "myDist",
            default_behavior=cloudfront.BehaviorOptions(
                origin=origins.OriginGroup(
                    primary_origin=origins.S3Origin(my_bucket),
                    fallback_origin=origins.HttpOrigin("www.example.com"),
                    # optional, defaults to: 500, 502, 503 and 504
                    fallback_status_codes=[404]
                )
            )
        )
    '''

    def __init__(
        self,
        domain_name: builtins.str,
        *,
        http_port: typing.Optional[jsii.Number] = None,
        https_port: typing.Optional[jsii.Number] = None,
        keepalive_timeout: typing.Optional[_aws_cdk_core_f4b25747.Duration] = None,
        origin_ssl_protocols: typing.Optional[typing.Sequence[_aws_cdk_aws_cloudfront_d69ac3eb.OriginSslPolicy]] = None,
        protocol_policy: typing.Optional[_aws_cdk_aws_cloudfront_d69ac3eb.OriginProtocolPolicy] = None,
        read_timeout: typing.Optional[_aws_cdk_core_f4b25747.Duration] = None,
        origin_path: typing.Optional[builtins.str] = None,
        connection_attempts: typing.Optional[jsii.Number] = None,
        connection_timeout: typing.Optional[_aws_cdk_core_f4b25747.Duration] = None,
        custom_headers: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        origin_shield_region: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param domain_name: -
        :param http_port: The HTTP port that CloudFront uses to connect to the origin. Default: 80
        :param https_port: The HTTPS port that CloudFront uses to connect to the origin. Default: 443
        :param keepalive_timeout: Specifies how long, in seconds, CloudFront persists its connection to the origin. The valid range is from 1 to 180 seconds, inclusive. Note that values over 60 seconds are possible only after a limit increase request for the origin response timeout quota has been approved in the target account; otherwise, values over 60 seconds will produce an error at deploy time. Default: Duration.seconds(5)
        :param origin_ssl_protocols: The SSL versions to use when interacting with the origin. Default: OriginSslPolicy.TLS_V1_2
        :param protocol_policy: Specifies the protocol (HTTP or HTTPS) that CloudFront uses to connect to the origin. Default: OriginProtocolPolicy.HTTPS_ONLY
        :param read_timeout: Specifies how long, in seconds, CloudFront waits for a response from the origin, also known as the origin response timeout. The valid range is from 1 to 180 seconds, inclusive. Note that values over 60 seconds are possible only after a limit increase request for the origin response timeout quota has been approved in the target account; otherwise, values over 60 seconds will produce an error at deploy time. Default: Duration.seconds(30)
        :param origin_path: An optional path that CloudFront appends to the origin domain name when CloudFront requests content from the origin. Must begin, but not end, with '/' (e.g., '/production/images'). Default: '/'
        :param connection_attempts: The number of times that CloudFront attempts to connect to the origin; valid values are 1, 2, or 3 attempts. Default: 3
        :param connection_timeout: The number of seconds that CloudFront waits when trying to establish a connection to the origin. Valid values are 1-10 seconds, inclusive. Default: Duration.seconds(10)
        :param custom_headers: A list of HTTP header names and values that CloudFront adds to requests it sends to the origin. Default: {}
        :param origin_shield_region: When you enable Origin Shield in the AWS Region that has the lowest latency to your origin, you can get better network performance. Default: - origin shield not enabled
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__80556d712d11fb2bd89cd3782060b31fd9a00cb8c9dd7b82ff3fe7041c080c41)
            check_type(argname="argument domain_name", value=domain_name, expected_type=type_hints["domain_name"])
        props = HttpOriginProps(
            http_port=http_port,
            https_port=https_port,
            keepalive_timeout=keepalive_timeout,
            origin_ssl_protocols=origin_ssl_protocols,
            protocol_policy=protocol_policy,
            read_timeout=read_timeout,
            origin_path=origin_path,
            connection_attempts=connection_attempts,
            connection_timeout=connection_timeout,
            custom_headers=custom_headers,
            origin_shield_region=origin_shield_region,
        )

        jsii.create(self.__class__, self, [domain_name, props])

    @jsii.member(jsii_name="renderCustomOriginConfig")
    def _render_custom_origin_config(
        self,
    ) -> typing.Optional[_aws_cdk_aws_cloudfront_d69ac3eb.CfnDistribution.CustomOriginConfigProperty]:
        return typing.cast(typing.Optional[_aws_cdk_aws_cloudfront_d69ac3eb.CfnDistribution.CustomOriginConfigProperty], jsii.invoke(self, "renderCustomOriginConfig", []))


@jsii.data_type(
    jsii_type="@aws-cdk/aws-cloudfront-origins.HttpOriginProps",
    jsii_struct_bases=[_aws_cdk_aws_cloudfront_d69ac3eb.OriginProps],
    name_mapping={
        "connection_attempts": "connectionAttempts",
        "connection_timeout": "connectionTimeout",
        "custom_headers": "customHeaders",
        "origin_shield_region": "originShieldRegion",
        "origin_path": "originPath",
        "http_port": "httpPort",
        "https_port": "httpsPort",
        "keepalive_timeout": "keepaliveTimeout",
        "origin_ssl_protocols": "originSslProtocols",
        "protocol_policy": "protocolPolicy",
        "read_timeout": "readTimeout",
    },
)
class HttpOriginProps(_aws_cdk_aws_cloudfront_d69ac3eb.OriginProps):
    def __init__(
        self,
        *,
        connection_attempts: typing.Optional[jsii.Number] = None,
        connection_timeout: typing.Optional[_aws_cdk_core_f4b25747.Duration] = None,
        custom_headers: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        origin_shield_region: typing.Optional[builtins.str] = None,
        origin_path: typing.Optional[builtins.str] = None,
        http_port: typing.Optional[jsii.Number] = None,
        https_port: typing.Optional[jsii.Number] = None,
        keepalive_timeout: typing.Optional[_aws_cdk_core_f4b25747.Duration] = None,
        origin_ssl_protocols: typing.Optional[typing.Sequence[_aws_cdk_aws_cloudfront_d69ac3eb.OriginSslPolicy]] = None,
        protocol_policy: typing.Optional[_aws_cdk_aws_cloudfront_d69ac3eb.OriginProtocolPolicy] = None,
        read_timeout: typing.Optional[_aws_cdk_core_f4b25747.Duration] = None,
    ) -> None:
        '''Properties for an Origin backed by an S3 website-configured bucket, load balancer, or custom HTTP server.

        :param connection_attempts: The number of times that CloudFront attempts to connect to the origin; valid values are 1, 2, or 3 attempts. Default: 3
        :param connection_timeout: The number of seconds that CloudFront waits when trying to establish a connection to the origin. Valid values are 1-10 seconds, inclusive. Default: Duration.seconds(10)
        :param custom_headers: A list of HTTP header names and values that CloudFront adds to requests it sends to the origin. Default: {}
        :param origin_shield_region: When you enable Origin Shield in the AWS Region that has the lowest latency to your origin, you can get better network performance. Default: - origin shield not enabled
        :param origin_path: An optional path that CloudFront appends to the origin domain name when CloudFront requests content from the origin. Must begin, but not end, with '/' (e.g., '/production/images'). Default: '/'
        :param http_port: The HTTP port that CloudFront uses to connect to the origin. Default: 80
        :param https_port: The HTTPS port that CloudFront uses to connect to the origin. Default: 443
        :param keepalive_timeout: Specifies how long, in seconds, CloudFront persists its connection to the origin. The valid range is from 1 to 180 seconds, inclusive. Note that values over 60 seconds are possible only after a limit increase request for the origin response timeout quota has been approved in the target account; otherwise, values over 60 seconds will produce an error at deploy time. Default: Duration.seconds(5)
        :param origin_ssl_protocols: The SSL versions to use when interacting with the origin. Default: OriginSslPolicy.TLS_V1_2
        :param protocol_policy: Specifies the protocol (HTTP or HTTPS) that CloudFront uses to connect to the origin. Default: OriginProtocolPolicy.HTTPS_ONLY
        :param read_timeout: Specifies how long, in seconds, CloudFront waits for a response from the origin, also known as the origin response timeout. The valid range is from 1 to 180 seconds, inclusive. Note that values over 60 seconds are possible only after a limit increase request for the origin response timeout quota has been approved in the target account; otherwise, values over 60 seconds will produce an error at deploy time. Default: Duration.seconds(30)

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            import aws_cdk.aws_cloudfront as cloudfront
            import aws_cdk.aws_cloudfront_origins as cloudfront_origins
            import aws_cdk.core as cdk
            
            http_origin_props = cloudfront_origins.HttpOriginProps(
                connection_attempts=123,
                connection_timeout=cdk.Duration.minutes(30),
                custom_headers={
                    "custom_headers_key": "customHeaders"
                },
                http_port=123,
                https_port=123,
                keepalive_timeout=cdk.Duration.minutes(30),
                origin_path="originPath",
                origin_shield_region="originShieldRegion",
                origin_ssl_protocols=[cloudfront.OriginSslPolicy.SSL_V3],
                protocol_policy=cloudfront.OriginProtocolPolicy.HTTP_ONLY,
                read_timeout=cdk.Duration.minutes(30)
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__efab676370935d5817b60974f30035c2debfb370297f5c071ce0372a0ddbe8cc)
            check_type(argname="argument connection_attempts", value=connection_attempts, expected_type=type_hints["connection_attempts"])
            check_type(argname="argument connection_timeout", value=connection_timeout, expected_type=type_hints["connection_timeout"])
            check_type(argname="argument custom_headers", value=custom_headers, expected_type=type_hints["custom_headers"])
            check_type(argname="argument origin_shield_region", value=origin_shield_region, expected_type=type_hints["origin_shield_region"])
            check_type(argname="argument origin_path", value=origin_path, expected_type=type_hints["origin_path"])
            check_type(argname="argument http_port", value=http_port, expected_type=type_hints["http_port"])
            check_type(argname="argument https_port", value=https_port, expected_type=type_hints["https_port"])
            check_type(argname="argument keepalive_timeout", value=keepalive_timeout, expected_type=type_hints["keepalive_timeout"])
            check_type(argname="argument origin_ssl_protocols", value=origin_ssl_protocols, expected_type=type_hints["origin_ssl_protocols"])
            check_type(argname="argument protocol_policy", value=protocol_policy, expected_type=type_hints["protocol_policy"])
            check_type(argname="argument read_timeout", value=read_timeout, expected_type=type_hints["read_timeout"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if connection_attempts is not None:
            self._values["connection_attempts"] = connection_attempts
        if connection_timeout is not None:
            self._values["connection_timeout"] = connection_timeout
        if custom_headers is not None:
            self._values["custom_headers"] = custom_headers
        if origin_shield_region is not None:
            self._values["origin_shield_region"] = origin_shield_region
        if origin_path is not None:
            self._values["origin_path"] = origin_path
        if http_port is not None:
            self._values["http_port"] = http_port
        if https_port is not None:
            self._values["https_port"] = https_port
        if keepalive_timeout is not None:
            self._values["keepalive_timeout"] = keepalive_timeout
        if origin_ssl_protocols is not None:
            self._values["origin_ssl_protocols"] = origin_ssl_protocols
        if protocol_policy is not None:
            self._values["protocol_policy"] = protocol_policy
        if read_timeout is not None:
            self._values["read_timeout"] = read_timeout

    @builtins.property
    def connection_attempts(self) -> typing.Optional[jsii.Number]:
        '''The number of times that CloudFront attempts to connect to the origin;

        valid values are 1, 2, or 3 attempts.

        :default: 3
        '''
        result = self._values.get("connection_attempts")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def connection_timeout(self) -> typing.Optional[_aws_cdk_core_f4b25747.Duration]:
        '''The number of seconds that CloudFront waits when trying to establish a connection to the origin.

        Valid values are 1-10 seconds, inclusive.

        :default: Duration.seconds(10)
        '''
        result = self._values.get("connection_timeout")
        return typing.cast(typing.Optional[_aws_cdk_core_f4b25747.Duration], result)

    @builtins.property
    def custom_headers(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''A list of HTTP header names and values that CloudFront adds to requests it sends to the origin.

        :default: {}
        '''
        result = self._values.get("custom_headers")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def origin_shield_region(self) -> typing.Optional[builtins.str]:
        '''When you enable Origin Shield in the AWS Region that has the lowest latency to your origin, you can get better network performance.

        :default: - origin shield not enabled

        :see: https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/origin-shield.html
        '''
        result = self._values.get("origin_shield_region")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def origin_path(self) -> typing.Optional[builtins.str]:
        '''An optional path that CloudFront appends to the origin domain name when CloudFront requests content from the origin.

        Must begin, but not end, with '/' (e.g., '/production/images').

        :default: '/'
        '''
        result = self._values.get("origin_path")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def http_port(self) -> typing.Optional[jsii.Number]:
        '''The HTTP port that CloudFront uses to connect to the origin.

        :default: 80
        '''
        result = self._values.get("http_port")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def https_port(self) -> typing.Optional[jsii.Number]:
        '''The HTTPS port that CloudFront uses to connect to the origin.

        :default: 443
        '''
        result = self._values.get("https_port")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def keepalive_timeout(self) -> typing.Optional[_aws_cdk_core_f4b25747.Duration]:
        '''Specifies how long, in seconds, CloudFront persists its connection to the origin.

        The valid range is from 1 to 180 seconds, inclusive.

        Note that values over 60 seconds are possible only after a limit increase request for the origin response timeout quota
        has been approved in the target account; otherwise, values over 60 seconds will produce an error at deploy time.

        :default: Duration.seconds(5)
        '''
        result = self._values.get("keepalive_timeout")
        return typing.cast(typing.Optional[_aws_cdk_core_f4b25747.Duration], result)

    @builtins.property
    def origin_ssl_protocols(
        self,
    ) -> typing.Optional[typing.List[_aws_cdk_aws_cloudfront_d69ac3eb.OriginSslPolicy]]:
        '''The SSL versions to use when interacting with the origin.

        :default: OriginSslPolicy.TLS_V1_2
        '''
        result = self._values.get("origin_ssl_protocols")
        return typing.cast(typing.Optional[typing.List[_aws_cdk_aws_cloudfront_d69ac3eb.OriginSslPolicy]], result)

    @builtins.property
    def protocol_policy(
        self,
    ) -> typing.Optional[_aws_cdk_aws_cloudfront_d69ac3eb.OriginProtocolPolicy]:
        '''Specifies the protocol (HTTP or HTTPS) that CloudFront uses to connect to the origin.

        :default: OriginProtocolPolicy.HTTPS_ONLY
        '''
        result = self._values.get("protocol_policy")
        return typing.cast(typing.Optional[_aws_cdk_aws_cloudfront_d69ac3eb.OriginProtocolPolicy], result)

    @builtins.property
    def read_timeout(self) -> typing.Optional[_aws_cdk_core_f4b25747.Duration]:
        '''Specifies how long, in seconds, CloudFront waits for a response from the origin, also known as the origin response timeout.

        The valid range is from 1 to 180 seconds, inclusive.

        Note that values over 60 seconds are possible only after a limit increase request for the origin response timeout quota
        has been approved in the target account; otherwise, values over 60 seconds will produce an error at deploy time.

        :default: Duration.seconds(30)
        '''
        result = self._values.get("read_timeout")
        return typing.cast(typing.Optional[_aws_cdk_core_f4b25747.Duration], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "HttpOriginProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class LoadBalancerV2Origin(
    HttpOrigin,
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/aws-cloudfront-origins.LoadBalancerV2Origin",
):
    '''An Origin for a v2 load balancer.

    :exampleMetadata: infused

    Example::

        import aws_cdk.aws_ec2 as ec2
        import aws_cdk.aws_elasticloadbalancingv2 as elbv2
        
        # vpc: ec2.Vpc
        
        # Create an application load balancer in a VPC. 'internetFacing' must be 'true'
        # for CloudFront to access the load balancer and use it as an origin.
        lb = elbv2.ApplicationLoadBalancer(self, "LB",
            vpc=vpc,
            internet_facing=True
        )
        cloudfront.Distribution(self, "myDist",
            default_behavior=cloudfront.BehaviorOptions(origin=origins.LoadBalancerV2Origin(lb))
        )
    '''

    def __init__(
        self,
        load_balancer: _aws_cdk_aws_elasticloadbalancingv2_e93c784f.ILoadBalancerV2,
        *,
        http_port: typing.Optional[jsii.Number] = None,
        https_port: typing.Optional[jsii.Number] = None,
        keepalive_timeout: typing.Optional[_aws_cdk_core_f4b25747.Duration] = None,
        origin_ssl_protocols: typing.Optional[typing.Sequence[_aws_cdk_aws_cloudfront_d69ac3eb.OriginSslPolicy]] = None,
        protocol_policy: typing.Optional[_aws_cdk_aws_cloudfront_d69ac3eb.OriginProtocolPolicy] = None,
        read_timeout: typing.Optional[_aws_cdk_core_f4b25747.Duration] = None,
        origin_path: typing.Optional[builtins.str] = None,
        connection_attempts: typing.Optional[jsii.Number] = None,
        connection_timeout: typing.Optional[_aws_cdk_core_f4b25747.Duration] = None,
        custom_headers: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        origin_shield_region: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param load_balancer: -
        :param http_port: The HTTP port that CloudFront uses to connect to the origin. Default: 80
        :param https_port: The HTTPS port that CloudFront uses to connect to the origin. Default: 443
        :param keepalive_timeout: Specifies how long, in seconds, CloudFront persists its connection to the origin. The valid range is from 1 to 180 seconds, inclusive. Note that values over 60 seconds are possible only after a limit increase request for the origin response timeout quota has been approved in the target account; otherwise, values over 60 seconds will produce an error at deploy time. Default: Duration.seconds(5)
        :param origin_ssl_protocols: The SSL versions to use when interacting with the origin. Default: OriginSslPolicy.TLS_V1_2
        :param protocol_policy: Specifies the protocol (HTTP or HTTPS) that CloudFront uses to connect to the origin. Default: OriginProtocolPolicy.HTTPS_ONLY
        :param read_timeout: Specifies how long, in seconds, CloudFront waits for a response from the origin, also known as the origin response timeout. The valid range is from 1 to 180 seconds, inclusive. Note that values over 60 seconds are possible only after a limit increase request for the origin response timeout quota has been approved in the target account; otherwise, values over 60 seconds will produce an error at deploy time. Default: Duration.seconds(30)
        :param origin_path: An optional path that CloudFront appends to the origin domain name when CloudFront requests content from the origin. Must begin, but not end, with '/' (e.g., '/production/images'). Default: '/'
        :param connection_attempts: The number of times that CloudFront attempts to connect to the origin; valid values are 1, 2, or 3 attempts. Default: 3
        :param connection_timeout: The number of seconds that CloudFront waits when trying to establish a connection to the origin. Valid values are 1-10 seconds, inclusive. Default: Duration.seconds(10)
        :param custom_headers: A list of HTTP header names and values that CloudFront adds to requests it sends to the origin. Default: {}
        :param origin_shield_region: When you enable Origin Shield in the AWS Region that has the lowest latency to your origin, you can get better network performance. Default: - origin shield not enabled
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ce7b59996e38f581b525a0eb4783a46ca6b6421dc5d2ef4c9e9867669a8e0610)
            check_type(argname="argument load_balancer", value=load_balancer, expected_type=type_hints["load_balancer"])
        props = LoadBalancerV2OriginProps(
            http_port=http_port,
            https_port=https_port,
            keepalive_timeout=keepalive_timeout,
            origin_ssl_protocols=origin_ssl_protocols,
            protocol_policy=protocol_policy,
            read_timeout=read_timeout,
            origin_path=origin_path,
            connection_attempts=connection_attempts,
            connection_timeout=connection_timeout,
            custom_headers=custom_headers,
            origin_shield_region=origin_shield_region,
        )

        jsii.create(self.__class__, self, [load_balancer, props])


@jsii.data_type(
    jsii_type="@aws-cdk/aws-cloudfront-origins.LoadBalancerV2OriginProps",
    jsii_struct_bases=[HttpOriginProps],
    name_mapping={
        "connection_attempts": "connectionAttempts",
        "connection_timeout": "connectionTimeout",
        "custom_headers": "customHeaders",
        "origin_shield_region": "originShieldRegion",
        "origin_path": "originPath",
        "http_port": "httpPort",
        "https_port": "httpsPort",
        "keepalive_timeout": "keepaliveTimeout",
        "origin_ssl_protocols": "originSslProtocols",
        "protocol_policy": "protocolPolicy",
        "read_timeout": "readTimeout",
    },
)
class LoadBalancerV2OriginProps(HttpOriginProps):
    def __init__(
        self,
        *,
        connection_attempts: typing.Optional[jsii.Number] = None,
        connection_timeout: typing.Optional[_aws_cdk_core_f4b25747.Duration] = None,
        custom_headers: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        origin_shield_region: typing.Optional[builtins.str] = None,
        origin_path: typing.Optional[builtins.str] = None,
        http_port: typing.Optional[jsii.Number] = None,
        https_port: typing.Optional[jsii.Number] = None,
        keepalive_timeout: typing.Optional[_aws_cdk_core_f4b25747.Duration] = None,
        origin_ssl_protocols: typing.Optional[typing.Sequence[_aws_cdk_aws_cloudfront_d69ac3eb.OriginSslPolicy]] = None,
        protocol_policy: typing.Optional[_aws_cdk_aws_cloudfront_d69ac3eb.OriginProtocolPolicy] = None,
        read_timeout: typing.Optional[_aws_cdk_core_f4b25747.Duration] = None,
    ) -> None:
        '''Properties for an Origin backed by a v2 load balancer.

        :param connection_attempts: The number of times that CloudFront attempts to connect to the origin; valid values are 1, 2, or 3 attempts. Default: 3
        :param connection_timeout: The number of seconds that CloudFront waits when trying to establish a connection to the origin. Valid values are 1-10 seconds, inclusive. Default: Duration.seconds(10)
        :param custom_headers: A list of HTTP header names and values that CloudFront adds to requests it sends to the origin. Default: {}
        :param origin_shield_region: When you enable Origin Shield in the AWS Region that has the lowest latency to your origin, you can get better network performance. Default: - origin shield not enabled
        :param origin_path: An optional path that CloudFront appends to the origin domain name when CloudFront requests content from the origin. Must begin, but not end, with '/' (e.g., '/production/images'). Default: '/'
        :param http_port: The HTTP port that CloudFront uses to connect to the origin. Default: 80
        :param https_port: The HTTPS port that CloudFront uses to connect to the origin. Default: 443
        :param keepalive_timeout: Specifies how long, in seconds, CloudFront persists its connection to the origin. The valid range is from 1 to 180 seconds, inclusive. Note that values over 60 seconds are possible only after a limit increase request for the origin response timeout quota has been approved in the target account; otherwise, values over 60 seconds will produce an error at deploy time. Default: Duration.seconds(5)
        :param origin_ssl_protocols: The SSL versions to use when interacting with the origin. Default: OriginSslPolicy.TLS_V1_2
        :param protocol_policy: Specifies the protocol (HTTP or HTTPS) that CloudFront uses to connect to the origin. Default: OriginProtocolPolicy.HTTPS_ONLY
        :param read_timeout: Specifies how long, in seconds, CloudFront waits for a response from the origin, also known as the origin response timeout. The valid range is from 1 to 180 seconds, inclusive. Note that values over 60 seconds are possible only after a limit increase request for the origin response timeout quota has been approved in the target account; otherwise, values over 60 seconds will produce an error at deploy time. Default: Duration.seconds(30)

        :exampleMetadata: infused

        Example::

            import aws_cdk.aws_elasticloadbalancingv2 as elbv2
            
            # load_balancer: elbv2.ApplicationLoadBalancer
            
            origin = origins.LoadBalancerV2Origin(load_balancer,
                connection_attempts=3,
                connection_timeout=Duration.seconds(5),
                read_timeout=Duration.seconds(45),
                keepalive_timeout=Duration.seconds(45),
                protocol_policy=cloudfront.OriginProtocolPolicy.MATCH_VIEWER
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bc17e20512d081355cee847e3007d0169cbe851fcf59cb8aedf9337ff4babbcb)
            check_type(argname="argument connection_attempts", value=connection_attempts, expected_type=type_hints["connection_attempts"])
            check_type(argname="argument connection_timeout", value=connection_timeout, expected_type=type_hints["connection_timeout"])
            check_type(argname="argument custom_headers", value=custom_headers, expected_type=type_hints["custom_headers"])
            check_type(argname="argument origin_shield_region", value=origin_shield_region, expected_type=type_hints["origin_shield_region"])
            check_type(argname="argument origin_path", value=origin_path, expected_type=type_hints["origin_path"])
            check_type(argname="argument http_port", value=http_port, expected_type=type_hints["http_port"])
            check_type(argname="argument https_port", value=https_port, expected_type=type_hints["https_port"])
            check_type(argname="argument keepalive_timeout", value=keepalive_timeout, expected_type=type_hints["keepalive_timeout"])
            check_type(argname="argument origin_ssl_protocols", value=origin_ssl_protocols, expected_type=type_hints["origin_ssl_protocols"])
            check_type(argname="argument protocol_policy", value=protocol_policy, expected_type=type_hints["protocol_policy"])
            check_type(argname="argument read_timeout", value=read_timeout, expected_type=type_hints["read_timeout"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if connection_attempts is not None:
            self._values["connection_attempts"] = connection_attempts
        if connection_timeout is not None:
            self._values["connection_timeout"] = connection_timeout
        if custom_headers is not None:
            self._values["custom_headers"] = custom_headers
        if origin_shield_region is not None:
            self._values["origin_shield_region"] = origin_shield_region
        if origin_path is not None:
            self._values["origin_path"] = origin_path
        if http_port is not None:
            self._values["http_port"] = http_port
        if https_port is not None:
            self._values["https_port"] = https_port
        if keepalive_timeout is not None:
            self._values["keepalive_timeout"] = keepalive_timeout
        if origin_ssl_protocols is not None:
            self._values["origin_ssl_protocols"] = origin_ssl_protocols
        if protocol_policy is not None:
            self._values["protocol_policy"] = protocol_policy
        if read_timeout is not None:
            self._values["read_timeout"] = read_timeout

    @builtins.property
    def connection_attempts(self) -> typing.Optional[jsii.Number]:
        '''The number of times that CloudFront attempts to connect to the origin;

        valid values are 1, 2, or 3 attempts.

        :default: 3
        '''
        result = self._values.get("connection_attempts")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def connection_timeout(self) -> typing.Optional[_aws_cdk_core_f4b25747.Duration]:
        '''The number of seconds that CloudFront waits when trying to establish a connection to the origin.

        Valid values are 1-10 seconds, inclusive.

        :default: Duration.seconds(10)
        '''
        result = self._values.get("connection_timeout")
        return typing.cast(typing.Optional[_aws_cdk_core_f4b25747.Duration], result)

    @builtins.property
    def custom_headers(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''A list of HTTP header names and values that CloudFront adds to requests it sends to the origin.

        :default: {}
        '''
        result = self._values.get("custom_headers")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def origin_shield_region(self) -> typing.Optional[builtins.str]:
        '''When you enable Origin Shield in the AWS Region that has the lowest latency to your origin, you can get better network performance.

        :default: - origin shield not enabled

        :see: https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/origin-shield.html
        '''
        result = self._values.get("origin_shield_region")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def origin_path(self) -> typing.Optional[builtins.str]:
        '''An optional path that CloudFront appends to the origin domain name when CloudFront requests content from the origin.

        Must begin, but not end, with '/' (e.g., '/production/images').

        :default: '/'
        '''
        result = self._values.get("origin_path")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def http_port(self) -> typing.Optional[jsii.Number]:
        '''The HTTP port that CloudFront uses to connect to the origin.

        :default: 80
        '''
        result = self._values.get("http_port")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def https_port(self) -> typing.Optional[jsii.Number]:
        '''The HTTPS port that CloudFront uses to connect to the origin.

        :default: 443
        '''
        result = self._values.get("https_port")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def keepalive_timeout(self) -> typing.Optional[_aws_cdk_core_f4b25747.Duration]:
        '''Specifies how long, in seconds, CloudFront persists its connection to the origin.

        The valid range is from 1 to 180 seconds, inclusive.

        Note that values over 60 seconds are possible only after a limit increase request for the origin response timeout quota
        has been approved in the target account; otherwise, values over 60 seconds will produce an error at deploy time.

        :default: Duration.seconds(5)
        '''
        result = self._values.get("keepalive_timeout")
        return typing.cast(typing.Optional[_aws_cdk_core_f4b25747.Duration], result)

    @builtins.property
    def origin_ssl_protocols(
        self,
    ) -> typing.Optional[typing.List[_aws_cdk_aws_cloudfront_d69ac3eb.OriginSslPolicy]]:
        '''The SSL versions to use when interacting with the origin.

        :default: OriginSslPolicy.TLS_V1_2
        '''
        result = self._values.get("origin_ssl_protocols")
        return typing.cast(typing.Optional[typing.List[_aws_cdk_aws_cloudfront_d69ac3eb.OriginSslPolicy]], result)

    @builtins.property
    def protocol_policy(
        self,
    ) -> typing.Optional[_aws_cdk_aws_cloudfront_d69ac3eb.OriginProtocolPolicy]:
        '''Specifies the protocol (HTTP or HTTPS) that CloudFront uses to connect to the origin.

        :default: OriginProtocolPolicy.HTTPS_ONLY
        '''
        result = self._values.get("protocol_policy")
        return typing.cast(typing.Optional[_aws_cdk_aws_cloudfront_d69ac3eb.OriginProtocolPolicy], result)

    @builtins.property
    def read_timeout(self) -> typing.Optional[_aws_cdk_core_f4b25747.Duration]:
        '''Specifies how long, in seconds, CloudFront waits for a response from the origin, also known as the origin response timeout.

        The valid range is from 1 to 180 seconds, inclusive.

        Note that values over 60 seconds are possible only after a limit increase request for the origin response timeout quota
        has been approved in the target account; otherwise, values over 60 seconds will produce an error at deploy time.

        :default: Duration.seconds(30)
        '''
        result = self._values.get("read_timeout")
        return typing.cast(typing.Optional[_aws_cdk_core_f4b25747.Duration], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LoadBalancerV2OriginProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_aws_cdk_aws_cloudfront_d69ac3eb.IOrigin)
class OriginGroup(
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/aws-cloudfront-origins.OriginGroup",
):
    '''An Origin that represents a group.

    Consists of a primary Origin,
    and a fallback Origin called when the primary returns one of the provided HTTP status codes.

    :exampleMetadata: infused

    Example::

        my_bucket = s3.Bucket(self, "myBucket")
        cloudfront.Distribution(self, "myDist",
            default_behavior=cloudfront.BehaviorOptions(
                origin=origins.OriginGroup(
                    primary_origin=origins.S3Origin(my_bucket),
                    fallback_origin=origins.HttpOrigin("www.example.com"),
                    # optional, defaults to: 500, 502, 503 and 504
                    fallback_status_codes=[404]
                )
            )
        )
    '''

    def __init__(
        self,
        *,
        fallback_origin: _aws_cdk_aws_cloudfront_d69ac3eb.IOrigin,
        primary_origin: _aws_cdk_aws_cloudfront_d69ac3eb.IOrigin,
        fallback_status_codes: typing.Optional[typing.Sequence[jsii.Number]] = None,
    ) -> None:
        '''
        :param fallback_origin: The fallback origin that should serve requests when the primary fails.
        :param primary_origin: The primary origin that should serve requests for this group.
        :param fallback_status_codes: The list of HTTP status codes that, when returned from the primary origin, would cause querying the fallback origin. Default: - 500, 502, 503 and 504
        '''
        props = OriginGroupProps(
            fallback_origin=fallback_origin,
            primary_origin=primary_origin,
            fallback_status_codes=fallback_status_codes,
        )

        jsii.create(self.__class__, self, [props])

    @jsii.member(jsii_name="bind")
    def bind(
        self,
        scope: _aws_cdk_core_f4b25747.Construct,
        *,
        origin_id: builtins.str,
    ) -> _aws_cdk_aws_cloudfront_d69ac3eb.OriginBindConfig:
        '''The method called when a given Origin is added (for the first time) to a Distribution.

        :param scope: -
        :param origin_id: The identifier of this Origin, as assigned by the Distribution this Origin has been used added to.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2e893186fb7ee6bc9c220b875ec95e92397950e15397e9b99f34aa2fe5890e17)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
        options = _aws_cdk_aws_cloudfront_d69ac3eb.OriginBindOptions(
            origin_id=origin_id
        )

        return typing.cast(_aws_cdk_aws_cloudfront_d69ac3eb.OriginBindConfig, jsii.invoke(self, "bind", [scope, options]))


@jsii.data_type(
    jsii_type="@aws-cdk/aws-cloudfront-origins.OriginGroupProps",
    jsii_struct_bases=[],
    name_mapping={
        "fallback_origin": "fallbackOrigin",
        "primary_origin": "primaryOrigin",
        "fallback_status_codes": "fallbackStatusCodes",
    },
)
class OriginGroupProps:
    def __init__(
        self,
        *,
        fallback_origin: _aws_cdk_aws_cloudfront_d69ac3eb.IOrigin,
        primary_origin: _aws_cdk_aws_cloudfront_d69ac3eb.IOrigin,
        fallback_status_codes: typing.Optional[typing.Sequence[jsii.Number]] = None,
    ) -> None:
        '''Construction properties for {@link OriginGroup}.

        :param fallback_origin: The fallback origin that should serve requests when the primary fails.
        :param primary_origin: The primary origin that should serve requests for this group.
        :param fallback_status_codes: The list of HTTP status codes that, when returned from the primary origin, would cause querying the fallback origin. Default: - 500, 502, 503 and 504

        :exampleMetadata: infused

        Example::

            my_bucket = s3.Bucket(self, "myBucket")
            cloudfront.Distribution(self, "myDist",
                default_behavior=cloudfront.BehaviorOptions(
                    origin=origins.OriginGroup(
                        primary_origin=origins.S3Origin(my_bucket),
                        fallback_origin=origins.HttpOrigin("www.example.com"),
                        # optional, defaults to: 500, 502, 503 and 504
                        fallback_status_codes=[404]
                    )
                )
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9ab5299e4307e2e8c2d38920556956772b2fb0ce3f42ca3719e43a91d7e4101a)
            check_type(argname="argument fallback_origin", value=fallback_origin, expected_type=type_hints["fallback_origin"])
            check_type(argname="argument primary_origin", value=primary_origin, expected_type=type_hints["primary_origin"])
            check_type(argname="argument fallback_status_codes", value=fallback_status_codes, expected_type=type_hints["fallback_status_codes"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "fallback_origin": fallback_origin,
            "primary_origin": primary_origin,
        }
        if fallback_status_codes is not None:
            self._values["fallback_status_codes"] = fallback_status_codes

    @builtins.property
    def fallback_origin(self) -> _aws_cdk_aws_cloudfront_d69ac3eb.IOrigin:
        '''The fallback origin that should serve requests when the primary fails.'''
        result = self._values.get("fallback_origin")
        assert result is not None, "Required property 'fallback_origin' is missing"
        return typing.cast(_aws_cdk_aws_cloudfront_d69ac3eb.IOrigin, result)

    @builtins.property
    def primary_origin(self) -> _aws_cdk_aws_cloudfront_d69ac3eb.IOrigin:
        '''The primary origin that should serve requests for this group.'''
        result = self._values.get("primary_origin")
        assert result is not None, "Required property 'primary_origin' is missing"
        return typing.cast(_aws_cdk_aws_cloudfront_d69ac3eb.IOrigin, result)

    @builtins.property
    def fallback_status_codes(self) -> typing.Optional[typing.List[jsii.Number]]:
        '''The list of HTTP status codes that, when returned from the primary origin, would cause querying the fallback origin.

        :default: - 500, 502, 503 and 504
        '''
        result = self._values.get("fallback_status_codes")
        return typing.cast(typing.Optional[typing.List[jsii.Number]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "OriginGroupProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class RestApiOrigin(
    _aws_cdk_aws_cloudfront_d69ac3eb.OriginBase,
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/aws-cloudfront-origins.RestApiOrigin",
):
    '''An Origin for an API Gateway REST API.

    :exampleMetadata: infused

    Example::

        # api: apigateway.RestApi
        
        cloudfront.Distribution(self, "Distribution",
            default_behavior=cloudfront.BehaviorOptions(origin=origins.RestApiOrigin(api))
        )
    '''

    def __init__(
        self,
        rest_api: _aws_cdk_aws_apigateway_f01c2838.RestApi,
        *,
        keepalive_timeout: typing.Optional[_aws_cdk_core_f4b25747.Duration] = None,
        read_timeout: typing.Optional[_aws_cdk_core_f4b25747.Duration] = None,
        connection_attempts: typing.Optional[jsii.Number] = None,
        connection_timeout: typing.Optional[_aws_cdk_core_f4b25747.Duration] = None,
        custom_headers: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        origin_shield_region: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param rest_api: -
        :param keepalive_timeout: Specifies how long, in seconds, CloudFront persists its connection to the origin. The valid range is from 1 to 180 seconds, inclusive. Note that values over 60 seconds are possible only after a limit increase request for the origin response timeout quota has been approved in the target account; otherwise, values over 60 seconds will produce an error at deploy time. Default: Duration.seconds(5)
        :param read_timeout: Specifies how long, in seconds, CloudFront waits for a response from the origin, also known as the origin response timeout. The valid range is from 1 to 180 seconds, inclusive. Note that values over 60 seconds are possible only after a limit increase request for the origin response timeout quota has been approved in the target account; otherwise, values over 60 seconds will produce an error at deploy time. Default: Duration.seconds(30)
        :param connection_attempts: The number of times that CloudFront attempts to connect to the origin; valid values are 1, 2, or 3 attempts. Default: 3
        :param connection_timeout: The number of seconds that CloudFront waits when trying to establish a connection to the origin. Valid values are 1-10 seconds, inclusive. Default: Duration.seconds(10)
        :param custom_headers: A list of HTTP header names and values that CloudFront adds to requests it sends to the origin. Default: {}
        :param origin_shield_region: When you enable Origin Shield in the AWS Region that has the lowest latency to your origin, you can get better network performance. Default: - origin shield not enabled
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2dbeba11af2d4cd02be40baa2ec15dc5faa24916b7dbf0adbff6a19b75d2f6cf)
            check_type(argname="argument rest_api", value=rest_api, expected_type=type_hints["rest_api"])
        props = RestApiOriginProps(
            keepalive_timeout=keepalive_timeout,
            read_timeout=read_timeout,
            connection_attempts=connection_attempts,
            connection_timeout=connection_timeout,
            custom_headers=custom_headers,
            origin_shield_region=origin_shield_region,
        )

        jsii.create(self.__class__, self, [rest_api, props])

    @jsii.member(jsii_name="renderCustomOriginConfig")
    def _render_custom_origin_config(
        self,
    ) -> typing.Optional[_aws_cdk_aws_cloudfront_d69ac3eb.CfnDistribution.CustomOriginConfigProperty]:
        return typing.cast(typing.Optional[_aws_cdk_aws_cloudfront_d69ac3eb.CfnDistribution.CustomOriginConfigProperty], jsii.invoke(self, "renderCustomOriginConfig", []))


@jsii.data_type(
    jsii_type="@aws-cdk/aws-cloudfront-origins.RestApiOriginProps",
    jsii_struct_bases=[_aws_cdk_aws_cloudfront_d69ac3eb.OriginOptions],
    name_mapping={
        "connection_attempts": "connectionAttempts",
        "connection_timeout": "connectionTimeout",
        "custom_headers": "customHeaders",
        "origin_shield_region": "originShieldRegion",
        "keepalive_timeout": "keepaliveTimeout",
        "read_timeout": "readTimeout",
    },
)
class RestApiOriginProps(_aws_cdk_aws_cloudfront_d69ac3eb.OriginOptions):
    def __init__(
        self,
        *,
        connection_attempts: typing.Optional[jsii.Number] = None,
        connection_timeout: typing.Optional[_aws_cdk_core_f4b25747.Duration] = None,
        custom_headers: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        origin_shield_region: typing.Optional[builtins.str] = None,
        keepalive_timeout: typing.Optional[_aws_cdk_core_f4b25747.Duration] = None,
        read_timeout: typing.Optional[_aws_cdk_core_f4b25747.Duration] = None,
    ) -> None:
        '''Properties for an Origin for an API Gateway REST API.

        :param connection_attempts: The number of times that CloudFront attempts to connect to the origin; valid values are 1, 2, or 3 attempts. Default: 3
        :param connection_timeout: The number of seconds that CloudFront waits when trying to establish a connection to the origin. Valid values are 1-10 seconds, inclusive. Default: Duration.seconds(10)
        :param custom_headers: A list of HTTP header names and values that CloudFront adds to requests it sends to the origin. Default: {}
        :param origin_shield_region: When you enable Origin Shield in the AWS Region that has the lowest latency to your origin, you can get better network performance. Default: - origin shield not enabled
        :param keepalive_timeout: Specifies how long, in seconds, CloudFront persists its connection to the origin. The valid range is from 1 to 180 seconds, inclusive. Note that values over 60 seconds are possible only after a limit increase request for the origin response timeout quota has been approved in the target account; otherwise, values over 60 seconds will produce an error at deploy time. Default: Duration.seconds(5)
        :param read_timeout: Specifies how long, in seconds, CloudFront waits for a response from the origin, also known as the origin response timeout. The valid range is from 1 to 180 seconds, inclusive. Note that values over 60 seconds are possible only after a limit increase request for the origin response timeout quota has been approved in the target account; otherwise, values over 60 seconds will produce an error at deploy time. Default: Duration.seconds(30)

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            import aws_cdk.aws_cloudfront_origins as cloudfront_origins
            import aws_cdk.core as cdk
            
            rest_api_origin_props = cloudfront_origins.RestApiOriginProps(
                connection_attempts=123,
                connection_timeout=cdk.Duration.minutes(30),
                custom_headers={
                    "custom_headers_key": "customHeaders"
                },
                keepalive_timeout=cdk.Duration.minutes(30),
                origin_shield_region="originShieldRegion",
                read_timeout=cdk.Duration.minutes(30)
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__da56733ceafa5514eb555bb4499476983f4a9eefb50c60343162a33e80079e5c)
            check_type(argname="argument connection_attempts", value=connection_attempts, expected_type=type_hints["connection_attempts"])
            check_type(argname="argument connection_timeout", value=connection_timeout, expected_type=type_hints["connection_timeout"])
            check_type(argname="argument custom_headers", value=custom_headers, expected_type=type_hints["custom_headers"])
            check_type(argname="argument origin_shield_region", value=origin_shield_region, expected_type=type_hints["origin_shield_region"])
            check_type(argname="argument keepalive_timeout", value=keepalive_timeout, expected_type=type_hints["keepalive_timeout"])
            check_type(argname="argument read_timeout", value=read_timeout, expected_type=type_hints["read_timeout"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if connection_attempts is not None:
            self._values["connection_attempts"] = connection_attempts
        if connection_timeout is not None:
            self._values["connection_timeout"] = connection_timeout
        if custom_headers is not None:
            self._values["custom_headers"] = custom_headers
        if origin_shield_region is not None:
            self._values["origin_shield_region"] = origin_shield_region
        if keepalive_timeout is not None:
            self._values["keepalive_timeout"] = keepalive_timeout
        if read_timeout is not None:
            self._values["read_timeout"] = read_timeout

    @builtins.property
    def connection_attempts(self) -> typing.Optional[jsii.Number]:
        '''The number of times that CloudFront attempts to connect to the origin;

        valid values are 1, 2, or 3 attempts.

        :default: 3
        '''
        result = self._values.get("connection_attempts")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def connection_timeout(self) -> typing.Optional[_aws_cdk_core_f4b25747.Duration]:
        '''The number of seconds that CloudFront waits when trying to establish a connection to the origin.

        Valid values are 1-10 seconds, inclusive.

        :default: Duration.seconds(10)
        '''
        result = self._values.get("connection_timeout")
        return typing.cast(typing.Optional[_aws_cdk_core_f4b25747.Duration], result)

    @builtins.property
    def custom_headers(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''A list of HTTP header names and values that CloudFront adds to requests it sends to the origin.

        :default: {}
        '''
        result = self._values.get("custom_headers")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def origin_shield_region(self) -> typing.Optional[builtins.str]:
        '''When you enable Origin Shield in the AWS Region that has the lowest latency to your origin, you can get better network performance.

        :default: - origin shield not enabled

        :see: https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/origin-shield.html
        '''
        result = self._values.get("origin_shield_region")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def keepalive_timeout(self) -> typing.Optional[_aws_cdk_core_f4b25747.Duration]:
        '''Specifies how long, in seconds, CloudFront persists its connection to the origin.

        The valid range is from 1 to 180 seconds, inclusive.

        Note that values over 60 seconds are possible only after a limit increase request for the origin response timeout quota
        has been approved in the target account; otherwise, values over 60 seconds will produce an error at deploy time.

        :default: Duration.seconds(5)
        '''
        result = self._values.get("keepalive_timeout")
        return typing.cast(typing.Optional[_aws_cdk_core_f4b25747.Duration], result)

    @builtins.property
    def read_timeout(self) -> typing.Optional[_aws_cdk_core_f4b25747.Duration]:
        '''Specifies how long, in seconds, CloudFront waits for a response from the origin, also known as the origin response timeout.

        The valid range is from 1 to 180 seconds, inclusive.

        Note that values over 60 seconds are possible only after a limit increase request for the origin response timeout quota
        has been approved in the target account; otherwise, values over 60 seconds will produce an error at deploy time.

        :default: Duration.seconds(30)
        '''
        result = self._values.get("read_timeout")
        return typing.cast(typing.Optional[_aws_cdk_core_f4b25747.Duration], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "RestApiOriginProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_aws_cdk_aws_cloudfront_d69ac3eb.IOrigin)
class S3Origin(
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/aws-cloudfront-origins.S3Origin",
):
    '''An Origin that is backed by an S3 bucket.

    If the bucket is configured for website hosting, this origin will be configured to use the bucket as an
    HTTP server origin and will use the bucket's configured website redirects and error handling. Otherwise,
    the origin is created as a bucket origin and will use CloudFront's redirect and error handling.

    :exampleMetadata: infused

    Example::

        # Adding an existing Lambda@Edge function created in a different stack
        # to a CloudFront distribution.
        # s3_bucket: s3.Bucket
        
        function_version = lambda_.Version.from_version_arn(self, "Version", "arn:aws:lambda:us-east-1:123456789012:function:functionName:1")
        
        cloudfront.Distribution(self, "distro",
            default_behavior=cloudfront.BehaviorOptions(
                origin=origins.S3Origin(s3_bucket),
                edge_lambdas=[cloudfront.EdgeLambda(
                    function_version=function_version,
                    event_type=cloudfront.LambdaEdgeEventType.VIEWER_REQUEST
                )
                ]
            )
        )
    '''

    def __init__(
        self,
        bucket: _aws_cdk_aws_s3_55f001a5.IBucket,
        *,
        origin_access_identity: typing.Optional[_aws_cdk_aws_cloudfront_d69ac3eb.IOriginAccessIdentity] = None,
        origin_path: typing.Optional[builtins.str] = None,
        connection_attempts: typing.Optional[jsii.Number] = None,
        connection_timeout: typing.Optional[_aws_cdk_core_f4b25747.Duration] = None,
        custom_headers: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        origin_shield_region: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param bucket: -
        :param origin_access_identity: An optional Origin Access Identity of the origin identity cloudfront will use when calling your s3 bucket. Default: - An Origin Access Identity will be created.
        :param origin_path: An optional path that CloudFront appends to the origin domain name when CloudFront requests content from the origin. Must begin, but not end, with '/' (e.g., '/production/images'). Default: '/'
        :param connection_attempts: The number of times that CloudFront attempts to connect to the origin; valid values are 1, 2, or 3 attempts. Default: 3
        :param connection_timeout: The number of seconds that CloudFront waits when trying to establish a connection to the origin. Valid values are 1-10 seconds, inclusive. Default: Duration.seconds(10)
        :param custom_headers: A list of HTTP header names and values that CloudFront adds to requests it sends to the origin. Default: {}
        :param origin_shield_region: When you enable Origin Shield in the AWS Region that has the lowest latency to your origin, you can get better network performance. Default: - origin shield not enabled
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__449a2194c8f9663dc39059b68cb71db6c3e5755939a8230f6c2dce29221d4536)
            check_type(argname="argument bucket", value=bucket, expected_type=type_hints["bucket"])
        props = S3OriginProps(
            origin_access_identity=origin_access_identity,
            origin_path=origin_path,
            connection_attempts=connection_attempts,
            connection_timeout=connection_timeout,
            custom_headers=custom_headers,
            origin_shield_region=origin_shield_region,
        )

        jsii.create(self.__class__, self, [bucket, props])

    @jsii.member(jsii_name="bind")
    def bind(
        self,
        scope: _aws_cdk_core_f4b25747.Construct,
        *,
        origin_id: builtins.str,
    ) -> _aws_cdk_aws_cloudfront_d69ac3eb.OriginBindConfig:
        '''The method called when a given Origin is added (for the first time) to a Distribution.

        :param scope: -
        :param origin_id: The identifier of this Origin, as assigned by the Distribution this Origin has been used added to.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__330b1efffbbd43a06790400595de8147376e9c2a95dad3f2841ecfef437b6d4a)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
        options = _aws_cdk_aws_cloudfront_d69ac3eb.OriginBindOptions(
            origin_id=origin_id
        )

        return typing.cast(_aws_cdk_aws_cloudfront_d69ac3eb.OriginBindConfig, jsii.invoke(self, "bind", [scope, options]))


@jsii.data_type(
    jsii_type="@aws-cdk/aws-cloudfront-origins.S3OriginProps",
    jsii_struct_bases=[_aws_cdk_aws_cloudfront_d69ac3eb.OriginProps],
    name_mapping={
        "connection_attempts": "connectionAttempts",
        "connection_timeout": "connectionTimeout",
        "custom_headers": "customHeaders",
        "origin_shield_region": "originShieldRegion",
        "origin_path": "originPath",
        "origin_access_identity": "originAccessIdentity",
    },
)
class S3OriginProps(_aws_cdk_aws_cloudfront_d69ac3eb.OriginProps):
    def __init__(
        self,
        *,
        connection_attempts: typing.Optional[jsii.Number] = None,
        connection_timeout: typing.Optional[_aws_cdk_core_f4b25747.Duration] = None,
        custom_headers: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        origin_shield_region: typing.Optional[builtins.str] = None,
        origin_path: typing.Optional[builtins.str] = None,
        origin_access_identity: typing.Optional[_aws_cdk_aws_cloudfront_d69ac3eb.IOriginAccessIdentity] = None,
    ) -> None:
        '''Properties to use to customize an S3 Origin.

        :param connection_attempts: The number of times that CloudFront attempts to connect to the origin; valid values are 1, 2, or 3 attempts. Default: 3
        :param connection_timeout: The number of seconds that CloudFront waits when trying to establish a connection to the origin. Valid values are 1-10 seconds, inclusive. Default: Duration.seconds(10)
        :param custom_headers: A list of HTTP header names and values that CloudFront adds to requests it sends to the origin. Default: {}
        :param origin_shield_region: When you enable Origin Shield in the AWS Region that has the lowest latency to your origin, you can get better network performance. Default: - origin shield not enabled
        :param origin_path: An optional path that CloudFront appends to the origin domain name when CloudFront requests content from the origin. Must begin, but not end, with '/' (e.g., '/production/images'). Default: '/'
        :param origin_access_identity: An optional Origin Access Identity of the origin identity cloudfront will use when calling your s3 bucket. Default: - An Origin Access Identity will be created.

        :exampleMetadata: infused

        Example::

            my_bucket = s3.Bucket(self, "myBucket")
            cloudfront.Distribution(self, "myDist",
                default_behavior=cloudfront.BehaviorOptions(origin=origins.S3Origin(my_bucket,
                    custom_headers={
                        "Foo": "bar"
                    }
                ))
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fb74a563d4e1d6d29240bd853f374f8f927865e97f6c5bb40cb8ee9467ccd5c8)
            check_type(argname="argument connection_attempts", value=connection_attempts, expected_type=type_hints["connection_attempts"])
            check_type(argname="argument connection_timeout", value=connection_timeout, expected_type=type_hints["connection_timeout"])
            check_type(argname="argument custom_headers", value=custom_headers, expected_type=type_hints["custom_headers"])
            check_type(argname="argument origin_shield_region", value=origin_shield_region, expected_type=type_hints["origin_shield_region"])
            check_type(argname="argument origin_path", value=origin_path, expected_type=type_hints["origin_path"])
            check_type(argname="argument origin_access_identity", value=origin_access_identity, expected_type=type_hints["origin_access_identity"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if connection_attempts is not None:
            self._values["connection_attempts"] = connection_attempts
        if connection_timeout is not None:
            self._values["connection_timeout"] = connection_timeout
        if custom_headers is not None:
            self._values["custom_headers"] = custom_headers
        if origin_shield_region is not None:
            self._values["origin_shield_region"] = origin_shield_region
        if origin_path is not None:
            self._values["origin_path"] = origin_path
        if origin_access_identity is not None:
            self._values["origin_access_identity"] = origin_access_identity

    @builtins.property
    def connection_attempts(self) -> typing.Optional[jsii.Number]:
        '''The number of times that CloudFront attempts to connect to the origin;

        valid values are 1, 2, or 3 attempts.

        :default: 3
        '''
        result = self._values.get("connection_attempts")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def connection_timeout(self) -> typing.Optional[_aws_cdk_core_f4b25747.Duration]:
        '''The number of seconds that CloudFront waits when trying to establish a connection to the origin.

        Valid values are 1-10 seconds, inclusive.

        :default: Duration.seconds(10)
        '''
        result = self._values.get("connection_timeout")
        return typing.cast(typing.Optional[_aws_cdk_core_f4b25747.Duration], result)

    @builtins.property
    def custom_headers(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''A list of HTTP header names and values that CloudFront adds to requests it sends to the origin.

        :default: {}
        '''
        result = self._values.get("custom_headers")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def origin_shield_region(self) -> typing.Optional[builtins.str]:
        '''When you enable Origin Shield in the AWS Region that has the lowest latency to your origin, you can get better network performance.

        :default: - origin shield not enabled

        :see: https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/origin-shield.html
        '''
        result = self._values.get("origin_shield_region")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def origin_path(self) -> typing.Optional[builtins.str]:
        '''An optional path that CloudFront appends to the origin domain name when CloudFront requests content from the origin.

        Must begin, but not end, with '/' (e.g., '/production/images').

        :default: '/'
        '''
        result = self._values.get("origin_path")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def origin_access_identity(
        self,
    ) -> typing.Optional[_aws_cdk_aws_cloudfront_d69ac3eb.IOriginAccessIdentity]:
        '''An optional Origin Access Identity of the origin identity cloudfront will use when calling your s3 bucket.

        :default: - An Origin Access Identity will be created.
        '''
        result = self._values.get("origin_access_identity")
        return typing.cast(typing.Optional[_aws_cdk_aws_cloudfront_d69ac3eb.IOriginAccessIdentity], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "S3OriginProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "HttpOrigin",
    "HttpOriginProps",
    "LoadBalancerV2Origin",
    "LoadBalancerV2OriginProps",
    "OriginGroup",
    "OriginGroupProps",
    "RestApiOrigin",
    "RestApiOriginProps",
    "S3Origin",
    "S3OriginProps",
]

publication.publish()

def _typecheckingstub__80556d712d11fb2bd89cd3782060b31fd9a00cb8c9dd7b82ff3fe7041c080c41(
    domain_name: builtins.str,
    *,
    http_port: typing.Optional[jsii.Number] = None,
    https_port: typing.Optional[jsii.Number] = None,
    keepalive_timeout: typing.Optional[_aws_cdk_core_f4b25747.Duration] = None,
    origin_ssl_protocols: typing.Optional[typing.Sequence[_aws_cdk_aws_cloudfront_d69ac3eb.OriginSslPolicy]] = None,
    protocol_policy: typing.Optional[_aws_cdk_aws_cloudfront_d69ac3eb.OriginProtocolPolicy] = None,
    read_timeout: typing.Optional[_aws_cdk_core_f4b25747.Duration] = None,
    origin_path: typing.Optional[builtins.str] = None,
    connection_attempts: typing.Optional[jsii.Number] = None,
    connection_timeout: typing.Optional[_aws_cdk_core_f4b25747.Duration] = None,
    custom_headers: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    origin_shield_region: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__efab676370935d5817b60974f30035c2debfb370297f5c071ce0372a0ddbe8cc(
    *,
    connection_attempts: typing.Optional[jsii.Number] = None,
    connection_timeout: typing.Optional[_aws_cdk_core_f4b25747.Duration] = None,
    custom_headers: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    origin_shield_region: typing.Optional[builtins.str] = None,
    origin_path: typing.Optional[builtins.str] = None,
    http_port: typing.Optional[jsii.Number] = None,
    https_port: typing.Optional[jsii.Number] = None,
    keepalive_timeout: typing.Optional[_aws_cdk_core_f4b25747.Duration] = None,
    origin_ssl_protocols: typing.Optional[typing.Sequence[_aws_cdk_aws_cloudfront_d69ac3eb.OriginSslPolicy]] = None,
    protocol_policy: typing.Optional[_aws_cdk_aws_cloudfront_d69ac3eb.OriginProtocolPolicy] = None,
    read_timeout: typing.Optional[_aws_cdk_core_f4b25747.Duration] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ce7b59996e38f581b525a0eb4783a46ca6b6421dc5d2ef4c9e9867669a8e0610(
    load_balancer: _aws_cdk_aws_elasticloadbalancingv2_e93c784f.ILoadBalancerV2,
    *,
    http_port: typing.Optional[jsii.Number] = None,
    https_port: typing.Optional[jsii.Number] = None,
    keepalive_timeout: typing.Optional[_aws_cdk_core_f4b25747.Duration] = None,
    origin_ssl_protocols: typing.Optional[typing.Sequence[_aws_cdk_aws_cloudfront_d69ac3eb.OriginSslPolicy]] = None,
    protocol_policy: typing.Optional[_aws_cdk_aws_cloudfront_d69ac3eb.OriginProtocolPolicy] = None,
    read_timeout: typing.Optional[_aws_cdk_core_f4b25747.Duration] = None,
    origin_path: typing.Optional[builtins.str] = None,
    connection_attempts: typing.Optional[jsii.Number] = None,
    connection_timeout: typing.Optional[_aws_cdk_core_f4b25747.Duration] = None,
    custom_headers: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    origin_shield_region: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bc17e20512d081355cee847e3007d0169cbe851fcf59cb8aedf9337ff4babbcb(
    *,
    connection_attempts: typing.Optional[jsii.Number] = None,
    connection_timeout: typing.Optional[_aws_cdk_core_f4b25747.Duration] = None,
    custom_headers: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    origin_shield_region: typing.Optional[builtins.str] = None,
    origin_path: typing.Optional[builtins.str] = None,
    http_port: typing.Optional[jsii.Number] = None,
    https_port: typing.Optional[jsii.Number] = None,
    keepalive_timeout: typing.Optional[_aws_cdk_core_f4b25747.Duration] = None,
    origin_ssl_protocols: typing.Optional[typing.Sequence[_aws_cdk_aws_cloudfront_d69ac3eb.OriginSslPolicy]] = None,
    protocol_policy: typing.Optional[_aws_cdk_aws_cloudfront_d69ac3eb.OriginProtocolPolicy] = None,
    read_timeout: typing.Optional[_aws_cdk_core_f4b25747.Duration] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2e893186fb7ee6bc9c220b875ec95e92397950e15397e9b99f34aa2fe5890e17(
    scope: _aws_cdk_core_f4b25747.Construct,
    *,
    origin_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9ab5299e4307e2e8c2d38920556956772b2fb0ce3f42ca3719e43a91d7e4101a(
    *,
    fallback_origin: _aws_cdk_aws_cloudfront_d69ac3eb.IOrigin,
    primary_origin: _aws_cdk_aws_cloudfront_d69ac3eb.IOrigin,
    fallback_status_codes: typing.Optional[typing.Sequence[jsii.Number]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2dbeba11af2d4cd02be40baa2ec15dc5faa24916b7dbf0adbff6a19b75d2f6cf(
    rest_api: _aws_cdk_aws_apigateway_f01c2838.RestApi,
    *,
    keepalive_timeout: typing.Optional[_aws_cdk_core_f4b25747.Duration] = None,
    read_timeout: typing.Optional[_aws_cdk_core_f4b25747.Duration] = None,
    connection_attempts: typing.Optional[jsii.Number] = None,
    connection_timeout: typing.Optional[_aws_cdk_core_f4b25747.Duration] = None,
    custom_headers: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    origin_shield_region: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__da56733ceafa5514eb555bb4499476983f4a9eefb50c60343162a33e80079e5c(
    *,
    connection_attempts: typing.Optional[jsii.Number] = None,
    connection_timeout: typing.Optional[_aws_cdk_core_f4b25747.Duration] = None,
    custom_headers: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    origin_shield_region: typing.Optional[builtins.str] = None,
    keepalive_timeout: typing.Optional[_aws_cdk_core_f4b25747.Duration] = None,
    read_timeout: typing.Optional[_aws_cdk_core_f4b25747.Duration] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__449a2194c8f9663dc39059b68cb71db6c3e5755939a8230f6c2dce29221d4536(
    bucket: _aws_cdk_aws_s3_55f001a5.IBucket,
    *,
    origin_access_identity: typing.Optional[_aws_cdk_aws_cloudfront_d69ac3eb.IOriginAccessIdentity] = None,
    origin_path: typing.Optional[builtins.str] = None,
    connection_attempts: typing.Optional[jsii.Number] = None,
    connection_timeout: typing.Optional[_aws_cdk_core_f4b25747.Duration] = None,
    custom_headers: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    origin_shield_region: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__330b1efffbbd43a06790400595de8147376e9c2a95dad3f2841ecfef437b6d4a(
    scope: _aws_cdk_core_f4b25747.Construct,
    *,
    origin_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fb74a563d4e1d6d29240bd853f374f8f927865e97f6c5bb40cb8ee9467ccd5c8(
    *,
    connection_attempts: typing.Optional[jsii.Number] = None,
    connection_timeout: typing.Optional[_aws_cdk_core_f4b25747.Duration] = None,
    custom_headers: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    origin_shield_region: typing.Optional[builtins.str] = None,
    origin_path: typing.Optional[builtins.str] = None,
    origin_access_identity: typing.Optional[_aws_cdk_aws_cloudfront_d69ac3eb.IOriginAccessIdentity] = None,
) -> None:
    """Type checking stubs"""
    pass
