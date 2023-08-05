'''
# AWS AppSync Construct Library

<!--BEGIN STABILITY BANNER-->---


![cdk-constructs: Experimental](https://img.shields.io/badge/cdk--constructs-experimental-important.svg?style=for-the-badge)

> The APIs of higher level constructs in this module are experimental and under active development.
> They are subject to non-backward compatible changes or removal in any future version. These are
> not subject to the [Semantic Versioning](https://semver.org/) model and breaking changes will be
> announced in the release notes. This means that while you may use them, you may need to update
> your source code when upgrading to a newer version of this package.

---
<!--END STABILITY BANNER-->

The `@aws-cdk/aws-appsync` package contains constructs for building flexible
APIs that use GraphQL.

```python
import aws_cdk.aws_appsync_alpha as appsync
```

## Example

### DynamoDB

Example of a GraphQL API with `AWS_IAM` [authorization](#authorization) resolving into a DynamoDb
backend data source.

GraphQL schema file `schema.graphql`:

```gql
type demo {
  id: String!
  version: String!
}
type Query {
  getDemos: [ demo! ]
}
input DemoInput {
  version: String!
}
type Mutation {
  addDemo(input: DemoInput!): demo
}
```

CDK stack file `app-stack.ts`:

```python
api = appsync.GraphqlApi(self, "Api",
    name="demo",
    schema=appsync.SchemaFile.from_asset(path.join(__dirname, "schema.graphql")),
    authorization_config=appsync.AuthorizationConfig(
        default_authorization=appsync.AuthorizationMode(
            authorization_type=appsync.AuthorizationType.IAM
        )
    ),
    xray_enabled=True
)

demo_table = dynamodb.Table(self, "DemoTable",
    partition_key=dynamodb.Attribute(
        name="id",
        type=dynamodb.AttributeType.STRING
    )
)

demo_dS = api.add_dynamo_db_data_source("demoDataSource", demo_table)

# Resolver for the Query "getDemos" that scans the DynamoDb table and returns the entire list.
# Resolver Mapping Template Reference:
# https://docs.aws.amazon.com/appsync/latest/devguide/resolver-mapping-template-reference-dynamodb.html
demo_dS.create_resolver("QueryGetDemosResolver",
    type_name="Query",
    field_name="getDemos",
    request_mapping_template=appsync.MappingTemplate.dynamo_db_scan_table(),
    response_mapping_template=appsync.MappingTemplate.dynamo_db_result_list()
)

# Resolver for the Mutation "addDemo" that puts the item into the DynamoDb table.
demo_dS.create_resolver("MutationAddDemoResolver",
    type_name="Mutation",
    field_name="addDemo",
    request_mapping_template=appsync.MappingTemplate.dynamo_db_put_item(
        appsync.PrimaryKey.partition("id").auto(),
        appsync.Values.projecting("input")),
    response_mapping_template=appsync.MappingTemplate.dynamo_db_result_item()
)

# To enable DynamoDB read consistency with the `MappingTemplate`:
demo_dS.create_resolver("QueryGetDemosConsistentResolver",
    type_name="Query",
    field_name="getDemosConsistent",
    request_mapping_template=appsync.MappingTemplate.dynamo_db_scan_table(True),
    response_mapping_template=appsync.MappingTemplate.dynamo_db_result_list()
)
```

### Aurora Serverless

AppSync provides a data source for executing SQL commands against Amazon Aurora
Serverless clusters. You can use AppSync resolvers to execute SQL statements
against the Data API with GraphQL queries, mutations, and subscriptions.

```python
# Build a data source for AppSync to access the database.
# api: appsync.GraphqlApi
# Create username and password secret for DB Cluster
secret = rds.DatabaseSecret(self, "AuroraSecret",
    username="clusteradmin"
)

# The VPC to place the cluster in
vpc = ec2.Vpc(self, "AuroraVpc")

# Create the serverless cluster, provide all values needed to customise the database.
cluster = rds.ServerlessCluster(self, "AuroraCluster",
    engine=rds.DatabaseClusterEngine.AURORA_MYSQL,
    vpc=vpc,
    credentials={"username": "clusteradmin"},
    cluster_identifier="db-endpoint-test",
    default_database_name="demos"
)
rds_dS = api.add_rds_data_source("rds", cluster, secret, "demos")

# Set up a resolver for an RDS query.
rds_dS.create_resolver("QueryGetDemosRdsResolver",
    type_name="Query",
    field_name="getDemosRds",
    request_mapping_template=appsync.MappingTemplate.from_string("""
          {
            "version": "2018-05-29",
            "statements": [
              "SELECT * FROM demos"
            ]
          }
          """),
    response_mapping_template=appsync.MappingTemplate.from_string("""
            $utils.toJson($utils.rds.toJsonObject($ctx.result)[0])
          """)
)

# Set up a resolver for an RDS mutation.
rds_dS.create_resolver("MutationAddDemoRdsResolver",
    type_name="Mutation",
    field_name="addDemoRds",
    request_mapping_template=appsync.MappingTemplate.from_string("""
          {
            "version": "2018-05-29",
            "statements": [
              "INSERT INTO demos VALUES (:id, :version)",
              "SELECT * WHERE id = :id"
            ],
            "variableMap": {
              ":id": $util.toJson($util.autoId()),
              ":version": $util.toJson($ctx.args.version)
            }
          }
          """),
    response_mapping_template=appsync.MappingTemplate.from_string("""
            $utils.toJson($utils.rds.toJsonObject($ctx.result)[1][0])
          """)
)
```

### HTTP Endpoints

GraphQL schema file `schema.graphql`:

```gql
type job {
  id: String!
  version: String!
}

input DemoInput {
  version: String!
}

type Mutation {
  callStepFunction(input: DemoInput!): job
}
```

GraphQL request mapping template `request.vtl`:

```json
{
  "version": "2018-05-29",
  "method": "POST",
  "resourcePath": "/",
  "params": {
    "headers": {
      "content-type": "application/x-amz-json-1.0",
      "x-amz-target":"AWSStepFunctions.StartExecution"
    },
    "body": {
      "stateMachineArn": "<your step functions arn>",
      "input": "{ \"id\": \"$context.arguments.id\" }"
    }
  }
}
```

GraphQL response mapping template `response.vtl`:

```json
{
  "id": "${context.result.id}"
}
```

CDK stack file `app-stack.ts`:

```python
api = appsync.GraphqlApi(self, "api",
    name="api",
    schema=appsync.SchemaFile.from_asset(path.join(__dirname, "schema.graphql"))
)

http_ds = api.add_http_data_source("ds", "https://states.amazonaws.com",
    name="httpDsWithStepF",
    description="from appsync to StepFunctions Workflow",
    authorization_config=appsync.AwsIamConfig(
        signing_region="us-east-1",
        signing_service_name="states"
    )
)

http_ds.create_resolver("MutationCallStepFunctionResolver",
    type_name="Mutation",
    field_name="callStepFunction",
    request_mapping_template=appsync.MappingTemplate.from_file("request.vtl"),
    response_mapping_template=appsync.MappingTemplate.from_file("response.vtl")
)
```

### Amazon OpenSearch Service

AppSync has builtin support for Amazon OpenSearch Service (successor to Amazon
Elasticsearch Service) from domains that are provisioned through your AWS account. You can
use AppSync resolvers to perform GraphQL operations such as queries, mutations, and
subscriptions.

```python
import aws_cdk.aws_opensearchservice as opensearch

# api: appsync.GraphqlApi


user = iam.User(self, "User")
domain = opensearch.Domain(self, "Domain",
    version=opensearch.EngineVersion.OPENSEARCH_1_3,
    removal_policy=RemovalPolicy.DESTROY,
    fine_grained_access_control=opensearch.AdvancedSecurityOptions(master_user_arn=user.user_arn),
    encryption_at_rest=opensearch.EncryptionAtRestOptions(enabled=True),
    node_to_node_encryption=True,
    enforce_https=True
)
ds = api.add_open_search_data_source("ds", domain)

ds.create_resolver("QueryGetTestsResolver",
    type_name="Query",
    field_name="getTests",
    request_mapping_template=appsync.MappingTemplate.from_string(JSON.stringify({
        "version": "2017-02-28",
        "operation": "GET",
        "path": "/id/post/_search",
        "params": {
            "headers": {},
            "query_string": {},
            "body": {"from": 0, "size": 50}
        }
    })),
    response_mapping_template=appsync.MappingTemplate.from_string("""[
            #foreach($entry in $context.result.hits.hits)
            #if( $velocityCount > 1 ) , #end
            $utils.toJson($entry.get("_source"))
            #end
          ]""")
)
```

## Custom Domain Names

For many use cases you may want to associate a custom domain name with your
GraphQL API. This can be done during the API creation.

```python
import aws_cdk.aws_certificatemanager as acm
import aws_cdk.aws_route53 as route53

# hosted zone and route53 features
# hosted_zone_id: str
zone_name = "example.com"


my_domain_name = "api.example.com"
certificate = acm.Certificate(self, "cert", domain_name=my_domain_name)
schema = appsync.SchemaFile(file_path="mySchemaFile")
api = appsync.GraphqlApi(self, "api",
    name="myApi",
    schema=schema,
    domain_name=appsync.DomainOptions(
        certificate=certificate,
        domain_name=my_domain_name
    )
)

# hosted zone for adding appsync domain
zone = route53.HostedZone.from_hosted_zone_attributes(self, "HostedZone",
    hosted_zone_id=hosted_zone_id,
    zone_name=zone_name
)

# create a cname to the appsync domain. will map to something like xxxx.cloudfront.net
route53.CnameRecord(self, "CnameApiRecord",
    record_name="api",
    zone=zone,
    domain_name=api.app_sync_domain_name
)
```

## Log Group

AppSync automatically create a log group with the name `/aws/appsync/apis/<graphql_api_id>` upon deployment with
log data set to never expire. If you want to set a different expiration period, use the `logConfig.retention` property.

To obtain the GraphQL API's log group as a `logs.ILogGroup` use the `logGroup` property of the
`GraphqlApi` construct.

```python
import aws_cdk.aws_logs as logs


log_config = appsync.LogConfig(
    retention=logs.RetentionDays.ONE_WEEK
)

appsync.GraphqlApi(self, "api",
    authorization_config=appsync.AuthorizationConfig(),
    name="myApi",
    schema=appsync.SchemaFile.from_asset(path.join(__dirname, "myApi.graphql")),
    log_config=log_config
)
```

## Schema

You can define a schema using from a local file using `SchemaFile.fromAsset`

```python
api = appsync.GraphqlApi(self, "api",
    name="myApi",
    schema=appsync.SchemaFile.from_asset(path.join(__dirname, "schema.graphl"))
)
```

### ISchema

Alternative schema sources can be defined by implementing the `ISchema`
interface. An example of this is the `CodeFirstSchema` class provided in
[awscdk-appsync-utils](https://github.com/cdklabs/awscdk-appsync-utils)

## Imports

Any GraphQL Api that has been created outside the stack can be imported from
another stack into your CDK app. Utilizing the `fromXxx` function, you have
the ability to add data sources and resolvers through a `IGraphqlApi` interface.

```python
# api: appsync.GraphqlApi
# table: dynamodb.Table

imported_api = appsync.GraphqlApi.from_graphql_api_attributes(self, "IApi",
    graphql_api_id=api.api_id,
    graphql_api_arn=api.arn
)
imported_api.add_dynamo_db_data_source("TableDataSource", table)
```

If you don't specify `graphqlArn` in `fromXxxAttributes`, CDK will autogenerate
the expected `arn` for the imported api, given the `apiId`. For creating data
sources and resolvers, an `apiId` is sufficient.

## Authorization

There are multiple authorization types available for GraphQL API to cater to different
access use cases. They are:

* API Keys (`AuthorizationType.API_KEY`)
* Amazon Cognito User Pools (`AuthorizationType.USER_POOL`)
* OpenID Connect (`AuthorizationType.OPENID_CONNECT`)
* AWS Identity and Access Management (`AuthorizationType.AWS_IAM`)
* AWS Lambda (`AuthorizationType.AWS_LAMBDA`)

These types can be used simultaneously in a single API, allowing different types of clients to
access data. When you specify an authorization type, you can also specify the corresponding
authorization mode to finish defining your authorization. For example, this is a GraphQL API
with AWS Lambda Authorization.

```python
import aws_cdk.aws_lambda as lambda_
# auth_function: lambda.Function


appsync.GraphqlApi(self, "api",
    name="api",
    schema=appsync.SchemaFile.from_asset(path.join(__dirname, "appsync.test.graphql")),
    authorization_config=appsync.AuthorizationConfig(
        default_authorization=appsync.AuthorizationMode(
            authorization_type=appsync.AuthorizationType.LAMBDA,
            lambda_authorizer_config=appsync.LambdaAuthorizerConfig(
                handler=auth_function
            )
        )
    )
)
```

## Permissions

When using `AWS_IAM` as the authorization type for GraphQL API, an IAM Role
with correct permissions must be used for access to API.

When configuring permissions, you can specify specific resources to only be
accessible by `IAM` authorization. For example, if you want to only allow mutability
for `IAM` authorized access you would configure the following.

In `schema.graphql`:

```gql
type Mutation {
  updateExample(...): ...
    @aws_iam
}
```

In `IAM`:

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "appsync:GraphQL"
      ],
      "Resource": [
        "arn:aws:appsync:REGION:ACCOUNT_ID:apis/GRAPHQL_ID/types/Mutation/fields/updateExample"
      ]
    }
  ]
}
```

See [documentation](https://docs.aws.amazon.com/appsync/latest/devguide/security.html#aws-iam-authorization) for more details.

To make this easier, CDK provides `grant` API.

Use the `grant` function for more granular authorization.

```python
# api: appsync.GraphqlApi
role = iam.Role(self, "Role",
    assumed_by=iam.ServicePrincipal("lambda.amazonaws.com")
)

api.grant(role, appsync.IamResource.custom("types/Mutation/fields/updateExample"), "appsync:GraphQL")
```

### IamResource

In order to use the `grant` functions, you need to use the class `IamResource`.

* `IamResource.custom(...arns)` permits custom ARNs and requires an argument.
* `IamResouce.ofType(type, ...fields)` permits ARNs for types and their fields.
* `IamResource.all()` permits ALL resources.

### Generic Permissions

Alternatively, you can use more generic `grant` functions to accomplish the same usage.

These include:

* grantMutation (use to grant access to Mutation fields)
* grantQuery (use to grant access to Query fields)
* grantSubscription (use to grant access to Subscription fields)

```python
# api: appsync.GraphqlApi
# role: iam.Role


# For generic types
api.grant_mutation(role, "updateExample")

# For custom types and granular design
api.grant(role, appsync.IamResource.of_type("Mutation", "updateExample"), "appsync:GraphQL")
```

## Pipeline Resolvers and AppSync Functions

AppSync Functions are local functions that perform certain operations onto a
backend data source. Developers can compose operations (Functions) and execute
them in sequence with Pipeline Resolvers.

```python
# api: appsync.GraphqlApi


appsync_function = appsync.AppsyncFunction(self, "function",
    name="appsync_function",
    api=api,
    data_source=api.add_none_data_source("none"),
    request_mapping_template=appsync.MappingTemplate.from_file("request.vtl"),
    response_mapping_template=appsync.MappingTemplate.from_file("response.vtl")
)
```

AppSync Functions are used in tandem with pipeline resolvers to compose multiple
operations.

```python
# api: appsync.GraphqlApi
# appsync_function: appsync.AppsyncFunction


pipeline_resolver = appsync.Resolver(self, "pipeline",
    api=api,
    data_source=api.add_none_data_source("none"),
    type_name="typeName",
    field_name="fieldName",
    request_mapping_template=appsync.MappingTemplate.from_file("beforeRequest.vtl"),
    pipeline_config=[appsync_function],
    response_mapping_template=appsync.MappingTemplate.from_file("afterResponse.vtl")
)
```

Learn more about Pipeline Resolvers and AppSync Functions [here](https://docs.aws.amazon.com/appsync/latest/devguide/pipeline-resolvers.html).
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

import aws_cdk as _aws_cdk_ceddda9d
import aws_cdk.aws_appsync as _aws_cdk_aws_appsync_ceddda9d
import aws_cdk.aws_certificatemanager as _aws_cdk_aws_certificatemanager_ceddda9d
import aws_cdk.aws_cognito as _aws_cdk_aws_cognito_ceddda9d
import aws_cdk.aws_dynamodb as _aws_cdk_aws_dynamodb_ceddda9d
import aws_cdk.aws_elasticsearch as _aws_cdk_aws_elasticsearch_ceddda9d
import aws_cdk.aws_iam as _aws_cdk_aws_iam_ceddda9d
import aws_cdk.aws_lambda as _aws_cdk_aws_lambda_ceddda9d
import aws_cdk.aws_logs as _aws_cdk_aws_logs_ceddda9d
import aws_cdk.aws_opensearchservice as _aws_cdk_aws_opensearchservice_ceddda9d
import aws_cdk.aws_rds as _aws_cdk_aws_rds_ceddda9d
import aws_cdk.aws_secretsmanager as _aws_cdk_aws_secretsmanager_ceddda9d
import constructs as _constructs_77d1e7e8


@jsii.data_type(
    jsii_type="@aws-cdk/aws-appsync-alpha.ApiKeyConfig",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "expires": "expires", "name": "name"},
)
class ApiKeyConfig:
    def __init__(
        self,
        *,
        description: typing.Optional[builtins.str] = None,
        expires: typing.Optional[_aws_cdk_ceddda9d.Expiration] = None,
        name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''(experimental) Configuration for API Key authorization in AppSync.

        :param description: (experimental) Description of API key. Default: - 'Default API Key created by CDK'
        :param expires: (experimental) The time from creation time after which the API key expires. It must be a minimum of 1 day and a maximum of 365 days from date of creation. Rounded down to the nearest hour. Default: - 7 days rounded down to nearest hour
        :param name: (experimental) Unique name of the API Key. Default: - 'DefaultAPIKey'

        :stability: experimental
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            import aws_cdk.aws_appsync_alpha as appsync_alpha
            import aws_cdk as cdk
            
            # expiration: cdk.Expiration
            
            api_key_config = appsync_alpha.ApiKeyConfig(
                description="description",
                expires=expiration,
                name="name"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a3b49a22fd22a3a67a8ef82fe9f7e42c6334bcdce794d96bb3fd399270c6bf22)
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument expires", value=expires, expected_type=type_hints["expires"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if description is not None:
            self._values["description"] = description
        if expires is not None:
            self._values["expires"] = expires
        if name is not None:
            self._values["name"] = name

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''(experimental) Description of API key.

        :default: - 'Default API Key created by CDK'

        :stability: experimental
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def expires(self) -> typing.Optional[_aws_cdk_ceddda9d.Expiration]:
        '''(experimental) The time from creation time after which the API key expires.

        It must be a minimum of 1 day and a maximum of 365 days from date of creation.
        Rounded down to the nearest hour.

        :default: - 7 days rounded down to nearest hour

        :stability: experimental
        '''
        result = self._values.get("expires")
        return typing.cast(typing.Optional[_aws_cdk_ceddda9d.Expiration], result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''(experimental) Unique name of the API Key.

        :default: - 'DefaultAPIKey'

        :stability: experimental
        '''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ApiKeyConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@aws-cdk/aws-appsync-alpha.AppsyncFunctionAttributes",
    jsii_struct_bases=[],
    name_mapping={"function_arn": "functionArn"},
)
class AppsyncFunctionAttributes:
    def __init__(self, *, function_arn: builtins.str) -> None:
        '''(experimental) The attributes for imported AppSync Functions.

        :param function_arn: (experimental) the ARN of the AppSync function.

        :stability: experimental
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            import aws_cdk.aws_appsync_alpha as appsync_alpha
            
            appsync_function_attributes = appsync_alpha.AppsyncFunctionAttributes(
                function_arn="functionArn"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__143ac0b9b860d1ddfeac07bd7a8f178e8d8775fd8b64f5ab612b5e2afc10aa7b)
            check_type(argname="argument function_arn", value=function_arn, expected_type=type_hints["function_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "function_arn": function_arn,
        }

    @builtins.property
    def function_arn(self) -> builtins.str:
        '''(experimental) the ARN of the AppSync function.

        :stability: experimental
        '''
        result = self._values.get("function_arn")
        assert result is not None, "Required property 'function_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppsyncFunctionAttributes(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class Assign(metaclass=jsii.JSIIMeta, jsii_type="@aws-cdk/aws-appsync-alpha.Assign"):
    '''(experimental) Utility class representing the assigment of a value to an attribute.

    :stability: experimental
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        import aws_cdk.aws_appsync_alpha as appsync_alpha
        
        assign = appsync_alpha.Assign("attr", "arg")
    '''

    def __init__(self, attr: builtins.str, arg: builtins.str) -> None:
        '''
        :param attr: -
        :param arg: -

        :stability: experimental
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1b6d95b57768d71a938baa5b03f2059496ebd7ea514ade00f491018a3cf6b38f)
            check_type(argname="argument attr", value=attr, expected_type=type_hints["attr"])
            check_type(argname="argument arg", value=arg, expected_type=type_hints["arg"])
        jsii.create(self.__class__, self, [attr, arg])

    @jsii.member(jsii_name="putInMap")
    def put_in_map(self, map: builtins.str) -> builtins.str:
        '''(experimental) Renders the assignment as a map element.

        :param map: -

        :stability: experimental
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b956087c555a29842faba7ca34342da4c651120110854b50e76f77eaba7d9fee)
            check_type(argname="argument map", value=map, expected_type=type_hints["map"])
        return typing.cast(builtins.str, jsii.invoke(self, "putInMap", [map]))

    @jsii.member(jsii_name="renderAsAssignment")
    def render_as_assignment(self) -> builtins.str:
        '''(experimental) Renders the assignment as a VTL string.

        :stability: experimental
        '''
        return typing.cast(builtins.str, jsii.invoke(self, "renderAsAssignment", []))


class AttributeValues(
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/aws-appsync-alpha.AttributeValues",
):
    '''(experimental) Specifies the attribute value assignments.

    :stability: experimental
    :exampleMetadata: infused

    Example::

        api = appsync.GraphqlApi(self, "Api",
            name="demo",
            schema=appsync.SchemaFile.from_asset(path.join(__dirname, "schema.graphql")),
            authorization_config=appsync.AuthorizationConfig(
                default_authorization=appsync.AuthorizationMode(
                    authorization_type=appsync.AuthorizationType.IAM
                )
            ),
            xray_enabled=True
        )
        
        demo_table = dynamodb.Table(self, "DemoTable",
            partition_key=dynamodb.Attribute(
                name="id",
                type=dynamodb.AttributeType.STRING
            )
        )
        
        demo_dS = api.add_dynamo_db_data_source("demoDataSource", demo_table)
        
        # Resolver for the Query "getDemos" that scans the DynamoDb table and returns the entire list.
        # Resolver Mapping Template Reference:
        # https://docs.aws.amazon.com/appsync/latest/devguide/resolver-mapping-template-reference-dynamodb.html
        demo_dS.create_resolver("QueryGetDemosResolver",
            type_name="Query",
            field_name="getDemos",
            request_mapping_template=appsync.MappingTemplate.dynamo_db_scan_table(),
            response_mapping_template=appsync.MappingTemplate.dynamo_db_result_list()
        )
        
        # Resolver for the Mutation "addDemo" that puts the item into the DynamoDb table.
        demo_dS.create_resolver("MutationAddDemoResolver",
            type_name="Mutation",
            field_name="addDemo",
            request_mapping_template=appsync.MappingTemplate.dynamo_db_put_item(
                appsync.PrimaryKey.partition("id").auto(),
                appsync.Values.projecting("input")),
            response_mapping_template=appsync.MappingTemplate.dynamo_db_result_item()
        )
        
        # To enable DynamoDB read consistency with the `MappingTemplate`:
        demo_dS.create_resolver("QueryGetDemosConsistentResolver",
            type_name="Query",
            field_name="getDemosConsistent",
            request_mapping_template=appsync.MappingTemplate.dynamo_db_scan_table(True),
            response_mapping_template=appsync.MappingTemplate.dynamo_db_result_list()
        )
    '''

    def __init__(
        self,
        container: builtins.str,
        assignments: typing.Optional[typing.Sequence[Assign]] = None,
    ) -> None:
        '''
        :param container: -
        :param assignments: -

        :stability: experimental
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3a415b2a5f94a53c2e175bcb6c745edf9e25b58de67d004bfa0b7a186236b3aa)
            check_type(argname="argument container", value=container, expected_type=type_hints["container"])
            check_type(argname="argument assignments", value=assignments, expected_type=type_hints["assignments"])
        jsii.create(self.__class__, self, [container, assignments])

    @jsii.member(jsii_name="attribute")
    def attribute(self, attr: builtins.str) -> "AttributeValuesStep":
        '''(experimental) Allows assigning a value to the specified attribute.

        :param attr: -

        :stability: experimental
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b30aadf8e36dc621a4e5768f51bda7a879edcb854b3eda7b03f39d6b26bad17c)
            check_type(argname="argument attr", value=attr, expected_type=type_hints["attr"])
        return typing.cast("AttributeValuesStep", jsii.invoke(self, "attribute", [attr]))

    @jsii.member(jsii_name="renderTemplate")
    def render_template(self) -> builtins.str:
        '''(experimental) Renders the attribute value assingments to a VTL string.

        :stability: experimental
        '''
        return typing.cast(builtins.str, jsii.invoke(self, "renderTemplate", []))

    @jsii.member(jsii_name="renderVariables")
    def render_variables(self) -> builtins.str:
        '''(experimental) Renders the variables required for ``renderTemplate``.

        :stability: experimental
        '''
        return typing.cast(builtins.str, jsii.invoke(self, "renderVariables", []))


class AttributeValuesStep(
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/aws-appsync-alpha.AttributeValuesStep",
):
    '''(experimental) Utility class to allow assigning a value to an attribute.

    :stability: experimental
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        import aws_cdk.aws_appsync_alpha as appsync_alpha
        
        # assign: appsync_alpha.Assign
        
        attribute_values_step = appsync_alpha.AttributeValuesStep("attr", "container", [assign])
    '''

    def __init__(
        self,
        attr: builtins.str,
        container: builtins.str,
        assignments: typing.Sequence[Assign],
    ) -> None:
        '''
        :param attr: -
        :param container: -
        :param assignments: -

        :stability: experimental
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bb1677701427a21638e46fb1fe64a75c996ccd57ff8bdd9d80e1323d16015aea)
            check_type(argname="argument attr", value=attr, expected_type=type_hints["attr"])
            check_type(argname="argument container", value=container, expected_type=type_hints["container"])
            check_type(argname="argument assignments", value=assignments, expected_type=type_hints["assignments"])
        jsii.create(self.__class__, self, [attr, container, assignments])

    @jsii.member(jsii_name="is")
    def is_(self, val: builtins.str) -> AttributeValues:
        '''(experimental) Assign the value to the current attribute.

        :param val: -

        :stability: experimental
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cedcb433c4c0e028a47d72ef53e8659972c4eedf4df86504e61097654f716506)
            check_type(argname="argument val", value=val, expected_type=type_hints["val"])
        return typing.cast(AttributeValues, jsii.invoke(self, "is", [val]))


@jsii.data_type(
    jsii_type="@aws-cdk/aws-appsync-alpha.AuthorizationConfig",
    jsii_struct_bases=[],
    name_mapping={
        "additional_authorization_modes": "additionalAuthorizationModes",
        "default_authorization": "defaultAuthorization",
    },
)
class AuthorizationConfig:
    def __init__(
        self,
        *,
        additional_authorization_modes: typing.Optional[typing.Sequence[typing.Union["AuthorizationMode", typing.Dict[builtins.str, typing.Any]]]] = None,
        default_authorization: typing.Optional[typing.Union["AuthorizationMode", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''(experimental) Configuration of the API authorization modes.

        :param additional_authorization_modes: (experimental) Additional authorization modes. Default: - No other modes
        :param default_authorization: (experimental) Optional authorization configuration. Default: - API Key authorization

        :stability: experimental
        :exampleMetadata: infused

        Example::

            import aws_cdk.aws_lambda as lambda_
            # auth_function: lambda.Function
            
            
            appsync.GraphqlApi(self, "api",
                name="api",
                schema=appsync.SchemaFile.from_asset(path.join(__dirname, "appsync.test.graphql")),
                authorization_config=appsync.AuthorizationConfig(
                    default_authorization=appsync.AuthorizationMode(
                        authorization_type=appsync.AuthorizationType.LAMBDA,
                        lambda_authorizer_config=appsync.LambdaAuthorizerConfig(
                            handler=auth_function
                        )
                    )
                )
            )
        '''
        if isinstance(default_authorization, dict):
            default_authorization = AuthorizationMode(**default_authorization)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__072ee2d208cf787904aca8fab9d6d5adea904fbaafa9053ba7e1144bbe49a1d1)
            check_type(argname="argument additional_authorization_modes", value=additional_authorization_modes, expected_type=type_hints["additional_authorization_modes"])
            check_type(argname="argument default_authorization", value=default_authorization, expected_type=type_hints["default_authorization"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if additional_authorization_modes is not None:
            self._values["additional_authorization_modes"] = additional_authorization_modes
        if default_authorization is not None:
            self._values["default_authorization"] = default_authorization

    @builtins.property
    def additional_authorization_modes(
        self,
    ) -> typing.Optional[typing.List["AuthorizationMode"]]:
        '''(experimental) Additional authorization modes.

        :default: - No other modes

        :stability: experimental
        '''
        result = self._values.get("additional_authorization_modes")
        return typing.cast(typing.Optional[typing.List["AuthorizationMode"]], result)

    @builtins.property
    def default_authorization(self) -> typing.Optional["AuthorizationMode"]:
        '''(experimental) Optional authorization configuration.

        :default: - API Key authorization

        :stability: experimental
        '''
        result = self._values.get("default_authorization")
        return typing.cast(typing.Optional["AuthorizationMode"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AuthorizationConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@aws-cdk/aws-appsync-alpha.AuthorizationMode",
    jsii_struct_bases=[],
    name_mapping={
        "authorization_type": "authorizationType",
        "api_key_config": "apiKeyConfig",
        "lambda_authorizer_config": "lambdaAuthorizerConfig",
        "open_id_connect_config": "openIdConnectConfig",
        "user_pool_config": "userPoolConfig",
    },
)
class AuthorizationMode:
    def __init__(
        self,
        *,
        authorization_type: "AuthorizationType",
        api_key_config: typing.Optional[typing.Union[ApiKeyConfig, typing.Dict[builtins.str, typing.Any]]] = None,
        lambda_authorizer_config: typing.Optional[typing.Union["LambdaAuthorizerConfig", typing.Dict[builtins.str, typing.Any]]] = None,
        open_id_connect_config: typing.Optional[typing.Union["OpenIdConnectConfig", typing.Dict[builtins.str, typing.Any]]] = None,
        user_pool_config: typing.Optional[typing.Union["UserPoolConfig", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''(experimental) Interface to specify default or additional authorization(s).

        :param authorization_type: (experimental) One of possible four values AppSync supports. Default: - ``AuthorizationType.API_KEY``
        :param api_key_config: (experimental) If authorizationType is ``AuthorizationType.API_KEY``, this option can be configured. Default: - name: 'DefaultAPIKey' | description: 'Default API Key created by CDK'
        :param lambda_authorizer_config: (experimental) If authorizationType is ``AuthorizationType.LAMBDA``, this option is required. Default: - none
        :param open_id_connect_config: (experimental) If authorizationType is ``AuthorizationType.OIDC``, this option is required. Default: - none
        :param user_pool_config: (experimental) If authorizationType is ``AuthorizationType.USER_POOL``, this option is required. Default: - none

        :stability: experimental
        :exampleMetadata: infused

        Example::

            api = appsync.GraphqlApi(self, "Api",
                name="demo",
                schema=appsync.SchemaFile.from_asset(path.join(__dirname, "schema.graphql")),
                authorization_config=appsync.AuthorizationConfig(
                    default_authorization=appsync.AuthorizationMode(
                        authorization_type=appsync.AuthorizationType.IAM
                    )
                ),
                xray_enabled=True
            )
            
            demo_table = dynamodb.Table(self, "DemoTable",
                partition_key=dynamodb.Attribute(
                    name="id",
                    type=dynamodb.AttributeType.STRING
                )
            )
            
            demo_dS = api.add_dynamo_db_data_source("demoDataSource", demo_table)
            
            # Resolver for the Query "getDemos" that scans the DynamoDb table and returns the entire list.
            # Resolver Mapping Template Reference:
            # https://docs.aws.amazon.com/appsync/latest/devguide/resolver-mapping-template-reference-dynamodb.html
            demo_dS.create_resolver("QueryGetDemosResolver",
                type_name="Query",
                field_name="getDemos",
                request_mapping_template=appsync.MappingTemplate.dynamo_db_scan_table(),
                response_mapping_template=appsync.MappingTemplate.dynamo_db_result_list()
            )
            
            # Resolver for the Mutation "addDemo" that puts the item into the DynamoDb table.
            demo_dS.create_resolver("MutationAddDemoResolver",
                type_name="Mutation",
                field_name="addDemo",
                request_mapping_template=appsync.MappingTemplate.dynamo_db_put_item(
                    appsync.PrimaryKey.partition("id").auto(),
                    appsync.Values.projecting("input")),
                response_mapping_template=appsync.MappingTemplate.dynamo_db_result_item()
            )
            
            # To enable DynamoDB read consistency with the `MappingTemplate`:
            demo_dS.create_resolver("QueryGetDemosConsistentResolver",
                type_name="Query",
                field_name="getDemosConsistent",
                request_mapping_template=appsync.MappingTemplate.dynamo_db_scan_table(True),
                response_mapping_template=appsync.MappingTemplate.dynamo_db_result_list()
            )
        '''
        if isinstance(api_key_config, dict):
            api_key_config = ApiKeyConfig(**api_key_config)
        if isinstance(lambda_authorizer_config, dict):
            lambda_authorizer_config = LambdaAuthorizerConfig(**lambda_authorizer_config)
        if isinstance(open_id_connect_config, dict):
            open_id_connect_config = OpenIdConnectConfig(**open_id_connect_config)
        if isinstance(user_pool_config, dict):
            user_pool_config = UserPoolConfig(**user_pool_config)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f3349010ec6e7e227bfbf74f157ec83c8752b9ac70a93f3b9ef045558ab8cc3a)
            check_type(argname="argument authorization_type", value=authorization_type, expected_type=type_hints["authorization_type"])
            check_type(argname="argument api_key_config", value=api_key_config, expected_type=type_hints["api_key_config"])
            check_type(argname="argument lambda_authorizer_config", value=lambda_authorizer_config, expected_type=type_hints["lambda_authorizer_config"])
            check_type(argname="argument open_id_connect_config", value=open_id_connect_config, expected_type=type_hints["open_id_connect_config"])
            check_type(argname="argument user_pool_config", value=user_pool_config, expected_type=type_hints["user_pool_config"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "authorization_type": authorization_type,
        }
        if api_key_config is not None:
            self._values["api_key_config"] = api_key_config
        if lambda_authorizer_config is not None:
            self._values["lambda_authorizer_config"] = lambda_authorizer_config
        if open_id_connect_config is not None:
            self._values["open_id_connect_config"] = open_id_connect_config
        if user_pool_config is not None:
            self._values["user_pool_config"] = user_pool_config

    @builtins.property
    def authorization_type(self) -> "AuthorizationType":
        '''(experimental) One of possible four values AppSync supports.

        :default: - ``AuthorizationType.API_KEY``

        :see: https://docs.aws.amazon.com/appsync/latest/devguide/security.html
        :stability: experimental
        '''
        result = self._values.get("authorization_type")
        assert result is not None, "Required property 'authorization_type' is missing"
        return typing.cast("AuthorizationType", result)

    @builtins.property
    def api_key_config(self) -> typing.Optional[ApiKeyConfig]:
        '''(experimental) If authorizationType is ``AuthorizationType.API_KEY``, this option can be configured.

        :default: - name: 'DefaultAPIKey' | description: 'Default API Key created by CDK'

        :stability: experimental
        '''
        result = self._values.get("api_key_config")
        return typing.cast(typing.Optional[ApiKeyConfig], result)

    @builtins.property
    def lambda_authorizer_config(self) -> typing.Optional["LambdaAuthorizerConfig"]:
        '''(experimental) If authorizationType is ``AuthorizationType.LAMBDA``, this option is required.

        :default: - none

        :stability: experimental
        '''
        result = self._values.get("lambda_authorizer_config")
        return typing.cast(typing.Optional["LambdaAuthorizerConfig"], result)

    @builtins.property
    def open_id_connect_config(self) -> typing.Optional["OpenIdConnectConfig"]:
        '''(experimental) If authorizationType is ``AuthorizationType.OIDC``, this option is required.

        :default: - none

        :stability: experimental
        '''
        result = self._values.get("open_id_connect_config")
        return typing.cast(typing.Optional["OpenIdConnectConfig"], result)

    @builtins.property
    def user_pool_config(self) -> typing.Optional["UserPoolConfig"]:
        '''(experimental) If authorizationType is ``AuthorizationType.USER_POOL``, this option is required.

        :default: - none

        :stability: experimental
        '''
        result = self._values.get("user_pool_config")
        return typing.cast(typing.Optional["UserPoolConfig"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AuthorizationMode(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.enum(jsii_type="@aws-cdk/aws-appsync-alpha.AuthorizationType")
class AuthorizationType(enum.Enum):
    '''(experimental) enum with all possible values for AppSync authorization type.

    :stability: experimental
    :exampleMetadata: infused

    Example::

        api = appsync.GraphqlApi(self, "Api",
            name="demo",
            schema=appsync.SchemaFile.from_asset(path.join(__dirname, "schema.graphql")),
            authorization_config=appsync.AuthorizationConfig(
                default_authorization=appsync.AuthorizationMode(
                    authorization_type=appsync.AuthorizationType.IAM
                )
            ),
            xray_enabled=True
        )
        
        demo_table = dynamodb.Table(self, "DemoTable",
            partition_key=dynamodb.Attribute(
                name="id",
                type=dynamodb.AttributeType.STRING
            )
        )
        
        demo_dS = api.add_dynamo_db_data_source("demoDataSource", demo_table)
        
        # Resolver for the Query "getDemos" that scans the DynamoDb table and returns the entire list.
        # Resolver Mapping Template Reference:
        # https://docs.aws.amazon.com/appsync/latest/devguide/resolver-mapping-template-reference-dynamodb.html
        demo_dS.create_resolver("QueryGetDemosResolver",
            type_name="Query",
            field_name="getDemos",
            request_mapping_template=appsync.MappingTemplate.dynamo_db_scan_table(),
            response_mapping_template=appsync.MappingTemplate.dynamo_db_result_list()
        )
        
        # Resolver for the Mutation "addDemo" that puts the item into the DynamoDb table.
        demo_dS.create_resolver("MutationAddDemoResolver",
            type_name="Mutation",
            field_name="addDemo",
            request_mapping_template=appsync.MappingTemplate.dynamo_db_put_item(
                appsync.PrimaryKey.partition("id").auto(),
                appsync.Values.projecting("input")),
            response_mapping_template=appsync.MappingTemplate.dynamo_db_result_item()
        )
        
        # To enable DynamoDB read consistency with the `MappingTemplate`:
        demo_dS.create_resolver("QueryGetDemosConsistentResolver",
            type_name="Query",
            field_name="getDemosConsistent",
            request_mapping_template=appsync.MappingTemplate.dynamo_db_scan_table(True),
            response_mapping_template=appsync.MappingTemplate.dynamo_db_result_list()
        )
    '''

    API_KEY = "API_KEY"
    '''(experimental) API Key authorization type.

    :stability: experimental
    '''
    IAM = "IAM"
    '''(experimental) AWS IAM authorization type.

    Can be used with Cognito Identity Pool federated credentials

    :stability: experimental
    '''
    USER_POOL = "USER_POOL"
    '''(experimental) Cognito User Pool authorization type.

    :stability: experimental
    '''
    OIDC = "OIDC"
    '''(experimental) OpenID Connect authorization type.

    :stability: experimental
    '''
    LAMBDA = "LAMBDA"
    '''(experimental) Lambda authorization type.

    :stability: experimental
    '''


@jsii.data_type(
    jsii_type="@aws-cdk/aws-appsync-alpha.AwsIamConfig",
    jsii_struct_bases=[],
    name_mapping={
        "signing_region": "signingRegion",
        "signing_service_name": "signingServiceName",
    },
)
class AwsIamConfig:
    def __init__(
        self,
        *,
        signing_region: builtins.str,
        signing_service_name: builtins.str,
    ) -> None:
        '''(experimental) The authorization config in case the HTTP endpoint requires authorization.

        :param signing_region: (experimental) The signing region for AWS IAM authorization.
        :param signing_service_name: (experimental) The signing service name for AWS IAM authorization.

        :stability: experimental
        :exampleMetadata: infused

        Example::

            api = appsync.GraphqlApi(self, "api",
                name="api",
                schema=appsync.SchemaFile.from_asset(path.join(__dirname, "schema.graphql"))
            )
            
            http_ds = api.add_http_data_source("ds", "https://states.amazonaws.com",
                name="httpDsWithStepF",
                description="from appsync to StepFunctions Workflow",
                authorization_config=appsync.AwsIamConfig(
                    signing_region="us-east-1",
                    signing_service_name="states"
                )
            )
            
            http_ds.create_resolver("MutationCallStepFunctionResolver",
                type_name="Mutation",
                field_name="callStepFunction",
                request_mapping_template=appsync.MappingTemplate.from_file("request.vtl"),
                response_mapping_template=appsync.MappingTemplate.from_file("response.vtl")
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d1415d5dc4ff285ee5d54e74f7f22a7ed36988d11435b4fafd907c540d98d742)
            check_type(argname="argument signing_region", value=signing_region, expected_type=type_hints["signing_region"])
            check_type(argname="argument signing_service_name", value=signing_service_name, expected_type=type_hints["signing_service_name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "signing_region": signing_region,
            "signing_service_name": signing_service_name,
        }

    @builtins.property
    def signing_region(self) -> builtins.str:
        '''(experimental) The signing region for AWS IAM authorization.

        :stability: experimental
        '''
        result = self._values.get("signing_region")
        assert result is not None, "Required property 'signing_region' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def signing_service_name(self) -> builtins.str:
        '''(experimental) The signing service name for AWS IAM authorization.

        :stability: experimental
        '''
        result = self._values.get("signing_service_name")
        assert result is not None, "Required property 'signing_service_name' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AwsIamConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@aws-cdk/aws-appsync-alpha.BaseAppsyncFunctionProps",
    jsii_struct_bases=[],
    name_mapping={
        "name": "name",
        "description": "description",
        "request_mapping_template": "requestMappingTemplate",
        "response_mapping_template": "responseMappingTemplate",
    },
)
class BaseAppsyncFunctionProps:
    def __init__(
        self,
        *,
        name: builtins.str,
        description: typing.Optional[builtins.str] = None,
        request_mapping_template: typing.Optional["MappingTemplate"] = None,
        response_mapping_template: typing.Optional["MappingTemplate"] = None,
    ) -> None:
        '''(experimental) the base properties for AppSync Functions.

        :param name: (experimental) the name of the AppSync Function.
        :param description: (experimental) the description for this AppSync Function. Default: - no description
        :param request_mapping_template: (experimental) the request mapping template for the AppSync Function. Default: - no request mapping template
        :param response_mapping_template: (experimental) the response mapping template for the AppSync Function. Default: - no response mapping template

        :stability: experimental
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            import aws_cdk.aws_appsync_alpha as appsync_alpha
            
            # mapping_template: appsync_alpha.MappingTemplate
            
            base_appsync_function_props = appsync_alpha.BaseAppsyncFunctionProps(
                name="name",
            
                # the properties below are optional
                description="description",
                request_mapping_template=mapping_template,
                response_mapping_template=mapping_template
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d93e8cab7d8bd9de61fc51911cddaf5a17946653da71d37056a44550b0a84387)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument request_mapping_template", value=request_mapping_template, expected_type=type_hints["request_mapping_template"])
            check_type(argname="argument response_mapping_template", value=response_mapping_template, expected_type=type_hints["response_mapping_template"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "name": name,
        }
        if description is not None:
            self._values["description"] = description
        if request_mapping_template is not None:
            self._values["request_mapping_template"] = request_mapping_template
        if response_mapping_template is not None:
            self._values["response_mapping_template"] = response_mapping_template

    @builtins.property
    def name(self) -> builtins.str:
        '''(experimental) the name of the AppSync Function.

        :stability: experimental
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''(experimental) the description for this AppSync Function.

        :default: - no description

        :stability: experimental
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def request_mapping_template(self) -> typing.Optional["MappingTemplate"]:
        '''(experimental) the request mapping template for the AppSync Function.

        :default: - no request mapping template

        :stability: experimental
        '''
        result = self._values.get("request_mapping_template")
        return typing.cast(typing.Optional["MappingTemplate"], result)

    @builtins.property
    def response_mapping_template(self) -> typing.Optional["MappingTemplate"]:
        '''(experimental) the response mapping template for the AppSync Function.

        :default: - no response mapping template

        :stability: experimental
        '''
        result = self._values.get("response_mapping_template")
        return typing.cast(typing.Optional["MappingTemplate"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "BaseAppsyncFunctionProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class BaseDataSource(
    _constructs_77d1e7e8.Construct,
    metaclass=jsii.JSIIAbstractClass,
    jsii_type="@aws-cdk/aws-appsync-alpha.BaseDataSource",
):
    '''(experimental) Abstract AppSync datasource implementation.

    Do not use directly but use subclasses for concrete datasources

    :stability: experimental
    :exampleMetadata: infused

    Example::

        # api: appsync.GraphqlApi
        
        
        appsync_function = appsync.AppsyncFunction(self, "function",
            name="appsync_function",
            api=api,
            data_source=api.add_none_data_source("none"),
            request_mapping_template=appsync.MappingTemplate.from_file("request.vtl"),
            response_mapping_template=appsync.MappingTemplate.from_file("response.vtl")
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        props: typing.Union["BackedDataSourceProps", typing.Dict[builtins.str, typing.Any]],
        *,
        type: builtins.str,
        dynamo_db_config: typing.Optional[typing.Union[typing.Union[_aws_cdk_aws_appsync_ceddda9d.CfnDataSource.DynamoDBConfigProperty, typing.Dict[builtins.str, typing.Any]], _aws_cdk_ceddda9d.IResolvable]] = None,
        elasticsearch_config: typing.Optional[typing.Union[typing.Union[_aws_cdk_aws_appsync_ceddda9d.CfnDataSource.ElasticsearchConfigProperty, typing.Dict[builtins.str, typing.Any]], _aws_cdk_ceddda9d.IResolvable]] = None,
        http_config: typing.Optional[typing.Union[typing.Union[_aws_cdk_aws_appsync_ceddda9d.CfnDataSource.HttpConfigProperty, typing.Dict[builtins.str, typing.Any]], _aws_cdk_ceddda9d.IResolvable]] = None,
        lambda_config: typing.Optional[typing.Union[typing.Union[_aws_cdk_aws_appsync_ceddda9d.CfnDataSource.LambdaConfigProperty, typing.Dict[builtins.str, typing.Any]], _aws_cdk_ceddda9d.IResolvable]] = None,
        open_search_service_config: typing.Optional[typing.Union[typing.Union[_aws_cdk_aws_appsync_ceddda9d.CfnDataSource.OpenSearchServiceConfigProperty, typing.Dict[builtins.str, typing.Any]], _aws_cdk_ceddda9d.IResolvable]] = None,
        relational_database_config: typing.Optional[typing.Union[typing.Union[_aws_cdk_aws_appsync_ceddda9d.CfnDataSource.RelationalDatabaseConfigProperty, typing.Dict[builtins.str, typing.Any]], _aws_cdk_ceddda9d.IResolvable]] = None,
    ) -> None:
        '''
        :param scope: -
        :param id: -
        :param props: -
        :param type: (experimental) the type of the AppSync datasource.
        :param dynamo_db_config: (experimental) configuration for DynamoDB Datasource. Default: - No config
        :param elasticsearch_config: (deprecated) configuration for Elasticsearch data source. Default: - No config
        :param http_config: (experimental) configuration for HTTP Datasource. Default: - No config
        :param lambda_config: (experimental) configuration for Lambda Datasource. Default: - No config
        :param open_search_service_config: (experimental) configuration for OpenSearch data source. Default: - No config
        :param relational_database_config: (experimental) configuration for RDS Datasource. Default: - No config

        :stability: experimental
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__230d9ab3d2c96a0794535e1481ac98d0795f10ceaed29ae16702d9cb6748b189)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        extended = ExtendedDataSourceProps(
            type=type,
            dynamo_db_config=dynamo_db_config,
            elasticsearch_config=elasticsearch_config,
            http_config=http_config,
            lambda_config=lambda_config,
            open_search_service_config=open_search_service_config,
            relational_database_config=relational_database_config,
        )

        jsii.create(self.__class__, self, [scope, id, props, extended])

    @jsii.member(jsii_name="createFunction")
    def create_function(
        self,
        id: builtins.str,
        *,
        name: builtins.str,
        description: typing.Optional[builtins.str] = None,
        request_mapping_template: typing.Optional["MappingTemplate"] = None,
        response_mapping_template: typing.Optional["MappingTemplate"] = None,
    ) -> "AppsyncFunction":
        '''(experimental) creates a new appsync function for this datasource and API using the given properties.

        :param id: -
        :param name: (experimental) the name of the AppSync Function.
        :param description: (experimental) the description for this AppSync Function. Default: - no description
        :param request_mapping_template: (experimental) the request mapping template for the AppSync Function. Default: - no request mapping template
        :param response_mapping_template: (experimental) the response mapping template for the AppSync Function. Default: - no response mapping template

        :stability: experimental
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6ec867efbcdaffdbb6b832d4eb07531ba4093e9678029b86b16528ad6a61f89b)
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = BaseAppsyncFunctionProps(
            name=name,
            description=description,
            request_mapping_template=request_mapping_template,
            response_mapping_template=response_mapping_template,
        )

        return typing.cast("AppsyncFunction", jsii.invoke(self, "createFunction", [id, props]))

    @jsii.member(jsii_name="createResolver")
    def create_resolver(
        self,
        id: builtins.str,
        *,
        field_name: builtins.str,
        type_name: builtins.str,
        caching_config: typing.Optional[typing.Union["CachingConfig", typing.Dict[builtins.str, typing.Any]]] = None,
        max_batch_size: typing.Optional[jsii.Number] = None,
        pipeline_config: typing.Optional[typing.Sequence["IAppsyncFunction"]] = None,
        request_mapping_template: typing.Optional["MappingTemplate"] = None,
        response_mapping_template: typing.Optional["MappingTemplate"] = None,
    ) -> "Resolver":
        '''(experimental) creates a new resolver for this datasource and API using the given properties.

        :param id: -
        :param field_name: (experimental) name of the GraphQL field in the given type this resolver is attached to.
        :param type_name: (experimental) name of the GraphQL type this resolver is attached to.
        :param caching_config: (experimental) The caching configuration for this resolver. Default: - No caching configuration
        :param max_batch_size: (experimental) The maximum number of elements per batch, when using batch invoke. Default: - No max batch size
        :param pipeline_config: (experimental) configuration of the pipeline resolver. Default: - no pipeline resolver configuration An empty array | undefined sets resolver to be of kind, unit
        :param request_mapping_template: (experimental) The request mapping template for this resolver. Default: - No mapping template
        :param response_mapping_template: (experimental) The response mapping template for this resolver. Default: - No mapping template

        :stability: experimental
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a95dbdc6dd3fef41be042eb94e18a28c05f4ad7e9e9bd81749248f7a3076b0f1)
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = BaseResolverProps(
            field_name=field_name,
            type_name=type_name,
            caching_config=caching_config,
            max_batch_size=max_batch_size,
            pipeline_config=pipeline_config,
            request_mapping_template=request_mapping_template,
            response_mapping_template=response_mapping_template,
        )

        return typing.cast("Resolver", jsii.invoke(self, "createResolver", [id, props]))

    @builtins.property
    @jsii.member(jsii_name="ds")
    def ds(self) -> _aws_cdk_aws_appsync_ceddda9d.CfnDataSource:
        '''(experimental) the underlying CFN data source resource.

        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_appsync_ceddda9d.CfnDataSource, jsii.get(self, "ds"))

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        '''(experimental) the name of the data source.

        :stability: experimental
        '''
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @builtins.property
    @jsii.member(jsii_name="api")
    def _api(self) -> "IGraphqlApi":
        '''
        :stability: experimental
        '''
        return typing.cast("IGraphqlApi", jsii.get(self, "api"))

    @_api.setter
    def _api(self, value: "IGraphqlApi") -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7d09ed5dcda77685d77b0b66879b9fe85a162b99036c9b19fdb07c18de061fe6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "api", value)

    @builtins.property
    @jsii.member(jsii_name="serviceRole")
    def _service_role(self) -> typing.Optional[_aws_cdk_aws_iam_ceddda9d.IRole]:
        '''
        :stability: experimental
        '''
        return typing.cast(typing.Optional[_aws_cdk_aws_iam_ceddda9d.IRole], jsii.get(self, "serviceRole"))

    @_service_role.setter
    def _service_role(
        self,
        value: typing.Optional[_aws_cdk_aws_iam_ceddda9d.IRole],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cccc9facb1cc9a3256ee2aa3a69d4a8231537882e991e26308994c2fa99ee141)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "serviceRole", value)


class _BaseDataSourceProxy(BaseDataSource):
    pass

# Adding a "__jsii_proxy_class__(): typing.Type" function to the abstract class
typing.cast(typing.Any, BaseDataSource).__jsii_proxy_class__ = lambda : _BaseDataSourceProxy


@jsii.data_type(
    jsii_type="@aws-cdk/aws-appsync-alpha.BaseDataSourceProps",
    jsii_struct_bases=[],
    name_mapping={"api": "api", "description": "description", "name": "name"},
)
class BaseDataSourceProps:
    def __init__(
        self,
        *,
        api: "IGraphqlApi",
        description: typing.Optional[builtins.str] = None,
        name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''(experimental) Base properties for an AppSync datasource.

        :param api: (experimental) The API to attach this data source to.
        :param description: (experimental) the description of the data source. Default: - None
        :param name: (experimental) The name of the data source. Default: - id of data source

        :stability: experimental
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            import aws_cdk.aws_appsync_alpha as appsync_alpha
            
            # graphql_api: appsync_alpha.GraphqlApi
            
            base_data_source_props = appsync_alpha.BaseDataSourceProps(
                api=graphql_api,
            
                # the properties below are optional
                description="description",
                name="name"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cc7c7973c849c1142cbbf9c779179a1a713a542a3c5bfb4e907ece94b1dcf339)
            check_type(argname="argument api", value=api, expected_type=type_hints["api"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "api": api,
        }
        if description is not None:
            self._values["description"] = description
        if name is not None:
            self._values["name"] = name

    @builtins.property
    def api(self) -> "IGraphqlApi":
        '''(experimental) The API to attach this data source to.

        :stability: experimental
        '''
        result = self._values.get("api")
        assert result is not None, "Required property 'api' is missing"
        return typing.cast("IGraphqlApi", result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''(experimental) the description of the data source.

        :default: - None

        :stability: experimental
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''(experimental) The name of the data source.

        :default: - id of data source

        :stability: experimental
        '''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "BaseDataSourceProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@aws-cdk/aws-appsync-alpha.BaseResolverProps",
    jsii_struct_bases=[],
    name_mapping={
        "field_name": "fieldName",
        "type_name": "typeName",
        "caching_config": "cachingConfig",
        "max_batch_size": "maxBatchSize",
        "pipeline_config": "pipelineConfig",
        "request_mapping_template": "requestMappingTemplate",
        "response_mapping_template": "responseMappingTemplate",
    },
)
class BaseResolverProps:
    def __init__(
        self,
        *,
        field_name: builtins.str,
        type_name: builtins.str,
        caching_config: typing.Optional[typing.Union["CachingConfig", typing.Dict[builtins.str, typing.Any]]] = None,
        max_batch_size: typing.Optional[jsii.Number] = None,
        pipeline_config: typing.Optional[typing.Sequence["IAppsyncFunction"]] = None,
        request_mapping_template: typing.Optional["MappingTemplate"] = None,
        response_mapping_template: typing.Optional["MappingTemplate"] = None,
    ) -> None:
        '''(experimental) Basic properties for an AppSync resolver.

        :param field_name: (experimental) name of the GraphQL field in the given type this resolver is attached to.
        :param type_name: (experimental) name of the GraphQL type this resolver is attached to.
        :param caching_config: (experimental) The caching configuration for this resolver. Default: - No caching configuration
        :param max_batch_size: (experimental) The maximum number of elements per batch, when using batch invoke. Default: - No max batch size
        :param pipeline_config: (experimental) configuration of the pipeline resolver. Default: - no pipeline resolver configuration An empty array | undefined sets resolver to be of kind, unit
        :param request_mapping_template: (experimental) The request mapping template for this resolver. Default: - No mapping template
        :param response_mapping_template: (experimental) The response mapping template for this resolver. Default: - No mapping template

        :stability: experimental
        :exampleMetadata: infused

        Example::

            # Build a data source for AppSync to access the database.
            # api: appsync.GraphqlApi
            # Create username and password secret for DB Cluster
            secret = rds.DatabaseSecret(self, "AuroraSecret",
                username="clusteradmin"
            )
            
            # The VPC to place the cluster in
            vpc = ec2.Vpc(self, "AuroraVpc")
            
            # Create the serverless cluster, provide all values needed to customise the database.
            cluster = rds.ServerlessCluster(self, "AuroraCluster",
                engine=rds.DatabaseClusterEngine.AURORA_MYSQL,
                vpc=vpc,
                credentials={"username": "clusteradmin"},
                cluster_identifier="db-endpoint-test",
                default_database_name="demos"
            )
            rds_dS = api.add_rds_data_source("rds", cluster, secret, "demos")
            
            # Set up a resolver for an RDS query.
            rds_dS.create_resolver("QueryGetDemosRdsResolver",
                type_name="Query",
                field_name="getDemosRds",
                request_mapping_template=appsync.MappingTemplate.from_string("""
                      {
                        "version": "2018-05-29",
                        "statements": [
                          "SELECT * FROM demos"
                        ]
                      }
                      """),
                response_mapping_template=appsync.MappingTemplate.from_string("""
                        $utils.toJson($utils.rds.toJsonObject($ctx.result)[0])
                      """)
            )
            
            # Set up a resolver for an RDS mutation.
            rds_dS.create_resolver("MutationAddDemoRdsResolver",
                type_name="Mutation",
                field_name="addDemoRds",
                request_mapping_template=appsync.MappingTemplate.from_string("""
                      {
                        "version": "2018-05-29",
                        "statements": [
                          "INSERT INTO demos VALUES (:id, :version)",
                          "SELECT * WHERE id = :id"
                        ],
                        "variableMap": {
                          ":id": $util.toJson($util.autoId()),
                          ":version": $util.toJson($ctx.args.version)
                        }
                      }
                      """),
                response_mapping_template=appsync.MappingTemplate.from_string("""
                        $utils.toJson($utils.rds.toJsonObject($ctx.result)[1][0])
                      """)
            )
        '''
        if isinstance(caching_config, dict):
            caching_config = CachingConfig(**caching_config)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1247604f97a7e79118f8e17cbadbbd5727fb645bf9880b1e91f1f0731da521ff)
            check_type(argname="argument field_name", value=field_name, expected_type=type_hints["field_name"])
            check_type(argname="argument type_name", value=type_name, expected_type=type_hints["type_name"])
            check_type(argname="argument caching_config", value=caching_config, expected_type=type_hints["caching_config"])
            check_type(argname="argument max_batch_size", value=max_batch_size, expected_type=type_hints["max_batch_size"])
            check_type(argname="argument pipeline_config", value=pipeline_config, expected_type=type_hints["pipeline_config"])
            check_type(argname="argument request_mapping_template", value=request_mapping_template, expected_type=type_hints["request_mapping_template"])
            check_type(argname="argument response_mapping_template", value=response_mapping_template, expected_type=type_hints["response_mapping_template"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "field_name": field_name,
            "type_name": type_name,
        }
        if caching_config is not None:
            self._values["caching_config"] = caching_config
        if max_batch_size is not None:
            self._values["max_batch_size"] = max_batch_size
        if pipeline_config is not None:
            self._values["pipeline_config"] = pipeline_config
        if request_mapping_template is not None:
            self._values["request_mapping_template"] = request_mapping_template
        if response_mapping_template is not None:
            self._values["response_mapping_template"] = response_mapping_template

    @builtins.property
    def field_name(self) -> builtins.str:
        '''(experimental) name of the GraphQL field in the given type this resolver is attached to.

        :stability: experimental
        '''
        result = self._values.get("field_name")
        assert result is not None, "Required property 'field_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type_name(self) -> builtins.str:
        '''(experimental) name of the GraphQL type this resolver is attached to.

        :stability: experimental
        '''
        result = self._values.get("type_name")
        assert result is not None, "Required property 'type_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def caching_config(self) -> typing.Optional["CachingConfig"]:
        '''(experimental) The caching configuration for this resolver.

        :default: - No caching configuration

        :stability: experimental
        '''
        result = self._values.get("caching_config")
        return typing.cast(typing.Optional["CachingConfig"], result)

    @builtins.property
    def max_batch_size(self) -> typing.Optional[jsii.Number]:
        '''(experimental) The maximum number of elements per batch, when using batch invoke.

        :default: - No max batch size

        :stability: experimental
        '''
        result = self._values.get("max_batch_size")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def pipeline_config(self) -> typing.Optional[typing.List["IAppsyncFunction"]]:
        '''(experimental) configuration of the pipeline resolver.

        :default:

        - no pipeline resolver configuration
        An empty array | undefined sets resolver to be of kind, unit

        :stability: experimental
        '''
        result = self._values.get("pipeline_config")
        return typing.cast(typing.Optional[typing.List["IAppsyncFunction"]], result)

    @builtins.property
    def request_mapping_template(self) -> typing.Optional["MappingTemplate"]:
        '''(experimental) The request mapping template for this resolver.

        :default: - No mapping template

        :stability: experimental
        '''
        result = self._values.get("request_mapping_template")
        return typing.cast(typing.Optional["MappingTemplate"], result)

    @builtins.property
    def response_mapping_template(self) -> typing.Optional["MappingTemplate"]:
        '''(experimental) The response mapping template for this resolver.

        :default: - No mapping template

        :stability: experimental
        '''
        result = self._values.get("response_mapping_template")
        return typing.cast(typing.Optional["MappingTemplate"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "BaseResolverProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@aws-cdk/aws-appsync-alpha.CachingConfig",
    jsii_struct_bases=[],
    name_mapping={"ttl": "ttl", "caching_keys": "cachingKeys"},
)
class CachingConfig:
    def __init__(
        self,
        *,
        ttl: _aws_cdk_ceddda9d.Duration,
        caching_keys: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''(experimental) CachingConfig for AppSync resolvers.

        :param ttl: (experimental) The TTL in seconds for a resolver that has caching enabled. Valid values are between 1 and 3600 seconds.
        :param caching_keys: (experimental) The caching keys for a resolver that has caching enabled. Valid values are entries from the $context.arguments, $context.source, and $context.identity maps. Default: - No caching keys

        :stability: experimental
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            import aws_cdk.aws_appsync_alpha as appsync_alpha
            import aws_cdk as cdk
            
            caching_config = appsync_alpha.CachingConfig(
                ttl=cdk.Duration.minutes(30),
            
                # the properties below are optional
                caching_keys=["cachingKeys"]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__24bbe35162b5b4ead5d7cdba050bb2ab9f017c763245480227a2f816d53294d2)
            check_type(argname="argument ttl", value=ttl, expected_type=type_hints["ttl"])
            check_type(argname="argument caching_keys", value=caching_keys, expected_type=type_hints["caching_keys"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "ttl": ttl,
        }
        if caching_keys is not None:
            self._values["caching_keys"] = caching_keys

    @builtins.property
    def ttl(self) -> _aws_cdk_ceddda9d.Duration:
        '''(experimental) The TTL in seconds for a resolver that has caching enabled.

        Valid values are between 1 and 3600 seconds.

        :stability: experimental
        '''
        result = self._values.get("ttl")
        assert result is not None, "Required property 'ttl' is missing"
        return typing.cast(_aws_cdk_ceddda9d.Duration, result)

    @builtins.property
    def caching_keys(self) -> typing.Optional[typing.List[builtins.str]]:
        '''(experimental) The caching keys for a resolver that has caching enabled.

        Valid values are entries from the $context.arguments, $context.source, and $context.identity maps.

        :default: - No caching keys

        :stability: experimental
        '''
        result = self._values.get("caching_keys")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CachingConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@aws-cdk/aws-appsync-alpha.DataSourceOptions",
    jsii_struct_bases=[],
    name_mapping={"description": "description", "name": "name"},
)
class DataSourceOptions:
    def __init__(
        self,
        *,
        description: typing.Optional[builtins.str] = None,
        name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''(experimental) Optional configuration for data sources.

        :param description: (experimental) The description of the data source. Default: - No description
        :param name: (experimental) The name of the data source, overrides the id given by cdk. Default: - generated by cdk given the id

        :stability: experimental
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            import aws_cdk.aws_appsync_alpha as appsync_alpha
            
            data_source_options = appsync_alpha.DataSourceOptions(
                description="description",
                name="name"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5d4872a33bcd7830c8e9ba05ba045a2dc10b6926f77aac1bbee29fb9dfa4510b)
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if description is not None:
            self._values["description"] = description
        if name is not None:
            self._values["name"] = name

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''(experimental) The description of the data source.

        :default: - No description

        :stability: experimental
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''(experimental) The name of the data source, overrides the id given by cdk.

        :default: - generated by cdk given the id

        :stability: experimental
        '''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataSourceOptions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@aws-cdk/aws-appsync-alpha.DomainOptions",
    jsii_struct_bases=[],
    name_mapping={"certificate": "certificate", "domain_name": "domainName"},
)
class DomainOptions:
    def __init__(
        self,
        *,
        certificate: _aws_cdk_aws_certificatemanager_ceddda9d.ICertificate,
        domain_name: builtins.str,
    ) -> None:
        '''(experimental) Domain name configuration for AppSync.

        :param certificate: (experimental) The certificate to use with the domain name.
        :param domain_name: (experimental) The actual domain name. For example, ``api.example.com``.

        :stability: experimental
        :exampleMetadata: infused

        Example::

            import aws_cdk.aws_certificatemanager as acm
            import aws_cdk.aws_route53 as route53
            
            # hosted zone and route53 features
            # hosted_zone_id: str
            zone_name = "example.com"
            
            
            my_domain_name = "api.example.com"
            certificate = acm.Certificate(self, "cert", domain_name=my_domain_name)
            schema = appsync.SchemaFile(file_path="mySchemaFile")
            api = appsync.GraphqlApi(self, "api",
                name="myApi",
                schema=schema,
                domain_name=appsync.DomainOptions(
                    certificate=certificate,
                    domain_name=my_domain_name
                )
            )
            
            # hosted zone for adding appsync domain
            zone = route53.HostedZone.from_hosted_zone_attributes(self, "HostedZone",
                hosted_zone_id=hosted_zone_id,
                zone_name=zone_name
            )
            
            # create a cname to the appsync domain. will map to something like xxxx.cloudfront.net
            route53.CnameRecord(self, "CnameApiRecord",
                record_name="api",
                zone=zone,
                domain_name=api.app_sync_domain_name
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__eeded7b0dde6896a11d8a28127d0d2002269687de25559c00d05be06499990d7)
            check_type(argname="argument certificate", value=certificate, expected_type=type_hints["certificate"])
            check_type(argname="argument domain_name", value=domain_name, expected_type=type_hints["domain_name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "certificate": certificate,
            "domain_name": domain_name,
        }

    @builtins.property
    def certificate(self) -> _aws_cdk_aws_certificatemanager_ceddda9d.ICertificate:
        '''(experimental) The certificate to use with the domain name.

        :stability: experimental
        '''
        result = self._values.get("certificate")
        assert result is not None, "Required property 'certificate' is missing"
        return typing.cast(_aws_cdk_aws_certificatemanager_ceddda9d.ICertificate, result)

    @builtins.property
    def domain_name(self) -> builtins.str:
        '''(experimental) The actual domain name.

        For example, ``api.example.com``.

        :stability: experimental
        '''
        result = self._values.get("domain_name")
        assert result is not None, "Required property 'domain_name' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DomainOptions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@aws-cdk/aws-appsync-alpha.ExtendedDataSourceProps",
    jsii_struct_bases=[],
    name_mapping={
        "type": "type",
        "dynamo_db_config": "dynamoDbConfig",
        "elasticsearch_config": "elasticsearchConfig",
        "http_config": "httpConfig",
        "lambda_config": "lambdaConfig",
        "open_search_service_config": "openSearchServiceConfig",
        "relational_database_config": "relationalDatabaseConfig",
    },
)
class ExtendedDataSourceProps:
    def __init__(
        self,
        *,
        type: builtins.str,
        dynamo_db_config: typing.Optional[typing.Union[typing.Union[_aws_cdk_aws_appsync_ceddda9d.CfnDataSource.DynamoDBConfigProperty, typing.Dict[builtins.str, typing.Any]], _aws_cdk_ceddda9d.IResolvable]] = None,
        elasticsearch_config: typing.Optional[typing.Union[typing.Union[_aws_cdk_aws_appsync_ceddda9d.CfnDataSource.ElasticsearchConfigProperty, typing.Dict[builtins.str, typing.Any]], _aws_cdk_ceddda9d.IResolvable]] = None,
        http_config: typing.Optional[typing.Union[typing.Union[_aws_cdk_aws_appsync_ceddda9d.CfnDataSource.HttpConfigProperty, typing.Dict[builtins.str, typing.Any]], _aws_cdk_ceddda9d.IResolvable]] = None,
        lambda_config: typing.Optional[typing.Union[typing.Union[_aws_cdk_aws_appsync_ceddda9d.CfnDataSource.LambdaConfigProperty, typing.Dict[builtins.str, typing.Any]], _aws_cdk_ceddda9d.IResolvable]] = None,
        open_search_service_config: typing.Optional[typing.Union[typing.Union[_aws_cdk_aws_appsync_ceddda9d.CfnDataSource.OpenSearchServiceConfigProperty, typing.Dict[builtins.str, typing.Any]], _aws_cdk_ceddda9d.IResolvable]] = None,
        relational_database_config: typing.Optional[typing.Union[typing.Union[_aws_cdk_aws_appsync_ceddda9d.CfnDataSource.RelationalDatabaseConfigProperty, typing.Dict[builtins.str, typing.Any]], _aws_cdk_ceddda9d.IResolvable]] = None,
    ) -> None:
        '''(experimental) props used by implementations of BaseDataSource to provide configuration.

        Should not be used directly.

        :param type: (experimental) the type of the AppSync datasource.
        :param dynamo_db_config: (experimental) configuration for DynamoDB Datasource. Default: - No config
        :param elasticsearch_config: (deprecated) configuration for Elasticsearch data source. Default: - No config
        :param http_config: (experimental) configuration for HTTP Datasource. Default: - No config
        :param lambda_config: (experimental) configuration for Lambda Datasource. Default: - No config
        :param open_search_service_config: (experimental) configuration for OpenSearch data source. Default: - No config
        :param relational_database_config: (experimental) configuration for RDS Datasource. Default: - No config

        :stability: experimental
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            import aws_cdk.aws_appsync_alpha as appsync_alpha
            
            extended_data_source_props = appsync_alpha.ExtendedDataSourceProps(
                type="type",
            
                # the properties below are optional
                dynamo_db_config=DynamoDBConfigProperty(
                    aws_region="awsRegion",
                    table_name="tableName",
            
                    # the properties below are optional
                    delta_sync_config=DeltaSyncConfigProperty(
                        base_table_ttl="baseTableTtl",
                        delta_sync_table_name="deltaSyncTableName",
                        delta_sync_table_ttl="deltaSyncTableTtl"
                    ),
                    use_caller_credentials=False,
                    versioned=False
                ),
                elasticsearch_config=ElasticsearchConfigProperty(
                    aws_region="awsRegion",
                    endpoint="endpoint"
                ),
                http_config=HttpConfigProperty(
                    endpoint="endpoint",
            
                    # the properties below are optional
                    authorization_config=AuthorizationConfigProperty(
                        authorization_type="authorizationType",
            
                        # the properties below are optional
                        aws_iam_config=AwsIamConfigProperty(
                            signing_region="signingRegion",
                            signing_service_name="signingServiceName"
                        )
                    )
                ),
                lambda_config=LambdaConfigProperty(
                    lambda_function_arn="lambdaFunctionArn"
                ),
                open_search_service_config=OpenSearchServiceConfigProperty(
                    aws_region="awsRegion",
                    endpoint="endpoint"
                ),
                relational_database_config=RelationalDatabaseConfigProperty(
                    relational_database_source_type="relationalDatabaseSourceType",
            
                    # the properties below are optional
                    rds_http_endpoint_config=RdsHttpEndpointConfigProperty(
                        aws_region="awsRegion",
                        aws_secret_store_arn="awsSecretStoreArn",
                        db_cluster_identifier="dbClusterIdentifier",
            
                        # the properties below are optional
                        database_name="databaseName",
                        schema="schema"
                    )
                )
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c317114b1e4283481b6e478cbf1b446de4e66b3f8e6e74c9df7ce3f0215cb6ca)
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
            check_type(argname="argument dynamo_db_config", value=dynamo_db_config, expected_type=type_hints["dynamo_db_config"])
            check_type(argname="argument elasticsearch_config", value=elasticsearch_config, expected_type=type_hints["elasticsearch_config"])
            check_type(argname="argument http_config", value=http_config, expected_type=type_hints["http_config"])
            check_type(argname="argument lambda_config", value=lambda_config, expected_type=type_hints["lambda_config"])
            check_type(argname="argument open_search_service_config", value=open_search_service_config, expected_type=type_hints["open_search_service_config"])
            check_type(argname="argument relational_database_config", value=relational_database_config, expected_type=type_hints["relational_database_config"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "type": type,
        }
        if dynamo_db_config is not None:
            self._values["dynamo_db_config"] = dynamo_db_config
        if elasticsearch_config is not None:
            self._values["elasticsearch_config"] = elasticsearch_config
        if http_config is not None:
            self._values["http_config"] = http_config
        if lambda_config is not None:
            self._values["lambda_config"] = lambda_config
        if open_search_service_config is not None:
            self._values["open_search_service_config"] = open_search_service_config
        if relational_database_config is not None:
            self._values["relational_database_config"] = relational_database_config

    @builtins.property
    def type(self) -> builtins.str:
        '''(experimental) the type of the AppSync datasource.

        :stability: experimental
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def dynamo_db_config(
        self,
    ) -> typing.Optional[typing.Union[_aws_cdk_aws_appsync_ceddda9d.CfnDataSource.DynamoDBConfigProperty, _aws_cdk_ceddda9d.IResolvable]]:
        '''(experimental) configuration for DynamoDB Datasource.

        :default: - No config

        :stability: experimental
        '''
        result = self._values.get("dynamo_db_config")
        return typing.cast(typing.Optional[typing.Union[_aws_cdk_aws_appsync_ceddda9d.CfnDataSource.DynamoDBConfigProperty, _aws_cdk_ceddda9d.IResolvable]], result)

    @builtins.property
    def elasticsearch_config(
        self,
    ) -> typing.Optional[typing.Union[_aws_cdk_aws_appsync_ceddda9d.CfnDataSource.ElasticsearchConfigProperty, _aws_cdk_ceddda9d.IResolvable]]:
        '''(deprecated) configuration for Elasticsearch data source.

        :default: - No config

        :deprecated: - use ``openSearchConfig``

        :stability: deprecated
        '''
        result = self._values.get("elasticsearch_config")
        return typing.cast(typing.Optional[typing.Union[_aws_cdk_aws_appsync_ceddda9d.CfnDataSource.ElasticsearchConfigProperty, _aws_cdk_ceddda9d.IResolvable]], result)

    @builtins.property
    def http_config(
        self,
    ) -> typing.Optional[typing.Union[_aws_cdk_aws_appsync_ceddda9d.CfnDataSource.HttpConfigProperty, _aws_cdk_ceddda9d.IResolvable]]:
        '''(experimental) configuration for HTTP Datasource.

        :default: - No config

        :stability: experimental
        '''
        result = self._values.get("http_config")
        return typing.cast(typing.Optional[typing.Union[_aws_cdk_aws_appsync_ceddda9d.CfnDataSource.HttpConfigProperty, _aws_cdk_ceddda9d.IResolvable]], result)

    @builtins.property
    def lambda_config(
        self,
    ) -> typing.Optional[typing.Union[_aws_cdk_aws_appsync_ceddda9d.CfnDataSource.LambdaConfigProperty, _aws_cdk_ceddda9d.IResolvable]]:
        '''(experimental) configuration for Lambda Datasource.

        :default: - No config

        :stability: experimental
        '''
        result = self._values.get("lambda_config")
        return typing.cast(typing.Optional[typing.Union[_aws_cdk_aws_appsync_ceddda9d.CfnDataSource.LambdaConfigProperty, _aws_cdk_ceddda9d.IResolvable]], result)

    @builtins.property
    def open_search_service_config(
        self,
    ) -> typing.Optional[typing.Union[_aws_cdk_aws_appsync_ceddda9d.CfnDataSource.OpenSearchServiceConfigProperty, _aws_cdk_ceddda9d.IResolvable]]:
        '''(experimental) configuration for OpenSearch data source.

        :default: - No config

        :stability: experimental
        '''
        result = self._values.get("open_search_service_config")
        return typing.cast(typing.Optional[typing.Union[_aws_cdk_aws_appsync_ceddda9d.CfnDataSource.OpenSearchServiceConfigProperty, _aws_cdk_ceddda9d.IResolvable]], result)

    @builtins.property
    def relational_database_config(
        self,
    ) -> typing.Optional[typing.Union[_aws_cdk_aws_appsync_ceddda9d.CfnDataSource.RelationalDatabaseConfigProperty, _aws_cdk_ceddda9d.IResolvable]]:
        '''(experimental) configuration for RDS Datasource.

        :default: - No config

        :stability: experimental
        '''
        result = self._values.get("relational_database_config")
        return typing.cast(typing.Optional[typing.Union[_aws_cdk_aws_appsync_ceddda9d.CfnDataSource.RelationalDatabaseConfigProperty, _aws_cdk_ceddda9d.IResolvable]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ExtendedDataSourceProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@aws-cdk/aws-appsync-alpha.ExtendedResolverProps",
    jsii_struct_bases=[BaseResolverProps],
    name_mapping={
        "field_name": "fieldName",
        "type_name": "typeName",
        "caching_config": "cachingConfig",
        "max_batch_size": "maxBatchSize",
        "pipeline_config": "pipelineConfig",
        "request_mapping_template": "requestMappingTemplate",
        "response_mapping_template": "responseMappingTemplate",
        "data_source": "dataSource",
    },
)
class ExtendedResolverProps(BaseResolverProps):
    def __init__(
        self,
        *,
        field_name: builtins.str,
        type_name: builtins.str,
        caching_config: typing.Optional[typing.Union[CachingConfig, typing.Dict[builtins.str, typing.Any]]] = None,
        max_batch_size: typing.Optional[jsii.Number] = None,
        pipeline_config: typing.Optional[typing.Sequence["IAppsyncFunction"]] = None,
        request_mapping_template: typing.Optional["MappingTemplate"] = None,
        response_mapping_template: typing.Optional["MappingTemplate"] = None,
        data_source: typing.Optional[BaseDataSource] = None,
    ) -> None:
        '''(experimental) Additional property for an AppSync resolver for data source reference.

        :param field_name: (experimental) name of the GraphQL field in the given type this resolver is attached to.
        :param type_name: (experimental) name of the GraphQL type this resolver is attached to.
        :param caching_config: (experimental) The caching configuration for this resolver. Default: - No caching configuration
        :param max_batch_size: (experimental) The maximum number of elements per batch, when using batch invoke. Default: - No max batch size
        :param pipeline_config: (experimental) configuration of the pipeline resolver. Default: - no pipeline resolver configuration An empty array | undefined sets resolver to be of kind, unit
        :param request_mapping_template: (experimental) The request mapping template for this resolver. Default: - No mapping template
        :param response_mapping_template: (experimental) The response mapping template for this resolver. Default: - No mapping template
        :param data_source: (experimental) The data source this resolver is using. Default: - No datasource

        :stability: experimental
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            import aws_cdk.aws_appsync_alpha as appsync_alpha
            import aws_cdk as cdk
            
            # appsync_function: appsync_alpha.AppsyncFunction
            # base_data_source: appsync_alpha.BaseDataSource
            # mapping_template: appsync_alpha.MappingTemplate
            
            extended_resolver_props = appsync_alpha.ExtendedResolverProps(
                field_name="fieldName",
                type_name="typeName",
            
                # the properties below are optional
                caching_config=appsync_alpha.CachingConfig(
                    ttl=cdk.Duration.minutes(30),
            
                    # the properties below are optional
                    caching_keys=["cachingKeys"]
                ),
                data_source=base_data_source,
                max_batch_size=123,
                pipeline_config=[appsync_function],
                request_mapping_template=mapping_template,
                response_mapping_template=mapping_template
            )
        '''
        if isinstance(caching_config, dict):
            caching_config = CachingConfig(**caching_config)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__03f1147a0c345927a67b86638d192631cbb3ebb7cf920f9116c64ab461d319e3)
            check_type(argname="argument field_name", value=field_name, expected_type=type_hints["field_name"])
            check_type(argname="argument type_name", value=type_name, expected_type=type_hints["type_name"])
            check_type(argname="argument caching_config", value=caching_config, expected_type=type_hints["caching_config"])
            check_type(argname="argument max_batch_size", value=max_batch_size, expected_type=type_hints["max_batch_size"])
            check_type(argname="argument pipeline_config", value=pipeline_config, expected_type=type_hints["pipeline_config"])
            check_type(argname="argument request_mapping_template", value=request_mapping_template, expected_type=type_hints["request_mapping_template"])
            check_type(argname="argument response_mapping_template", value=response_mapping_template, expected_type=type_hints["response_mapping_template"])
            check_type(argname="argument data_source", value=data_source, expected_type=type_hints["data_source"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "field_name": field_name,
            "type_name": type_name,
        }
        if caching_config is not None:
            self._values["caching_config"] = caching_config
        if max_batch_size is not None:
            self._values["max_batch_size"] = max_batch_size
        if pipeline_config is not None:
            self._values["pipeline_config"] = pipeline_config
        if request_mapping_template is not None:
            self._values["request_mapping_template"] = request_mapping_template
        if response_mapping_template is not None:
            self._values["response_mapping_template"] = response_mapping_template
        if data_source is not None:
            self._values["data_source"] = data_source

    @builtins.property
    def field_name(self) -> builtins.str:
        '''(experimental) name of the GraphQL field in the given type this resolver is attached to.

        :stability: experimental
        '''
        result = self._values.get("field_name")
        assert result is not None, "Required property 'field_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type_name(self) -> builtins.str:
        '''(experimental) name of the GraphQL type this resolver is attached to.

        :stability: experimental
        '''
        result = self._values.get("type_name")
        assert result is not None, "Required property 'type_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def caching_config(self) -> typing.Optional[CachingConfig]:
        '''(experimental) The caching configuration for this resolver.

        :default: - No caching configuration

        :stability: experimental
        '''
        result = self._values.get("caching_config")
        return typing.cast(typing.Optional[CachingConfig], result)

    @builtins.property
    def max_batch_size(self) -> typing.Optional[jsii.Number]:
        '''(experimental) The maximum number of elements per batch, when using batch invoke.

        :default: - No max batch size

        :stability: experimental
        '''
        result = self._values.get("max_batch_size")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def pipeline_config(self) -> typing.Optional[typing.List["IAppsyncFunction"]]:
        '''(experimental) configuration of the pipeline resolver.

        :default:

        - no pipeline resolver configuration
        An empty array | undefined sets resolver to be of kind, unit

        :stability: experimental
        '''
        result = self._values.get("pipeline_config")
        return typing.cast(typing.Optional[typing.List["IAppsyncFunction"]], result)

    @builtins.property
    def request_mapping_template(self) -> typing.Optional["MappingTemplate"]:
        '''(experimental) The request mapping template for this resolver.

        :default: - No mapping template

        :stability: experimental
        '''
        result = self._values.get("request_mapping_template")
        return typing.cast(typing.Optional["MappingTemplate"], result)

    @builtins.property
    def response_mapping_template(self) -> typing.Optional["MappingTemplate"]:
        '''(experimental) The response mapping template for this resolver.

        :default: - No mapping template

        :stability: experimental
        '''
        result = self._values.get("response_mapping_template")
        return typing.cast(typing.Optional["MappingTemplate"], result)

    @builtins.property
    def data_source(self) -> typing.Optional[BaseDataSource]:
        '''(experimental) The data source this resolver is using.

        :default: - No datasource

        :stability: experimental
        '''
        result = self._values.get("data_source")
        return typing.cast(typing.Optional[BaseDataSource], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ExtendedResolverProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.enum(jsii_type="@aws-cdk/aws-appsync-alpha.FieldLogLevel")
class FieldLogLevel(enum.Enum):
    '''(experimental) log-level for fields in AppSync.

    :stability: experimental
    '''

    NONE = "NONE"
    '''(experimental) No logging.

    :stability: experimental
    '''
    ERROR = "ERROR"
    '''(experimental) Error logging.

    :stability: experimental
    '''
    ALL = "ALL"
    '''(experimental) All logging.

    :stability: experimental
    '''


@jsii.data_type(
    jsii_type="@aws-cdk/aws-appsync-alpha.GraphqlApiAttributes",
    jsii_struct_bases=[],
    name_mapping={
        "graphql_api_id": "graphqlApiId",
        "graphql_api_arn": "graphqlApiArn",
    },
)
class GraphqlApiAttributes:
    def __init__(
        self,
        *,
        graphql_api_id: builtins.str,
        graphql_api_arn: typing.Optional[builtins.str] = None,
    ) -> None:
        '''(experimental) Attributes for GraphQL imports.

        :param graphql_api_id: (experimental) an unique AWS AppSync GraphQL API identifier i.e. 'lxz775lwdrgcndgz3nurvac7oa'.
        :param graphql_api_arn: (experimental) the arn for the GraphQL Api. Default: - autogenerated arn

        :stability: experimental
        :exampleMetadata: infused

        Example::

            # api: appsync.GraphqlApi
            # table: dynamodb.Table
            
            imported_api = appsync.GraphqlApi.from_graphql_api_attributes(self, "IApi",
                graphql_api_id=api.api_id,
                graphql_api_arn=api.arn
            )
            imported_api.add_dynamo_db_data_source("TableDataSource", table)
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b955959104b2f3e9d432c1b7e9ba97a97d7ccc986380a56840ca2758111ef604)
            check_type(argname="argument graphql_api_id", value=graphql_api_id, expected_type=type_hints["graphql_api_id"])
            check_type(argname="argument graphql_api_arn", value=graphql_api_arn, expected_type=type_hints["graphql_api_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "graphql_api_id": graphql_api_id,
        }
        if graphql_api_arn is not None:
            self._values["graphql_api_arn"] = graphql_api_arn

    @builtins.property
    def graphql_api_id(self) -> builtins.str:
        '''(experimental) an unique AWS AppSync GraphQL API identifier i.e. 'lxz775lwdrgcndgz3nurvac7oa'.

        :stability: experimental
        '''
        result = self._values.get("graphql_api_id")
        assert result is not None, "Required property 'graphql_api_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def graphql_api_arn(self) -> typing.Optional[builtins.str]:
        '''(experimental) the arn for the GraphQL Api.

        :default: - autogenerated arn

        :stability: experimental
        '''
        result = self._values.get("graphql_api_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GraphqlApiAttributes(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@aws-cdk/aws-appsync-alpha.GraphqlApiProps",
    jsii_struct_bases=[],
    name_mapping={
        "name": "name",
        "schema": "schema",
        "authorization_config": "authorizationConfig",
        "domain_name": "domainName",
        "log_config": "logConfig",
        "xray_enabled": "xrayEnabled",
    },
)
class GraphqlApiProps:
    def __init__(
        self,
        *,
        name: builtins.str,
        schema: "ISchema",
        authorization_config: typing.Optional[typing.Union[AuthorizationConfig, typing.Dict[builtins.str, typing.Any]]] = None,
        domain_name: typing.Optional[typing.Union[DomainOptions, typing.Dict[builtins.str, typing.Any]]] = None,
        log_config: typing.Optional[typing.Union["LogConfig", typing.Dict[builtins.str, typing.Any]]] = None,
        xray_enabled: typing.Optional[builtins.bool] = None,
    ) -> None:
        '''(experimental) Properties for an AppSync GraphQL API.

        :param name: (experimental) the name of the GraphQL API.
        :param schema: (experimental) GraphQL schema definition. Specify how you want to define your schema. Schema.fromFile(filePath: string) allows schema definition through schema.graphql file Default: - schema will be generated code-first (i.e. addType, addObjectType, etc.)
        :param authorization_config: (experimental) Optional authorization configuration. Default: - API Key authorization
        :param domain_name: (experimental) The domain name configuration for the GraphQL API. The Route 53 hosted zone and CName DNS record must be configured in addition to this setting to enable custom domain URL Default: - no domain name
        :param log_config: (experimental) Logging configuration for this api. Default: - None
        :param xray_enabled: (experimental) A flag indicating whether or not X-Ray tracing is enabled for the GraphQL API. Default: - false

        :stability: experimental
        :exampleMetadata: infused

        Example::

            api = appsync.GraphqlApi(self, "api",
                name="api",
                schema=appsync.SchemaFile.from_asset(path.join(__dirname, "schema.graphql"))
            )
            
            http_ds = api.add_http_data_source("ds", "https://states.amazonaws.com",
                name="httpDsWithStepF",
                description="from appsync to StepFunctions Workflow",
                authorization_config=appsync.AwsIamConfig(
                    signing_region="us-east-1",
                    signing_service_name="states"
                )
            )
            
            http_ds.create_resolver("MutationCallStepFunctionResolver",
                type_name="Mutation",
                field_name="callStepFunction",
                request_mapping_template=appsync.MappingTemplate.from_file("request.vtl"),
                response_mapping_template=appsync.MappingTemplate.from_file("response.vtl")
            )
        '''
        if isinstance(authorization_config, dict):
            authorization_config = AuthorizationConfig(**authorization_config)
        if isinstance(domain_name, dict):
            domain_name = DomainOptions(**domain_name)
        if isinstance(log_config, dict):
            log_config = LogConfig(**log_config)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2ae7ca336b2b5866de05582f2dd15607c59c1dd91c84b9220160e01b90f87e94)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument schema", value=schema, expected_type=type_hints["schema"])
            check_type(argname="argument authorization_config", value=authorization_config, expected_type=type_hints["authorization_config"])
            check_type(argname="argument domain_name", value=domain_name, expected_type=type_hints["domain_name"])
            check_type(argname="argument log_config", value=log_config, expected_type=type_hints["log_config"])
            check_type(argname="argument xray_enabled", value=xray_enabled, expected_type=type_hints["xray_enabled"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "name": name,
            "schema": schema,
        }
        if authorization_config is not None:
            self._values["authorization_config"] = authorization_config
        if domain_name is not None:
            self._values["domain_name"] = domain_name
        if log_config is not None:
            self._values["log_config"] = log_config
        if xray_enabled is not None:
            self._values["xray_enabled"] = xray_enabled

    @builtins.property
    def name(self) -> builtins.str:
        '''(experimental) the name of the GraphQL API.

        :stability: experimental
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def schema(self) -> "ISchema":
        '''(experimental) GraphQL schema definition. Specify how you want to define your schema.

        Schema.fromFile(filePath: string) allows schema definition through schema.graphql file

        :default: - schema will be generated code-first (i.e. addType, addObjectType, etc.)

        :stability: experimental
        '''
        result = self._values.get("schema")
        assert result is not None, "Required property 'schema' is missing"
        return typing.cast("ISchema", result)

    @builtins.property
    def authorization_config(self) -> typing.Optional[AuthorizationConfig]:
        '''(experimental) Optional authorization configuration.

        :default: - API Key authorization

        :stability: experimental
        '''
        result = self._values.get("authorization_config")
        return typing.cast(typing.Optional[AuthorizationConfig], result)

    @builtins.property
    def domain_name(self) -> typing.Optional[DomainOptions]:
        '''(experimental) The domain name configuration for the GraphQL API.

        The Route 53 hosted zone and CName DNS record must be configured in addition to this setting to
        enable custom domain URL

        :default: - no domain name

        :stability: experimental
        '''
        result = self._values.get("domain_name")
        return typing.cast(typing.Optional[DomainOptions], result)

    @builtins.property
    def log_config(self) -> typing.Optional["LogConfig"]:
        '''(experimental) Logging configuration for this api.

        :default: - None

        :stability: experimental
        '''
        result = self._values.get("log_config")
        return typing.cast(typing.Optional["LogConfig"], result)

    @builtins.property
    def xray_enabled(self) -> typing.Optional[builtins.bool]:
        '''(experimental) A flag indicating whether or not X-Ray tracing is enabled for the GraphQL API.

        :default: - false

        :stability: experimental
        '''
        result = self._values.get("xray_enabled")
        return typing.cast(typing.Optional[builtins.bool], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GraphqlApiProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@aws-cdk/aws-appsync-alpha.HttpDataSourceOptions",
    jsii_struct_bases=[DataSourceOptions],
    name_mapping={
        "description": "description",
        "name": "name",
        "authorization_config": "authorizationConfig",
    },
)
class HttpDataSourceOptions(DataSourceOptions):
    def __init__(
        self,
        *,
        description: typing.Optional[builtins.str] = None,
        name: typing.Optional[builtins.str] = None,
        authorization_config: typing.Optional[typing.Union[AwsIamConfig, typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''(experimental) Optional configuration for Http data sources.

        :param description: (experimental) The description of the data source. Default: - No description
        :param name: (experimental) The name of the data source, overrides the id given by cdk. Default: - generated by cdk given the id
        :param authorization_config: (experimental) The authorization config in case the HTTP endpoint requires authorization. Default: - none

        :stability: experimental
        :exampleMetadata: infused

        Example::

            api = appsync.GraphqlApi(self, "api",
                name="api",
                schema=appsync.SchemaFile.from_asset(path.join(__dirname, "schema.graphql"))
            )
            
            http_ds = api.add_http_data_source("ds", "https://states.amazonaws.com",
                name="httpDsWithStepF",
                description="from appsync to StepFunctions Workflow",
                authorization_config=appsync.AwsIamConfig(
                    signing_region="us-east-1",
                    signing_service_name="states"
                )
            )
            
            http_ds.create_resolver("MutationCallStepFunctionResolver",
                type_name="Mutation",
                field_name="callStepFunction",
                request_mapping_template=appsync.MappingTemplate.from_file("request.vtl"),
                response_mapping_template=appsync.MappingTemplate.from_file("response.vtl")
            )
        '''
        if isinstance(authorization_config, dict):
            authorization_config = AwsIamConfig(**authorization_config)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9871a67ca2dd2cf444a8b2cfbe0b1832a07ef45ea81c443c282b11e117b4d7c7)
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument authorization_config", value=authorization_config, expected_type=type_hints["authorization_config"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if description is not None:
            self._values["description"] = description
        if name is not None:
            self._values["name"] = name
        if authorization_config is not None:
            self._values["authorization_config"] = authorization_config

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''(experimental) The description of the data source.

        :default: - No description

        :stability: experimental
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''(experimental) The name of the data source, overrides the id given by cdk.

        :default: - generated by cdk given the id

        :stability: experimental
        '''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def authorization_config(self) -> typing.Optional[AwsIamConfig]:
        '''(experimental) The authorization config in case the HTTP endpoint requires authorization.

        :default: - none

        :stability: experimental
        '''
        result = self._values.get("authorization_config")
        return typing.cast(typing.Optional[AwsIamConfig], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "HttpDataSourceOptions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@aws-cdk/aws-appsync-alpha.HttpDataSourceProps",
    jsii_struct_bases=[BaseDataSourceProps],
    name_mapping={
        "api": "api",
        "description": "description",
        "name": "name",
        "endpoint": "endpoint",
        "authorization_config": "authorizationConfig",
    },
)
class HttpDataSourceProps(BaseDataSourceProps):
    def __init__(
        self,
        *,
        api: "IGraphqlApi",
        description: typing.Optional[builtins.str] = None,
        name: typing.Optional[builtins.str] = None,
        endpoint: builtins.str,
        authorization_config: typing.Optional[typing.Union[AwsIamConfig, typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''(experimental) Properties for an AppSync http datasource.

        :param api: (experimental) The API to attach this data source to.
        :param description: (experimental) the description of the data source. Default: - None
        :param name: (experimental) The name of the data source. Default: - id of data source
        :param endpoint: (experimental) The http endpoint.
        :param authorization_config: (experimental) The authorization config in case the HTTP endpoint requires authorization. Default: - none

        :stability: experimental
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            import aws_cdk.aws_appsync_alpha as appsync_alpha
            
            # graphql_api: appsync_alpha.GraphqlApi
            
            http_data_source_props = appsync_alpha.HttpDataSourceProps(
                api=graphql_api,
                endpoint="endpoint",
            
                # the properties below are optional
                authorization_config=appsync_alpha.AwsIamConfig(
                    signing_region="signingRegion",
                    signing_service_name="signingServiceName"
                ),
                description="description",
                name="name"
            )
        '''
        if isinstance(authorization_config, dict):
            authorization_config = AwsIamConfig(**authorization_config)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__89dc282ac92a5f3d2f4eca5d3d197e40ce4abe4440127160825a934090a73b07)
            check_type(argname="argument api", value=api, expected_type=type_hints["api"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument endpoint", value=endpoint, expected_type=type_hints["endpoint"])
            check_type(argname="argument authorization_config", value=authorization_config, expected_type=type_hints["authorization_config"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "api": api,
            "endpoint": endpoint,
        }
        if description is not None:
            self._values["description"] = description
        if name is not None:
            self._values["name"] = name
        if authorization_config is not None:
            self._values["authorization_config"] = authorization_config

    @builtins.property
    def api(self) -> "IGraphqlApi":
        '''(experimental) The API to attach this data source to.

        :stability: experimental
        '''
        result = self._values.get("api")
        assert result is not None, "Required property 'api' is missing"
        return typing.cast("IGraphqlApi", result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''(experimental) the description of the data source.

        :default: - None

        :stability: experimental
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''(experimental) The name of the data source.

        :default: - id of data source

        :stability: experimental
        '''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def endpoint(self) -> builtins.str:
        '''(experimental) The http endpoint.

        :stability: experimental
        '''
        result = self._values.get("endpoint")
        assert result is not None, "Required property 'endpoint' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def authorization_config(self) -> typing.Optional[AwsIamConfig]:
        '''(experimental) The authorization config in case the HTTP endpoint requires authorization.

        :default: - none

        :stability: experimental
        '''
        result = self._values.get("authorization_config")
        return typing.cast(typing.Optional[AwsIamConfig], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "HttpDataSourceProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.interface(jsii_type="@aws-cdk/aws-appsync-alpha.IAppsyncFunction")
class IAppsyncFunction(_aws_cdk_ceddda9d.IResource, typing_extensions.Protocol):
    '''(experimental) Interface for AppSync Functions.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="functionArn")
    def function_arn(self) -> builtins.str:
        '''(experimental) the ARN of the AppSync function.

        :stability: experimental
        :attribute: true
        '''
        ...

    @builtins.property
    @jsii.member(jsii_name="functionId")
    def function_id(self) -> builtins.str:
        '''(experimental) the name of this AppSync Function.

        :stability: experimental
        :attribute: true
        '''
        ...


class _IAppsyncFunctionProxy(
    jsii.proxy_for(_aws_cdk_ceddda9d.IResource), # type: ignore[misc]
):
    '''(experimental) Interface for AppSync Functions.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "@aws-cdk/aws-appsync-alpha.IAppsyncFunction"

    @builtins.property
    @jsii.member(jsii_name="functionArn")
    def function_arn(self) -> builtins.str:
        '''(experimental) the ARN of the AppSync function.

        :stability: experimental
        :attribute: true
        '''
        return typing.cast(builtins.str, jsii.get(self, "functionArn"))

    @builtins.property
    @jsii.member(jsii_name="functionId")
    def function_id(self) -> builtins.str:
        '''(experimental) the name of this AppSync Function.

        :stability: experimental
        :attribute: true
        '''
        return typing.cast(builtins.str, jsii.get(self, "functionId"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IAppsyncFunction).__jsii_proxy_class__ = lambda : _IAppsyncFunctionProxy


@jsii.interface(jsii_type="@aws-cdk/aws-appsync-alpha.IGraphqlApi")
class IGraphqlApi(_aws_cdk_ceddda9d.IResource, typing_extensions.Protocol):
    '''(experimental) Interface for GraphQL.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="apiId")
    def api_id(self) -> builtins.str:
        '''(experimental) an unique AWS AppSync GraphQL API identifier i.e. 'lxz775lwdrgcndgz3nurvac7oa'.

        :stability: experimental
        :attribute: true
        '''
        ...

    @builtins.property
    @jsii.member(jsii_name="arn")
    def arn(self) -> builtins.str:
        '''(experimental) the ARN of the API.

        :stability: experimental
        :attribute: true
        '''
        ...

    @jsii.member(jsii_name="addDynamoDbDataSource")
    def add_dynamo_db_data_source(
        self,
        id: builtins.str,
        table: _aws_cdk_aws_dynamodb_ceddda9d.ITable,
        *,
        description: typing.Optional[builtins.str] = None,
        name: typing.Optional[builtins.str] = None,
    ) -> "DynamoDbDataSource":
        '''(experimental) add a new DynamoDB data source to this API.

        :param id: The data source's id.
        :param table: The DynamoDB table backing this data source.
        :param description: (experimental) The description of the data source. Default: - No description
        :param name: (experimental) The name of the data source, overrides the id given by cdk. Default: - generated by cdk given the id

        :stability: experimental
        '''
        ...

    @jsii.member(jsii_name="addElasticsearchDataSource")
    def add_elasticsearch_data_source(
        self,
        id: builtins.str,
        domain: _aws_cdk_aws_elasticsearch_ceddda9d.IDomain,
        *,
        description: typing.Optional[builtins.str] = None,
        name: typing.Optional[builtins.str] = None,
    ) -> "ElasticsearchDataSource":
        '''(deprecated) add a new elasticsearch data source to this API.

        :param id: The data source's id.
        :param domain: The elasticsearch domain for this data source.
        :param description: (experimental) The description of the data source. Default: - No description
        :param name: (experimental) The name of the data source, overrides the id given by cdk. Default: - generated by cdk given the id

        :deprecated: - use ``addOpenSearchDataSource``

        :stability: deprecated
        '''
        ...

    @jsii.member(jsii_name="addHttpDataSource")
    def add_http_data_source(
        self,
        id: builtins.str,
        endpoint: builtins.str,
        *,
        authorization_config: typing.Optional[typing.Union[AwsIamConfig, typing.Dict[builtins.str, typing.Any]]] = None,
        description: typing.Optional[builtins.str] = None,
        name: typing.Optional[builtins.str] = None,
    ) -> "HttpDataSource":
        '''(experimental) add a new http data source to this API.

        :param id: The data source's id.
        :param endpoint: The http endpoint.
        :param authorization_config: (experimental) The authorization config in case the HTTP endpoint requires authorization. Default: - none
        :param description: (experimental) The description of the data source. Default: - No description
        :param name: (experimental) The name of the data source, overrides the id given by cdk. Default: - generated by cdk given the id

        :stability: experimental
        '''
        ...

    @jsii.member(jsii_name="addLambdaDataSource")
    def add_lambda_data_source(
        self,
        id: builtins.str,
        lambda_function: _aws_cdk_aws_lambda_ceddda9d.IFunction,
        *,
        description: typing.Optional[builtins.str] = None,
        name: typing.Optional[builtins.str] = None,
    ) -> "LambdaDataSource":
        '''(experimental) add a new Lambda data source to this API.

        :param id: The data source's id.
        :param lambda_function: The Lambda function to call to interact with this data source.
        :param description: (experimental) The description of the data source. Default: - No description
        :param name: (experimental) The name of the data source, overrides the id given by cdk. Default: - generated by cdk given the id

        :stability: experimental
        '''
        ...

    @jsii.member(jsii_name="addNoneDataSource")
    def add_none_data_source(
        self,
        id: builtins.str,
        *,
        description: typing.Optional[builtins.str] = None,
        name: typing.Optional[builtins.str] = None,
    ) -> "NoneDataSource":
        '''(experimental) add a new dummy data source to this API.

        Useful for pipeline resolvers
        and for backend changes that don't require a data source.

        :param id: The data source's id.
        :param description: (experimental) The description of the data source. Default: - No description
        :param name: (experimental) The name of the data source, overrides the id given by cdk. Default: - generated by cdk given the id

        :stability: experimental
        '''
        ...

    @jsii.member(jsii_name="addOpenSearchDataSource")
    def add_open_search_data_source(
        self,
        id: builtins.str,
        domain: _aws_cdk_aws_opensearchservice_ceddda9d.IDomain,
        *,
        description: typing.Optional[builtins.str] = None,
        name: typing.Optional[builtins.str] = None,
    ) -> "OpenSearchDataSource":
        '''(experimental) Add a new OpenSearch data source to this API.

        :param id: The data source's id.
        :param domain: The OpenSearch domain for this data source.
        :param description: (experimental) The description of the data source. Default: - No description
        :param name: (experimental) The name of the data source, overrides the id given by cdk. Default: - generated by cdk given the id

        :stability: experimental
        '''
        ...

    @jsii.member(jsii_name="addRdsDataSource")
    def add_rds_data_source(
        self,
        id: builtins.str,
        serverless_cluster: _aws_cdk_aws_rds_ceddda9d.IServerlessCluster,
        secret_store: _aws_cdk_aws_secretsmanager_ceddda9d.ISecret,
        database_name: typing.Optional[builtins.str] = None,
        *,
        description: typing.Optional[builtins.str] = None,
        name: typing.Optional[builtins.str] = None,
    ) -> "RdsDataSource":
        '''(experimental) add a new Rds data source to this API.

        :param id: The data source's id.
        :param serverless_cluster: The serverless cluster to interact with this data source.
        :param secret_store: The secret store that contains the username and password for the serverless cluster.
        :param database_name: The optional name of the database to use within the cluster.
        :param description: (experimental) The description of the data source. Default: - No description
        :param name: (experimental) The name of the data source, overrides the id given by cdk. Default: - generated by cdk given the id

        :stability: experimental
        '''
        ...

    @jsii.member(jsii_name="addSchemaDependency")
    def add_schema_dependency(
        self,
        construct: _aws_cdk_ceddda9d.CfnResource,
    ) -> builtins.bool:
        '''(experimental) Add schema dependency if not imported.

        :param construct: the dependee.

        :stability: experimental
        '''
        ...

    @jsii.member(jsii_name="createResolver")
    def create_resolver(
        self,
        id: builtins.str,
        *,
        data_source: typing.Optional[BaseDataSource] = None,
        field_name: builtins.str,
        type_name: builtins.str,
        caching_config: typing.Optional[typing.Union[CachingConfig, typing.Dict[builtins.str, typing.Any]]] = None,
        max_batch_size: typing.Optional[jsii.Number] = None,
        pipeline_config: typing.Optional[typing.Sequence[IAppsyncFunction]] = None,
        request_mapping_template: typing.Optional["MappingTemplate"] = None,
        response_mapping_template: typing.Optional["MappingTemplate"] = None,
    ) -> "Resolver":
        '''(experimental) creates a new resolver for this datasource and API using the given properties.

        :param id: -
        :param data_source: (experimental) The data source this resolver is using. Default: - No datasource
        :param field_name: (experimental) name of the GraphQL field in the given type this resolver is attached to.
        :param type_name: (experimental) name of the GraphQL type this resolver is attached to.
        :param caching_config: (experimental) The caching configuration for this resolver. Default: - No caching configuration
        :param max_batch_size: (experimental) The maximum number of elements per batch, when using batch invoke. Default: - No max batch size
        :param pipeline_config: (experimental) configuration of the pipeline resolver. Default: - no pipeline resolver configuration An empty array | undefined sets resolver to be of kind, unit
        :param request_mapping_template: (experimental) The request mapping template for this resolver. Default: - No mapping template
        :param response_mapping_template: (experimental) The response mapping template for this resolver. Default: - No mapping template

        :stability: experimental
        '''
        ...


class _IGraphqlApiProxy(
    jsii.proxy_for(_aws_cdk_ceddda9d.IResource), # type: ignore[misc]
):
    '''(experimental) Interface for GraphQL.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "@aws-cdk/aws-appsync-alpha.IGraphqlApi"

    @builtins.property
    @jsii.member(jsii_name="apiId")
    def api_id(self) -> builtins.str:
        '''(experimental) an unique AWS AppSync GraphQL API identifier i.e. 'lxz775lwdrgcndgz3nurvac7oa'.

        :stability: experimental
        :attribute: true
        '''
        return typing.cast(builtins.str, jsii.get(self, "apiId"))

    @builtins.property
    @jsii.member(jsii_name="arn")
    def arn(self) -> builtins.str:
        '''(experimental) the ARN of the API.

        :stability: experimental
        :attribute: true
        '''
        return typing.cast(builtins.str, jsii.get(self, "arn"))

    @jsii.member(jsii_name="addDynamoDbDataSource")
    def add_dynamo_db_data_source(
        self,
        id: builtins.str,
        table: _aws_cdk_aws_dynamodb_ceddda9d.ITable,
        *,
        description: typing.Optional[builtins.str] = None,
        name: typing.Optional[builtins.str] = None,
    ) -> "DynamoDbDataSource":
        '''(experimental) add a new DynamoDB data source to this API.

        :param id: The data source's id.
        :param table: The DynamoDB table backing this data source.
        :param description: (experimental) The description of the data source. Default: - No description
        :param name: (experimental) The name of the data source, overrides the id given by cdk. Default: - generated by cdk given the id

        :stability: experimental
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ff2ae55f5180f89ed93ef13fa0c7ecceb1eb90bee7521aa97617041f0a549e9b)
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument table", value=table, expected_type=type_hints["table"])
        options = DataSourceOptions(description=description, name=name)

        return typing.cast("DynamoDbDataSource", jsii.invoke(self, "addDynamoDbDataSource", [id, table, options]))

    @jsii.member(jsii_name="addElasticsearchDataSource")
    def add_elasticsearch_data_source(
        self,
        id: builtins.str,
        domain: _aws_cdk_aws_elasticsearch_ceddda9d.IDomain,
        *,
        description: typing.Optional[builtins.str] = None,
        name: typing.Optional[builtins.str] = None,
    ) -> "ElasticsearchDataSource":
        '''(deprecated) add a new elasticsearch data source to this API.

        :param id: The data source's id.
        :param domain: The elasticsearch domain for this data source.
        :param description: (experimental) The description of the data source. Default: - No description
        :param name: (experimental) The name of the data source, overrides the id given by cdk. Default: - generated by cdk given the id

        :deprecated: - use ``addOpenSearchDataSource``

        :stability: deprecated
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e0a7a045a50e105c29fbe85eecdc85bf5e477b5ca2830d524cd42de5b8c50a35)
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument domain", value=domain, expected_type=type_hints["domain"])
        options = DataSourceOptions(description=description, name=name)

        return typing.cast("ElasticsearchDataSource", jsii.invoke(self, "addElasticsearchDataSource", [id, domain, options]))

    @jsii.member(jsii_name="addHttpDataSource")
    def add_http_data_source(
        self,
        id: builtins.str,
        endpoint: builtins.str,
        *,
        authorization_config: typing.Optional[typing.Union[AwsIamConfig, typing.Dict[builtins.str, typing.Any]]] = None,
        description: typing.Optional[builtins.str] = None,
        name: typing.Optional[builtins.str] = None,
    ) -> "HttpDataSource":
        '''(experimental) add a new http data source to this API.

        :param id: The data source's id.
        :param endpoint: The http endpoint.
        :param authorization_config: (experimental) The authorization config in case the HTTP endpoint requires authorization. Default: - none
        :param description: (experimental) The description of the data source. Default: - No description
        :param name: (experimental) The name of the data source, overrides the id given by cdk. Default: - generated by cdk given the id

        :stability: experimental
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fc508a77d0bf87c350f1e50bf16ddcf8f2b1edf36752e9a6a5759912e0ef7025)
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument endpoint", value=endpoint, expected_type=type_hints["endpoint"])
        options = HttpDataSourceOptions(
            authorization_config=authorization_config,
            description=description,
            name=name,
        )

        return typing.cast("HttpDataSource", jsii.invoke(self, "addHttpDataSource", [id, endpoint, options]))

    @jsii.member(jsii_name="addLambdaDataSource")
    def add_lambda_data_source(
        self,
        id: builtins.str,
        lambda_function: _aws_cdk_aws_lambda_ceddda9d.IFunction,
        *,
        description: typing.Optional[builtins.str] = None,
        name: typing.Optional[builtins.str] = None,
    ) -> "LambdaDataSource":
        '''(experimental) add a new Lambda data source to this API.

        :param id: The data source's id.
        :param lambda_function: The Lambda function to call to interact with this data source.
        :param description: (experimental) The description of the data source. Default: - No description
        :param name: (experimental) The name of the data source, overrides the id given by cdk. Default: - generated by cdk given the id

        :stability: experimental
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b09472740cf51bd70588a88680d9e9bfb0c43e6ce6829eaa7db6719cc888de29)
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument lambda_function", value=lambda_function, expected_type=type_hints["lambda_function"])
        options = DataSourceOptions(description=description, name=name)

        return typing.cast("LambdaDataSource", jsii.invoke(self, "addLambdaDataSource", [id, lambda_function, options]))

    @jsii.member(jsii_name="addNoneDataSource")
    def add_none_data_source(
        self,
        id: builtins.str,
        *,
        description: typing.Optional[builtins.str] = None,
        name: typing.Optional[builtins.str] = None,
    ) -> "NoneDataSource":
        '''(experimental) add a new dummy data source to this API.

        Useful for pipeline resolvers
        and for backend changes that don't require a data source.

        :param id: The data source's id.
        :param description: (experimental) The description of the data source. Default: - No description
        :param name: (experimental) The name of the data source, overrides the id given by cdk. Default: - generated by cdk given the id

        :stability: experimental
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5b4d3c2f5386ab847f1317af811d59fbbda87fe916d2a4f6bbd35a3458a91a76)
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        options = DataSourceOptions(description=description, name=name)

        return typing.cast("NoneDataSource", jsii.invoke(self, "addNoneDataSource", [id, options]))

    @jsii.member(jsii_name="addOpenSearchDataSource")
    def add_open_search_data_source(
        self,
        id: builtins.str,
        domain: _aws_cdk_aws_opensearchservice_ceddda9d.IDomain,
        *,
        description: typing.Optional[builtins.str] = None,
        name: typing.Optional[builtins.str] = None,
    ) -> "OpenSearchDataSource":
        '''(experimental) Add a new OpenSearch data source to this API.

        :param id: The data source's id.
        :param domain: The OpenSearch domain for this data source.
        :param description: (experimental) The description of the data source. Default: - No description
        :param name: (experimental) The name of the data source, overrides the id given by cdk. Default: - generated by cdk given the id

        :stability: experimental
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__99b1759e6e50fc3fb6c0cc4ecee7445d98d908aa6aecd0041d548db46f72ffb9)
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument domain", value=domain, expected_type=type_hints["domain"])
        options = DataSourceOptions(description=description, name=name)

        return typing.cast("OpenSearchDataSource", jsii.invoke(self, "addOpenSearchDataSource", [id, domain, options]))

    @jsii.member(jsii_name="addRdsDataSource")
    def add_rds_data_source(
        self,
        id: builtins.str,
        serverless_cluster: _aws_cdk_aws_rds_ceddda9d.IServerlessCluster,
        secret_store: _aws_cdk_aws_secretsmanager_ceddda9d.ISecret,
        database_name: typing.Optional[builtins.str] = None,
        *,
        description: typing.Optional[builtins.str] = None,
        name: typing.Optional[builtins.str] = None,
    ) -> "RdsDataSource":
        '''(experimental) add a new Rds data source to this API.

        :param id: The data source's id.
        :param serverless_cluster: The serverless cluster to interact with this data source.
        :param secret_store: The secret store that contains the username and password for the serverless cluster.
        :param database_name: The optional name of the database to use within the cluster.
        :param description: (experimental) The description of the data source. Default: - No description
        :param name: (experimental) The name of the data source, overrides the id given by cdk. Default: - generated by cdk given the id

        :stability: experimental
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__78791ea5025839853c0dcfdb18166f833bba60087b82eb17c8afa2f9302901f9)
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument serverless_cluster", value=serverless_cluster, expected_type=type_hints["serverless_cluster"])
            check_type(argname="argument secret_store", value=secret_store, expected_type=type_hints["secret_store"])
            check_type(argname="argument database_name", value=database_name, expected_type=type_hints["database_name"])
        options = DataSourceOptions(description=description, name=name)

        return typing.cast("RdsDataSource", jsii.invoke(self, "addRdsDataSource", [id, serverless_cluster, secret_store, database_name, options]))

    @jsii.member(jsii_name="addSchemaDependency")
    def add_schema_dependency(
        self,
        construct: _aws_cdk_ceddda9d.CfnResource,
    ) -> builtins.bool:
        '''(experimental) Add schema dependency if not imported.

        :param construct: the dependee.

        :stability: experimental
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7fd621ea81eec4c759f3ef88dd4c25efb275910cdc93e28e795c91bcee871626)
            check_type(argname="argument construct", value=construct, expected_type=type_hints["construct"])
        return typing.cast(builtins.bool, jsii.invoke(self, "addSchemaDependency", [construct]))

    @jsii.member(jsii_name="createResolver")
    def create_resolver(
        self,
        id: builtins.str,
        *,
        data_source: typing.Optional[BaseDataSource] = None,
        field_name: builtins.str,
        type_name: builtins.str,
        caching_config: typing.Optional[typing.Union[CachingConfig, typing.Dict[builtins.str, typing.Any]]] = None,
        max_batch_size: typing.Optional[jsii.Number] = None,
        pipeline_config: typing.Optional[typing.Sequence[IAppsyncFunction]] = None,
        request_mapping_template: typing.Optional["MappingTemplate"] = None,
        response_mapping_template: typing.Optional["MappingTemplate"] = None,
    ) -> "Resolver":
        '''(experimental) creates a new resolver for this datasource and API using the given properties.

        :param id: -
        :param data_source: (experimental) The data source this resolver is using. Default: - No datasource
        :param field_name: (experimental) name of the GraphQL field in the given type this resolver is attached to.
        :param type_name: (experimental) name of the GraphQL type this resolver is attached to.
        :param caching_config: (experimental) The caching configuration for this resolver. Default: - No caching configuration
        :param max_batch_size: (experimental) The maximum number of elements per batch, when using batch invoke. Default: - No max batch size
        :param pipeline_config: (experimental) configuration of the pipeline resolver. Default: - no pipeline resolver configuration An empty array | undefined sets resolver to be of kind, unit
        :param request_mapping_template: (experimental) The request mapping template for this resolver. Default: - No mapping template
        :param response_mapping_template: (experimental) The response mapping template for this resolver. Default: - No mapping template

        :stability: experimental
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d950aad73fe8c1264ecd6c12999cf8fa3c2aee009208495b4eed8e1693d34916)
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = ExtendedResolverProps(
            data_source=data_source,
            field_name=field_name,
            type_name=type_name,
            caching_config=caching_config,
            max_batch_size=max_batch_size,
            pipeline_config=pipeline_config,
            request_mapping_template=request_mapping_template,
            response_mapping_template=response_mapping_template,
        )

        return typing.cast("Resolver", jsii.invoke(self, "createResolver", [id, props]))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IGraphqlApi).__jsii_proxy_class__ = lambda : _IGraphqlApiProxy


@jsii.interface(jsii_type="@aws-cdk/aws-appsync-alpha.ISchema")
class ISchema(typing_extensions.Protocol):
    '''(experimental) Interface for implementing your own schema.

    Useful for providing schema's from sources other than assets

    :stability: experimental
    '''

    @jsii.member(jsii_name="bind")
    def bind(self, api: IGraphqlApi) -> "ISchemaConfig":
        '''(experimental) Binds a schema string to a GraphQlApi.

        :param api: the api to bind the schema to.

        :return: ISchemaConfig with apiId and schema definition string

        :stability: experimental
        '''
        ...


class _ISchemaProxy:
    '''(experimental) Interface for implementing your own schema.

    Useful for providing schema's from sources other than assets

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "@aws-cdk/aws-appsync-alpha.ISchema"

    @jsii.member(jsii_name="bind")
    def bind(self, api: IGraphqlApi) -> "ISchemaConfig":
        '''(experimental) Binds a schema string to a GraphQlApi.

        :param api: the api to bind the schema to.

        :return: ISchemaConfig with apiId and schema definition string

        :stability: experimental
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__dd4d10a0673d71595a61dc4bb10b344bca207d9a1006f2fbdeb9dae0dc415813)
            check_type(argname="argument api", value=api, expected_type=type_hints["api"])
        options = SchemaBindOptions()

        return typing.cast("ISchemaConfig", jsii.invoke(self, "bind", [api, options]))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, ISchema).__jsii_proxy_class__ = lambda : _ISchemaProxy


@jsii.interface(jsii_type="@aws-cdk/aws-appsync-alpha.ISchemaConfig")
class ISchemaConfig(typing_extensions.Protocol):
    '''(experimental) Configuration for bound graphql schema.

    Returned from ISchema.bind allowing late binding of schemas to graphqlapi-base

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="apiId")
    def api_id(self) -> builtins.str:
        '''(experimental) The ID of the api the schema is bound to.

        :stability: experimental
        '''
        ...

    @api_id.setter
    def api_id(self, value: builtins.str) -> None:
        ...

    @builtins.property
    @jsii.member(jsii_name="definition")
    def definition(self) -> builtins.str:
        '''(experimental) The schema definition string.

        :stability: experimental
        '''
        ...

    @definition.setter
    def definition(self, value: builtins.str) -> None:
        ...


class _ISchemaConfigProxy:
    '''(experimental) Configuration for bound graphql schema.

    Returned from ISchema.bind allowing late binding of schemas to graphqlapi-base

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "@aws-cdk/aws-appsync-alpha.ISchemaConfig"

    @builtins.property
    @jsii.member(jsii_name="apiId")
    def api_id(self) -> builtins.str:
        '''(experimental) The ID of the api the schema is bound to.

        :stability: experimental
        '''
        return typing.cast(builtins.str, jsii.get(self, "apiId"))

    @api_id.setter
    def api_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bb8546d484aa114efdb76ea1c5936dd17700b77edd7fe05d087febc1a2124f9d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "apiId", value)

    @builtins.property
    @jsii.member(jsii_name="definition")
    def definition(self) -> builtins.str:
        '''(experimental) The schema definition string.

        :stability: experimental
        '''
        return typing.cast(builtins.str, jsii.get(self, "definition"))

    @definition.setter
    def definition(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__59fbd981dd279d0e7e3eeb7b1ef47a81c7b418737ff11744afeae2d4988e32a2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "definition", value)

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, ISchemaConfig).__jsii_proxy_class__ = lambda : _ISchemaConfigProxy


class IamResource(
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/aws-appsync-alpha.IamResource",
):
    '''(experimental) A class used to generate resource arns for AppSync.

    :stability: experimental
    :exampleMetadata: infused

    Example::

        # api: appsync.GraphqlApi
        role = iam.Role(self, "Role",
            assumed_by=iam.ServicePrincipal("lambda.amazonaws.com")
        )
        
        api.grant(role, appsync.IamResource.custom("types/Mutation/fields/updateExample"), "appsync:GraphQL")
    '''

    @jsii.member(jsii_name="all")
    @builtins.classmethod
    def all(cls) -> "IamResource":
        '''(experimental) Generate the resource names that accepts all types: ``*``.

        :stability: experimental
        '''
        return typing.cast("IamResource", jsii.sinvoke(cls, "all", []))

    @jsii.member(jsii_name="custom")
    @builtins.classmethod
    def custom(cls, *arns: builtins.str) -> "IamResource":
        '''(experimental) Generate the resource names given custom arns.

        :param arns: The custom arns that need to be permissioned. Example: custom('/types/Query/fields/getExample')

        :stability: experimental
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c6f60e3a1ac4741bd3c425e40094fe5f56ea9ccde593a2913b08ff83c5c218d5)
            check_type(argname="argument arns", value=arns, expected_type=typing.Tuple[type_hints["arns"], ...]) # pyright: ignore [reportGeneralTypeIssues]
        return typing.cast("IamResource", jsii.sinvoke(cls, "custom", [*arns]))

    @jsii.member(jsii_name="ofType")
    @builtins.classmethod
    def of_type(cls, type: builtins.str, *fields: builtins.str) -> "IamResource":
        '''(experimental) Generate the resource names given a type and fields.

        :param type: The type that needs to be allowed.
        :param fields: The fields that need to be allowed, if empty grant permissions to ALL fields. Example: ofType('Query', 'GetExample')

        :stability: experimental
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d713a6dda131c90c74621df3df92e7fa8a68fb94973c2211649b62def0b137f9)
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
            check_type(argname="argument fields", value=fields, expected_type=typing.Tuple[type_hints["fields"], ...]) # pyright: ignore [reportGeneralTypeIssues]
        return typing.cast("IamResource", jsii.sinvoke(cls, "ofType", [type, *fields]))

    @jsii.member(jsii_name="resourceArns")
    def resource_arns(self, api: "GraphqlApi") -> typing.List[builtins.str]:
        '''(experimental) Return the Resource ARN.

        :param api: The GraphQL API to give permissions.

        :stability: experimental
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__23e87d2e18ac29ea314572a6b768d884ac9ad9bc4e883dcd1d62a41834bea3ea)
            check_type(argname="argument api", value=api, expected_type=type_hints["api"])
        return typing.cast(typing.List[builtins.str], jsii.invoke(self, "resourceArns", [api]))


class KeyCondition(
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/aws-appsync-alpha.KeyCondition",
):
    '''(experimental) Factory class for DynamoDB key conditions.

    :stability: experimental
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        import aws_cdk.aws_appsync_alpha as appsync_alpha
        
        key_condition = appsync_alpha.KeyCondition.begins_with("keyName", "arg")
    '''

    @jsii.member(jsii_name="beginsWith")
    @builtins.classmethod
    def begins_with(cls, key_name: builtins.str, arg: builtins.str) -> "KeyCondition":
        '''(experimental) Condition (k, arg).

        True if the key attribute k begins with the Query argument.

        :param key_name: -
        :param arg: -

        :stability: experimental
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__249d661d83f55f407b240686349b23c6481909b60d2f14ff74045e4d25a3cf6c)
            check_type(argname="argument key_name", value=key_name, expected_type=type_hints["key_name"])
            check_type(argname="argument arg", value=arg, expected_type=type_hints["arg"])
        return typing.cast("KeyCondition", jsii.sinvoke(cls, "beginsWith", [key_name, arg]))

    @jsii.member(jsii_name="between")
    @builtins.classmethod
    def between(
        cls,
        key_name: builtins.str,
        arg1: builtins.str,
        arg2: builtins.str,
    ) -> "KeyCondition":
        '''(experimental) Condition k BETWEEN arg1 AND arg2, true if k >= arg1 and k <= arg2.

        :param key_name: -
        :param arg1: -
        :param arg2: -

        :stability: experimental
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cf4b6c447afa94150fb522751b30ac92d849a8e075eeeb8bd8e5aa248411b2c1)
            check_type(argname="argument key_name", value=key_name, expected_type=type_hints["key_name"])
            check_type(argname="argument arg1", value=arg1, expected_type=type_hints["arg1"])
            check_type(argname="argument arg2", value=arg2, expected_type=type_hints["arg2"])
        return typing.cast("KeyCondition", jsii.sinvoke(cls, "between", [key_name, arg1, arg2]))

    @jsii.member(jsii_name="eq")
    @builtins.classmethod
    def eq(cls, key_name: builtins.str, arg: builtins.str) -> "KeyCondition":
        '''(experimental) Condition k = arg, true if the key attribute k is equal to the Query argument.

        :param key_name: -
        :param arg: -

        :stability: experimental
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b94e5f52a19e49dfd1f6583a49cdc85f11d062218e64487e88c721d13a24db6b)
            check_type(argname="argument key_name", value=key_name, expected_type=type_hints["key_name"])
            check_type(argname="argument arg", value=arg, expected_type=type_hints["arg"])
        return typing.cast("KeyCondition", jsii.sinvoke(cls, "eq", [key_name, arg]))

    @jsii.member(jsii_name="ge")
    @builtins.classmethod
    def ge(cls, key_name: builtins.str, arg: builtins.str) -> "KeyCondition":
        '''(experimental) Condition k >= arg, true if the key attribute k is greater or equal to the Query argument.

        :param key_name: -
        :param arg: -

        :stability: experimental
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d44bcbcfc6e10e5782ed664f9ae213b2c3dbb20dc50ff985e70af6adba1f26f0)
            check_type(argname="argument key_name", value=key_name, expected_type=type_hints["key_name"])
            check_type(argname="argument arg", value=arg, expected_type=type_hints["arg"])
        return typing.cast("KeyCondition", jsii.sinvoke(cls, "ge", [key_name, arg]))

    @jsii.member(jsii_name="gt")
    @builtins.classmethod
    def gt(cls, key_name: builtins.str, arg: builtins.str) -> "KeyCondition":
        '''(experimental) Condition k > arg, true if the key attribute k is greater than the the Query argument.

        :param key_name: -
        :param arg: -

        :stability: experimental
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__48446eaa70b45f70cb39edb4ec644179feba91a0a515c80b62c8973f2ce475dd)
            check_type(argname="argument key_name", value=key_name, expected_type=type_hints["key_name"])
            check_type(argname="argument arg", value=arg, expected_type=type_hints["arg"])
        return typing.cast("KeyCondition", jsii.sinvoke(cls, "gt", [key_name, arg]))

    @jsii.member(jsii_name="le")
    @builtins.classmethod
    def le(cls, key_name: builtins.str, arg: builtins.str) -> "KeyCondition":
        '''(experimental) Condition k <= arg, true if the key attribute k is less than or equal to the Query argument.

        :param key_name: -
        :param arg: -

        :stability: experimental
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__eed64948103f5281dc8a58c4065e9929af45a55da65267c27869535ba74eeb46)
            check_type(argname="argument key_name", value=key_name, expected_type=type_hints["key_name"])
            check_type(argname="argument arg", value=arg, expected_type=type_hints["arg"])
        return typing.cast("KeyCondition", jsii.sinvoke(cls, "le", [key_name, arg]))

    @jsii.member(jsii_name="lt")
    @builtins.classmethod
    def lt(cls, key_name: builtins.str, arg: builtins.str) -> "KeyCondition":
        '''(experimental) Condition k < arg, true if the key attribute k is less than the Query argument.

        :param key_name: -
        :param arg: -

        :stability: experimental
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c8475f31ba6af44ec7922d2131bf0a584363b40658ba03fe3bff16afba1eb653)
            check_type(argname="argument key_name", value=key_name, expected_type=type_hints["key_name"])
            check_type(argname="argument arg", value=arg, expected_type=type_hints["arg"])
        return typing.cast("KeyCondition", jsii.sinvoke(cls, "lt", [key_name, arg]))

    @jsii.member(jsii_name="and")
    def and_(self, key_cond: "KeyCondition") -> "KeyCondition":
        '''(experimental) Conjunction between two conditions.

        :param key_cond: -

        :stability: experimental
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b1f5b233c3377890d5e80a80088da68fbd8868df7ad5fa1cbe3f77c0f9f68481)
            check_type(argname="argument key_cond", value=key_cond, expected_type=type_hints["key_cond"])
        return typing.cast("KeyCondition", jsii.invoke(self, "and", [key_cond]))

    @jsii.member(jsii_name="renderTemplate")
    def render_template(self) -> builtins.str:
        '''(experimental) Renders the key condition to a VTL string.

        :stability: experimental
        '''
        return typing.cast(builtins.str, jsii.invoke(self, "renderTemplate", []))


@jsii.data_type(
    jsii_type="@aws-cdk/aws-appsync-alpha.LambdaAuthorizerConfig",
    jsii_struct_bases=[],
    name_mapping={
        "handler": "handler",
        "results_cache_ttl": "resultsCacheTtl",
        "validation_regex": "validationRegex",
    },
)
class LambdaAuthorizerConfig:
    def __init__(
        self,
        *,
        handler: _aws_cdk_aws_lambda_ceddda9d.IFunction,
        results_cache_ttl: typing.Optional[_aws_cdk_ceddda9d.Duration] = None,
        validation_regex: typing.Optional[builtins.str] = None,
    ) -> None:
        '''(experimental) Configuration for Lambda authorization in AppSync.

        Note that you can only have a single AWS Lambda function configured to authorize your API.

        :param handler: (experimental) The authorizer lambda function.
        :param results_cache_ttl: (experimental) How long the results are cached. Disable caching by setting this to 0. Default: Duration.minutes(5)
        :param validation_regex: (experimental) A regular expression for validation of tokens before the Lambda function is called. Default: - no regex filter will be applied.

        :stability: experimental
        :exampleMetadata: infused

        Example::

            import aws_cdk.aws_lambda as lambda_
            # auth_function: lambda.Function
            
            
            appsync.GraphqlApi(self, "api",
                name="api",
                schema=appsync.SchemaFile.from_asset(path.join(__dirname, "appsync.test.graphql")),
                authorization_config=appsync.AuthorizationConfig(
                    default_authorization=appsync.AuthorizationMode(
                        authorization_type=appsync.AuthorizationType.LAMBDA,
                        lambda_authorizer_config=appsync.LambdaAuthorizerConfig(
                            handler=auth_function
                        )
                    )
                )
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__337672240ca00d046f3802c4ae541ca278b767ffd2ef146e4643d9de023bd497)
            check_type(argname="argument handler", value=handler, expected_type=type_hints["handler"])
            check_type(argname="argument results_cache_ttl", value=results_cache_ttl, expected_type=type_hints["results_cache_ttl"])
            check_type(argname="argument validation_regex", value=validation_regex, expected_type=type_hints["validation_regex"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "handler": handler,
        }
        if results_cache_ttl is not None:
            self._values["results_cache_ttl"] = results_cache_ttl
        if validation_regex is not None:
            self._values["validation_regex"] = validation_regex

    @builtins.property
    def handler(self) -> _aws_cdk_aws_lambda_ceddda9d.IFunction:
        '''(experimental) The authorizer lambda function.

        :see: https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appsync-graphqlapi-lambdaauthorizerconfig.html
        :stability: experimental
        '''
        result = self._values.get("handler")
        assert result is not None, "Required property 'handler' is missing"
        return typing.cast(_aws_cdk_aws_lambda_ceddda9d.IFunction, result)

    @builtins.property
    def results_cache_ttl(self) -> typing.Optional[_aws_cdk_ceddda9d.Duration]:
        '''(experimental) How long the results are cached.

        Disable caching by setting this to 0.

        :default: Duration.minutes(5)

        :stability: experimental
        '''
        result = self._values.get("results_cache_ttl")
        return typing.cast(typing.Optional[_aws_cdk_ceddda9d.Duration], result)

    @builtins.property
    def validation_regex(self) -> typing.Optional[builtins.str]:
        '''(experimental) A regular expression for validation of tokens before the Lambda function is called.

        :default: - no regex filter will be applied.

        :stability: experimental
        '''
        result = self._values.get("validation_regex")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LambdaAuthorizerConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@aws-cdk/aws-appsync-alpha.LogConfig",
    jsii_struct_bases=[],
    name_mapping={
        "exclude_verbose_content": "excludeVerboseContent",
        "field_log_level": "fieldLogLevel",
        "retention": "retention",
        "role": "role",
    },
)
class LogConfig:
    def __init__(
        self,
        *,
        exclude_verbose_content: typing.Optional[typing.Union[builtins.bool, _aws_cdk_ceddda9d.IResolvable]] = None,
        field_log_level: typing.Optional[FieldLogLevel] = None,
        retention: typing.Optional[_aws_cdk_aws_logs_ceddda9d.RetentionDays] = None,
        role: typing.Optional[_aws_cdk_aws_iam_ceddda9d.IRole] = None,
    ) -> None:
        '''(experimental) Logging configuration for AppSync.

        :param exclude_verbose_content: (experimental) exclude verbose content. Default: false
        :param field_log_level: (experimental) log level for fields. Default: - Use AppSync default
        :param retention: (experimental) The number of days log events are kept in CloudWatch Logs. By default AppSync keeps the logs infinitely. When updating this property, unsetting it doesn't remove the log retention policy. To remove the retention policy, set the value to ``INFINITE`` Default: RetentionDays.INFINITE
        :param role: (experimental) The role for CloudWatch Logs. Default: - None

        :stability: experimental
        :exampleMetadata: infused

        Example::

            import aws_cdk.aws_logs as logs
            
            
            log_config = appsync.LogConfig(
                retention=logs.RetentionDays.ONE_WEEK
            )
            
            appsync.GraphqlApi(self, "api",
                authorization_config=appsync.AuthorizationConfig(),
                name="myApi",
                schema=appsync.SchemaFile.from_asset(path.join(__dirname, "myApi.graphql")),
                log_config=log_config
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__36317ddb5cfa6740a1e01acd100fb65164ebf89c8241e5d73c276c30f0948284)
            check_type(argname="argument exclude_verbose_content", value=exclude_verbose_content, expected_type=type_hints["exclude_verbose_content"])
            check_type(argname="argument field_log_level", value=field_log_level, expected_type=type_hints["field_log_level"])
            check_type(argname="argument retention", value=retention, expected_type=type_hints["retention"])
            check_type(argname="argument role", value=role, expected_type=type_hints["role"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if exclude_verbose_content is not None:
            self._values["exclude_verbose_content"] = exclude_verbose_content
        if field_log_level is not None:
            self._values["field_log_level"] = field_log_level
        if retention is not None:
            self._values["retention"] = retention
        if role is not None:
            self._values["role"] = role

    @builtins.property
    def exclude_verbose_content(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _aws_cdk_ceddda9d.IResolvable]]:
        '''(experimental) exclude verbose content.

        :default: false

        :stability: experimental
        '''
        result = self._values.get("exclude_verbose_content")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _aws_cdk_ceddda9d.IResolvable]], result)

    @builtins.property
    def field_log_level(self) -> typing.Optional[FieldLogLevel]:
        '''(experimental) log level for fields.

        :default: - Use AppSync default

        :stability: experimental
        '''
        result = self._values.get("field_log_level")
        return typing.cast(typing.Optional[FieldLogLevel], result)

    @builtins.property
    def retention(self) -> typing.Optional[_aws_cdk_aws_logs_ceddda9d.RetentionDays]:
        '''(experimental) The number of days log events are kept in CloudWatch Logs.

        By default AppSync keeps the logs infinitely. When updating this property,
        unsetting it doesn't remove the log retention policy.
        To remove the retention policy, set the value to ``INFINITE``

        :default: RetentionDays.INFINITE

        :stability: experimental
        '''
        result = self._values.get("retention")
        return typing.cast(typing.Optional[_aws_cdk_aws_logs_ceddda9d.RetentionDays], result)

    @builtins.property
    def role(self) -> typing.Optional[_aws_cdk_aws_iam_ceddda9d.IRole]:
        '''(experimental) The role for CloudWatch Logs.

        :default: - None

        :stability: experimental
        '''
        result = self._values.get("role")
        return typing.cast(typing.Optional[_aws_cdk_aws_iam_ceddda9d.IRole], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LogConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class MappingTemplate(
    metaclass=jsii.JSIIAbstractClass,
    jsii_type="@aws-cdk/aws-appsync-alpha.MappingTemplate",
):
    '''(experimental) MappingTemplates for AppSync resolvers.

    :stability: experimental
    :exampleMetadata: infused

    Example::

        api = appsync.GraphqlApi(self, "api",
            name="api",
            schema=appsync.SchemaFile.from_asset(path.join(__dirname, "schema.graphql"))
        )
        
        http_ds = api.add_http_data_source("ds", "https://states.amazonaws.com",
            name="httpDsWithStepF",
            description="from appsync to StepFunctions Workflow",
            authorization_config=appsync.AwsIamConfig(
                signing_region="us-east-1",
                signing_service_name="states"
            )
        )
        
        http_ds.create_resolver("MutationCallStepFunctionResolver",
            type_name="Mutation",
            field_name="callStepFunction",
            request_mapping_template=appsync.MappingTemplate.from_file("request.vtl"),
            response_mapping_template=appsync.MappingTemplate.from_file("response.vtl")
        )
    '''

    def __init__(self) -> None:
        '''
        :stability: experimental
        '''
        jsii.create(self.__class__, self, [])

    @jsii.member(jsii_name="dynamoDbDeleteItem")
    @builtins.classmethod
    def dynamo_db_delete_item(
        cls,
        key_name: builtins.str,
        id_arg: builtins.str,
    ) -> "MappingTemplate":
        '''(experimental) Mapping template to delete a single item from a DynamoDB table.

        :param key_name: the name of the hash key field.
        :param id_arg: the name of the Mutation argument.

        :stability: experimental
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2bbbc24defe1ead1c5d593f8a96a090ffc053476513612cafa21ea0f3d28bd90)
            check_type(argname="argument key_name", value=key_name, expected_type=type_hints["key_name"])
            check_type(argname="argument id_arg", value=id_arg, expected_type=type_hints["id_arg"])
        return typing.cast("MappingTemplate", jsii.sinvoke(cls, "dynamoDbDeleteItem", [key_name, id_arg]))

    @jsii.member(jsii_name="dynamoDbGetItem")
    @builtins.classmethod
    def dynamo_db_get_item(
        cls,
        key_name: builtins.str,
        id_arg: builtins.str,
        consistent_read: typing.Optional[builtins.bool] = None,
    ) -> "MappingTemplate":
        '''(experimental) Mapping template to get a single item from a DynamoDB table.

        :param key_name: the name of the hash key field.
        :param id_arg: the name of the Query argument.
        :param consistent_read: -

        :stability: experimental
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__88f230adbd2614b0171120a1a8527fd1a1e6c693193302dd2fbdf007cc81c53a)
            check_type(argname="argument key_name", value=key_name, expected_type=type_hints["key_name"])
            check_type(argname="argument id_arg", value=id_arg, expected_type=type_hints["id_arg"])
            check_type(argname="argument consistent_read", value=consistent_read, expected_type=type_hints["consistent_read"])
        return typing.cast("MappingTemplate", jsii.sinvoke(cls, "dynamoDbGetItem", [key_name, id_arg, consistent_read]))

    @jsii.member(jsii_name="dynamoDbPutItem")
    @builtins.classmethod
    def dynamo_db_put_item(
        cls,
        key: "PrimaryKey",
        values: AttributeValues,
    ) -> "MappingTemplate":
        '''(experimental) Mapping template to save a single item to a DynamoDB table.

        :param key: the assigment of Mutation values to the primary key.
        :param values: the assignment of Mutation values to the table attributes.

        :stability: experimental
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__80a975a5fc43dfb3faea0329aacb1fff0deb5d5dc2c4d915b316bc62272b280f)
            check_type(argname="argument key", value=key, expected_type=type_hints["key"])
            check_type(argname="argument values", value=values, expected_type=type_hints["values"])
        return typing.cast("MappingTemplate", jsii.sinvoke(cls, "dynamoDbPutItem", [key, values]))

    @jsii.member(jsii_name="dynamoDbQuery")
    @builtins.classmethod
    def dynamo_db_query(
        cls,
        cond: KeyCondition,
        index_name: typing.Optional[builtins.str] = None,
        consistent_read: typing.Optional[builtins.bool] = None,
    ) -> "MappingTemplate":
        '''(experimental) Mapping template to query a set of items from a DynamoDB table.

        :param cond: the key condition for the query.
        :param index_name: -
        :param consistent_read: -

        :stability: experimental
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a72ae026d9b26589761269f103be4ab5e54045463bc3e81ba28fc53fba600985)
            check_type(argname="argument cond", value=cond, expected_type=type_hints["cond"])
            check_type(argname="argument index_name", value=index_name, expected_type=type_hints["index_name"])
            check_type(argname="argument consistent_read", value=consistent_read, expected_type=type_hints["consistent_read"])
        return typing.cast("MappingTemplate", jsii.sinvoke(cls, "dynamoDbQuery", [cond, index_name, consistent_read]))

    @jsii.member(jsii_name="dynamoDbResultItem")
    @builtins.classmethod
    def dynamo_db_result_item(cls) -> "MappingTemplate":
        '''(experimental) Mapping template for a single result item from DynamoDB.

        :stability: experimental
        '''
        return typing.cast("MappingTemplate", jsii.sinvoke(cls, "dynamoDbResultItem", []))

    @jsii.member(jsii_name="dynamoDbResultList")
    @builtins.classmethod
    def dynamo_db_result_list(cls) -> "MappingTemplate":
        '''(experimental) Mapping template for a result list from DynamoDB.

        :stability: experimental
        '''
        return typing.cast("MappingTemplate", jsii.sinvoke(cls, "dynamoDbResultList", []))

    @jsii.member(jsii_name="dynamoDbScanTable")
    @builtins.classmethod
    def dynamo_db_scan_table(
        cls,
        consistent_read: typing.Optional[builtins.bool] = None,
    ) -> "MappingTemplate":
        '''(experimental) Mapping template to scan a DynamoDB table to fetch all entries.

        :param consistent_read: -

        :stability: experimental
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b3041c1fcc301d4fc26400649d89043d6f95853ec04e917e1af73e30e82280e5)
            check_type(argname="argument consistent_read", value=consistent_read, expected_type=type_hints["consistent_read"])
        return typing.cast("MappingTemplate", jsii.sinvoke(cls, "dynamoDbScanTable", [consistent_read]))

    @jsii.member(jsii_name="fromFile")
    @builtins.classmethod
    def from_file(cls, file_name: builtins.str) -> "MappingTemplate":
        '''(experimental) Create a mapping template from the given file.

        :param file_name: -

        :stability: experimental
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ebe69081dff043b43090319e95b83f4481413f1f86322c327fab1f7c44bccf38)
            check_type(argname="argument file_name", value=file_name, expected_type=type_hints["file_name"])
        return typing.cast("MappingTemplate", jsii.sinvoke(cls, "fromFile", [file_name]))

    @jsii.member(jsii_name="fromString")
    @builtins.classmethod
    def from_string(cls, template: builtins.str) -> "MappingTemplate":
        '''(experimental) Create a mapping template from the given string.

        :param template: -

        :stability: experimental
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__25f5e91db3a6dbc5b261f20cc5f8dbf06bbc2ae0f3e8c13feade8fc27473d834)
            check_type(argname="argument template", value=template, expected_type=type_hints["template"])
        return typing.cast("MappingTemplate", jsii.sinvoke(cls, "fromString", [template]))

    @jsii.member(jsii_name="lambdaRequest")
    @builtins.classmethod
    def lambda_request(
        cls,
        payload: typing.Optional[builtins.str] = None,
        operation: typing.Optional[builtins.str] = None,
    ) -> "MappingTemplate":
        '''(experimental) Mapping template to invoke a Lambda function.

        :param payload: the VTL template snippet of the payload to send to the lambda. If no payload is provided all available context fields are sent to the Lambda function
        :param operation: the type of operation AppSync should perform on the data source.

        :stability: experimental
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e7c6788a8a901e91d9597c87d05bbc2a8e7dae237778c02046c9477b51d2ac68)
            check_type(argname="argument payload", value=payload, expected_type=type_hints["payload"])
            check_type(argname="argument operation", value=operation, expected_type=type_hints["operation"])
        return typing.cast("MappingTemplate", jsii.sinvoke(cls, "lambdaRequest", [payload, operation]))

    @jsii.member(jsii_name="lambdaResult")
    @builtins.classmethod
    def lambda_result(cls) -> "MappingTemplate":
        '''(experimental) Mapping template to return the Lambda result to the caller.

        :stability: experimental
        '''
        return typing.cast("MappingTemplate", jsii.sinvoke(cls, "lambdaResult", []))

    @jsii.member(jsii_name="renderTemplate")
    @abc.abstractmethod
    def render_template(self) -> builtins.str:
        '''(experimental) this is called to render the mapping template to a VTL string.

        :stability: experimental
        '''
        ...


class _MappingTemplateProxy(MappingTemplate):
    @jsii.member(jsii_name="renderTemplate")
    def render_template(self) -> builtins.str:
        '''(experimental) this is called to render the mapping template to a VTL string.

        :stability: experimental
        '''
        return typing.cast(builtins.str, jsii.invoke(self, "renderTemplate", []))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the abstract class
typing.cast(typing.Any, MappingTemplate).__jsii_proxy_class__ = lambda : _MappingTemplateProxy


class NoneDataSource(
    BaseDataSource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/aws-appsync-alpha.NoneDataSource",
):
    '''(experimental) An AppSync dummy datasource.

    :stability: experimental
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        import aws_cdk.aws_appsync_alpha as appsync_alpha
        
        # graphql_api: appsync_alpha.GraphqlApi
        
        none_data_source = appsync_alpha.NoneDataSource(self, "MyNoneDataSource",
            api=graphql_api,
        
            # the properties below are optional
            description="description",
            name="name"
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        api: IGraphqlApi,
        description: typing.Optional[builtins.str] = None,
        name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param scope: -
        :param id: -
        :param api: (experimental) The API to attach this data source to.
        :param description: (experimental) the description of the data source. Default: - None
        :param name: (experimental) The name of the data source. Default: - id of data source

        :stability: experimental
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9c01b452aae5d4fe43a1776547ba3ab36167d802faf716669cb664fbd4d61044)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = NoneDataSourceProps(api=api, description=description, name=name)

        jsii.create(self.__class__, self, [scope, id, props])


@jsii.data_type(
    jsii_type="@aws-cdk/aws-appsync-alpha.NoneDataSourceProps",
    jsii_struct_bases=[BaseDataSourceProps],
    name_mapping={"api": "api", "description": "description", "name": "name"},
)
class NoneDataSourceProps(BaseDataSourceProps):
    def __init__(
        self,
        *,
        api: IGraphqlApi,
        description: typing.Optional[builtins.str] = None,
        name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''(experimental) Properties for an AppSync dummy datasource.

        :param api: (experimental) The API to attach this data source to.
        :param description: (experimental) the description of the data source. Default: - None
        :param name: (experimental) The name of the data source. Default: - id of data source

        :stability: experimental
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            import aws_cdk.aws_appsync_alpha as appsync_alpha
            
            # graphql_api: appsync_alpha.GraphqlApi
            
            none_data_source_props = appsync_alpha.NoneDataSourceProps(
                api=graphql_api,
            
                # the properties below are optional
                description="description",
                name="name"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c9bb8be0e14e063d89233a7c97225ce92a2a4996f23bf770cc677eca7ecf5bd5)
            check_type(argname="argument api", value=api, expected_type=type_hints["api"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "api": api,
        }
        if description is not None:
            self._values["description"] = description
        if name is not None:
            self._values["name"] = name

    @builtins.property
    def api(self) -> IGraphqlApi:
        '''(experimental) The API to attach this data source to.

        :stability: experimental
        '''
        result = self._values.get("api")
        assert result is not None, "Required property 'api' is missing"
        return typing.cast(IGraphqlApi, result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''(experimental) the description of the data source.

        :default: - None

        :stability: experimental
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''(experimental) The name of the data source.

        :default: - id of data source

        :stability: experimental
        '''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "NoneDataSourceProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@aws-cdk/aws-appsync-alpha.OpenIdConnectConfig",
    jsii_struct_bases=[],
    name_mapping={
        "oidc_provider": "oidcProvider",
        "client_id": "clientId",
        "token_expiry_from_auth": "tokenExpiryFromAuth",
        "token_expiry_from_issue": "tokenExpiryFromIssue",
    },
)
class OpenIdConnectConfig:
    def __init__(
        self,
        *,
        oidc_provider: builtins.str,
        client_id: typing.Optional[builtins.str] = None,
        token_expiry_from_auth: typing.Optional[jsii.Number] = None,
        token_expiry_from_issue: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''(experimental) Configuration for OpenID Connect authorization in AppSync.

        :param oidc_provider: (experimental) The issuer for the OIDC configuration. The issuer returned by discovery must exactly match the value of ``iss`` in the OIDC token.
        :param client_id: (experimental) The client identifier of the Relying party at the OpenID identity provider. A regular expression can be specified so AppSync can validate against multiple client identifiers at a time. Default: - - (All)
        :param token_expiry_from_auth: (experimental) The number of milliseconds an OIDC token is valid after being authenticated by OIDC provider. ``auth_time`` claim in OIDC token is required for this validation to work. Default: - no validation
        :param token_expiry_from_issue: (experimental) The number of milliseconds an OIDC token is valid after being issued to a user. This validation uses ``iat`` claim of OIDC token. Default: - no validation

        :stability: experimental
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            import aws_cdk.aws_appsync_alpha as appsync_alpha
            
            open_id_connect_config = appsync_alpha.OpenIdConnectConfig(
                oidc_provider="oidcProvider",
            
                # the properties below are optional
                client_id="clientId",
                token_expiry_from_auth=123,
                token_expiry_from_issue=123
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8b878562c2013c394e2633ff6318afd2a12cf83b22e9dd30c04af54c1576a197)
            check_type(argname="argument oidc_provider", value=oidc_provider, expected_type=type_hints["oidc_provider"])
            check_type(argname="argument client_id", value=client_id, expected_type=type_hints["client_id"])
            check_type(argname="argument token_expiry_from_auth", value=token_expiry_from_auth, expected_type=type_hints["token_expiry_from_auth"])
            check_type(argname="argument token_expiry_from_issue", value=token_expiry_from_issue, expected_type=type_hints["token_expiry_from_issue"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "oidc_provider": oidc_provider,
        }
        if client_id is not None:
            self._values["client_id"] = client_id
        if token_expiry_from_auth is not None:
            self._values["token_expiry_from_auth"] = token_expiry_from_auth
        if token_expiry_from_issue is not None:
            self._values["token_expiry_from_issue"] = token_expiry_from_issue

    @builtins.property
    def oidc_provider(self) -> builtins.str:
        '''(experimental) The issuer for the OIDC configuration.

        The issuer returned by discovery must exactly match the value of ``iss`` in the OIDC token.

        :stability: experimental
        '''
        result = self._values.get("oidc_provider")
        assert result is not None, "Required property 'oidc_provider' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def client_id(self) -> typing.Optional[builtins.str]:
        '''(experimental) The client identifier of the Relying party at the OpenID identity provider.

        A regular expression can be specified so AppSync can validate against multiple client identifiers at a time.

        :default:

        -
        - (All)

        :stability: experimental

        Example::

            -"ABCD|CDEF"
        '''
        result = self._values.get("client_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def token_expiry_from_auth(self) -> typing.Optional[jsii.Number]:
        '''(experimental) The number of milliseconds an OIDC token is valid after being authenticated by OIDC provider.

        ``auth_time`` claim in OIDC token is required for this validation to work.

        :default: - no validation

        :stability: experimental
        '''
        result = self._values.get("token_expiry_from_auth")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def token_expiry_from_issue(self) -> typing.Optional[jsii.Number]:
        '''(experimental) The number of milliseconds an OIDC token is valid after being issued to a user.

        This validation uses ``iat`` claim of OIDC token.

        :default: - no validation

        :stability: experimental
        '''
        result = self._values.get("token_expiry_from_issue")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "OpenIdConnectConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class PartitionKeyStep(
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/aws-appsync-alpha.PartitionKeyStep",
):
    '''(experimental) Utility class to allow assigning a value or an auto-generated id to a partition key.

    :stability: experimental
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        import aws_cdk.aws_appsync_alpha as appsync_alpha
        
        partition_key_step = appsync_alpha.PartitionKeyStep("key")
    '''

    def __init__(self, key: builtins.str) -> None:
        '''
        :param key: -

        :stability: experimental
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a1fba092401cd01d508bb92a007d1f1a73f24d2b8c5dbe573357db4b2f7ee073)
            check_type(argname="argument key", value=key, expected_type=type_hints["key"])
        jsii.create(self.__class__, self, [key])

    @jsii.member(jsii_name="auto")
    def auto(self) -> "PartitionKey":
        '''(experimental) Assign an auto-generated value to the partition key.

        :stability: experimental
        '''
        return typing.cast("PartitionKey", jsii.invoke(self, "auto", []))

    @jsii.member(jsii_name="is")
    def is_(self, val: builtins.str) -> "PartitionKey":
        '''(experimental) Assign an auto-generated value to the partition key.

        :param val: -

        :stability: experimental
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a99a744b2615c70db51e7e97f7a78bebcda8333da4a1c53d8b9da8256681c5d3)
            check_type(argname="argument val", value=val, expected_type=type_hints["val"])
        return typing.cast("PartitionKey", jsii.invoke(self, "is", [val]))


class PrimaryKey(
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/aws-appsync-alpha.PrimaryKey",
):
    '''(experimental) Specifies the assignment to the primary key.

    It either
    contains the full primary key or only the partition key.

    :stability: experimental
    :exampleMetadata: infused

    Example::

        api = appsync.GraphqlApi(self, "Api",
            name="demo",
            schema=appsync.SchemaFile.from_asset(path.join(__dirname, "schema.graphql")),
            authorization_config=appsync.AuthorizationConfig(
                default_authorization=appsync.AuthorizationMode(
                    authorization_type=appsync.AuthorizationType.IAM
                )
            ),
            xray_enabled=True
        )
        
        demo_table = dynamodb.Table(self, "DemoTable",
            partition_key=dynamodb.Attribute(
                name="id",
                type=dynamodb.AttributeType.STRING
            )
        )
        
        demo_dS = api.add_dynamo_db_data_source("demoDataSource", demo_table)
        
        # Resolver for the Query "getDemos" that scans the DynamoDb table and returns the entire list.
        # Resolver Mapping Template Reference:
        # https://docs.aws.amazon.com/appsync/latest/devguide/resolver-mapping-template-reference-dynamodb.html
        demo_dS.create_resolver("QueryGetDemosResolver",
            type_name="Query",
            field_name="getDemos",
            request_mapping_template=appsync.MappingTemplate.dynamo_db_scan_table(),
            response_mapping_template=appsync.MappingTemplate.dynamo_db_result_list()
        )
        
        # Resolver for the Mutation "addDemo" that puts the item into the DynamoDb table.
        demo_dS.create_resolver("MutationAddDemoResolver",
            type_name="Mutation",
            field_name="addDemo",
            request_mapping_template=appsync.MappingTemplate.dynamo_db_put_item(
                appsync.PrimaryKey.partition("id").auto(),
                appsync.Values.projecting("input")),
            response_mapping_template=appsync.MappingTemplate.dynamo_db_result_item()
        )
        
        # To enable DynamoDB read consistency with the `MappingTemplate`:
        demo_dS.create_resolver("QueryGetDemosConsistentResolver",
            type_name="Query",
            field_name="getDemosConsistent",
            request_mapping_template=appsync.MappingTemplate.dynamo_db_scan_table(True),
            response_mapping_template=appsync.MappingTemplate.dynamo_db_result_list()
        )
    '''

    def __init__(self, pkey: Assign, skey: typing.Optional[Assign] = None) -> None:
        '''
        :param pkey: -
        :param skey: -

        :stability: experimental
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__04f1b1f314b8748cf24e4dd79c346b1eaba199a34d9d062703427899a303de05)
            check_type(argname="argument pkey", value=pkey, expected_type=type_hints["pkey"])
            check_type(argname="argument skey", value=skey, expected_type=type_hints["skey"])
        jsii.create(self.__class__, self, [pkey, skey])

    @jsii.member(jsii_name="partition")
    @builtins.classmethod
    def partition(cls, key: builtins.str) -> PartitionKeyStep:
        '''(experimental) Allows assigning a value to the partition key.

        :param key: -

        :stability: experimental
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d0724c26db7323c3293b63cc0b59f3db0d2568df2cfb8a1ed43d6cd084b14a9b)
            check_type(argname="argument key", value=key, expected_type=type_hints["key"])
        return typing.cast(PartitionKeyStep, jsii.sinvoke(cls, "partition", [key]))

    @jsii.member(jsii_name="renderTemplate")
    def render_template(self) -> builtins.str:
        '''(experimental) Renders the key assignment to a VTL string.

        :stability: experimental
        '''
        return typing.cast(builtins.str, jsii.invoke(self, "renderTemplate", []))

    @builtins.property
    @jsii.member(jsii_name="pkey")
    def _pkey(self) -> Assign:
        '''
        :stability: experimental
        '''
        return typing.cast(Assign, jsii.get(self, "pkey"))


class Resolver(
    _constructs_77d1e7e8.Construct,
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/aws-appsync-alpha.Resolver",
):
    '''(experimental) An AppSync resolver.

    :stability: experimental
    :exampleMetadata: infused

    Example::

        # api: appsync.GraphqlApi
        # appsync_function: appsync.AppsyncFunction
        
        
        pipeline_resolver = appsync.Resolver(self, "pipeline",
            api=api,
            data_source=api.add_none_data_source("none"),
            type_name="typeName",
            field_name="fieldName",
            request_mapping_template=appsync.MappingTemplate.from_file("beforeRequest.vtl"),
            pipeline_config=[appsync_function],
            response_mapping_template=appsync.MappingTemplate.from_file("afterResponse.vtl")
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        api: IGraphqlApi,
        data_source: typing.Optional[BaseDataSource] = None,
        field_name: builtins.str,
        type_name: builtins.str,
        caching_config: typing.Optional[typing.Union[CachingConfig, typing.Dict[builtins.str, typing.Any]]] = None,
        max_batch_size: typing.Optional[jsii.Number] = None,
        pipeline_config: typing.Optional[typing.Sequence[IAppsyncFunction]] = None,
        request_mapping_template: typing.Optional[MappingTemplate] = None,
        response_mapping_template: typing.Optional[MappingTemplate] = None,
    ) -> None:
        '''
        :param scope: -
        :param id: -
        :param api: (experimental) The API this resolver is attached to.
        :param data_source: (experimental) The data source this resolver is using. Default: - No datasource
        :param field_name: (experimental) name of the GraphQL field in the given type this resolver is attached to.
        :param type_name: (experimental) name of the GraphQL type this resolver is attached to.
        :param caching_config: (experimental) The caching configuration for this resolver. Default: - No caching configuration
        :param max_batch_size: (experimental) The maximum number of elements per batch, when using batch invoke. Default: - No max batch size
        :param pipeline_config: (experimental) configuration of the pipeline resolver. Default: - no pipeline resolver configuration An empty array | undefined sets resolver to be of kind, unit
        :param request_mapping_template: (experimental) The request mapping template for this resolver. Default: - No mapping template
        :param response_mapping_template: (experimental) The response mapping template for this resolver. Default: - No mapping template

        :stability: experimental
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__16fda65d626ad085d09ff6eb0a22ed286fb1d2d616cc1f9585a4a0da9284e27d)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = ResolverProps(
            api=api,
            data_source=data_source,
            field_name=field_name,
            type_name=type_name,
            caching_config=caching_config,
            max_batch_size=max_batch_size,
            pipeline_config=pipeline_config,
            request_mapping_template=request_mapping_template,
            response_mapping_template=response_mapping_template,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @builtins.property
    @jsii.member(jsii_name="arn")
    def arn(self) -> builtins.str:
        '''(experimental) the ARN of the resolver.

        :stability: experimental
        '''
        return typing.cast(builtins.str, jsii.get(self, "arn"))


@jsii.data_type(
    jsii_type="@aws-cdk/aws-appsync-alpha.ResolverProps",
    jsii_struct_bases=[ExtendedResolverProps],
    name_mapping={
        "field_name": "fieldName",
        "type_name": "typeName",
        "caching_config": "cachingConfig",
        "max_batch_size": "maxBatchSize",
        "pipeline_config": "pipelineConfig",
        "request_mapping_template": "requestMappingTemplate",
        "response_mapping_template": "responseMappingTemplate",
        "data_source": "dataSource",
        "api": "api",
    },
)
class ResolverProps(ExtendedResolverProps):
    def __init__(
        self,
        *,
        field_name: builtins.str,
        type_name: builtins.str,
        caching_config: typing.Optional[typing.Union[CachingConfig, typing.Dict[builtins.str, typing.Any]]] = None,
        max_batch_size: typing.Optional[jsii.Number] = None,
        pipeline_config: typing.Optional[typing.Sequence[IAppsyncFunction]] = None,
        request_mapping_template: typing.Optional[MappingTemplate] = None,
        response_mapping_template: typing.Optional[MappingTemplate] = None,
        data_source: typing.Optional[BaseDataSource] = None,
        api: IGraphqlApi,
    ) -> None:
        '''(experimental) Additional property for an AppSync resolver for GraphQL API reference.

        :param field_name: (experimental) name of the GraphQL field in the given type this resolver is attached to.
        :param type_name: (experimental) name of the GraphQL type this resolver is attached to.
        :param caching_config: (experimental) The caching configuration for this resolver. Default: - No caching configuration
        :param max_batch_size: (experimental) The maximum number of elements per batch, when using batch invoke. Default: - No max batch size
        :param pipeline_config: (experimental) configuration of the pipeline resolver. Default: - no pipeline resolver configuration An empty array | undefined sets resolver to be of kind, unit
        :param request_mapping_template: (experimental) The request mapping template for this resolver. Default: - No mapping template
        :param response_mapping_template: (experimental) The response mapping template for this resolver. Default: - No mapping template
        :param data_source: (experimental) The data source this resolver is using. Default: - No datasource
        :param api: (experimental) The API this resolver is attached to.

        :stability: experimental
        :exampleMetadata: infused

        Example::

            # api: appsync.GraphqlApi
            # appsync_function: appsync.AppsyncFunction
            
            
            pipeline_resolver = appsync.Resolver(self, "pipeline",
                api=api,
                data_source=api.add_none_data_source("none"),
                type_name="typeName",
                field_name="fieldName",
                request_mapping_template=appsync.MappingTemplate.from_file("beforeRequest.vtl"),
                pipeline_config=[appsync_function],
                response_mapping_template=appsync.MappingTemplate.from_file("afterResponse.vtl")
            )
        '''
        if isinstance(caching_config, dict):
            caching_config = CachingConfig(**caching_config)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0544034ffa38a1349f4df5068fc81a07e076e8e79912d653716af3085b44950c)
            check_type(argname="argument field_name", value=field_name, expected_type=type_hints["field_name"])
            check_type(argname="argument type_name", value=type_name, expected_type=type_hints["type_name"])
            check_type(argname="argument caching_config", value=caching_config, expected_type=type_hints["caching_config"])
            check_type(argname="argument max_batch_size", value=max_batch_size, expected_type=type_hints["max_batch_size"])
            check_type(argname="argument pipeline_config", value=pipeline_config, expected_type=type_hints["pipeline_config"])
            check_type(argname="argument request_mapping_template", value=request_mapping_template, expected_type=type_hints["request_mapping_template"])
            check_type(argname="argument response_mapping_template", value=response_mapping_template, expected_type=type_hints["response_mapping_template"])
            check_type(argname="argument data_source", value=data_source, expected_type=type_hints["data_source"])
            check_type(argname="argument api", value=api, expected_type=type_hints["api"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "field_name": field_name,
            "type_name": type_name,
            "api": api,
        }
        if caching_config is not None:
            self._values["caching_config"] = caching_config
        if max_batch_size is not None:
            self._values["max_batch_size"] = max_batch_size
        if pipeline_config is not None:
            self._values["pipeline_config"] = pipeline_config
        if request_mapping_template is not None:
            self._values["request_mapping_template"] = request_mapping_template
        if response_mapping_template is not None:
            self._values["response_mapping_template"] = response_mapping_template
        if data_source is not None:
            self._values["data_source"] = data_source

    @builtins.property
    def field_name(self) -> builtins.str:
        '''(experimental) name of the GraphQL field in the given type this resolver is attached to.

        :stability: experimental
        '''
        result = self._values.get("field_name")
        assert result is not None, "Required property 'field_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type_name(self) -> builtins.str:
        '''(experimental) name of the GraphQL type this resolver is attached to.

        :stability: experimental
        '''
        result = self._values.get("type_name")
        assert result is not None, "Required property 'type_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def caching_config(self) -> typing.Optional[CachingConfig]:
        '''(experimental) The caching configuration for this resolver.

        :default: - No caching configuration

        :stability: experimental
        '''
        result = self._values.get("caching_config")
        return typing.cast(typing.Optional[CachingConfig], result)

    @builtins.property
    def max_batch_size(self) -> typing.Optional[jsii.Number]:
        '''(experimental) The maximum number of elements per batch, when using batch invoke.

        :default: - No max batch size

        :stability: experimental
        '''
        result = self._values.get("max_batch_size")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def pipeline_config(self) -> typing.Optional[typing.List[IAppsyncFunction]]:
        '''(experimental) configuration of the pipeline resolver.

        :default:

        - no pipeline resolver configuration
        An empty array | undefined sets resolver to be of kind, unit

        :stability: experimental
        '''
        result = self._values.get("pipeline_config")
        return typing.cast(typing.Optional[typing.List[IAppsyncFunction]], result)

    @builtins.property
    def request_mapping_template(self) -> typing.Optional[MappingTemplate]:
        '''(experimental) The request mapping template for this resolver.

        :default: - No mapping template

        :stability: experimental
        '''
        result = self._values.get("request_mapping_template")
        return typing.cast(typing.Optional[MappingTemplate], result)

    @builtins.property
    def response_mapping_template(self) -> typing.Optional[MappingTemplate]:
        '''(experimental) The response mapping template for this resolver.

        :default: - No mapping template

        :stability: experimental
        '''
        result = self._values.get("response_mapping_template")
        return typing.cast(typing.Optional[MappingTemplate], result)

    @builtins.property
    def data_source(self) -> typing.Optional[BaseDataSource]:
        '''(experimental) The data source this resolver is using.

        :default: - No datasource

        :stability: experimental
        '''
        result = self._values.get("data_source")
        return typing.cast(typing.Optional[BaseDataSource], result)

    @builtins.property
    def api(self) -> IGraphqlApi:
        '''(experimental) The API this resolver is attached to.

        :stability: experimental
        '''
        result = self._values.get("api")
        assert result is not None, "Required property 'api' is missing"
        return typing.cast(IGraphqlApi, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ResolverProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@aws-cdk/aws-appsync-alpha.SchemaBindOptions",
    jsii_struct_bases=[],
    name_mapping={},
)
class SchemaBindOptions:
    def __init__(self) -> None:
        '''(experimental) Used for configuring schema bind behavior.

        This is intended to prevent breaking changes to implementors of ISchema
        if needing to add new behavior.

        :stability: experimental
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            import aws_cdk.aws_appsync_alpha as appsync_alpha
            
            schema_bind_options = appsync_alpha.SchemaBindOptions()
        '''
        self._values: typing.Dict[builtins.str, typing.Any] = {}

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SchemaBindOptions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(ISchema)
class SchemaFile(
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/aws-appsync-alpha.SchemaFile",
):
    '''(experimental) The Schema for a GraphQL Api.

    If no options are configured, schema will be generated
    code-first.

    :stability: experimental
    :exampleMetadata: infused

    Example::

        api = appsync.GraphqlApi(self, "api",
            name="api",
            schema=appsync.SchemaFile.from_asset(path.join(__dirname, "schema.graphql"))
        )
        
        http_ds = api.add_http_data_source("ds", "https://states.amazonaws.com",
            name="httpDsWithStepF",
            description="from appsync to StepFunctions Workflow",
            authorization_config=appsync.AwsIamConfig(
                signing_region="us-east-1",
                signing_service_name="states"
            )
        )
        
        http_ds.create_resolver("MutationCallStepFunctionResolver",
            type_name="Mutation",
            field_name="callStepFunction",
            request_mapping_template=appsync.MappingTemplate.from_file("request.vtl"),
            response_mapping_template=appsync.MappingTemplate.from_file("response.vtl")
        )
    '''

    def __init__(self, *, file_path: builtins.str) -> None:
        '''
        :param file_path: (experimental) The file path for the schema. When this option is configured, then the schema will be generated from an existing file from disk.

        :stability: experimental
        '''
        options = SchemaProps(file_path=file_path)

        jsii.create(self.__class__, self, [options])

    @jsii.member(jsii_name="fromAsset")
    @builtins.classmethod
    def from_asset(cls, file_path: builtins.str) -> "SchemaFile":
        '''(experimental) Generate a Schema from file.

        :param file_path: the file path of the schema file.

        :return: ``SchemaAsset`` with immutable schema defintion

        :stability: experimental
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__90c6507328fd41f3320f52fac14454c95e67b3606153a65102df6f21b7cc1a3b)
            check_type(argname="argument file_path", value=file_path, expected_type=type_hints["file_path"])
        return typing.cast("SchemaFile", jsii.sinvoke(cls, "fromAsset", [file_path]))

    @jsii.member(jsii_name="bind")
    def bind(self, api: IGraphqlApi) -> ISchemaConfig:
        '''(experimental) Called when the GraphQL Api is initialized to allow this object to bind to the stack.

        :param api: The binding GraphQL Api.

        :stability: experimental
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__18f56bb1836a4289e7269271f0246c6611c7c56847cbf623482019852eacc689)
            check_type(argname="argument api", value=api, expected_type=type_hints["api"])
        _options = SchemaBindOptions()

        return typing.cast(ISchemaConfig, jsii.invoke(self, "bind", [api, _options]))

    @builtins.property
    @jsii.member(jsii_name="definition")
    def definition(self) -> builtins.str:
        '''(experimental) The definition for this schema.

        :stability: experimental
        '''
        return typing.cast(builtins.str, jsii.get(self, "definition"))

    @definition.setter
    def definition(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__76feb135877e53281f9ff4edf266df32e0dcd1820ef716bb01cedec5ec7003df)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "definition", value)


@jsii.data_type(
    jsii_type="@aws-cdk/aws-appsync-alpha.SchemaProps",
    jsii_struct_bases=[],
    name_mapping={"file_path": "filePath"},
)
class SchemaProps:
    def __init__(self, *, file_path: builtins.str) -> None:
        '''(experimental) The options for configuring a schema from an existing file.

        :param file_path: (experimental) The file path for the schema. When this option is configured, then the schema will be generated from an existing file from disk.

        :stability: experimental
        :exampleMetadata: infused

        Example::

            import aws_cdk.aws_certificatemanager as acm
            import aws_cdk.aws_route53 as route53
            
            # hosted zone and route53 features
            # hosted_zone_id: str
            zone_name = "example.com"
            
            
            my_domain_name = "api.example.com"
            certificate = acm.Certificate(self, "cert", domain_name=my_domain_name)
            schema = appsync.SchemaFile(file_path="mySchemaFile")
            api = appsync.GraphqlApi(self, "api",
                name="myApi",
                schema=schema,
                domain_name=appsync.DomainOptions(
                    certificate=certificate,
                    domain_name=my_domain_name
                )
            )
            
            # hosted zone for adding appsync domain
            zone = route53.HostedZone.from_hosted_zone_attributes(self, "HostedZone",
                hosted_zone_id=hosted_zone_id,
                zone_name=zone_name
            )
            
            # create a cname to the appsync domain. will map to something like xxxx.cloudfront.net
            route53.CnameRecord(self, "CnameApiRecord",
                record_name="api",
                zone=zone,
                domain_name=api.app_sync_domain_name
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__74fb8ec7796991b3d4c9a0ddfefb868ed0e3ac71be7dffbb11827b0f21f8cd20)
            check_type(argname="argument file_path", value=file_path, expected_type=type_hints["file_path"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "file_path": file_path,
        }

    @builtins.property
    def file_path(self) -> builtins.str:
        '''(experimental) The file path for the schema.

        When this option is
        configured, then the schema will be generated from an
        existing file from disk.

        :stability: experimental
        '''
        result = self._values.get("file_path")
        assert result is not None, "Required property 'file_path' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SchemaProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class SortKeyStep(
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/aws-appsync-alpha.SortKeyStep",
):
    '''(experimental) Utility class to allow assigning a value or an auto-generated id to a sort key.

    :stability: experimental
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        import aws_cdk.aws_appsync_alpha as appsync_alpha
        
        # assign: appsync_alpha.Assign
        
        sort_key_step = appsync_alpha.SortKeyStep(assign, "skey")
    '''

    def __init__(self, pkey: Assign, skey: builtins.str) -> None:
        '''
        :param pkey: -
        :param skey: -

        :stability: experimental
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7521a793cdf36117708b84d1a01bef63160ade233906dd87f3d03f02bcd1ba6e)
            check_type(argname="argument pkey", value=pkey, expected_type=type_hints["pkey"])
            check_type(argname="argument skey", value=skey, expected_type=type_hints["skey"])
        jsii.create(self.__class__, self, [pkey, skey])

    @jsii.member(jsii_name="auto")
    def auto(self) -> PrimaryKey:
        '''(experimental) Assign an auto-generated value to the sort key.

        :stability: experimental
        '''
        return typing.cast(PrimaryKey, jsii.invoke(self, "auto", []))

    @jsii.member(jsii_name="is")
    def is_(self, val: builtins.str) -> PrimaryKey:
        '''(experimental) Assign an auto-generated value to the sort key.

        :param val: -

        :stability: experimental
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f28f5c9bacf653797e54b516bde341e12edee2e096290d0fcf35116bd7eb3313)
            check_type(argname="argument val", value=val, expected_type=type_hints["val"])
        return typing.cast(PrimaryKey, jsii.invoke(self, "is", [val]))


@jsii.data_type(
    jsii_type="@aws-cdk/aws-appsync-alpha.UserPoolConfig",
    jsii_struct_bases=[],
    name_mapping={
        "user_pool": "userPool",
        "app_id_client_regex": "appIdClientRegex",
        "default_action": "defaultAction",
    },
)
class UserPoolConfig:
    def __init__(
        self,
        *,
        user_pool: _aws_cdk_aws_cognito_ceddda9d.IUserPool,
        app_id_client_regex: typing.Optional[builtins.str] = None,
        default_action: typing.Optional["UserPoolDefaultAction"] = None,
    ) -> None:
        '''(experimental) Configuration for Cognito user-pools in AppSync.

        :param user_pool: (experimental) The Cognito user pool to use as identity source.
        :param app_id_client_regex: (experimental) the optional app id regex. Default: - None
        :param default_action: (experimental) Default auth action. Default: ALLOW

        :stability: experimental
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            import aws_cdk.aws_appsync_alpha as appsync_alpha
            from aws_cdk import aws_cognito as cognito
            
            # user_pool: cognito.UserPool
            
            user_pool_config = appsync_alpha.UserPoolConfig(
                user_pool=user_pool,
            
                # the properties below are optional
                app_id_client_regex="appIdClientRegex",
                default_action=appsync_alpha.UserPoolDefaultAction.ALLOW
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c0d45a53d3fc953aeaa93f0fe0dd8bedea69cba522adb8a9f611beae1c994767)
            check_type(argname="argument user_pool", value=user_pool, expected_type=type_hints["user_pool"])
            check_type(argname="argument app_id_client_regex", value=app_id_client_regex, expected_type=type_hints["app_id_client_regex"])
            check_type(argname="argument default_action", value=default_action, expected_type=type_hints["default_action"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "user_pool": user_pool,
        }
        if app_id_client_regex is not None:
            self._values["app_id_client_regex"] = app_id_client_regex
        if default_action is not None:
            self._values["default_action"] = default_action

    @builtins.property
    def user_pool(self) -> _aws_cdk_aws_cognito_ceddda9d.IUserPool:
        '''(experimental) The Cognito user pool to use as identity source.

        :stability: experimental
        '''
        result = self._values.get("user_pool")
        assert result is not None, "Required property 'user_pool' is missing"
        return typing.cast(_aws_cdk_aws_cognito_ceddda9d.IUserPool, result)

    @builtins.property
    def app_id_client_regex(self) -> typing.Optional[builtins.str]:
        '''(experimental) the optional app id regex.

        :default: - None

        :stability: experimental
        '''
        result = self._values.get("app_id_client_regex")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def default_action(self) -> typing.Optional["UserPoolDefaultAction"]:
        '''(experimental) Default auth action.

        :default: ALLOW

        :stability: experimental
        '''
        result = self._values.get("default_action")
        return typing.cast(typing.Optional["UserPoolDefaultAction"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "UserPoolConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.enum(jsii_type="@aws-cdk/aws-appsync-alpha.UserPoolDefaultAction")
class UserPoolDefaultAction(enum.Enum):
    '''(experimental) enum with all possible values for Cognito user-pool default actions.

    :stability: experimental
    '''

    ALLOW = "ALLOW"
    '''(experimental) ALLOW access to API.

    :stability: experimental
    '''
    DENY = "DENY"
    '''(experimental) DENY access to API.

    :stability: experimental
    '''


class Values(metaclass=jsii.JSIIMeta, jsii_type="@aws-cdk/aws-appsync-alpha.Values"):
    '''(experimental) Factory class for attribute value assignments.

    :stability: experimental
    :exampleMetadata: infused

    Example::

        api = appsync.GraphqlApi(self, "Api",
            name="demo",
            schema=appsync.SchemaFile.from_asset(path.join(__dirname, "schema.graphql")),
            authorization_config=appsync.AuthorizationConfig(
                default_authorization=appsync.AuthorizationMode(
                    authorization_type=appsync.AuthorizationType.IAM
                )
            ),
            xray_enabled=True
        )
        
        demo_table = dynamodb.Table(self, "DemoTable",
            partition_key=dynamodb.Attribute(
                name="id",
                type=dynamodb.AttributeType.STRING
            )
        )
        
        demo_dS = api.add_dynamo_db_data_source("demoDataSource", demo_table)
        
        # Resolver for the Query "getDemos" that scans the DynamoDb table and returns the entire list.
        # Resolver Mapping Template Reference:
        # https://docs.aws.amazon.com/appsync/latest/devguide/resolver-mapping-template-reference-dynamodb.html
        demo_dS.create_resolver("QueryGetDemosResolver",
            type_name="Query",
            field_name="getDemos",
            request_mapping_template=appsync.MappingTemplate.dynamo_db_scan_table(),
            response_mapping_template=appsync.MappingTemplate.dynamo_db_result_list()
        )
        
        # Resolver for the Mutation "addDemo" that puts the item into the DynamoDb table.
        demo_dS.create_resolver("MutationAddDemoResolver",
            type_name="Mutation",
            field_name="addDemo",
            request_mapping_template=appsync.MappingTemplate.dynamo_db_put_item(
                appsync.PrimaryKey.partition("id").auto(),
                appsync.Values.projecting("input")),
            response_mapping_template=appsync.MappingTemplate.dynamo_db_result_item()
        )
        
        # To enable DynamoDB read consistency with the `MappingTemplate`:
        demo_dS.create_resolver("QueryGetDemosConsistentResolver",
            type_name="Query",
            field_name="getDemosConsistent",
            request_mapping_template=appsync.MappingTemplate.dynamo_db_scan_table(True),
            response_mapping_template=appsync.MappingTemplate.dynamo_db_result_list()
        )
    '''

    def __init__(self) -> None:
        '''
        :stability: experimental
        '''
        jsii.create(self.__class__, self, [])

    @jsii.member(jsii_name="attribute")
    @builtins.classmethod
    def attribute(cls, attr: builtins.str) -> AttributeValuesStep:
        '''(experimental) Allows assigning a value to the specified attribute.

        :param attr: -

        :stability: experimental
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fce54538d36746cac8ad392ca0efade9f94d7f0380883157e4fb0ec4aec80c1f)
            check_type(argname="argument attr", value=attr, expected_type=type_hints["attr"])
        return typing.cast(AttributeValuesStep, jsii.sinvoke(cls, "attribute", [attr]))

    @jsii.member(jsii_name="projecting")
    @builtins.classmethod
    def projecting(cls, arg: typing.Optional[builtins.str] = None) -> AttributeValues:
        '''(experimental) Treats the specified object as a map of assignments, where the property names represent attribute names.

        It’s opinionated about how it represents
        some of the nested objects: e.g., it will use lists (“L”) rather than sets
        (“SS”, “NS”, “BS”). By default it projects the argument container ("$ctx.args").

        :param arg: -

        :stability: experimental
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2041b7d86db3cf96e0e02fd003ec8df58ac040791ee720cce7fc45baf561ce53)
            check_type(argname="argument arg", value=arg, expected_type=type_hints["arg"])
        return typing.cast(AttributeValues, jsii.sinvoke(cls, "projecting", [arg]))


@jsii.implements(IAppsyncFunction)
class AppsyncFunction(
    _aws_cdk_ceddda9d.Resource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/aws-appsync-alpha.AppsyncFunction",
):
    '''(experimental) AppSync Functions are local functions that perform certain operations onto a backend data source.

    Developers can compose operations (Functions)
    and execute them in sequence with Pipeline Resolvers.

    :stability: experimental
    :resource: AWS::AppSync::FunctionConfiguration
    :exampleMetadata: infused

    Example::

        # api: appsync.GraphqlApi
        
        
        appsync_function = appsync.AppsyncFunction(self, "function",
            name="appsync_function",
            api=api,
            data_source=api.add_none_data_source("none"),
            request_mapping_template=appsync.MappingTemplate.from_file("request.vtl"),
            response_mapping_template=appsync.MappingTemplate.from_file("response.vtl")
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        api: IGraphqlApi,
        data_source: BaseDataSource,
        name: builtins.str,
        description: typing.Optional[builtins.str] = None,
        request_mapping_template: typing.Optional[MappingTemplate] = None,
        response_mapping_template: typing.Optional[MappingTemplate] = None,
    ) -> None:
        '''
        :param scope: -
        :param id: -
        :param api: (experimental) the GraphQL Api linked to this AppSync Function.
        :param data_source: (experimental) the data source linked to this AppSync Function.
        :param name: (experimental) the name of the AppSync Function.
        :param description: (experimental) the description for this AppSync Function. Default: - no description
        :param request_mapping_template: (experimental) the request mapping template for the AppSync Function. Default: - no request mapping template
        :param response_mapping_template: (experimental) the response mapping template for the AppSync Function. Default: - no response mapping template

        :stability: experimental
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ae4be0c00df7153d2b8df13c5a507f84c55a8fd1dfd654ffb322f8256f585840)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = AppsyncFunctionProps(
            api=api,
            data_source=data_source,
            name=name,
            description=description,
            request_mapping_template=request_mapping_template,
            response_mapping_template=response_mapping_template,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="fromAppsyncFunctionAttributes")
    @builtins.classmethod
    def from_appsync_function_attributes(
        cls,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        function_arn: builtins.str,
    ) -> IAppsyncFunction:
        '''(experimental) Import Appsync Function from arn.

        :param scope: -
        :param id: -
        :param function_arn: (experimental) the ARN of the AppSync function.

        :stability: experimental
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1d0577f3d312e5fa22c00353e17621d8c61ae169801f29d19726a2040375c8ad)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        attrs = AppsyncFunctionAttributes(function_arn=function_arn)

        return typing.cast(IAppsyncFunction, jsii.sinvoke(cls, "fromAppsyncFunctionAttributes", [scope, id, attrs]))

    @builtins.property
    @jsii.member(jsii_name="dataSource")
    def data_source(self) -> BaseDataSource:
        '''(experimental) the data source of this AppSync Function.

        :stability: experimental
        :attribute: DataSourceName
        '''
        return typing.cast(BaseDataSource, jsii.get(self, "dataSource"))

    @builtins.property
    @jsii.member(jsii_name="functionArn")
    def function_arn(self) -> builtins.str:
        '''(experimental) the ARN of the AppSync function.

        :stability: experimental
        :attribute: true
        '''
        return typing.cast(builtins.str, jsii.get(self, "functionArn"))

    @builtins.property
    @jsii.member(jsii_name="functionId")
    def function_id(self) -> builtins.str:
        '''(experimental) the ID of the AppSync function.

        :stability: experimental
        :attribute: true
        '''
        return typing.cast(builtins.str, jsii.get(self, "functionId"))

    @builtins.property
    @jsii.member(jsii_name="functionName")
    def function_name(self) -> builtins.str:
        '''(experimental) the name of this AppSync Function.

        :stability: experimental
        :attribute: Name
        '''
        return typing.cast(builtins.str, jsii.get(self, "functionName"))


@jsii.data_type(
    jsii_type="@aws-cdk/aws-appsync-alpha.AppsyncFunctionProps",
    jsii_struct_bases=[BaseAppsyncFunctionProps],
    name_mapping={
        "name": "name",
        "description": "description",
        "request_mapping_template": "requestMappingTemplate",
        "response_mapping_template": "responseMappingTemplate",
        "api": "api",
        "data_source": "dataSource",
    },
)
class AppsyncFunctionProps(BaseAppsyncFunctionProps):
    def __init__(
        self,
        *,
        name: builtins.str,
        description: typing.Optional[builtins.str] = None,
        request_mapping_template: typing.Optional[MappingTemplate] = None,
        response_mapping_template: typing.Optional[MappingTemplate] = None,
        api: IGraphqlApi,
        data_source: BaseDataSource,
    ) -> None:
        '''(experimental) the CDK properties for AppSync Functions.

        :param name: (experimental) the name of the AppSync Function.
        :param description: (experimental) the description for this AppSync Function. Default: - no description
        :param request_mapping_template: (experimental) the request mapping template for the AppSync Function. Default: - no request mapping template
        :param response_mapping_template: (experimental) the response mapping template for the AppSync Function. Default: - no response mapping template
        :param api: (experimental) the GraphQL Api linked to this AppSync Function.
        :param data_source: (experimental) the data source linked to this AppSync Function.

        :stability: experimental
        :exampleMetadata: infused

        Example::

            # api: appsync.GraphqlApi
            
            
            appsync_function = appsync.AppsyncFunction(self, "function",
                name="appsync_function",
                api=api,
                data_source=api.add_none_data_source("none"),
                request_mapping_template=appsync.MappingTemplate.from_file("request.vtl"),
                response_mapping_template=appsync.MappingTemplate.from_file("response.vtl")
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__10e97c994200b0a6907d75e73741660033ad46a0451d0480f4bdb955c615ab2a)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument request_mapping_template", value=request_mapping_template, expected_type=type_hints["request_mapping_template"])
            check_type(argname="argument response_mapping_template", value=response_mapping_template, expected_type=type_hints["response_mapping_template"])
            check_type(argname="argument api", value=api, expected_type=type_hints["api"])
            check_type(argname="argument data_source", value=data_source, expected_type=type_hints["data_source"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "name": name,
            "api": api,
            "data_source": data_source,
        }
        if description is not None:
            self._values["description"] = description
        if request_mapping_template is not None:
            self._values["request_mapping_template"] = request_mapping_template
        if response_mapping_template is not None:
            self._values["response_mapping_template"] = response_mapping_template

    @builtins.property
    def name(self) -> builtins.str:
        '''(experimental) the name of the AppSync Function.

        :stability: experimental
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''(experimental) the description for this AppSync Function.

        :default: - no description

        :stability: experimental
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def request_mapping_template(self) -> typing.Optional[MappingTemplate]:
        '''(experimental) the request mapping template for the AppSync Function.

        :default: - no request mapping template

        :stability: experimental
        '''
        result = self._values.get("request_mapping_template")
        return typing.cast(typing.Optional[MappingTemplate], result)

    @builtins.property
    def response_mapping_template(self) -> typing.Optional[MappingTemplate]:
        '''(experimental) the response mapping template for the AppSync Function.

        :default: - no response mapping template

        :stability: experimental
        '''
        result = self._values.get("response_mapping_template")
        return typing.cast(typing.Optional[MappingTemplate], result)

    @builtins.property
    def api(self) -> IGraphqlApi:
        '''(experimental) the GraphQL Api linked to this AppSync Function.

        :stability: experimental
        '''
        result = self._values.get("api")
        assert result is not None, "Required property 'api' is missing"
        return typing.cast(IGraphqlApi, result)

    @builtins.property
    def data_source(self) -> BaseDataSource:
        '''(experimental) the data source linked to this AppSync Function.

        :stability: experimental
        '''
        result = self._values.get("data_source")
        assert result is not None, "Required property 'data_source' is missing"
        return typing.cast(BaseDataSource, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppsyncFunctionProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_aws_cdk_aws_iam_ceddda9d.IGrantable)
class BackedDataSource(
    BaseDataSource,
    metaclass=jsii.JSIIAbstractClass,
    jsii_type="@aws-cdk/aws-appsync-alpha.BackedDataSource",
):
    '''(experimental) Abstract AppSync datasource implementation.

    Do not use directly but use subclasses for resource backed datasources

    :stability: experimental
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        props: typing.Union["BackedDataSourceProps", typing.Dict[builtins.str, typing.Any]],
        *,
        type: builtins.str,
        dynamo_db_config: typing.Optional[typing.Union[typing.Union[_aws_cdk_aws_appsync_ceddda9d.CfnDataSource.DynamoDBConfigProperty, typing.Dict[builtins.str, typing.Any]], _aws_cdk_ceddda9d.IResolvable]] = None,
        elasticsearch_config: typing.Optional[typing.Union[typing.Union[_aws_cdk_aws_appsync_ceddda9d.CfnDataSource.ElasticsearchConfigProperty, typing.Dict[builtins.str, typing.Any]], _aws_cdk_ceddda9d.IResolvable]] = None,
        http_config: typing.Optional[typing.Union[typing.Union[_aws_cdk_aws_appsync_ceddda9d.CfnDataSource.HttpConfigProperty, typing.Dict[builtins.str, typing.Any]], _aws_cdk_ceddda9d.IResolvable]] = None,
        lambda_config: typing.Optional[typing.Union[typing.Union[_aws_cdk_aws_appsync_ceddda9d.CfnDataSource.LambdaConfigProperty, typing.Dict[builtins.str, typing.Any]], _aws_cdk_ceddda9d.IResolvable]] = None,
        open_search_service_config: typing.Optional[typing.Union[typing.Union[_aws_cdk_aws_appsync_ceddda9d.CfnDataSource.OpenSearchServiceConfigProperty, typing.Dict[builtins.str, typing.Any]], _aws_cdk_ceddda9d.IResolvable]] = None,
        relational_database_config: typing.Optional[typing.Union[typing.Union[_aws_cdk_aws_appsync_ceddda9d.CfnDataSource.RelationalDatabaseConfigProperty, typing.Dict[builtins.str, typing.Any]], _aws_cdk_ceddda9d.IResolvable]] = None,
    ) -> None:
        '''
        :param scope: -
        :param id: -
        :param props: -
        :param type: (experimental) the type of the AppSync datasource.
        :param dynamo_db_config: (experimental) configuration for DynamoDB Datasource. Default: - No config
        :param elasticsearch_config: (deprecated) configuration for Elasticsearch data source. Default: - No config
        :param http_config: (experimental) configuration for HTTP Datasource. Default: - No config
        :param lambda_config: (experimental) configuration for Lambda Datasource. Default: - No config
        :param open_search_service_config: (experimental) configuration for OpenSearch data source. Default: - No config
        :param relational_database_config: (experimental) configuration for RDS Datasource. Default: - No config

        :stability: experimental
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__215ea606dd80608e35853c39b5e33223e4130143cd49461615b91a8cf968debe)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        extended = ExtendedDataSourceProps(
            type=type,
            dynamo_db_config=dynamo_db_config,
            elasticsearch_config=elasticsearch_config,
            http_config=http_config,
            lambda_config=lambda_config,
            open_search_service_config=open_search_service_config,
            relational_database_config=relational_database_config,
        )

        jsii.create(self.__class__, self, [scope, id, props, extended])

    @builtins.property
    @jsii.member(jsii_name="grantPrincipal")
    def grant_principal(self) -> _aws_cdk_aws_iam_ceddda9d.IPrincipal:
        '''(experimental) the principal of the data source to be IGrantable.

        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IPrincipal, jsii.get(self, "grantPrincipal"))


class _BackedDataSourceProxy(
    BackedDataSource,
    jsii.proxy_for(BaseDataSource), # type: ignore[misc]
):
    pass

# Adding a "__jsii_proxy_class__(): typing.Type" function to the abstract class
typing.cast(typing.Any, BackedDataSource).__jsii_proxy_class__ = lambda : _BackedDataSourceProxy


@jsii.data_type(
    jsii_type="@aws-cdk/aws-appsync-alpha.BackedDataSourceProps",
    jsii_struct_bases=[BaseDataSourceProps],
    name_mapping={
        "api": "api",
        "description": "description",
        "name": "name",
        "service_role": "serviceRole",
    },
)
class BackedDataSourceProps(BaseDataSourceProps):
    def __init__(
        self,
        *,
        api: IGraphqlApi,
        description: typing.Optional[builtins.str] = None,
        name: typing.Optional[builtins.str] = None,
        service_role: typing.Optional[_aws_cdk_aws_iam_ceddda9d.IRole] = None,
    ) -> None:
        '''(experimental) properties for an AppSync datasource backed by a resource.

        :param api: (experimental) The API to attach this data source to.
        :param description: (experimental) the description of the data source. Default: - None
        :param name: (experimental) The name of the data source. Default: - id of data source
        :param service_role: (experimental) The IAM service role to be assumed by AppSync to interact with the data source. Default: - Create a new role

        :stability: experimental
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            import aws_cdk.aws_appsync_alpha as appsync_alpha
            from aws_cdk import aws_iam as iam
            
            # graphql_api: appsync_alpha.GraphqlApi
            # role: iam.Role
            
            backed_data_source_props = appsync_alpha.BackedDataSourceProps(
                api=graphql_api,
            
                # the properties below are optional
                description="description",
                name="name",
                service_role=role
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ff628c288b521502363745cdded04a14655886e627b77fe903e1b89f3e57881a)
            check_type(argname="argument api", value=api, expected_type=type_hints["api"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument service_role", value=service_role, expected_type=type_hints["service_role"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "api": api,
        }
        if description is not None:
            self._values["description"] = description
        if name is not None:
            self._values["name"] = name
        if service_role is not None:
            self._values["service_role"] = service_role

    @builtins.property
    def api(self) -> IGraphqlApi:
        '''(experimental) The API to attach this data source to.

        :stability: experimental
        '''
        result = self._values.get("api")
        assert result is not None, "Required property 'api' is missing"
        return typing.cast(IGraphqlApi, result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''(experimental) the description of the data source.

        :default: - None

        :stability: experimental
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''(experimental) The name of the data source.

        :default: - id of data source

        :stability: experimental
        '''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def service_role(self) -> typing.Optional[_aws_cdk_aws_iam_ceddda9d.IRole]:
        '''(experimental) The IAM service role to be assumed by AppSync to interact with the data source.

        :default: - Create a new role

        :stability: experimental
        '''
        result = self._values.get("service_role")
        return typing.cast(typing.Optional[_aws_cdk_aws_iam_ceddda9d.IRole], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "BackedDataSourceProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DynamoDbDataSource(
    BackedDataSource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/aws-appsync-alpha.DynamoDbDataSource",
):
    '''(experimental) An AppSync datasource backed by a DynamoDB table.

    :stability: experimental
    :exampleMetadata: infused

    Example::

        api = appsync.GraphqlApi(self, "Api",
            name="demo",
            schema=appsync.SchemaFile.from_asset(path.join(__dirname, "schema.graphql")),
            authorization_config=appsync.AuthorizationConfig(
                default_authorization=appsync.AuthorizationMode(
                    authorization_type=appsync.AuthorizationType.IAM
                )
            ),
            xray_enabled=True
        )
        
        demo_table = dynamodb.Table(self, "DemoTable",
            partition_key=dynamodb.Attribute(
                name="id",
                type=dynamodb.AttributeType.STRING
            )
        )
        
        demo_dS = api.add_dynamo_db_data_source("demoDataSource", demo_table)
        
        # Resolver for the Query "getDemos" that scans the DynamoDb table and returns the entire list.
        # Resolver Mapping Template Reference:
        # https://docs.aws.amazon.com/appsync/latest/devguide/resolver-mapping-template-reference-dynamodb.html
        demo_dS.create_resolver("QueryGetDemosResolver",
            type_name="Query",
            field_name="getDemos",
            request_mapping_template=appsync.MappingTemplate.dynamo_db_scan_table(),
            response_mapping_template=appsync.MappingTemplate.dynamo_db_result_list()
        )
        
        # Resolver for the Mutation "addDemo" that puts the item into the DynamoDb table.
        demo_dS.create_resolver("MutationAddDemoResolver",
            type_name="Mutation",
            field_name="addDemo",
            request_mapping_template=appsync.MappingTemplate.dynamo_db_put_item(
                appsync.PrimaryKey.partition("id").auto(),
                appsync.Values.projecting("input")),
            response_mapping_template=appsync.MappingTemplate.dynamo_db_result_item()
        )
        
        # To enable DynamoDB read consistency with the `MappingTemplate`:
        demo_dS.create_resolver("QueryGetDemosConsistentResolver",
            type_name="Query",
            field_name="getDemosConsistent",
            request_mapping_template=appsync.MappingTemplate.dynamo_db_scan_table(True),
            response_mapping_template=appsync.MappingTemplate.dynamo_db_result_list()
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        table: _aws_cdk_aws_dynamodb_ceddda9d.ITable,
        read_only_access: typing.Optional[builtins.bool] = None,
        use_caller_credentials: typing.Optional[builtins.bool] = None,
        service_role: typing.Optional[_aws_cdk_aws_iam_ceddda9d.IRole] = None,
        api: IGraphqlApi,
        description: typing.Optional[builtins.str] = None,
        name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param scope: -
        :param id: -
        :param table: (experimental) The DynamoDB table backing this data source.
        :param read_only_access: (experimental) Specify whether this DS is read only or has read and write permissions to the DynamoDB table. Default: false
        :param use_caller_credentials: (experimental) use credentials of caller to access DynamoDB. Default: false
        :param service_role: (experimental) The IAM service role to be assumed by AppSync to interact with the data source. Default: - Create a new role
        :param api: (experimental) The API to attach this data source to.
        :param description: (experimental) the description of the data source. Default: - None
        :param name: (experimental) The name of the data source. Default: - id of data source

        :stability: experimental
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9a5b4c2ad4cc545351c4c404fc49eed5884f2dc008a1da2687cbd4f7db51d473)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = DynamoDbDataSourceProps(
            table=table,
            read_only_access=read_only_access,
            use_caller_credentials=use_caller_credentials,
            service_role=service_role,
            api=api,
            description=description,
            name=name,
        )

        jsii.create(self.__class__, self, [scope, id, props])


@jsii.data_type(
    jsii_type="@aws-cdk/aws-appsync-alpha.DynamoDbDataSourceProps",
    jsii_struct_bases=[BackedDataSourceProps],
    name_mapping={
        "api": "api",
        "description": "description",
        "name": "name",
        "service_role": "serviceRole",
        "table": "table",
        "read_only_access": "readOnlyAccess",
        "use_caller_credentials": "useCallerCredentials",
    },
)
class DynamoDbDataSourceProps(BackedDataSourceProps):
    def __init__(
        self,
        *,
        api: IGraphqlApi,
        description: typing.Optional[builtins.str] = None,
        name: typing.Optional[builtins.str] = None,
        service_role: typing.Optional[_aws_cdk_aws_iam_ceddda9d.IRole] = None,
        table: _aws_cdk_aws_dynamodb_ceddda9d.ITable,
        read_only_access: typing.Optional[builtins.bool] = None,
        use_caller_credentials: typing.Optional[builtins.bool] = None,
    ) -> None:
        '''(experimental) Properties for an AppSync DynamoDB datasource.

        :param api: (experimental) The API to attach this data source to.
        :param description: (experimental) the description of the data source. Default: - None
        :param name: (experimental) The name of the data source. Default: - id of data source
        :param service_role: (experimental) The IAM service role to be assumed by AppSync to interact with the data source. Default: - Create a new role
        :param table: (experimental) The DynamoDB table backing this data source.
        :param read_only_access: (experimental) Specify whether this DS is read only or has read and write permissions to the DynamoDB table. Default: false
        :param use_caller_credentials: (experimental) use credentials of caller to access DynamoDB. Default: false

        :stability: experimental
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            import aws_cdk.aws_appsync_alpha as appsync_alpha
            from aws_cdk import aws_dynamodb as dynamodb
            from aws_cdk import aws_iam as iam
            
            # graphql_api: appsync_alpha.GraphqlApi
            # role: iam.Role
            # table: dynamodb.Table
            
            dynamo_db_data_source_props = appsync_alpha.DynamoDbDataSourceProps(
                api=graphql_api,
                table=table,
            
                # the properties below are optional
                description="description",
                name="name",
                read_only_access=False,
                service_role=role,
                use_caller_credentials=False
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__00e3da2492e4229a1813c880b1e0fdab70a08ac780ed5c02eb6aa905704a7ccb)
            check_type(argname="argument api", value=api, expected_type=type_hints["api"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument service_role", value=service_role, expected_type=type_hints["service_role"])
            check_type(argname="argument table", value=table, expected_type=type_hints["table"])
            check_type(argname="argument read_only_access", value=read_only_access, expected_type=type_hints["read_only_access"])
            check_type(argname="argument use_caller_credentials", value=use_caller_credentials, expected_type=type_hints["use_caller_credentials"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "api": api,
            "table": table,
        }
        if description is not None:
            self._values["description"] = description
        if name is not None:
            self._values["name"] = name
        if service_role is not None:
            self._values["service_role"] = service_role
        if read_only_access is not None:
            self._values["read_only_access"] = read_only_access
        if use_caller_credentials is not None:
            self._values["use_caller_credentials"] = use_caller_credentials

    @builtins.property
    def api(self) -> IGraphqlApi:
        '''(experimental) The API to attach this data source to.

        :stability: experimental
        '''
        result = self._values.get("api")
        assert result is not None, "Required property 'api' is missing"
        return typing.cast(IGraphqlApi, result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''(experimental) the description of the data source.

        :default: - None

        :stability: experimental
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''(experimental) The name of the data source.

        :default: - id of data source

        :stability: experimental
        '''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def service_role(self) -> typing.Optional[_aws_cdk_aws_iam_ceddda9d.IRole]:
        '''(experimental) The IAM service role to be assumed by AppSync to interact with the data source.

        :default: - Create a new role

        :stability: experimental
        '''
        result = self._values.get("service_role")
        return typing.cast(typing.Optional[_aws_cdk_aws_iam_ceddda9d.IRole], result)

    @builtins.property
    def table(self) -> _aws_cdk_aws_dynamodb_ceddda9d.ITable:
        '''(experimental) The DynamoDB table backing this data source.

        :stability: experimental
        '''
        result = self._values.get("table")
        assert result is not None, "Required property 'table' is missing"
        return typing.cast(_aws_cdk_aws_dynamodb_ceddda9d.ITable, result)

    @builtins.property
    def read_only_access(self) -> typing.Optional[builtins.bool]:
        '''(experimental) Specify whether this DS is read only or has read and write permissions to the DynamoDB table.

        :default: false

        :stability: experimental
        '''
        result = self._values.get("read_only_access")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def use_caller_credentials(self) -> typing.Optional[builtins.bool]:
        '''(experimental) use credentials of caller to access DynamoDB.

        :default: false

        :stability: experimental
        '''
        result = self._values.get("use_caller_credentials")
        return typing.cast(typing.Optional[builtins.bool], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DynamoDbDataSourceProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ElasticsearchDataSource(
    BackedDataSource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/aws-appsync-alpha.ElasticsearchDataSource",
):
    '''(deprecated) An Appsync datasource backed by Elasticsearch.

    :deprecated: - use ``OpenSearchDataSource``

    :stability: deprecated
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        import aws_cdk.aws_appsync_alpha as appsync_alpha
        from aws_cdk import aws_elasticsearch as elasticsearch
        from aws_cdk import aws_iam as iam
        
        # domain: elasticsearch.Domain
        # graphql_api: appsync_alpha.GraphqlApi
        # role: iam.Role
        
        elasticsearch_data_source = appsync_alpha.ElasticsearchDataSource(self, "MyElasticsearchDataSource",
            api=graphql_api,
            domain=domain,
        
            # the properties below are optional
            description="description",
            name="name",
            service_role=role
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        domain: _aws_cdk_aws_elasticsearch_ceddda9d.IDomain,
        service_role: typing.Optional[_aws_cdk_aws_iam_ceddda9d.IRole] = None,
        api: IGraphqlApi,
        description: typing.Optional[builtins.str] = None,
        name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param scope: -
        :param id: -
        :param domain: (deprecated) The elasticsearch domain containing the endpoint for the data source.
        :param service_role: (experimental) The IAM service role to be assumed by AppSync to interact with the data source. Default: - Create a new role
        :param api: (experimental) The API to attach this data source to.
        :param description: (experimental) the description of the data source. Default: - None
        :param name: (experimental) The name of the data source. Default: - id of data source

        :stability: deprecated
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__218b9759a1ea729ae49c472141a2b492b6792f8ce50ab5b261799cbd005ce6e0)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = ElasticsearchDataSourceProps(
            domain=domain,
            service_role=service_role,
            api=api,
            description=description,
            name=name,
        )

        jsii.create(self.__class__, self, [scope, id, props])


@jsii.data_type(
    jsii_type="@aws-cdk/aws-appsync-alpha.ElasticsearchDataSourceProps",
    jsii_struct_bases=[BackedDataSourceProps],
    name_mapping={
        "api": "api",
        "description": "description",
        "name": "name",
        "service_role": "serviceRole",
        "domain": "domain",
    },
)
class ElasticsearchDataSourceProps(BackedDataSourceProps):
    def __init__(
        self,
        *,
        api: IGraphqlApi,
        description: typing.Optional[builtins.str] = None,
        name: typing.Optional[builtins.str] = None,
        service_role: typing.Optional[_aws_cdk_aws_iam_ceddda9d.IRole] = None,
        domain: _aws_cdk_aws_elasticsearch_ceddda9d.IDomain,
    ) -> None:
        '''(deprecated) Properties for the Elasticsearch Data Source.

        :param api: (experimental) The API to attach this data source to.
        :param description: (experimental) the description of the data source. Default: - None
        :param name: (experimental) The name of the data source. Default: - id of data source
        :param service_role: (experimental) The IAM service role to be assumed by AppSync to interact with the data source. Default: - Create a new role
        :param domain: (deprecated) The elasticsearch domain containing the endpoint for the data source.

        :deprecated: - use ``OpenSearchDataSourceProps`` with ``OpenSearchDataSource``

        :stability: deprecated
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            import aws_cdk.aws_appsync_alpha as appsync_alpha
            from aws_cdk import aws_elasticsearch as elasticsearch
            from aws_cdk import aws_iam as iam
            
            # domain: elasticsearch.Domain
            # graphql_api: appsync_alpha.GraphqlApi
            # role: iam.Role
            
            elasticsearch_data_source_props = appsync_alpha.ElasticsearchDataSourceProps(
                api=graphql_api,
                domain=domain,
            
                # the properties below are optional
                description="description",
                name="name",
                service_role=role
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7ec2ec75d494252faef9e4d153421e666bfca76ca970577a545c41aec7c1c77a)
            check_type(argname="argument api", value=api, expected_type=type_hints["api"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument service_role", value=service_role, expected_type=type_hints["service_role"])
            check_type(argname="argument domain", value=domain, expected_type=type_hints["domain"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "api": api,
            "domain": domain,
        }
        if description is not None:
            self._values["description"] = description
        if name is not None:
            self._values["name"] = name
        if service_role is not None:
            self._values["service_role"] = service_role

    @builtins.property
    def api(self) -> IGraphqlApi:
        '''(experimental) The API to attach this data source to.

        :stability: experimental
        '''
        result = self._values.get("api")
        assert result is not None, "Required property 'api' is missing"
        return typing.cast(IGraphqlApi, result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''(experimental) the description of the data source.

        :default: - None

        :stability: experimental
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''(experimental) The name of the data source.

        :default: - id of data source

        :stability: experimental
        '''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def service_role(self) -> typing.Optional[_aws_cdk_aws_iam_ceddda9d.IRole]:
        '''(experimental) The IAM service role to be assumed by AppSync to interact with the data source.

        :default: - Create a new role

        :stability: experimental
        '''
        result = self._values.get("service_role")
        return typing.cast(typing.Optional[_aws_cdk_aws_iam_ceddda9d.IRole], result)

    @builtins.property
    def domain(self) -> _aws_cdk_aws_elasticsearch_ceddda9d.IDomain:
        '''(deprecated) The elasticsearch domain containing the endpoint for the data source.

        :stability: deprecated
        '''
        result = self._values.get("domain")
        assert result is not None, "Required property 'domain' is missing"
        return typing.cast(_aws_cdk_aws_elasticsearch_ceddda9d.IDomain, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ElasticsearchDataSourceProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(IGraphqlApi)
class GraphqlApiBase(
    _aws_cdk_ceddda9d.Resource,
    metaclass=jsii.JSIIAbstractClass,
    jsii_type="@aws-cdk/aws-appsync-alpha.GraphqlApiBase",
):
    '''(experimental) Base Class for GraphQL API.

    :stability: experimental
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        account: typing.Optional[builtins.str] = None,
        environment_from_arn: typing.Optional[builtins.str] = None,
        physical_name: typing.Optional[builtins.str] = None,
        region: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param scope: -
        :param id: -
        :param account: The AWS account ID this resource belongs to. Default: - the resource is in the same account as the stack it belongs to
        :param environment_from_arn: ARN to deduce region and account from. The ARN is parsed and the account and region are taken from the ARN. This should be used for imported resources. Cannot be supplied together with either ``account`` or ``region``. Default: - take environment from ``account``, ``region`` parameters, or use Stack environment.
        :param physical_name: The value passed in by users to the physical name prop of the resource. - ``undefined`` implies that a physical name will be allocated by CloudFormation during deployment. - a concrete value implies a specific physical name - ``PhysicalName.GENERATE_IF_NEEDED`` is a marker that indicates that a physical will only be generated by the CDK if it is needed for cross-environment references. Otherwise, it will be allocated by CloudFormation. Default: - The physical name will be allocated by CloudFormation at deployment time
        :param region: The AWS region this resource belongs to. Default: - the resource is in the same region as the stack it belongs to
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__523fe479f81abf8faac00c284f3310629e45647b2a9e37d352a5665b59f803a1)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = _aws_cdk_ceddda9d.ResourceProps(
            account=account,
            environment_from_arn=environment_from_arn,
            physical_name=physical_name,
            region=region,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="addDynamoDbDataSource")
    def add_dynamo_db_data_source(
        self,
        id: builtins.str,
        table: _aws_cdk_aws_dynamodb_ceddda9d.ITable,
        *,
        description: typing.Optional[builtins.str] = None,
        name: typing.Optional[builtins.str] = None,
    ) -> DynamoDbDataSource:
        '''(experimental) add a new DynamoDB data source to this API.

        :param id: The data source's id.
        :param table: The DynamoDB table backing this data source.
        :param description: (experimental) The description of the data source. Default: - No description
        :param name: (experimental) The name of the data source, overrides the id given by cdk. Default: - generated by cdk given the id

        :stability: experimental
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__94e2cdd73a175e5019d14e6e050cf81272cc5bba6474743075c9027d864ac5ad)
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument table", value=table, expected_type=type_hints["table"])
        options = DataSourceOptions(description=description, name=name)

        return typing.cast(DynamoDbDataSource, jsii.invoke(self, "addDynamoDbDataSource", [id, table, options]))

    @jsii.member(jsii_name="addElasticsearchDataSource")
    def add_elasticsearch_data_source(
        self,
        id: builtins.str,
        domain: _aws_cdk_aws_elasticsearch_ceddda9d.IDomain,
        *,
        description: typing.Optional[builtins.str] = None,
        name: typing.Optional[builtins.str] = None,
    ) -> ElasticsearchDataSource:
        '''(deprecated) add a new elasticsearch data source to this API.

        :param id: The data source's id.
        :param domain: The elasticsearch domain for this data source.
        :param description: (experimental) The description of the data source. Default: - No description
        :param name: (experimental) The name of the data source, overrides the id given by cdk. Default: - generated by cdk given the id

        :deprecated: - use ``addOpenSearchDataSource``

        :stability: deprecated
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__486a98cd301c656f17aba987683eb8a1e71c203e3d9347b771ba373ed759e043)
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument domain", value=domain, expected_type=type_hints["domain"])
        options = DataSourceOptions(description=description, name=name)

        return typing.cast(ElasticsearchDataSource, jsii.invoke(self, "addElasticsearchDataSource", [id, domain, options]))

    @jsii.member(jsii_name="addHttpDataSource")
    def add_http_data_source(
        self,
        id: builtins.str,
        endpoint: builtins.str,
        *,
        authorization_config: typing.Optional[typing.Union[AwsIamConfig, typing.Dict[builtins.str, typing.Any]]] = None,
        description: typing.Optional[builtins.str] = None,
        name: typing.Optional[builtins.str] = None,
    ) -> "HttpDataSource":
        '''(experimental) add a new http data source to this API.

        :param id: The data source's id.
        :param endpoint: The http endpoint.
        :param authorization_config: (experimental) The authorization config in case the HTTP endpoint requires authorization. Default: - none
        :param description: (experimental) The description of the data source. Default: - No description
        :param name: (experimental) The name of the data source, overrides the id given by cdk. Default: - generated by cdk given the id

        :stability: experimental
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ecfb064c8a50703fb696e4a526e056950219e94519cc179d2a007f4aba247f3f)
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument endpoint", value=endpoint, expected_type=type_hints["endpoint"])
        options = HttpDataSourceOptions(
            authorization_config=authorization_config,
            description=description,
            name=name,
        )

        return typing.cast("HttpDataSource", jsii.invoke(self, "addHttpDataSource", [id, endpoint, options]))

    @jsii.member(jsii_name="addLambdaDataSource")
    def add_lambda_data_source(
        self,
        id: builtins.str,
        lambda_function: _aws_cdk_aws_lambda_ceddda9d.IFunction,
        *,
        description: typing.Optional[builtins.str] = None,
        name: typing.Optional[builtins.str] = None,
    ) -> "LambdaDataSource":
        '''(experimental) add a new Lambda data source to this API.

        :param id: The data source's id.
        :param lambda_function: The Lambda function to call to interact with this data source.
        :param description: (experimental) The description of the data source. Default: - No description
        :param name: (experimental) The name of the data source, overrides the id given by cdk. Default: - generated by cdk given the id

        :stability: experimental
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6bfafbb3d516b6c08eac48f102e5f98eb43be16dae3f7bdeeed708272f7076af)
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument lambda_function", value=lambda_function, expected_type=type_hints["lambda_function"])
        options = DataSourceOptions(description=description, name=name)

        return typing.cast("LambdaDataSource", jsii.invoke(self, "addLambdaDataSource", [id, lambda_function, options]))

    @jsii.member(jsii_name="addNoneDataSource")
    def add_none_data_source(
        self,
        id: builtins.str,
        *,
        description: typing.Optional[builtins.str] = None,
        name: typing.Optional[builtins.str] = None,
    ) -> NoneDataSource:
        '''(experimental) add a new dummy data source to this API.

        Useful for pipeline resolvers
        and for backend changes that don't require a data source.

        :param id: The data source's id.
        :param description: (experimental) The description of the data source. Default: - No description
        :param name: (experimental) The name of the data source, overrides the id given by cdk. Default: - generated by cdk given the id

        :stability: experimental
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6a96311b1d2416236de2dd1371bc6f02cf4524b49d862d33d88fe5231ec444e5)
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        options = DataSourceOptions(description=description, name=name)

        return typing.cast(NoneDataSource, jsii.invoke(self, "addNoneDataSource", [id, options]))

    @jsii.member(jsii_name="addOpenSearchDataSource")
    def add_open_search_data_source(
        self,
        id: builtins.str,
        domain: _aws_cdk_aws_opensearchservice_ceddda9d.IDomain,
        *,
        description: typing.Optional[builtins.str] = None,
        name: typing.Optional[builtins.str] = None,
    ) -> "OpenSearchDataSource":
        '''(experimental) add a new OpenSearch data source to this API.

        :param id: The data source's id.
        :param domain: The OpenSearch domain for this data source.
        :param description: (experimental) The description of the data source. Default: - No description
        :param name: (experimental) The name of the data source, overrides the id given by cdk. Default: - generated by cdk given the id

        :stability: experimental
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8c0c1eabe7b9f32d8afd05834ba199b0304ff656eafab6778c21c34c4f283c76)
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument domain", value=domain, expected_type=type_hints["domain"])
        options = DataSourceOptions(description=description, name=name)

        return typing.cast("OpenSearchDataSource", jsii.invoke(self, "addOpenSearchDataSource", [id, domain, options]))

    @jsii.member(jsii_name="addRdsDataSource")
    def add_rds_data_source(
        self,
        id: builtins.str,
        serverless_cluster: _aws_cdk_aws_rds_ceddda9d.IServerlessCluster,
        secret_store: _aws_cdk_aws_secretsmanager_ceddda9d.ISecret,
        database_name: typing.Optional[builtins.str] = None,
        *,
        description: typing.Optional[builtins.str] = None,
        name: typing.Optional[builtins.str] = None,
    ) -> "RdsDataSource":
        '''(experimental) add a new Rds data source to this API.

        :param id: The data source's id.
        :param serverless_cluster: The serverless cluster to interact with this data source.
        :param secret_store: The secret store that contains the username and password for the serverless cluster.
        :param database_name: The optional name of the database to use within the cluster.
        :param description: (experimental) The description of the data source. Default: - No description
        :param name: (experimental) The name of the data source, overrides the id given by cdk. Default: - generated by cdk given the id

        :stability: experimental
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e7a81701a9320c9569c6bd6e0d17789014c90d63c062ed932f347e6e96126333)
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument serverless_cluster", value=serverless_cluster, expected_type=type_hints["serverless_cluster"])
            check_type(argname="argument secret_store", value=secret_store, expected_type=type_hints["secret_store"])
            check_type(argname="argument database_name", value=database_name, expected_type=type_hints["database_name"])
        options = DataSourceOptions(description=description, name=name)

        return typing.cast("RdsDataSource", jsii.invoke(self, "addRdsDataSource", [id, serverless_cluster, secret_store, database_name, options]))

    @jsii.member(jsii_name="addSchemaDependency")
    def add_schema_dependency(
        self,
        construct: _aws_cdk_ceddda9d.CfnResource,
    ) -> builtins.bool:
        '''(experimental) Add schema dependency if not imported.

        :param construct: the dependee.

        :stability: experimental
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__33aa2a2e2fcba734874b8074322da06b3200ec4cb04743e0cceb6ced97651b0d)
            check_type(argname="argument construct", value=construct, expected_type=type_hints["construct"])
        return typing.cast(builtins.bool, jsii.invoke(self, "addSchemaDependency", [construct]))

    @jsii.member(jsii_name="createResolver")
    def create_resolver(
        self,
        id: builtins.str,
        *,
        data_source: typing.Optional[BaseDataSource] = None,
        field_name: builtins.str,
        type_name: builtins.str,
        caching_config: typing.Optional[typing.Union[CachingConfig, typing.Dict[builtins.str, typing.Any]]] = None,
        max_batch_size: typing.Optional[jsii.Number] = None,
        pipeline_config: typing.Optional[typing.Sequence[IAppsyncFunction]] = None,
        request_mapping_template: typing.Optional[MappingTemplate] = None,
        response_mapping_template: typing.Optional[MappingTemplate] = None,
    ) -> Resolver:
        '''(experimental) creates a new resolver for this datasource and API using the given properties.

        :param id: -
        :param data_source: (experimental) The data source this resolver is using. Default: - No datasource
        :param field_name: (experimental) name of the GraphQL field in the given type this resolver is attached to.
        :param type_name: (experimental) name of the GraphQL type this resolver is attached to.
        :param caching_config: (experimental) The caching configuration for this resolver. Default: - No caching configuration
        :param max_batch_size: (experimental) The maximum number of elements per batch, when using batch invoke. Default: - No max batch size
        :param pipeline_config: (experimental) configuration of the pipeline resolver. Default: - no pipeline resolver configuration An empty array | undefined sets resolver to be of kind, unit
        :param request_mapping_template: (experimental) The request mapping template for this resolver. Default: - No mapping template
        :param response_mapping_template: (experimental) The response mapping template for this resolver. Default: - No mapping template

        :stability: experimental
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4edf824fbab5e0903a1611680264800f7787642b27370977d8a745c0456324cf)
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = ExtendedResolverProps(
            data_source=data_source,
            field_name=field_name,
            type_name=type_name,
            caching_config=caching_config,
            max_batch_size=max_batch_size,
            pipeline_config=pipeline_config,
            request_mapping_template=request_mapping_template,
            response_mapping_template=response_mapping_template,
        )

        return typing.cast(Resolver, jsii.invoke(self, "createResolver", [id, props]))

    @builtins.property
    @jsii.member(jsii_name="apiId")
    @abc.abstractmethod
    def api_id(self) -> builtins.str:
        '''(experimental) an unique AWS AppSync GraphQL API identifier i.e. 'lxz775lwdrgcndgz3nurvac7oa'.

        :stability: experimental
        '''
        ...

    @builtins.property
    @jsii.member(jsii_name="arn")
    @abc.abstractmethod
    def arn(self) -> builtins.str:
        '''(experimental) the ARN of the API.

        :stability: experimental
        '''
        ...


class _GraphqlApiBaseProxy(
    GraphqlApiBase,
    jsii.proxy_for(_aws_cdk_ceddda9d.Resource), # type: ignore[misc]
):
    @builtins.property
    @jsii.member(jsii_name="apiId")
    def api_id(self) -> builtins.str:
        '''(experimental) an unique AWS AppSync GraphQL API identifier i.e. 'lxz775lwdrgcndgz3nurvac7oa'.

        :stability: experimental
        '''
        return typing.cast(builtins.str, jsii.get(self, "apiId"))

    @builtins.property
    @jsii.member(jsii_name="arn")
    def arn(self) -> builtins.str:
        '''(experimental) the ARN of the API.

        :stability: experimental
        '''
        return typing.cast(builtins.str, jsii.get(self, "arn"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the abstract class
typing.cast(typing.Any, GraphqlApiBase).__jsii_proxy_class__ = lambda : _GraphqlApiBaseProxy


class HttpDataSource(
    BackedDataSource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/aws-appsync-alpha.HttpDataSource",
):
    '''(experimental) An AppSync datasource backed by a http endpoint.

    :stability: experimental
    :exampleMetadata: infused

    Example::

        api = appsync.GraphqlApi(self, "api",
            name="api",
            schema=appsync.SchemaFile.from_asset(path.join(__dirname, "schema.graphql"))
        )
        
        http_ds = api.add_http_data_source("ds", "https://states.amazonaws.com",
            name="httpDsWithStepF",
            description="from appsync to StepFunctions Workflow",
            authorization_config=appsync.AwsIamConfig(
                signing_region="us-east-1",
                signing_service_name="states"
            )
        )
        
        http_ds.create_resolver("MutationCallStepFunctionResolver",
            type_name="Mutation",
            field_name="callStepFunction",
            request_mapping_template=appsync.MappingTemplate.from_file("request.vtl"),
            response_mapping_template=appsync.MappingTemplate.from_file("response.vtl")
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        endpoint: builtins.str,
        authorization_config: typing.Optional[typing.Union[AwsIamConfig, typing.Dict[builtins.str, typing.Any]]] = None,
        api: IGraphqlApi,
        description: typing.Optional[builtins.str] = None,
        name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param scope: -
        :param id: -
        :param endpoint: (experimental) The http endpoint.
        :param authorization_config: (experimental) The authorization config in case the HTTP endpoint requires authorization. Default: - none
        :param api: (experimental) The API to attach this data source to.
        :param description: (experimental) the description of the data source. Default: - None
        :param name: (experimental) The name of the data source. Default: - id of data source

        :stability: experimental
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b77d85138e18cad512b96f1db33702b184c66864aadafb6d6d16d71681c6c2de)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = HttpDataSourceProps(
            endpoint=endpoint,
            authorization_config=authorization_config,
            api=api,
            description=description,
            name=name,
        )

        jsii.create(self.__class__, self, [scope, id, props])


class LambdaDataSource(
    BackedDataSource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/aws-appsync-alpha.LambdaDataSource",
):
    '''(experimental) An AppSync datasource backed by a Lambda function.

    :stability: experimental
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        import aws_cdk.aws_appsync_alpha as appsync_alpha
        from aws_cdk import aws_iam as iam
        from aws_cdk import aws_lambda as lambda_
        
        # function_: lambda.Function
        # graphql_api: appsync_alpha.GraphqlApi
        # role: iam.Role
        
        lambda_data_source = appsync_alpha.LambdaDataSource(self, "MyLambdaDataSource",
            api=graphql_api,
            lambda_function=function_,
        
            # the properties below are optional
            description="description",
            name="name",
            service_role=role
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        lambda_function: _aws_cdk_aws_lambda_ceddda9d.IFunction,
        service_role: typing.Optional[_aws_cdk_aws_iam_ceddda9d.IRole] = None,
        api: IGraphqlApi,
        description: typing.Optional[builtins.str] = None,
        name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param scope: -
        :param id: -
        :param lambda_function: (experimental) The Lambda function to call to interact with this data source.
        :param service_role: (experimental) The IAM service role to be assumed by AppSync to interact with the data source. Default: - Create a new role
        :param api: (experimental) The API to attach this data source to.
        :param description: (experimental) the description of the data source. Default: - None
        :param name: (experimental) The name of the data source. Default: - id of data source

        :stability: experimental
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__dd360277d64e788625326cbbc6b23d5a86b71242516093d1f696ad7a6c3c5f5f)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = LambdaDataSourceProps(
            lambda_function=lambda_function,
            service_role=service_role,
            api=api,
            description=description,
            name=name,
        )

        jsii.create(self.__class__, self, [scope, id, props])


@jsii.data_type(
    jsii_type="@aws-cdk/aws-appsync-alpha.LambdaDataSourceProps",
    jsii_struct_bases=[BackedDataSourceProps],
    name_mapping={
        "api": "api",
        "description": "description",
        "name": "name",
        "service_role": "serviceRole",
        "lambda_function": "lambdaFunction",
    },
)
class LambdaDataSourceProps(BackedDataSourceProps):
    def __init__(
        self,
        *,
        api: IGraphqlApi,
        description: typing.Optional[builtins.str] = None,
        name: typing.Optional[builtins.str] = None,
        service_role: typing.Optional[_aws_cdk_aws_iam_ceddda9d.IRole] = None,
        lambda_function: _aws_cdk_aws_lambda_ceddda9d.IFunction,
    ) -> None:
        '''(experimental) Properties for an AppSync Lambda datasource.

        :param api: (experimental) The API to attach this data source to.
        :param description: (experimental) the description of the data source. Default: - None
        :param name: (experimental) The name of the data source. Default: - id of data source
        :param service_role: (experimental) The IAM service role to be assumed by AppSync to interact with the data source. Default: - Create a new role
        :param lambda_function: (experimental) The Lambda function to call to interact with this data source.

        :stability: experimental
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            import aws_cdk.aws_appsync_alpha as appsync_alpha
            from aws_cdk import aws_iam as iam
            from aws_cdk import aws_lambda as lambda_
            
            # function_: lambda.Function
            # graphql_api: appsync_alpha.GraphqlApi
            # role: iam.Role
            
            lambda_data_source_props = appsync_alpha.LambdaDataSourceProps(
                api=graphql_api,
                lambda_function=function_,
            
                # the properties below are optional
                description="description",
                name="name",
                service_role=role
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__09480a84bcca442f2c74291063c22d71becab43f875c393840768e69c982bcb6)
            check_type(argname="argument api", value=api, expected_type=type_hints["api"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument service_role", value=service_role, expected_type=type_hints["service_role"])
            check_type(argname="argument lambda_function", value=lambda_function, expected_type=type_hints["lambda_function"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "api": api,
            "lambda_function": lambda_function,
        }
        if description is not None:
            self._values["description"] = description
        if name is not None:
            self._values["name"] = name
        if service_role is not None:
            self._values["service_role"] = service_role

    @builtins.property
    def api(self) -> IGraphqlApi:
        '''(experimental) The API to attach this data source to.

        :stability: experimental
        '''
        result = self._values.get("api")
        assert result is not None, "Required property 'api' is missing"
        return typing.cast(IGraphqlApi, result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''(experimental) the description of the data source.

        :default: - None

        :stability: experimental
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''(experimental) The name of the data source.

        :default: - id of data source

        :stability: experimental
        '''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def service_role(self) -> typing.Optional[_aws_cdk_aws_iam_ceddda9d.IRole]:
        '''(experimental) The IAM service role to be assumed by AppSync to interact with the data source.

        :default: - Create a new role

        :stability: experimental
        '''
        result = self._values.get("service_role")
        return typing.cast(typing.Optional[_aws_cdk_aws_iam_ceddda9d.IRole], result)

    @builtins.property
    def lambda_function(self) -> _aws_cdk_aws_lambda_ceddda9d.IFunction:
        '''(experimental) The Lambda function to call to interact with this data source.

        :stability: experimental
        '''
        result = self._values.get("lambda_function")
        assert result is not None, "Required property 'lambda_function' is missing"
        return typing.cast(_aws_cdk_aws_lambda_ceddda9d.IFunction, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LambdaDataSourceProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class OpenSearchDataSource(
    BackedDataSource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/aws-appsync-alpha.OpenSearchDataSource",
):
    '''(experimental) An Appsync datasource backed by OpenSearch.

    :stability: experimental
    :exampleMetadata: infused

    Example::

        import aws_cdk.aws_opensearchservice as opensearch
        
        # api: appsync.GraphqlApi
        
        
        user = iam.User(self, "User")
        domain = opensearch.Domain(self, "Domain",
            version=opensearch.EngineVersion.OPENSEARCH_1_3,
            removal_policy=RemovalPolicy.DESTROY,
            fine_grained_access_control=opensearch.AdvancedSecurityOptions(master_user_arn=user.user_arn),
            encryption_at_rest=opensearch.EncryptionAtRestOptions(enabled=True),
            node_to_node_encryption=True,
            enforce_https=True
        )
        ds = api.add_open_search_data_source("ds", domain)
        
        ds.create_resolver("QueryGetTestsResolver",
            type_name="Query",
            field_name="getTests",
            request_mapping_template=appsync.MappingTemplate.from_string(JSON.stringify({
                "version": "2017-02-28",
                "operation": "GET",
                "path": "/id/post/_search",
                "params": {
                    "headers": {},
                    "query_string": {},
                    "body": {"from": 0, "size": 50}
                }
            })),
            response_mapping_template=appsync.MappingTemplate.from_string("""[
                    #foreach($entry in $context.result.hits.hits)
                    #if( $velocityCount > 1 ) , #end
                    $utils.toJson($entry.get("_source"))
                    #end
                  ]""")
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        domain: _aws_cdk_aws_opensearchservice_ceddda9d.IDomain,
        service_role: typing.Optional[_aws_cdk_aws_iam_ceddda9d.IRole] = None,
        api: IGraphqlApi,
        description: typing.Optional[builtins.str] = None,
        name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param scope: -
        :param id: -
        :param domain: (experimental) The OpenSearch domain containing the endpoint for the data source.
        :param service_role: (experimental) The IAM service role to be assumed by AppSync to interact with the data source. Default: - Create a new role
        :param api: (experimental) The API to attach this data source to.
        :param description: (experimental) the description of the data source. Default: - None
        :param name: (experimental) The name of the data source. Default: - id of data source

        :stability: experimental
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__806d535b2e5e6649463074cc89d3eef71463bd681270c0e2ec8d67ab9625a112)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = OpenSearchDataSourceProps(
            domain=domain,
            service_role=service_role,
            api=api,
            description=description,
            name=name,
        )

        jsii.create(self.__class__, self, [scope, id, props])


@jsii.data_type(
    jsii_type="@aws-cdk/aws-appsync-alpha.OpenSearchDataSourceProps",
    jsii_struct_bases=[BackedDataSourceProps],
    name_mapping={
        "api": "api",
        "description": "description",
        "name": "name",
        "service_role": "serviceRole",
        "domain": "domain",
    },
)
class OpenSearchDataSourceProps(BackedDataSourceProps):
    def __init__(
        self,
        *,
        api: IGraphqlApi,
        description: typing.Optional[builtins.str] = None,
        name: typing.Optional[builtins.str] = None,
        service_role: typing.Optional[_aws_cdk_aws_iam_ceddda9d.IRole] = None,
        domain: _aws_cdk_aws_opensearchservice_ceddda9d.IDomain,
    ) -> None:
        '''(experimental) Properties for the OpenSearch Data Source.

        :param api: (experimental) The API to attach this data source to.
        :param description: (experimental) the description of the data source. Default: - None
        :param name: (experimental) The name of the data source. Default: - id of data source
        :param service_role: (experimental) The IAM service role to be assumed by AppSync to interact with the data source. Default: - Create a new role
        :param domain: (experimental) The OpenSearch domain containing the endpoint for the data source.

        :stability: experimental
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            import aws_cdk.aws_appsync_alpha as appsync_alpha
            from aws_cdk import aws_iam as iam
            from aws_cdk import aws_opensearchservice as opensearchservice
            
            # domain: opensearchservice.Domain
            # graphql_api: appsync_alpha.GraphqlApi
            # role: iam.Role
            
            open_search_data_source_props = appsync_alpha.OpenSearchDataSourceProps(
                api=graphql_api,
                domain=domain,
            
                # the properties below are optional
                description="description",
                name="name",
                service_role=role
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f143aecf12cb9295e34e62376d2a6a103e604c85ca4104c2a2f14472fb83b94d)
            check_type(argname="argument api", value=api, expected_type=type_hints["api"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument service_role", value=service_role, expected_type=type_hints["service_role"])
            check_type(argname="argument domain", value=domain, expected_type=type_hints["domain"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "api": api,
            "domain": domain,
        }
        if description is not None:
            self._values["description"] = description
        if name is not None:
            self._values["name"] = name
        if service_role is not None:
            self._values["service_role"] = service_role

    @builtins.property
    def api(self) -> IGraphqlApi:
        '''(experimental) The API to attach this data source to.

        :stability: experimental
        '''
        result = self._values.get("api")
        assert result is not None, "Required property 'api' is missing"
        return typing.cast(IGraphqlApi, result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''(experimental) the description of the data source.

        :default: - None

        :stability: experimental
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''(experimental) The name of the data source.

        :default: - id of data source

        :stability: experimental
        '''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def service_role(self) -> typing.Optional[_aws_cdk_aws_iam_ceddda9d.IRole]:
        '''(experimental) The IAM service role to be assumed by AppSync to interact with the data source.

        :default: - Create a new role

        :stability: experimental
        '''
        result = self._values.get("service_role")
        return typing.cast(typing.Optional[_aws_cdk_aws_iam_ceddda9d.IRole], result)

    @builtins.property
    def domain(self) -> _aws_cdk_aws_opensearchservice_ceddda9d.IDomain:
        '''(experimental) The OpenSearch domain containing the endpoint for the data source.

        :stability: experimental
        '''
        result = self._values.get("domain")
        assert result is not None, "Required property 'domain' is missing"
        return typing.cast(_aws_cdk_aws_opensearchservice_ceddda9d.IDomain, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "OpenSearchDataSourceProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class PartitionKey(
    PrimaryKey,
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/aws-appsync-alpha.PartitionKey",
):
    '''(experimental) Specifies the assignment to the partition key.

    It can be
    enhanced with the assignment of the sort key.

    :stability: experimental
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        import aws_cdk.aws_appsync_alpha as appsync_alpha
        
        # assign: appsync_alpha.Assign
        
        partition_key = appsync_alpha.PartitionKey(assign)
    '''

    def __init__(self, pkey: Assign) -> None:
        '''
        :param pkey: -

        :stability: experimental
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7f8419af2cd92c85cbffe41568b08c3ff0bcdae5f8313824953c6e7ee2b86ca7)
            check_type(argname="argument pkey", value=pkey, expected_type=type_hints["pkey"])
        jsii.create(self.__class__, self, [pkey])

    @jsii.member(jsii_name="sort")
    def sort(self, key: builtins.str) -> SortKeyStep:
        '''(experimental) Allows assigning a value to the sort key.

        :param key: -

        :stability: experimental
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__03d25dce1ff151406d67cb5e80a8ff6bc8d26cad90e13cb0bbfddf653edc94dd)
            check_type(argname="argument key", value=key, expected_type=type_hints["key"])
        return typing.cast(SortKeyStep, jsii.invoke(self, "sort", [key]))


class RdsDataSource(
    BackedDataSource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/aws-appsync-alpha.RdsDataSource",
):
    '''(experimental) An AppSync datasource backed by RDS.

    :stability: experimental
    :exampleMetadata: infused

    Example::

        # Build a data source for AppSync to access the database.
        # api: appsync.GraphqlApi
        # Create username and password secret for DB Cluster
        secret = rds.DatabaseSecret(self, "AuroraSecret",
            username="clusteradmin"
        )
        
        # The VPC to place the cluster in
        vpc = ec2.Vpc(self, "AuroraVpc")
        
        # Create the serverless cluster, provide all values needed to customise the database.
        cluster = rds.ServerlessCluster(self, "AuroraCluster",
            engine=rds.DatabaseClusterEngine.AURORA_MYSQL,
            vpc=vpc,
            credentials={"username": "clusteradmin"},
            cluster_identifier="db-endpoint-test",
            default_database_name="demos"
        )
        rds_dS = api.add_rds_data_source("rds", cluster, secret, "demos")
        
        # Set up a resolver for an RDS query.
        rds_dS.create_resolver("QueryGetDemosRdsResolver",
            type_name="Query",
            field_name="getDemosRds",
            request_mapping_template=appsync.MappingTemplate.from_string("""
                  {
                    "version": "2018-05-29",
                    "statements": [
                      "SELECT * FROM demos"
                    ]
                  }
                  """),
            response_mapping_template=appsync.MappingTemplate.from_string("""
                    $utils.toJson($utils.rds.toJsonObject($ctx.result)[0])
                  """)
        )
        
        # Set up a resolver for an RDS mutation.
        rds_dS.create_resolver("MutationAddDemoRdsResolver",
            type_name="Mutation",
            field_name="addDemoRds",
            request_mapping_template=appsync.MappingTemplate.from_string("""
                  {
                    "version": "2018-05-29",
                    "statements": [
                      "INSERT INTO demos VALUES (:id, :version)",
                      "SELECT * WHERE id = :id"
                    ],
                    "variableMap": {
                      ":id": $util.toJson($util.autoId()),
                      ":version": $util.toJson($ctx.args.version)
                    }
                  }
                  """),
            response_mapping_template=appsync.MappingTemplate.from_string("""
                    $utils.toJson($utils.rds.toJsonObject($ctx.result)[1][0])
                  """)
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        secret_store: _aws_cdk_aws_secretsmanager_ceddda9d.ISecret,
        serverless_cluster: _aws_cdk_aws_rds_ceddda9d.IServerlessCluster,
        database_name: typing.Optional[builtins.str] = None,
        service_role: typing.Optional[_aws_cdk_aws_iam_ceddda9d.IRole] = None,
        api: IGraphqlApi,
        description: typing.Optional[builtins.str] = None,
        name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param scope: -
        :param id: -
        :param secret_store: (experimental) The secret containing the credentials for the database.
        :param serverless_cluster: (experimental) The serverless cluster to call to interact with this data source.
        :param database_name: (experimental) The name of the database to use within the cluster. Default: - None
        :param service_role: (experimental) The IAM service role to be assumed by AppSync to interact with the data source. Default: - Create a new role
        :param api: (experimental) The API to attach this data source to.
        :param description: (experimental) the description of the data source. Default: - None
        :param name: (experimental) The name of the data source. Default: - id of data source

        :stability: experimental
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6441252fabcc3030f951bd9c7f24a6d3dd03090d3c8546bf79a7623c540479e4)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = RdsDataSourceProps(
            secret_store=secret_store,
            serverless_cluster=serverless_cluster,
            database_name=database_name,
            service_role=service_role,
            api=api,
            description=description,
            name=name,
        )

        jsii.create(self.__class__, self, [scope, id, props])


@jsii.data_type(
    jsii_type="@aws-cdk/aws-appsync-alpha.RdsDataSourceProps",
    jsii_struct_bases=[BackedDataSourceProps],
    name_mapping={
        "api": "api",
        "description": "description",
        "name": "name",
        "service_role": "serviceRole",
        "secret_store": "secretStore",
        "serverless_cluster": "serverlessCluster",
        "database_name": "databaseName",
    },
)
class RdsDataSourceProps(BackedDataSourceProps):
    def __init__(
        self,
        *,
        api: IGraphqlApi,
        description: typing.Optional[builtins.str] = None,
        name: typing.Optional[builtins.str] = None,
        service_role: typing.Optional[_aws_cdk_aws_iam_ceddda9d.IRole] = None,
        secret_store: _aws_cdk_aws_secretsmanager_ceddda9d.ISecret,
        serverless_cluster: _aws_cdk_aws_rds_ceddda9d.IServerlessCluster,
        database_name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''(experimental) Properties for an AppSync RDS datasource.

        :param api: (experimental) The API to attach this data source to.
        :param description: (experimental) the description of the data source. Default: - None
        :param name: (experimental) The name of the data source. Default: - id of data source
        :param service_role: (experimental) The IAM service role to be assumed by AppSync to interact with the data source. Default: - Create a new role
        :param secret_store: (experimental) The secret containing the credentials for the database.
        :param serverless_cluster: (experimental) The serverless cluster to call to interact with this data source.
        :param database_name: (experimental) The name of the database to use within the cluster. Default: - None

        :stability: experimental
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            import aws_cdk.aws_appsync_alpha as appsync_alpha
            from aws_cdk import aws_iam as iam
            from aws_cdk import aws_rds as rds
            from aws_cdk import aws_secretsmanager as secretsmanager
            
            # graphql_api: appsync_alpha.GraphqlApi
            # role: iam.Role
            # secret: secretsmanager.Secret
            # serverless_cluster: rds.ServerlessCluster
            
            rds_data_source_props = appsync_alpha.RdsDataSourceProps(
                api=graphql_api,
                secret_store=secret,
                serverless_cluster=serverless_cluster,
            
                # the properties below are optional
                database_name="databaseName",
                description="description",
                name="name",
                service_role=role
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1e1dbdc39f8e8f411c9d0937bcba223b8f087c4394f648fd455304e646e57743)
            check_type(argname="argument api", value=api, expected_type=type_hints["api"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument service_role", value=service_role, expected_type=type_hints["service_role"])
            check_type(argname="argument secret_store", value=secret_store, expected_type=type_hints["secret_store"])
            check_type(argname="argument serverless_cluster", value=serverless_cluster, expected_type=type_hints["serverless_cluster"])
            check_type(argname="argument database_name", value=database_name, expected_type=type_hints["database_name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "api": api,
            "secret_store": secret_store,
            "serverless_cluster": serverless_cluster,
        }
        if description is not None:
            self._values["description"] = description
        if name is not None:
            self._values["name"] = name
        if service_role is not None:
            self._values["service_role"] = service_role
        if database_name is not None:
            self._values["database_name"] = database_name

    @builtins.property
    def api(self) -> IGraphqlApi:
        '''(experimental) The API to attach this data source to.

        :stability: experimental
        '''
        result = self._values.get("api")
        assert result is not None, "Required property 'api' is missing"
        return typing.cast(IGraphqlApi, result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''(experimental) the description of the data source.

        :default: - None

        :stability: experimental
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''(experimental) The name of the data source.

        :default: - id of data source

        :stability: experimental
        '''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def service_role(self) -> typing.Optional[_aws_cdk_aws_iam_ceddda9d.IRole]:
        '''(experimental) The IAM service role to be assumed by AppSync to interact with the data source.

        :default: - Create a new role

        :stability: experimental
        '''
        result = self._values.get("service_role")
        return typing.cast(typing.Optional[_aws_cdk_aws_iam_ceddda9d.IRole], result)

    @builtins.property
    def secret_store(self) -> _aws_cdk_aws_secretsmanager_ceddda9d.ISecret:
        '''(experimental) The secret containing the credentials for the database.

        :stability: experimental
        '''
        result = self._values.get("secret_store")
        assert result is not None, "Required property 'secret_store' is missing"
        return typing.cast(_aws_cdk_aws_secretsmanager_ceddda9d.ISecret, result)

    @builtins.property
    def serverless_cluster(self) -> _aws_cdk_aws_rds_ceddda9d.IServerlessCluster:
        '''(experimental) The serverless cluster to call to interact with this data source.

        :stability: experimental
        '''
        result = self._values.get("serverless_cluster")
        assert result is not None, "Required property 'serverless_cluster' is missing"
        return typing.cast(_aws_cdk_aws_rds_ceddda9d.IServerlessCluster, result)

    @builtins.property
    def database_name(self) -> typing.Optional[builtins.str]:
        '''(experimental) The name of the database to use within the cluster.

        :default: - None

        :stability: experimental
        '''
        result = self._values.get("database_name")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "RdsDataSourceProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GraphqlApi(
    GraphqlApiBase,
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/aws-appsync-alpha.GraphqlApi",
):
    '''(experimental) An AppSync GraphQL API.

    :stability: experimental
    :resource: AWS::AppSync::GraphQLApi
    :exampleMetadata: infused

    Example::

        api = appsync.GraphqlApi(self, "api",
            name="api",
            schema=appsync.SchemaFile.from_asset(path.join(__dirname, "schema.graphql"))
        )
        
        http_ds = api.add_http_data_source("ds", "https://states.amazonaws.com",
            name="httpDsWithStepF",
            description="from appsync to StepFunctions Workflow",
            authorization_config=appsync.AwsIamConfig(
                signing_region="us-east-1",
                signing_service_name="states"
            )
        )
        
        http_ds.create_resolver("MutationCallStepFunctionResolver",
            type_name="Mutation",
            field_name="callStepFunction",
            request_mapping_template=appsync.MappingTemplate.from_file("request.vtl"),
            response_mapping_template=appsync.MappingTemplate.from_file("response.vtl")
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        name: builtins.str,
        schema: ISchema,
        authorization_config: typing.Optional[typing.Union[AuthorizationConfig, typing.Dict[builtins.str, typing.Any]]] = None,
        domain_name: typing.Optional[typing.Union[DomainOptions, typing.Dict[builtins.str, typing.Any]]] = None,
        log_config: typing.Optional[typing.Union[LogConfig, typing.Dict[builtins.str, typing.Any]]] = None,
        xray_enabled: typing.Optional[builtins.bool] = None,
    ) -> None:
        '''
        :param scope: -
        :param id: -
        :param name: (experimental) the name of the GraphQL API.
        :param schema: (experimental) GraphQL schema definition. Specify how you want to define your schema. Schema.fromFile(filePath: string) allows schema definition through schema.graphql file Default: - schema will be generated code-first (i.e. addType, addObjectType, etc.)
        :param authorization_config: (experimental) Optional authorization configuration. Default: - API Key authorization
        :param domain_name: (experimental) The domain name configuration for the GraphQL API. The Route 53 hosted zone and CName DNS record must be configured in addition to this setting to enable custom domain URL Default: - no domain name
        :param log_config: (experimental) Logging configuration for this api. Default: - None
        :param xray_enabled: (experimental) A flag indicating whether or not X-Ray tracing is enabled for the GraphQL API. Default: - false

        :stability: experimental
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f8b18a8cc4d2899a6d0d8dd903405cccc750b7182af52e05a112055caab54323)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = GraphqlApiProps(
            name=name,
            schema=schema,
            authorization_config=authorization_config,
            domain_name=domain_name,
            log_config=log_config,
            xray_enabled=xray_enabled,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="fromGraphqlApiAttributes")
    @builtins.classmethod
    def from_graphql_api_attributes(
        cls,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        graphql_api_id: builtins.str,
        graphql_api_arn: typing.Optional[builtins.str] = None,
    ) -> IGraphqlApi:
        '''(experimental) Import a GraphQL API through this function.

        :param scope: scope.
        :param id: id.
        :param graphql_api_id: (experimental) an unique AWS AppSync GraphQL API identifier i.e. 'lxz775lwdrgcndgz3nurvac7oa'.
        :param graphql_api_arn: (experimental) the arn for the GraphQL Api. Default: - autogenerated arn

        :stability: experimental
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3a1b85d763f970b08c47edcdb144ff6d2faa3e2f836aa6961393d0b94359486c)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        attrs = GraphqlApiAttributes(
            graphql_api_id=graphql_api_id, graphql_api_arn=graphql_api_arn
        )

        return typing.cast(IGraphqlApi, jsii.sinvoke(cls, "fromGraphqlApiAttributes", [scope, id, attrs]))

    @jsii.member(jsii_name="addSchemaDependency")
    def add_schema_dependency(
        self,
        construct: _aws_cdk_ceddda9d.CfnResource,
    ) -> builtins.bool:
        '''(experimental) Add schema dependency to a given construct.

        :param construct: the dependee.

        :stability: experimental
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8d21ee92559eb3c98ba1905c4583d60dc0e84a92792abdeb13808e656ea72b50)
            check_type(argname="argument construct", value=construct, expected_type=type_hints["construct"])
        return typing.cast(builtins.bool, jsii.invoke(self, "addSchemaDependency", [construct]))

    @jsii.member(jsii_name="grant")
    def grant(
        self,
        grantee: _aws_cdk_aws_iam_ceddda9d.IGrantable,
        resources: IamResource,
        *actions: builtins.str,
    ) -> _aws_cdk_aws_iam_ceddda9d.Grant:
        '''(experimental) Adds an IAM policy statement associated with this GraphQLApi to an IAM principal's policy.

        :param grantee: The principal.
        :param resources: The set of resources to allow (i.e. ...:[region]:[accountId]:apis/GraphQLId/...).
        :param actions: The actions that should be granted to the principal (i.e. appsync:graphql ).

        :stability: experimental
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4c8d4a71d630c4b7db90a176f24f5f34deeab1f4505e2299ac642a83cf7886f0)
            check_type(argname="argument grantee", value=grantee, expected_type=type_hints["grantee"])
            check_type(argname="argument resources", value=resources, expected_type=type_hints["resources"])
            check_type(argname="argument actions", value=actions, expected_type=typing.Tuple[type_hints["actions"], ...]) # pyright: ignore [reportGeneralTypeIssues]
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.Grant, jsii.invoke(self, "grant", [grantee, resources, *actions]))

    @jsii.member(jsii_name="grantMutation")
    def grant_mutation(
        self,
        grantee: _aws_cdk_aws_iam_ceddda9d.IGrantable,
        *fields: builtins.str,
    ) -> _aws_cdk_aws_iam_ceddda9d.Grant:
        '''(experimental) Adds an IAM policy statement for Mutation access to this GraphQLApi to an IAM principal's policy.

        :param grantee: The principal.
        :param fields: The fields to grant access to that are Mutations (leave blank for all).

        :stability: experimental
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__387839a5a4accbd64ca63b01545c6df90b15ce90cceb3444c5ee501a0815d822)
            check_type(argname="argument grantee", value=grantee, expected_type=type_hints["grantee"])
            check_type(argname="argument fields", value=fields, expected_type=typing.Tuple[type_hints["fields"], ...]) # pyright: ignore [reportGeneralTypeIssues]
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.Grant, jsii.invoke(self, "grantMutation", [grantee, *fields]))

    @jsii.member(jsii_name="grantQuery")
    def grant_query(
        self,
        grantee: _aws_cdk_aws_iam_ceddda9d.IGrantable,
        *fields: builtins.str,
    ) -> _aws_cdk_aws_iam_ceddda9d.Grant:
        '''(experimental) Adds an IAM policy statement for Query access to this GraphQLApi to an IAM principal's policy.

        :param grantee: The principal.
        :param fields: The fields to grant access to that are Queries (leave blank for all).

        :stability: experimental
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f529b1bc2c013645370f8581f23f56f18c9f5cf7dbeee130158821911d80eb8a)
            check_type(argname="argument grantee", value=grantee, expected_type=type_hints["grantee"])
            check_type(argname="argument fields", value=fields, expected_type=typing.Tuple[type_hints["fields"], ...]) # pyright: ignore [reportGeneralTypeIssues]
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.Grant, jsii.invoke(self, "grantQuery", [grantee, *fields]))

    @jsii.member(jsii_name="grantSubscription")
    def grant_subscription(
        self,
        grantee: _aws_cdk_aws_iam_ceddda9d.IGrantable,
        *fields: builtins.str,
    ) -> _aws_cdk_aws_iam_ceddda9d.Grant:
        '''(experimental) Adds an IAM policy statement for Subscription access to this GraphQLApi to an IAM principal's policy.

        :param grantee: The principal.
        :param fields: The fields to grant access to that are Subscriptions (leave blank for all).

        :stability: experimental
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a35b53268db32b815084bb4924ac2592e097fcb15dde03629e2be24f7c3ce019)
            check_type(argname="argument grantee", value=grantee, expected_type=type_hints["grantee"])
            check_type(argname="argument fields", value=fields, expected_type=typing.Tuple[type_hints["fields"], ...]) # pyright: ignore [reportGeneralTypeIssues]
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.Grant, jsii.invoke(self, "grantSubscription", [grantee, *fields]))

    @builtins.property
    @jsii.member(jsii_name="apiId")
    def api_id(self) -> builtins.str:
        '''(experimental) an unique AWS AppSync GraphQL API identifier i.e. 'lxz775lwdrgcndgz3nurvac7oa'.

        :stability: experimental
        '''
        return typing.cast(builtins.str, jsii.get(self, "apiId"))

    @builtins.property
    @jsii.member(jsii_name="appSyncDomainName")
    def app_sync_domain_name(self) -> builtins.str:
        '''(experimental) The AppSyncDomainName of the associated custom domain.

        :stability: experimental
        '''
        return typing.cast(builtins.str, jsii.get(self, "appSyncDomainName"))

    @builtins.property
    @jsii.member(jsii_name="arn")
    def arn(self) -> builtins.str:
        '''(experimental) the ARN of the API.

        :stability: experimental
        '''
        return typing.cast(builtins.str, jsii.get(self, "arn"))

    @builtins.property
    @jsii.member(jsii_name="graphqlUrl")
    def graphql_url(self) -> builtins.str:
        '''(experimental) the URL of the endpoint created by AppSync.

        :stability: experimental
        :attribute: GraphQlUrl
        '''
        return typing.cast(builtins.str, jsii.get(self, "graphqlUrl"))

    @builtins.property
    @jsii.member(jsii_name="logGroup")
    def log_group(self) -> _aws_cdk_aws_logs_ceddda9d.ILogGroup:
        '''(experimental) the CloudWatch Log Group for this API.

        :stability: experimental
        '''
        return typing.cast(_aws_cdk_aws_logs_ceddda9d.ILogGroup, jsii.get(self, "logGroup"))

    @builtins.property
    @jsii.member(jsii_name="modes")
    def modes(self) -> typing.List[AuthorizationType]:
        '''(experimental) The Authorization Types for this GraphQL Api.

        :stability: experimental
        '''
        return typing.cast(typing.List[AuthorizationType], jsii.get(self, "modes"))

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        '''(experimental) the name of the API.

        :stability: experimental
        '''
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @builtins.property
    @jsii.member(jsii_name="schema")
    def schema(self) -> ISchema:
        '''(experimental) the schema attached to this api.

        :stability: experimental
        '''
        return typing.cast(ISchema, jsii.get(self, "schema"))

    @builtins.property
    @jsii.member(jsii_name="apiKey")
    def api_key(self) -> typing.Optional[builtins.str]:
        '''(experimental) the configured API key, if present.

        :default: - no api key

        :stability: experimental
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "apiKey"))


__all__ = [
    "ApiKeyConfig",
    "AppsyncFunction",
    "AppsyncFunctionAttributes",
    "AppsyncFunctionProps",
    "Assign",
    "AttributeValues",
    "AttributeValuesStep",
    "AuthorizationConfig",
    "AuthorizationMode",
    "AuthorizationType",
    "AwsIamConfig",
    "BackedDataSource",
    "BackedDataSourceProps",
    "BaseAppsyncFunctionProps",
    "BaseDataSource",
    "BaseDataSourceProps",
    "BaseResolverProps",
    "CachingConfig",
    "DataSourceOptions",
    "DomainOptions",
    "DynamoDbDataSource",
    "DynamoDbDataSourceProps",
    "ElasticsearchDataSource",
    "ElasticsearchDataSourceProps",
    "ExtendedDataSourceProps",
    "ExtendedResolverProps",
    "FieldLogLevel",
    "GraphqlApi",
    "GraphqlApiAttributes",
    "GraphqlApiBase",
    "GraphqlApiProps",
    "HttpDataSource",
    "HttpDataSourceOptions",
    "HttpDataSourceProps",
    "IAppsyncFunction",
    "IGraphqlApi",
    "ISchema",
    "ISchemaConfig",
    "IamResource",
    "KeyCondition",
    "LambdaAuthorizerConfig",
    "LambdaDataSource",
    "LambdaDataSourceProps",
    "LogConfig",
    "MappingTemplate",
    "NoneDataSource",
    "NoneDataSourceProps",
    "OpenIdConnectConfig",
    "OpenSearchDataSource",
    "OpenSearchDataSourceProps",
    "PartitionKey",
    "PartitionKeyStep",
    "PrimaryKey",
    "RdsDataSource",
    "RdsDataSourceProps",
    "Resolver",
    "ResolverProps",
    "SchemaBindOptions",
    "SchemaFile",
    "SchemaProps",
    "SortKeyStep",
    "UserPoolConfig",
    "UserPoolDefaultAction",
    "Values",
]

publication.publish()

def _typecheckingstub__a3b49a22fd22a3a67a8ef82fe9f7e42c6334bcdce794d96bb3fd399270c6bf22(
    *,
    description: typing.Optional[builtins.str] = None,
    expires: typing.Optional[_aws_cdk_ceddda9d.Expiration] = None,
    name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__143ac0b9b860d1ddfeac07bd7a8f178e8d8775fd8b64f5ab612b5e2afc10aa7b(
    *,
    function_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1b6d95b57768d71a938baa5b03f2059496ebd7ea514ade00f491018a3cf6b38f(
    attr: builtins.str,
    arg: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b956087c555a29842faba7ca34342da4c651120110854b50e76f77eaba7d9fee(
    map: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3a415b2a5f94a53c2e175bcb6c745edf9e25b58de67d004bfa0b7a186236b3aa(
    container: builtins.str,
    assignments: typing.Optional[typing.Sequence[Assign]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b30aadf8e36dc621a4e5768f51bda7a879edcb854b3eda7b03f39d6b26bad17c(
    attr: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bb1677701427a21638e46fb1fe64a75c996ccd57ff8bdd9d80e1323d16015aea(
    attr: builtins.str,
    container: builtins.str,
    assignments: typing.Sequence[Assign],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cedcb433c4c0e028a47d72ef53e8659972c4eedf4df86504e61097654f716506(
    val: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__072ee2d208cf787904aca8fab9d6d5adea904fbaafa9053ba7e1144bbe49a1d1(
    *,
    additional_authorization_modes: typing.Optional[typing.Sequence[typing.Union[AuthorizationMode, typing.Dict[builtins.str, typing.Any]]]] = None,
    default_authorization: typing.Optional[typing.Union[AuthorizationMode, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f3349010ec6e7e227bfbf74f157ec83c8752b9ac70a93f3b9ef045558ab8cc3a(
    *,
    authorization_type: AuthorizationType,
    api_key_config: typing.Optional[typing.Union[ApiKeyConfig, typing.Dict[builtins.str, typing.Any]]] = None,
    lambda_authorizer_config: typing.Optional[typing.Union[LambdaAuthorizerConfig, typing.Dict[builtins.str, typing.Any]]] = None,
    open_id_connect_config: typing.Optional[typing.Union[OpenIdConnectConfig, typing.Dict[builtins.str, typing.Any]]] = None,
    user_pool_config: typing.Optional[typing.Union[UserPoolConfig, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d1415d5dc4ff285ee5d54e74f7f22a7ed36988d11435b4fafd907c540d98d742(
    *,
    signing_region: builtins.str,
    signing_service_name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d93e8cab7d8bd9de61fc51911cddaf5a17946653da71d37056a44550b0a84387(
    *,
    name: builtins.str,
    description: typing.Optional[builtins.str] = None,
    request_mapping_template: typing.Optional[MappingTemplate] = None,
    response_mapping_template: typing.Optional[MappingTemplate] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__230d9ab3d2c96a0794535e1481ac98d0795f10ceaed29ae16702d9cb6748b189(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    props: typing.Union[BackedDataSourceProps, typing.Dict[builtins.str, typing.Any]],
    *,
    type: builtins.str,
    dynamo_db_config: typing.Optional[typing.Union[typing.Union[_aws_cdk_aws_appsync_ceddda9d.CfnDataSource.DynamoDBConfigProperty, typing.Dict[builtins.str, typing.Any]], _aws_cdk_ceddda9d.IResolvable]] = None,
    elasticsearch_config: typing.Optional[typing.Union[typing.Union[_aws_cdk_aws_appsync_ceddda9d.CfnDataSource.ElasticsearchConfigProperty, typing.Dict[builtins.str, typing.Any]], _aws_cdk_ceddda9d.IResolvable]] = None,
    http_config: typing.Optional[typing.Union[typing.Union[_aws_cdk_aws_appsync_ceddda9d.CfnDataSource.HttpConfigProperty, typing.Dict[builtins.str, typing.Any]], _aws_cdk_ceddda9d.IResolvable]] = None,
    lambda_config: typing.Optional[typing.Union[typing.Union[_aws_cdk_aws_appsync_ceddda9d.CfnDataSource.LambdaConfigProperty, typing.Dict[builtins.str, typing.Any]], _aws_cdk_ceddda9d.IResolvable]] = None,
    open_search_service_config: typing.Optional[typing.Union[typing.Union[_aws_cdk_aws_appsync_ceddda9d.CfnDataSource.OpenSearchServiceConfigProperty, typing.Dict[builtins.str, typing.Any]], _aws_cdk_ceddda9d.IResolvable]] = None,
    relational_database_config: typing.Optional[typing.Union[typing.Union[_aws_cdk_aws_appsync_ceddda9d.CfnDataSource.RelationalDatabaseConfigProperty, typing.Dict[builtins.str, typing.Any]], _aws_cdk_ceddda9d.IResolvable]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6ec867efbcdaffdbb6b832d4eb07531ba4093e9678029b86b16528ad6a61f89b(
    id: builtins.str,
    *,
    name: builtins.str,
    description: typing.Optional[builtins.str] = None,
    request_mapping_template: typing.Optional[MappingTemplate] = None,
    response_mapping_template: typing.Optional[MappingTemplate] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a95dbdc6dd3fef41be042eb94e18a28c05f4ad7e9e9bd81749248f7a3076b0f1(
    id: builtins.str,
    *,
    field_name: builtins.str,
    type_name: builtins.str,
    caching_config: typing.Optional[typing.Union[CachingConfig, typing.Dict[builtins.str, typing.Any]]] = None,
    max_batch_size: typing.Optional[jsii.Number] = None,
    pipeline_config: typing.Optional[typing.Sequence[IAppsyncFunction]] = None,
    request_mapping_template: typing.Optional[MappingTemplate] = None,
    response_mapping_template: typing.Optional[MappingTemplate] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7d09ed5dcda77685d77b0b66879b9fe85a162b99036c9b19fdb07c18de061fe6(
    value: IGraphqlApi,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cccc9facb1cc9a3256ee2aa3a69d4a8231537882e991e26308994c2fa99ee141(
    value: typing.Optional[_aws_cdk_aws_iam_ceddda9d.IRole],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cc7c7973c849c1142cbbf9c779179a1a713a542a3c5bfb4e907ece94b1dcf339(
    *,
    api: IGraphqlApi,
    description: typing.Optional[builtins.str] = None,
    name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1247604f97a7e79118f8e17cbadbbd5727fb645bf9880b1e91f1f0731da521ff(
    *,
    field_name: builtins.str,
    type_name: builtins.str,
    caching_config: typing.Optional[typing.Union[CachingConfig, typing.Dict[builtins.str, typing.Any]]] = None,
    max_batch_size: typing.Optional[jsii.Number] = None,
    pipeline_config: typing.Optional[typing.Sequence[IAppsyncFunction]] = None,
    request_mapping_template: typing.Optional[MappingTemplate] = None,
    response_mapping_template: typing.Optional[MappingTemplate] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__24bbe35162b5b4ead5d7cdba050bb2ab9f017c763245480227a2f816d53294d2(
    *,
    ttl: _aws_cdk_ceddda9d.Duration,
    caching_keys: typing.Optional[typing.Sequence[builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5d4872a33bcd7830c8e9ba05ba045a2dc10b6926f77aac1bbee29fb9dfa4510b(
    *,
    description: typing.Optional[builtins.str] = None,
    name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__eeded7b0dde6896a11d8a28127d0d2002269687de25559c00d05be06499990d7(
    *,
    certificate: _aws_cdk_aws_certificatemanager_ceddda9d.ICertificate,
    domain_name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c317114b1e4283481b6e478cbf1b446de4e66b3f8e6e74c9df7ce3f0215cb6ca(
    *,
    type: builtins.str,
    dynamo_db_config: typing.Optional[typing.Union[typing.Union[_aws_cdk_aws_appsync_ceddda9d.CfnDataSource.DynamoDBConfigProperty, typing.Dict[builtins.str, typing.Any]], _aws_cdk_ceddda9d.IResolvable]] = None,
    elasticsearch_config: typing.Optional[typing.Union[typing.Union[_aws_cdk_aws_appsync_ceddda9d.CfnDataSource.ElasticsearchConfigProperty, typing.Dict[builtins.str, typing.Any]], _aws_cdk_ceddda9d.IResolvable]] = None,
    http_config: typing.Optional[typing.Union[typing.Union[_aws_cdk_aws_appsync_ceddda9d.CfnDataSource.HttpConfigProperty, typing.Dict[builtins.str, typing.Any]], _aws_cdk_ceddda9d.IResolvable]] = None,
    lambda_config: typing.Optional[typing.Union[typing.Union[_aws_cdk_aws_appsync_ceddda9d.CfnDataSource.LambdaConfigProperty, typing.Dict[builtins.str, typing.Any]], _aws_cdk_ceddda9d.IResolvable]] = None,
    open_search_service_config: typing.Optional[typing.Union[typing.Union[_aws_cdk_aws_appsync_ceddda9d.CfnDataSource.OpenSearchServiceConfigProperty, typing.Dict[builtins.str, typing.Any]], _aws_cdk_ceddda9d.IResolvable]] = None,
    relational_database_config: typing.Optional[typing.Union[typing.Union[_aws_cdk_aws_appsync_ceddda9d.CfnDataSource.RelationalDatabaseConfigProperty, typing.Dict[builtins.str, typing.Any]], _aws_cdk_ceddda9d.IResolvable]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__03f1147a0c345927a67b86638d192631cbb3ebb7cf920f9116c64ab461d319e3(
    *,
    field_name: builtins.str,
    type_name: builtins.str,
    caching_config: typing.Optional[typing.Union[CachingConfig, typing.Dict[builtins.str, typing.Any]]] = None,
    max_batch_size: typing.Optional[jsii.Number] = None,
    pipeline_config: typing.Optional[typing.Sequence[IAppsyncFunction]] = None,
    request_mapping_template: typing.Optional[MappingTemplate] = None,
    response_mapping_template: typing.Optional[MappingTemplate] = None,
    data_source: typing.Optional[BaseDataSource] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b955959104b2f3e9d432c1b7e9ba97a97d7ccc986380a56840ca2758111ef604(
    *,
    graphql_api_id: builtins.str,
    graphql_api_arn: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2ae7ca336b2b5866de05582f2dd15607c59c1dd91c84b9220160e01b90f87e94(
    *,
    name: builtins.str,
    schema: ISchema,
    authorization_config: typing.Optional[typing.Union[AuthorizationConfig, typing.Dict[builtins.str, typing.Any]]] = None,
    domain_name: typing.Optional[typing.Union[DomainOptions, typing.Dict[builtins.str, typing.Any]]] = None,
    log_config: typing.Optional[typing.Union[LogConfig, typing.Dict[builtins.str, typing.Any]]] = None,
    xray_enabled: typing.Optional[builtins.bool] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9871a67ca2dd2cf444a8b2cfbe0b1832a07ef45ea81c443c282b11e117b4d7c7(
    *,
    description: typing.Optional[builtins.str] = None,
    name: typing.Optional[builtins.str] = None,
    authorization_config: typing.Optional[typing.Union[AwsIamConfig, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__89dc282ac92a5f3d2f4eca5d3d197e40ce4abe4440127160825a934090a73b07(
    *,
    api: IGraphqlApi,
    description: typing.Optional[builtins.str] = None,
    name: typing.Optional[builtins.str] = None,
    endpoint: builtins.str,
    authorization_config: typing.Optional[typing.Union[AwsIamConfig, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ff2ae55f5180f89ed93ef13fa0c7ecceb1eb90bee7521aa97617041f0a549e9b(
    id: builtins.str,
    table: _aws_cdk_aws_dynamodb_ceddda9d.ITable,
    *,
    description: typing.Optional[builtins.str] = None,
    name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e0a7a045a50e105c29fbe85eecdc85bf5e477b5ca2830d524cd42de5b8c50a35(
    id: builtins.str,
    domain: _aws_cdk_aws_elasticsearch_ceddda9d.IDomain,
    *,
    description: typing.Optional[builtins.str] = None,
    name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fc508a77d0bf87c350f1e50bf16ddcf8f2b1edf36752e9a6a5759912e0ef7025(
    id: builtins.str,
    endpoint: builtins.str,
    *,
    authorization_config: typing.Optional[typing.Union[AwsIamConfig, typing.Dict[builtins.str, typing.Any]]] = None,
    description: typing.Optional[builtins.str] = None,
    name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b09472740cf51bd70588a88680d9e9bfb0c43e6ce6829eaa7db6719cc888de29(
    id: builtins.str,
    lambda_function: _aws_cdk_aws_lambda_ceddda9d.IFunction,
    *,
    description: typing.Optional[builtins.str] = None,
    name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5b4d3c2f5386ab847f1317af811d59fbbda87fe916d2a4f6bbd35a3458a91a76(
    id: builtins.str,
    *,
    description: typing.Optional[builtins.str] = None,
    name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__99b1759e6e50fc3fb6c0cc4ecee7445d98d908aa6aecd0041d548db46f72ffb9(
    id: builtins.str,
    domain: _aws_cdk_aws_opensearchservice_ceddda9d.IDomain,
    *,
    description: typing.Optional[builtins.str] = None,
    name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__78791ea5025839853c0dcfdb18166f833bba60087b82eb17c8afa2f9302901f9(
    id: builtins.str,
    serverless_cluster: _aws_cdk_aws_rds_ceddda9d.IServerlessCluster,
    secret_store: _aws_cdk_aws_secretsmanager_ceddda9d.ISecret,
    database_name: typing.Optional[builtins.str] = None,
    *,
    description: typing.Optional[builtins.str] = None,
    name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7fd621ea81eec4c759f3ef88dd4c25efb275910cdc93e28e795c91bcee871626(
    construct: _aws_cdk_ceddda9d.CfnResource,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d950aad73fe8c1264ecd6c12999cf8fa3c2aee009208495b4eed8e1693d34916(
    id: builtins.str,
    *,
    data_source: typing.Optional[BaseDataSource] = None,
    field_name: builtins.str,
    type_name: builtins.str,
    caching_config: typing.Optional[typing.Union[CachingConfig, typing.Dict[builtins.str, typing.Any]]] = None,
    max_batch_size: typing.Optional[jsii.Number] = None,
    pipeline_config: typing.Optional[typing.Sequence[IAppsyncFunction]] = None,
    request_mapping_template: typing.Optional[MappingTemplate] = None,
    response_mapping_template: typing.Optional[MappingTemplate] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__dd4d10a0673d71595a61dc4bb10b344bca207d9a1006f2fbdeb9dae0dc415813(
    api: IGraphqlApi,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bb8546d484aa114efdb76ea1c5936dd17700b77edd7fe05d087febc1a2124f9d(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__59fbd981dd279d0e7e3eeb7b1ef47a81c7b418737ff11744afeae2d4988e32a2(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c6f60e3a1ac4741bd3c425e40094fe5f56ea9ccde593a2913b08ff83c5c218d5(
    *arns: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d713a6dda131c90c74621df3df92e7fa8a68fb94973c2211649b62def0b137f9(
    type: builtins.str,
    *fields: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__23e87d2e18ac29ea314572a6b768d884ac9ad9bc4e883dcd1d62a41834bea3ea(
    api: GraphqlApi,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__249d661d83f55f407b240686349b23c6481909b60d2f14ff74045e4d25a3cf6c(
    key_name: builtins.str,
    arg: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cf4b6c447afa94150fb522751b30ac92d849a8e075eeeb8bd8e5aa248411b2c1(
    key_name: builtins.str,
    arg1: builtins.str,
    arg2: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b94e5f52a19e49dfd1f6583a49cdc85f11d062218e64487e88c721d13a24db6b(
    key_name: builtins.str,
    arg: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d44bcbcfc6e10e5782ed664f9ae213b2c3dbb20dc50ff985e70af6adba1f26f0(
    key_name: builtins.str,
    arg: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__48446eaa70b45f70cb39edb4ec644179feba91a0a515c80b62c8973f2ce475dd(
    key_name: builtins.str,
    arg: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__eed64948103f5281dc8a58c4065e9929af45a55da65267c27869535ba74eeb46(
    key_name: builtins.str,
    arg: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c8475f31ba6af44ec7922d2131bf0a584363b40658ba03fe3bff16afba1eb653(
    key_name: builtins.str,
    arg: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b1f5b233c3377890d5e80a80088da68fbd8868df7ad5fa1cbe3f77c0f9f68481(
    key_cond: KeyCondition,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__337672240ca00d046f3802c4ae541ca278b767ffd2ef146e4643d9de023bd497(
    *,
    handler: _aws_cdk_aws_lambda_ceddda9d.IFunction,
    results_cache_ttl: typing.Optional[_aws_cdk_ceddda9d.Duration] = None,
    validation_regex: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__36317ddb5cfa6740a1e01acd100fb65164ebf89c8241e5d73c276c30f0948284(
    *,
    exclude_verbose_content: typing.Optional[typing.Union[builtins.bool, _aws_cdk_ceddda9d.IResolvable]] = None,
    field_log_level: typing.Optional[FieldLogLevel] = None,
    retention: typing.Optional[_aws_cdk_aws_logs_ceddda9d.RetentionDays] = None,
    role: typing.Optional[_aws_cdk_aws_iam_ceddda9d.IRole] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2bbbc24defe1ead1c5d593f8a96a090ffc053476513612cafa21ea0f3d28bd90(
    key_name: builtins.str,
    id_arg: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__88f230adbd2614b0171120a1a8527fd1a1e6c693193302dd2fbdf007cc81c53a(
    key_name: builtins.str,
    id_arg: builtins.str,
    consistent_read: typing.Optional[builtins.bool] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__80a975a5fc43dfb3faea0329aacb1fff0deb5d5dc2c4d915b316bc62272b280f(
    key: PrimaryKey,
    values: AttributeValues,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a72ae026d9b26589761269f103be4ab5e54045463bc3e81ba28fc53fba600985(
    cond: KeyCondition,
    index_name: typing.Optional[builtins.str] = None,
    consistent_read: typing.Optional[builtins.bool] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b3041c1fcc301d4fc26400649d89043d6f95853ec04e917e1af73e30e82280e5(
    consistent_read: typing.Optional[builtins.bool] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ebe69081dff043b43090319e95b83f4481413f1f86322c327fab1f7c44bccf38(
    file_name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__25f5e91db3a6dbc5b261f20cc5f8dbf06bbc2ae0f3e8c13feade8fc27473d834(
    template: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e7c6788a8a901e91d9597c87d05bbc2a8e7dae237778c02046c9477b51d2ac68(
    payload: typing.Optional[builtins.str] = None,
    operation: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9c01b452aae5d4fe43a1776547ba3ab36167d802faf716669cb664fbd4d61044(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    api: IGraphqlApi,
    description: typing.Optional[builtins.str] = None,
    name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c9bb8be0e14e063d89233a7c97225ce92a2a4996f23bf770cc677eca7ecf5bd5(
    *,
    api: IGraphqlApi,
    description: typing.Optional[builtins.str] = None,
    name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8b878562c2013c394e2633ff6318afd2a12cf83b22e9dd30c04af54c1576a197(
    *,
    oidc_provider: builtins.str,
    client_id: typing.Optional[builtins.str] = None,
    token_expiry_from_auth: typing.Optional[jsii.Number] = None,
    token_expiry_from_issue: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a1fba092401cd01d508bb92a007d1f1a73f24d2b8c5dbe573357db4b2f7ee073(
    key: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a99a744b2615c70db51e7e97f7a78bebcda8333da4a1c53d8b9da8256681c5d3(
    val: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__04f1b1f314b8748cf24e4dd79c346b1eaba199a34d9d062703427899a303de05(
    pkey: Assign,
    skey: typing.Optional[Assign] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d0724c26db7323c3293b63cc0b59f3db0d2568df2cfb8a1ed43d6cd084b14a9b(
    key: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__16fda65d626ad085d09ff6eb0a22ed286fb1d2d616cc1f9585a4a0da9284e27d(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    api: IGraphqlApi,
    data_source: typing.Optional[BaseDataSource] = None,
    field_name: builtins.str,
    type_name: builtins.str,
    caching_config: typing.Optional[typing.Union[CachingConfig, typing.Dict[builtins.str, typing.Any]]] = None,
    max_batch_size: typing.Optional[jsii.Number] = None,
    pipeline_config: typing.Optional[typing.Sequence[IAppsyncFunction]] = None,
    request_mapping_template: typing.Optional[MappingTemplate] = None,
    response_mapping_template: typing.Optional[MappingTemplate] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0544034ffa38a1349f4df5068fc81a07e076e8e79912d653716af3085b44950c(
    *,
    field_name: builtins.str,
    type_name: builtins.str,
    caching_config: typing.Optional[typing.Union[CachingConfig, typing.Dict[builtins.str, typing.Any]]] = None,
    max_batch_size: typing.Optional[jsii.Number] = None,
    pipeline_config: typing.Optional[typing.Sequence[IAppsyncFunction]] = None,
    request_mapping_template: typing.Optional[MappingTemplate] = None,
    response_mapping_template: typing.Optional[MappingTemplate] = None,
    data_source: typing.Optional[BaseDataSource] = None,
    api: IGraphqlApi,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__90c6507328fd41f3320f52fac14454c95e67b3606153a65102df6f21b7cc1a3b(
    file_path: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__18f56bb1836a4289e7269271f0246c6611c7c56847cbf623482019852eacc689(
    api: IGraphqlApi,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__76feb135877e53281f9ff4edf266df32e0dcd1820ef716bb01cedec5ec7003df(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__74fb8ec7796991b3d4c9a0ddfefb868ed0e3ac71be7dffbb11827b0f21f8cd20(
    *,
    file_path: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7521a793cdf36117708b84d1a01bef63160ade233906dd87f3d03f02bcd1ba6e(
    pkey: Assign,
    skey: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f28f5c9bacf653797e54b516bde341e12edee2e096290d0fcf35116bd7eb3313(
    val: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c0d45a53d3fc953aeaa93f0fe0dd8bedea69cba522adb8a9f611beae1c994767(
    *,
    user_pool: _aws_cdk_aws_cognito_ceddda9d.IUserPool,
    app_id_client_regex: typing.Optional[builtins.str] = None,
    default_action: typing.Optional[UserPoolDefaultAction] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fce54538d36746cac8ad392ca0efade9f94d7f0380883157e4fb0ec4aec80c1f(
    attr: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2041b7d86db3cf96e0e02fd003ec8df58ac040791ee720cce7fc45baf561ce53(
    arg: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ae4be0c00df7153d2b8df13c5a507f84c55a8fd1dfd654ffb322f8256f585840(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    api: IGraphqlApi,
    data_source: BaseDataSource,
    name: builtins.str,
    description: typing.Optional[builtins.str] = None,
    request_mapping_template: typing.Optional[MappingTemplate] = None,
    response_mapping_template: typing.Optional[MappingTemplate] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1d0577f3d312e5fa22c00353e17621d8c61ae169801f29d19726a2040375c8ad(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    function_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__10e97c994200b0a6907d75e73741660033ad46a0451d0480f4bdb955c615ab2a(
    *,
    name: builtins.str,
    description: typing.Optional[builtins.str] = None,
    request_mapping_template: typing.Optional[MappingTemplate] = None,
    response_mapping_template: typing.Optional[MappingTemplate] = None,
    api: IGraphqlApi,
    data_source: BaseDataSource,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__215ea606dd80608e35853c39b5e33223e4130143cd49461615b91a8cf968debe(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    props: typing.Union[BackedDataSourceProps, typing.Dict[builtins.str, typing.Any]],
    *,
    type: builtins.str,
    dynamo_db_config: typing.Optional[typing.Union[typing.Union[_aws_cdk_aws_appsync_ceddda9d.CfnDataSource.DynamoDBConfigProperty, typing.Dict[builtins.str, typing.Any]], _aws_cdk_ceddda9d.IResolvable]] = None,
    elasticsearch_config: typing.Optional[typing.Union[typing.Union[_aws_cdk_aws_appsync_ceddda9d.CfnDataSource.ElasticsearchConfigProperty, typing.Dict[builtins.str, typing.Any]], _aws_cdk_ceddda9d.IResolvable]] = None,
    http_config: typing.Optional[typing.Union[typing.Union[_aws_cdk_aws_appsync_ceddda9d.CfnDataSource.HttpConfigProperty, typing.Dict[builtins.str, typing.Any]], _aws_cdk_ceddda9d.IResolvable]] = None,
    lambda_config: typing.Optional[typing.Union[typing.Union[_aws_cdk_aws_appsync_ceddda9d.CfnDataSource.LambdaConfigProperty, typing.Dict[builtins.str, typing.Any]], _aws_cdk_ceddda9d.IResolvable]] = None,
    open_search_service_config: typing.Optional[typing.Union[typing.Union[_aws_cdk_aws_appsync_ceddda9d.CfnDataSource.OpenSearchServiceConfigProperty, typing.Dict[builtins.str, typing.Any]], _aws_cdk_ceddda9d.IResolvable]] = None,
    relational_database_config: typing.Optional[typing.Union[typing.Union[_aws_cdk_aws_appsync_ceddda9d.CfnDataSource.RelationalDatabaseConfigProperty, typing.Dict[builtins.str, typing.Any]], _aws_cdk_ceddda9d.IResolvable]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ff628c288b521502363745cdded04a14655886e627b77fe903e1b89f3e57881a(
    *,
    api: IGraphqlApi,
    description: typing.Optional[builtins.str] = None,
    name: typing.Optional[builtins.str] = None,
    service_role: typing.Optional[_aws_cdk_aws_iam_ceddda9d.IRole] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9a5b4c2ad4cc545351c4c404fc49eed5884f2dc008a1da2687cbd4f7db51d473(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    table: _aws_cdk_aws_dynamodb_ceddda9d.ITable,
    read_only_access: typing.Optional[builtins.bool] = None,
    use_caller_credentials: typing.Optional[builtins.bool] = None,
    service_role: typing.Optional[_aws_cdk_aws_iam_ceddda9d.IRole] = None,
    api: IGraphqlApi,
    description: typing.Optional[builtins.str] = None,
    name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__00e3da2492e4229a1813c880b1e0fdab70a08ac780ed5c02eb6aa905704a7ccb(
    *,
    api: IGraphqlApi,
    description: typing.Optional[builtins.str] = None,
    name: typing.Optional[builtins.str] = None,
    service_role: typing.Optional[_aws_cdk_aws_iam_ceddda9d.IRole] = None,
    table: _aws_cdk_aws_dynamodb_ceddda9d.ITable,
    read_only_access: typing.Optional[builtins.bool] = None,
    use_caller_credentials: typing.Optional[builtins.bool] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__218b9759a1ea729ae49c472141a2b492b6792f8ce50ab5b261799cbd005ce6e0(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    domain: _aws_cdk_aws_elasticsearch_ceddda9d.IDomain,
    service_role: typing.Optional[_aws_cdk_aws_iam_ceddda9d.IRole] = None,
    api: IGraphqlApi,
    description: typing.Optional[builtins.str] = None,
    name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7ec2ec75d494252faef9e4d153421e666bfca76ca970577a545c41aec7c1c77a(
    *,
    api: IGraphqlApi,
    description: typing.Optional[builtins.str] = None,
    name: typing.Optional[builtins.str] = None,
    service_role: typing.Optional[_aws_cdk_aws_iam_ceddda9d.IRole] = None,
    domain: _aws_cdk_aws_elasticsearch_ceddda9d.IDomain,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__523fe479f81abf8faac00c284f3310629e45647b2a9e37d352a5665b59f803a1(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    account: typing.Optional[builtins.str] = None,
    environment_from_arn: typing.Optional[builtins.str] = None,
    physical_name: typing.Optional[builtins.str] = None,
    region: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__94e2cdd73a175e5019d14e6e050cf81272cc5bba6474743075c9027d864ac5ad(
    id: builtins.str,
    table: _aws_cdk_aws_dynamodb_ceddda9d.ITable,
    *,
    description: typing.Optional[builtins.str] = None,
    name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__486a98cd301c656f17aba987683eb8a1e71c203e3d9347b771ba373ed759e043(
    id: builtins.str,
    domain: _aws_cdk_aws_elasticsearch_ceddda9d.IDomain,
    *,
    description: typing.Optional[builtins.str] = None,
    name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ecfb064c8a50703fb696e4a526e056950219e94519cc179d2a007f4aba247f3f(
    id: builtins.str,
    endpoint: builtins.str,
    *,
    authorization_config: typing.Optional[typing.Union[AwsIamConfig, typing.Dict[builtins.str, typing.Any]]] = None,
    description: typing.Optional[builtins.str] = None,
    name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6bfafbb3d516b6c08eac48f102e5f98eb43be16dae3f7bdeeed708272f7076af(
    id: builtins.str,
    lambda_function: _aws_cdk_aws_lambda_ceddda9d.IFunction,
    *,
    description: typing.Optional[builtins.str] = None,
    name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6a96311b1d2416236de2dd1371bc6f02cf4524b49d862d33d88fe5231ec444e5(
    id: builtins.str,
    *,
    description: typing.Optional[builtins.str] = None,
    name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8c0c1eabe7b9f32d8afd05834ba199b0304ff656eafab6778c21c34c4f283c76(
    id: builtins.str,
    domain: _aws_cdk_aws_opensearchservice_ceddda9d.IDomain,
    *,
    description: typing.Optional[builtins.str] = None,
    name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e7a81701a9320c9569c6bd6e0d17789014c90d63c062ed932f347e6e96126333(
    id: builtins.str,
    serverless_cluster: _aws_cdk_aws_rds_ceddda9d.IServerlessCluster,
    secret_store: _aws_cdk_aws_secretsmanager_ceddda9d.ISecret,
    database_name: typing.Optional[builtins.str] = None,
    *,
    description: typing.Optional[builtins.str] = None,
    name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__33aa2a2e2fcba734874b8074322da06b3200ec4cb04743e0cceb6ced97651b0d(
    construct: _aws_cdk_ceddda9d.CfnResource,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4edf824fbab5e0903a1611680264800f7787642b27370977d8a745c0456324cf(
    id: builtins.str,
    *,
    data_source: typing.Optional[BaseDataSource] = None,
    field_name: builtins.str,
    type_name: builtins.str,
    caching_config: typing.Optional[typing.Union[CachingConfig, typing.Dict[builtins.str, typing.Any]]] = None,
    max_batch_size: typing.Optional[jsii.Number] = None,
    pipeline_config: typing.Optional[typing.Sequence[IAppsyncFunction]] = None,
    request_mapping_template: typing.Optional[MappingTemplate] = None,
    response_mapping_template: typing.Optional[MappingTemplate] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b77d85138e18cad512b96f1db33702b184c66864aadafb6d6d16d71681c6c2de(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    endpoint: builtins.str,
    authorization_config: typing.Optional[typing.Union[AwsIamConfig, typing.Dict[builtins.str, typing.Any]]] = None,
    api: IGraphqlApi,
    description: typing.Optional[builtins.str] = None,
    name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__dd360277d64e788625326cbbc6b23d5a86b71242516093d1f696ad7a6c3c5f5f(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    lambda_function: _aws_cdk_aws_lambda_ceddda9d.IFunction,
    service_role: typing.Optional[_aws_cdk_aws_iam_ceddda9d.IRole] = None,
    api: IGraphqlApi,
    description: typing.Optional[builtins.str] = None,
    name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__09480a84bcca442f2c74291063c22d71becab43f875c393840768e69c982bcb6(
    *,
    api: IGraphqlApi,
    description: typing.Optional[builtins.str] = None,
    name: typing.Optional[builtins.str] = None,
    service_role: typing.Optional[_aws_cdk_aws_iam_ceddda9d.IRole] = None,
    lambda_function: _aws_cdk_aws_lambda_ceddda9d.IFunction,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__806d535b2e5e6649463074cc89d3eef71463bd681270c0e2ec8d67ab9625a112(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    domain: _aws_cdk_aws_opensearchservice_ceddda9d.IDomain,
    service_role: typing.Optional[_aws_cdk_aws_iam_ceddda9d.IRole] = None,
    api: IGraphqlApi,
    description: typing.Optional[builtins.str] = None,
    name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f143aecf12cb9295e34e62376d2a6a103e604c85ca4104c2a2f14472fb83b94d(
    *,
    api: IGraphqlApi,
    description: typing.Optional[builtins.str] = None,
    name: typing.Optional[builtins.str] = None,
    service_role: typing.Optional[_aws_cdk_aws_iam_ceddda9d.IRole] = None,
    domain: _aws_cdk_aws_opensearchservice_ceddda9d.IDomain,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7f8419af2cd92c85cbffe41568b08c3ff0bcdae5f8313824953c6e7ee2b86ca7(
    pkey: Assign,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__03d25dce1ff151406d67cb5e80a8ff6bc8d26cad90e13cb0bbfddf653edc94dd(
    key: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6441252fabcc3030f951bd9c7f24a6d3dd03090d3c8546bf79a7623c540479e4(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    secret_store: _aws_cdk_aws_secretsmanager_ceddda9d.ISecret,
    serverless_cluster: _aws_cdk_aws_rds_ceddda9d.IServerlessCluster,
    database_name: typing.Optional[builtins.str] = None,
    service_role: typing.Optional[_aws_cdk_aws_iam_ceddda9d.IRole] = None,
    api: IGraphqlApi,
    description: typing.Optional[builtins.str] = None,
    name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1e1dbdc39f8e8f411c9d0937bcba223b8f087c4394f648fd455304e646e57743(
    *,
    api: IGraphqlApi,
    description: typing.Optional[builtins.str] = None,
    name: typing.Optional[builtins.str] = None,
    service_role: typing.Optional[_aws_cdk_aws_iam_ceddda9d.IRole] = None,
    secret_store: _aws_cdk_aws_secretsmanager_ceddda9d.ISecret,
    serverless_cluster: _aws_cdk_aws_rds_ceddda9d.IServerlessCluster,
    database_name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f8b18a8cc4d2899a6d0d8dd903405cccc750b7182af52e05a112055caab54323(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    name: builtins.str,
    schema: ISchema,
    authorization_config: typing.Optional[typing.Union[AuthorizationConfig, typing.Dict[builtins.str, typing.Any]]] = None,
    domain_name: typing.Optional[typing.Union[DomainOptions, typing.Dict[builtins.str, typing.Any]]] = None,
    log_config: typing.Optional[typing.Union[LogConfig, typing.Dict[builtins.str, typing.Any]]] = None,
    xray_enabled: typing.Optional[builtins.bool] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3a1b85d763f970b08c47edcdb144ff6d2faa3e2f836aa6961393d0b94359486c(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    graphql_api_id: builtins.str,
    graphql_api_arn: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8d21ee92559eb3c98ba1905c4583d60dc0e84a92792abdeb13808e656ea72b50(
    construct: _aws_cdk_ceddda9d.CfnResource,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4c8d4a71d630c4b7db90a176f24f5f34deeab1f4505e2299ac642a83cf7886f0(
    grantee: _aws_cdk_aws_iam_ceddda9d.IGrantable,
    resources: IamResource,
    *actions: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__387839a5a4accbd64ca63b01545c6df90b15ce90cceb3444c5ee501a0815d822(
    grantee: _aws_cdk_aws_iam_ceddda9d.IGrantable,
    *fields: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f529b1bc2c013645370f8581f23f56f18c9f5cf7dbeee130158821911d80eb8a(
    grantee: _aws_cdk_aws_iam_ceddda9d.IGrantable,
    *fields: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a35b53268db32b815084bb4924ac2592e097fcb15dde03629e2be24f7c3ce019(
    grantee: _aws_cdk_aws_iam_ceddda9d.IGrantable,
    *fields: builtins.str,
) -> None:
    """Type checking stubs"""
    pass
