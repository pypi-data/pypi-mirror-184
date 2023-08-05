'''
# Actions for AWS Elastic Load Balancing V2

<!--BEGIN STABILITY BANNER-->---


![cdk-constructs: Stable](https://img.shields.io/badge/cdk--constructs-stable-success.svg?style=for-the-badge)

---
<!--END STABILITY BANNER-->

This package contains integration actions for ELBv2. See the README of the `@aws-cdk/aws-elasticloadbalancingv2` library.

## Cognito

ELB allows for requests to be authenticated against a Cognito user pool using
the `AuthenticateCognitoAction`. For details on the setup's requirements,
read [Prepare to use Amazon
Cognito](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/listener-authenticate-users.html#cognito-requirements).
Here's an example:

```python
import aws_cdk.aws_cognito as cognito
import aws_cdk.aws_ec2 as ec2
import aws_cdk.aws_elasticloadbalancingv2 as elbv2
from aws_cdk.core import App, CfnOutput, Stack
from constructs import Construct
import aws_cdk.aws_elasticloadbalancingv2_actions as actions

Stack): lb = elbv2.ApplicationLoadBalancer(self, "LB",
    vpc=vpc,
    internet_facing=True
)

user_pool = cognito.UserPool(self, "UserPool")
user_pool_client = cognito.UserPoolClient(self, "Client",
    user_pool=user_pool,

    # Required minimal configuration for use with an ELB
    generate_secret=True,
    auth_flows=cognito.AuthFlow(
        user_password=True
    ),
    o_auth=cognito.OAuthSettings(
        flows=cognito.OAuthFlows(
            authorization_code_grant=True
        ),
        scopes=[cognito.OAuthScope.EMAIL],
        callback_urls=[f"https://{lb.loadBalancerDnsName}/oauth2/idpresponse"
        ]
    )
)
cfn_client = user_pool_client.node.default_child
cfn_client.add_property_override("RefreshTokenValidity", 1)
cfn_client.add_property_override("SupportedIdentityProviders", ["COGNITO"])

user_pool_domain = cognito.UserPoolDomain(self, "Domain",
    user_pool=user_pool,
    cognito_domain=cognito.CognitoDomainOptions(
        domain_prefix="test-cdk-prefix"
    )
)

lb.add_listener("Listener",
    port=443,
    certificates=[certificate],
    default_action=actions.AuthenticateCognitoAction(
        user_pool=user_pool,
        user_pool_client=user_pool_client,
        user_pool_domain=user_pool_domain,
        next=elbv2.ListenerAction.fixed_response(200,
            content_type="text/plain",
            message_body="Authenticated"
        )
    )
)

CfnOutput(self, "DNS",
    value=lb.load_balancer_dns_name
)

app = App()
CognitoStack(app, "integ-cognito")
app.synth()
```

> NOTE: this example seems incomplete, I was not able to get the redirect back to the
> Load Balancer after authentication working. Would love some pointers on what a full working
> setup actually looks like!
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

import aws_cdk.aws_cognito as _aws_cdk_aws_cognito_371ee794
import aws_cdk.aws_elasticloadbalancingv2 as _aws_cdk_aws_elasticloadbalancingv2_e93c784f
import aws_cdk.core as _aws_cdk_core_f4b25747


class AuthenticateCognitoAction(
    _aws_cdk_aws_elasticloadbalancingv2_e93c784f.ListenerAction,
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/aws-elasticloadbalancingv2-actions.AuthenticateCognitoAction",
):
    '''A Listener Action to authenticate with Cognito.

    :exampleMetadata: lit=test/integ.cognito.lit.ts infused

    Example::

        import aws_cdk.aws_cognito as cognito
        import aws_cdk.aws_ec2 as ec2
        import aws_cdk.aws_elasticloadbalancingv2 as elbv2
        from aws_cdk.core import App, CfnOutput, Stack
        from constructs import Construct
        import aws_cdk.aws_elasticloadbalancingv2_actions as actions
        
        Stack): lb = elbv2.ApplicationLoadBalancer(self, "LB",
            vpc=vpc,
            internet_facing=True
        )
        
        user_pool = cognito.UserPool(self, "UserPool")
        user_pool_client = cognito.UserPoolClient(self, "Client",
            user_pool=user_pool,
        
            # Required minimal configuration for use with an ELB
            generate_secret=True,
            auth_flows=cognito.AuthFlow(
                user_password=True
            ),
            o_auth=cognito.OAuthSettings(
                flows=cognito.OAuthFlows(
                    authorization_code_grant=True
                ),
                scopes=[cognito.OAuthScope.EMAIL],
                callback_urls=[f"https://{lb.loadBalancerDnsName}/oauth2/idpresponse"
                ]
            )
        )
        cfn_client = user_pool_client.node.default_child
        cfn_client.add_property_override("RefreshTokenValidity", 1)
        cfn_client.add_property_override("SupportedIdentityProviders", ["COGNITO"])
        
        user_pool_domain = cognito.UserPoolDomain(self, "Domain",
            user_pool=user_pool,
            cognito_domain=cognito.CognitoDomainOptions(
                domain_prefix="test-cdk-prefix"
            )
        )
        
        lb.add_listener("Listener",
            port=443,
            certificates=[certificate],
            default_action=actions.AuthenticateCognitoAction(
                user_pool=user_pool,
                user_pool_client=user_pool_client,
                user_pool_domain=user_pool_domain,
                next=elbv2.ListenerAction.fixed_response(200,
                    content_type="text/plain",
                    message_body="Authenticated"
                )
            )
        )
        
        CfnOutput(self, "DNS",
            value=lb.load_balancer_dns_name
        )
        
        app = App()
        CognitoStack(app, "integ-cognito")
        app.synth()
    '''

    def __init__(
        self,
        *,
        next: _aws_cdk_aws_elasticloadbalancingv2_e93c784f.ListenerAction,
        user_pool: _aws_cdk_aws_cognito_371ee794.IUserPool,
        user_pool_client: _aws_cdk_aws_cognito_371ee794.IUserPoolClient,
        user_pool_domain: _aws_cdk_aws_cognito_371ee794.IUserPoolDomain,
        authentication_request_extra_params: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        on_unauthenticated_request: typing.Optional[_aws_cdk_aws_elasticloadbalancingv2_e93c784f.UnauthenticatedAction] = None,
        scope: typing.Optional[builtins.str] = None,
        session_cookie_name: typing.Optional[builtins.str] = None,
        session_timeout: typing.Optional[_aws_cdk_core_f4b25747.Duration] = None,
    ) -> None:
        '''Authenticate using an identity provide (IdP) that is compliant with OpenID Connect (OIDC).

        :param next: What action to execute next. Multiple actions form a linked chain; the chain must always terminate in a (weighted)forward, fixedResponse or redirect action.
        :param user_pool: The Amazon Cognito user pool.
        :param user_pool_client: The Amazon Cognito user pool client.
        :param user_pool_domain: The domain prefix or fully-qualified domain name of the Amazon Cognito user pool.
        :param authentication_request_extra_params: The query parameters (up to 10) to include in the redirect request to the authorization endpoint. Default: - No extra parameters
        :param on_unauthenticated_request: The behavior if the user is not authenticated. Default: UnauthenticatedAction.AUTHENTICATE
        :param scope: The set of user claims to be requested from the IdP. To verify which scope values your IdP supports and how to separate multiple values, see the documentation for your IdP. Default: "openid"
        :param session_cookie_name: The name of the cookie used to maintain session information. Default: "AWSELBAuthSessionCookie"
        :param session_timeout: The maximum duration of the authentication session. Default: Duration.days(7)
        '''
        options = AuthenticateCognitoActionProps(
            next=next,
            user_pool=user_pool,
            user_pool_client=user_pool_client,
            user_pool_domain=user_pool_domain,
            authentication_request_extra_params=authentication_request_extra_params,
            on_unauthenticated_request=on_unauthenticated_request,
            scope=scope,
            session_cookie_name=session_cookie_name,
            session_timeout=session_timeout,
        )

        jsii.create(self.__class__, self, [options])


@jsii.data_type(
    jsii_type="@aws-cdk/aws-elasticloadbalancingv2-actions.AuthenticateCognitoActionProps",
    jsii_struct_bases=[],
    name_mapping={
        "next": "next",
        "user_pool": "userPool",
        "user_pool_client": "userPoolClient",
        "user_pool_domain": "userPoolDomain",
        "authentication_request_extra_params": "authenticationRequestExtraParams",
        "on_unauthenticated_request": "onUnauthenticatedRequest",
        "scope": "scope",
        "session_cookie_name": "sessionCookieName",
        "session_timeout": "sessionTimeout",
    },
)
class AuthenticateCognitoActionProps:
    def __init__(
        self,
        *,
        next: _aws_cdk_aws_elasticloadbalancingv2_e93c784f.ListenerAction,
        user_pool: _aws_cdk_aws_cognito_371ee794.IUserPool,
        user_pool_client: _aws_cdk_aws_cognito_371ee794.IUserPoolClient,
        user_pool_domain: _aws_cdk_aws_cognito_371ee794.IUserPoolDomain,
        authentication_request_extra_params: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        on_unauthenticated_request: typing.Optional[_aws_cdk_aws_elasticloadbalancingv2_e93c784f.UnauthenticatedAction] = None,
        scope: typing.Optional[builtins.str] = None,
        session_cookie_name: typing.Optional[builtins.str] = None,
        session_timeout: typing.Optional[_aws_cdk_core_f4b25747.Duration] = None,
    ) -> None:
        '''Properties for AuthenticateCognitoAction.

        :param next: What action to execute next. Multiple actions form a linked chain; the chain must always terminate in a (weighted)forward, fixedResponse or redirect action.
        :param user_pool: The Amazon Cognito user pool.
        :param user_pool_client: The Amazon Cognito user pool client.
        :param user_pool_domain: The domain prefix or fully-qualified domain name of the Amazon Cognito user pool.
        :param authentication_request_extra_params: The query parameters (up to 10) to include in the redirect request to the authorization endpoint. Default: - No extra parameters
        :param on_unauthenticated_request: The behavior if the user is not authenticated. Default: UnauthenticatedAction.AUTHENTICATE
        :param scope: The set of user claims to be requested from the IdP. To verify which scope values your IdP supports and how to separate multiple values, see the documentation for your IdP. Default: "openid"
        :param session_cookie_name: The name of the cookie used to maintain session information. Default: "AWSELBAuthSessionCookie"
        :param session_timeout: The maximum duration of the authentication session. Default: Duration.days(7)

        :exampleMetadata: lit=test/integ.cognito.lit.ts infused

        Example::

            import aws_cdk.aws_cognito as cognito
            import aws_cdk.aws_ec2 as ec2
            import aws_cdk.aws_elasticloadbalancingv2 as elbv2
            from aws_cdk.core import App, CfnOutput, Stack
            from constructs import Construct
            import aws_cdk.aws_elasticloadbalancingv2_actions as actions
            
            Stack): lb = elbv2.ApplicationLoadBalancer(self, "LB",
                vpc=vpc,
                internet_facing=True
            )
            
            user_pool = cognito.UserPool(self, "UserPool")
            user_pool_client = cognito.UserPoolClient(self, "Client",
                user_pool=user_pool,
            
                # Required minimal configuration for use with an ELB
                generate_secret=True,
                auth_flows=cognito.AuthFlow(
                    user_password=True
                ),
                o_auth=cognito.OAuthSettings(
                    flows=cognito.OAuthFlows(
                        authorization_code_grant=True
                    ),
                    scopes=[cognito.OAuthScope.EMAIL],
                    callback_urls=[f"https://{lb.loadBalancerDnsName}/oauth2/idpresponse"
                    ]
                )
            )
            cfn_client = user_pool_client.node.default_child
            cfn_client.add_property_override("RefreshTokenValidity", 1)
            cfn_client.add_property_override("SupportedIdentityProviders", ["COGNITO"])
            
            user_pool_domain = cognito.UserPoolDomain(self, "Domain",
                user_pool=user_pool,
                cognito_domain=cognito.CognitoDomainOptions(
                    domain_prefix="test-cdk-prefix"
                )
            )
            
            lb.add_listener("Listener",
                port=443,
                certificates=[certificate],
                default_action=actions.AuthenticateCognitoAction(
                    user_pool=user_pool,
                    user_pool_client=user_pool_client,
                    user_pool_domain=user_pool_domain,
                    next=elbv2.ListenerAction.fixed_response(200,
                        content_type="text/plain",
                        message_body="Authenticated"
                    )
                )
            )
            
            CfnOutput(self, "DNS",
                value=lb.load_balancer_dns_name
            )
            
            app = App()
            CognitoStack(app, "integ-cognito")
            app.synth()
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fbce001587e055b7c08d47f6e7ff3bf6e3f598eb42912711ad6a7de73ce43fcc)
            check_type(argname="argument next", value=next, expected_type=type_hints["next"])
            check_type(argname="argument user_pool", value=user_pool, expected_type=type_hints["user_pool"])
            check_type(argname="argument user_pool_client", value=user_pool_client, expected_type=type_hints["user_pool_client"])
            check_type(argname="argument user_pool_domain", value=user_pool_domain, expected_type=type_hints["user_pool_domain"])
            check_type(argname="argument authentication_request_extra_params", value=authentication_request_extra_params, expected_type=type_hints["authentication_request_extra_params"])
            check_type(argname="argument on_unauthenticated_request", value=on_unauthenticated_request, expected_type=type_hints["on_unauthenticated_request"])
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument session_cookie_name", value=session_cookie_name, expected_type=type_hints["session_cookie_name"])
            check_type(argname="argument session_timeout", value=session_timeout, expected_type=type_hints["session_timeout"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "next": next,
            "user_pool": user_pool,
            "user_pool_client": user_pool_client,
            "user_pool_domain": user_pool_domain,
        }
        if authentication_request_extra_params is not None:
            self._values["authentication_request_extra_params"] = authentication_request_extra_params
        if on_unauthenticated_request is not None:
            self._values["on_unauthenticated_request"] = on_unauthenticated_request
        if scope is not None:
            self._values["scope"] = scope
        if session_cookie_name is not None:
            self._values["session_cookie_name"] = session_cookie_name
        if session_timeout is not None:
            self._values["session_timeout"] = session_timeout

    @builtins.property
    def next(self) -> _aws_cdk_aws_elasticloadbalancingv2_e93c784f.ListenerAction:
        '''What action to execute next.

        Multiple actions form a linked chain; the chain must always terminate in a
        (weighted)forward, fixedResponse or redirect action.
        '''
        result = self._values.get("next")
        assert result is not None, "Required property 'next' is missing"
        return typing.cast(_aws_cdk_aws_elasticloadbalancingv2_e93c784f.ListenerAction, result)

    @builtins.property
    def user_pool(self) -> _aws_cdk_aws_cognito_371ee794.IUserPool:
        '''The Amazon Cognito user pool.'''
        result = self._values.get("user_pool")
        assert result is not None, "Required property 'user_pool' is missing"
        return typing.cast(_aws_cdk_aws_cognito_371ee794.IUserPool, result)

    @builtins.property
    def user_pool_client(self) -> _aws_cdk_aws_cognito_371ee794.IUserPoolClient:
        '''The Amazon Cognito user pool client.'''
        result = self._values.get("user_pool_client")
        assert result is not None, "Required property 'user_pool_client' is missing"
        return typing.cast(_aws_cdk_aws_cognito_371ee794.IUserPoolClient, result)

    @builtins.property
    def user_pool_domain(self) -> _aws_cdk_aws_cognito_371ee794.IUserPoolDomain:
        '''The domain prefix or fully-qualified domain name of the Amazon Cognito user pool.'''
        result = self._values.get("user_pool_domain")
        assert result is not None, "Required property 'user_pool_domain' is missing"
        return typing.cast(_aws_cdk_aws_cognito_371ee794.IUserPoolDomain, result)

    @builtins.property
    def authentication_request_extra_params(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''The query parameters (up to 10) to include in the redirect request to the authorization endpoint.

        :default: - No extra parameters
        '''
        result = self._values.get("authentication_request_extra_params")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def on_unauthenticated_request(
        self,
    ) -> typing.Optional[_aws_cdk_aws_elasticloadbalancingv2_e93c784f.UnauthenticatedAction]:
        '''The behavior if the user is not authenticated.

        :default: UnauthenticatedAction.AUTHENTICATE
        '''
        result = self._values.get("on_unauthenticated_request")
        return typing.cast(typing.Optional[_aws_cdk_aws_elasticloadbalancingv2_e93c784f.UnauthenticatedAction], result)

    @builtins.property
    def scope(self) -> typing.Optional[builtins.str]:
        '''The set of user claims to be requested from the IdP.

        To verify which scope values your IdP supports and how to separate multiple values, see the documentation for your IdP.

        :default: "openid"
        '''
        result = self._values.get("scope")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def session_cookie_name(self) -> typing.Optional[builtins.str]:
        '''The name of the cookie used to maintain session information.

        :default: "AWSELBAuthSessionCookie"
        '''
        result = self._values.get("session_cookie_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def session_timeout(self) -> typing.Optional[_aws_cdk_core_f4b25747.Duration]:
        '''The maximum duration of the authentication session.

        :default: Duration.days(7)
        '''
        result = self._values.get("session_timeout")
        return typing.cast(typing.Optional[_aws_cdk_core_f4b25747.Duration], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AuthenticateCognitoActionProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "AuthenticateCognitoAction",
    "AuthenticateCognitoActionProps",
]

publication.publish()

def _typecheckingstub__fbce001587e055b7c08d47f6e7ff3bf6e3f598eb42912711ad6a7de73ce43fcc(
    *,
    next: _aws_cdk_aws_elasticloadbalancingv2_e93c784f.ListenerAction,
    user_pool: _aws_cdk_aws_cognito_371ee794.IUserPool,
    user_pool_client: _aws_cdk_aws_cognito_371ee794.IUserPoolClient,
    user_pool_domain: _aws_cdk_aws_cognito_371ee794.IUserPoolDomain,
    authentication_request_extra_params: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    on_unauthenticated_request: typing.Optional[_aws_cdk_aws_elasticloadbalancingv2_e93c784f.UnauthenticatedAction] = None,
    scope: typing.Optional[builtins.str] = None,
    session_cookie_name: typing.Optional[builtins.str] = None,
    session_timeout: typing.Optional[_aws_cdk_core_f4b25747.Duration] = None,
) -> None:
    """Type checking stubs"""
    pass
