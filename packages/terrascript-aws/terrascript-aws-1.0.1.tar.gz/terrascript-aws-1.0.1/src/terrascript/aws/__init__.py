__all__ = [
    "rum",
    "lambda_",
    "location",
    "elasticsearch",
    "amp",
    "secretsmanager",
    "keyspaces",
    "codestarnotifications",
    "wavelength",
    "datasync",
    "elastic_beanstalk",
    "redshiftserverless",
    "route53domains",
    "api_gateway",
    "servicecatalog",
    "worklink",
    "ram",
    "codecommit",
    "application_auto_scaling",
    "batch",
    "dms",
    "codedeploy",
    "ebs",
    "ssm",
    "backup",
    "elb",
    "gamelift",
    "vpn",
    "ecrpublic",
    "ce",
    "transfer",
    "securityhub",
    "inspector",
    "dynamodb_accelerator",
    "acmpca",
    "route53_resolver",
    "storagegateway",
    "kinesis",
    "ecr",
    "detective",
    "kinesis_firehose",
    "transcribe",
    "amplify",
    "cognito_identity",
    "vpc_ipam",
    "synthetics",
    "pricing",
    "outposts",
    "sfn",
    "cloudtrail",
    "applicationinsights",
    "cloudcontrolapi",
    "auto_scaling",
    "globalaccelerator",
    "elb_classic",
    "organizations",
    "codeartifact",
    "resourcegroups",
    "schemas",
    "kinesis_video",
    "budgets",
    "eks",
    "s3control",
    "cost_and_usage_report",
    "meta_data_sources",
    "efs",
    "elastictranscoder",
    "lex",
    "cloudfront",
    "chime",
    "apigatewayv2",
    "workspaces",
    "elemental_mediapackage",
    "managed_streaming_for_kafka_connect",
    "s3",
    "config",
    "athena",
    "lakeformation",
    "rolesanywhere",
    "signer",
    "ssoadmin",
    "codebuild",
    "iot",
    "qldb",
    "elasticache",
    "codestarconnections",
    "managed_streaming_for_kafka",
    "route53recoveryreadiness",
    "redshift",
    "cloudhsm",
    "route53recoverycontrolconfig",
    "ec2",
    "servicequotas",
    "route53",
    "ecs",
    "cloudsearch",
    "swf",
    "dlm",
    "serverlessapplicationrepository",
    "fis",
    "pinpoint",
    "x_ray",
    "resourcegroupstagging",
    "rds",
    "cloud9",
    "emrcontainers",
    "cloudformation",
    "dynamodb",
    "neptune",
    "transit_gateway",
    "apprunner",
    "appmesh",
    "networkmanager",
    "mwaa",
    "kendra",
    "fsx",
    "accessanalyzer",
    "s3outposts",
    "sqs",
    "licensemanager",
    "devicefarm",
    "elemental_mediaconvert",
    "emrserverless",
    "appintegrations",
    "vpc",
    "appconfig",
    "lightsail",
    "elemental_mediastore",
    "networkfirewall",
    "macie",
    "autoscaling",
    "ses",
    "imagebuilder",
    "acm",
    "account",
    "fms",
    "sagemaker",
    "kinesisanalyticsv2",
    "kinesis_analytics",
    "timestreamwrite",
    "sdb",
    "cloud_map",
    "macie2",
    "opensearch",
    "grafana",
    "autoscalingplans",
    "cognito",
    "cloudwatch",
    "comprehend",
    "iam",
    "sns",
    "kms",
    "mq",
    "direct_connect",
    "emr",
    "guardduty",
    "eventbridge",
    "redshiftdata",
    "waf",
    "datapipeline",
    "appstream",
    "appsync",
    "dataexchange",
    "quicksight",
    "identitystore",
    "ds",
    "connect",
    "appflow",
    "docdb",
    "glacier",
    "shield",
    "codepipeline",
    "sts",
    "memorydb",
    "opsworks",
    "wafregional",
    "glue",
]

import terrascript.aws.accessanalyzer as accessanalyzer
import terrascript.aws.account as account
import terrascript.aws.acm as acm
import terrascript.aws.acmpca as acmpca
import terrascript.aws.amp as amp
import terrascript.aws.amplify as amplify
import terrascript.aws.api_gateway as api_gateway
import terrascript.aws.apigatewayv2 as apigatewayv2
import terrascript.aws.appconfig as appconfig
import terrascript.aws.appflow as appflow
import terrascript.aws.appintegrations as appintegrations
import terrascript.aws.application_auto_scaling as application_auto_scaling
import terrascript.aws.applicationinsights as applicationinsights
import terrascript.aws.appmesh as appmesh
import terrascript.aws.apprunner as apprunner
import terrascript.aws.appstream as appstream
import terrascript.aws.appsync as appsync
import terrascript.aws.athena as athena
import terrascript.aws.auto_scaling as auto_scaling
import terrascript.aws.autoscaling as autoscaling
import terrascript.aws.autoscalingplans as autoscalingplans
import terrascript.aws.backup as backup
import terrascript.aws.batch as batch
import terrascript.aws.budgets as budgets
import terrascript.aws.ce as ce
import terrascript.aws.chime as chime
import terrascript.aws.cloud9 as cloud9
import terrascript.aws.cloud_map as cloud_map
import terrascript.aws.cloudcontrolapi as cloudcontrolapi
import terrascript.aws.cloudformation as cloudformation
import terrascript.aws.cloudfront as cloudfront
import terrascript.aws.cloudhsm as cloudhsm
import terrascript.aws.cloudsearch as cloudsearch
import terrascript.aws.cloudtrail as cloudtrail
import terrascript.aws.cloudwatch as cloudwatch
import terrascript.aws.codeartifact as codeartifact
import terrascript.aws.codebuild as codebuild
import terrascript.aws.codecommit as codecommit
import terrascript.aws.codedeploy as codedeploy
import terrascript.aws.codepipeline as codepipeline
import terrascript.aws.codestarconnections as codestarconnections
import terrascript.aws.codestarnotifications as codestarnotifications
import terrascript.aws.cognito as cognito
import terrascript.aws.cognito_identity as cognito_identity
import terrascript.aws.comprehend as comprehend
import terrascript.aws.config as config
import terrascript.aws.connect as connect
import terrascript.aws.cost_and_usage_report as cost_and_usage_report
import terrascript.aws.dataexchange as dataexchange
import terrascript.aws.datapipeline as datapipeline
import terrascript.aws.datasync as datasync
import terrascript.aws.detective as detective
import terrascript.aws.devicefarm as devicefarm
import terrascript.aws.direct_connect as direct_connect
import terrascript.aws.dlm as dlm
import terrascript.aws.dms as dms
import terrascript.aws.docdb as docdb
import terrascript.aws.ds as ds
import terrascript.aws.dynamodb as dynamodb
import terrascript.aws.dynamodb_accelerator as dynamodb_accelerator
import terrascript.aws.ebs as ebs
import terrascript.aws.ec2 as ec2
import terrascript.aws.ecr as ecr
import terrascript.aws.ecrpublic as ecrpublic
import terrascript.aws.ecs as ecs
import terrascript.aws.efs as efs
import terrascript.aws.eks as eks
import terrascript.aws.elastic_beanstalk as elastic_beanstalk
import terrascript.aws.elasticache as elasticache
import terrascript.aws.elasticsearch as elasticsearch
import terrascript.aws.elastictranscoder as elastictranscoder
import terrascript.aws.elb as elb
import terrascript.aws.elb_classic as elb_classic
import terrascript.aws.elemental_mediaconvert as elemental_mediaconvert
import terrascript.aws.elemental_mediapackage as elemental_mediapackage
import terrascript.aws.elemental_mediastore as elemental_mediastore
import terrascript.aws.emr as emr
import terrascript.aws.emrcontainers as emrcontainers
import terrascript.aws.emrserverless as emrserverless
import terrascript.aws.eventbridge as eventbridge
import terrascript.aws.fis as fis
import terrascript.aws.fms as fms
import terrascript.aws.fsx as fsx
import terrascript.aws.gamelift as gamelift
import terrascript.aws.glacier as glacier
import terrascript.aws.globalaccelerator as globalaccelerator
import terrascript.aws.glue as glue
import terrascript.aws.grafana as grafana
import terrascript.aws.guardduty as guardduty
import terrascript.aws.iam as iam
import terrascript.aws.identitystore as identitystore
import terrascript.aws.imagebuilder as imagebuilder
import terrascript.aws.inspector as inspector
import terrascript.aws.iot as iot
import terrascript.aws.kendra as kendra
import terrascript.aws.keyspaces as keyspaces
import terrascript.aws.kinesis as kinesis
import terrascript.aws.kinesis_analytics as kinesis_analytics
import terrascript.aws.kinesis_firehose as kinesis_firehose
import terrascript.aws.kinesis_video as kinesis_video
import terrascript.aws.kinesisanalyticsv2 as kinesisanalyticsv2
import terrascript.aws.kms as kms
import terrascript.aws.lakeformation as lakeformation
import terrascript.aws.lambda_ as lambda_
import terrascript.aws.lex as lex
import terrascript.aws.licensemanager as licensemanager
import terrascript.aws.lightsail as lightsail
import terrascript.aws.location as location
import terrascript.aws.macie as macie
import terrascript.aws.macie2 as macie2
import terrascript.aws.managed_streaming_for_kafka as managed_streaming_for_kafka
import terrascript.aws.managed_streaming_for_kafka_connect as managed_streaming_for_kafka_connect
import terrascript.aws.memorydb as memorydb
import terrascript.aws.meta_data_sources as meta_data_sources
import terrascript.aws.mq as mq
import terrascript.aws.mwaa as mwaa
import terrascript.aws.neptune as neptune
import terrascript.aws.networkfirewall as networkfirewall
import terrascript.aws.networkmanager as networkmanager
import terrascript.aws.opensearch as opensearch
import terrascript.aws.opsworks as opsworks
import terrascript.aws.organizations as organizations
import terrascript.aws.outposts as outposts
import terrascript.aws.pinpoint as pinpoint
import terrascript.aws.pricing as pricing
import terrascript.aws.qldb as qldb
import terrascript.aws.quicksight as quicksight
import terrascript.aws.ram as ram
import terrascript.aws.rds as rds
import terrascript.aws.redshift as redshift
import terrascript.aws.redshiftdata as redshiftdata
import terrascript.aws.redshiftserverless as redshiftserverless
import terrascript.aws.resourcegroups as resourcegroups
import terrascript.aws.resourcegroupstagging as resourcegroupstagging
import terrascript.aws.rolesanywhere as rolesanywhere
import terrascript.aws.route53 as route53
import terrascript.aws.route53_resolver as route53_resolver
import terrascript.aws.route53domains as route53domains
import terrascript.aws.route53recoverycontrolconfig as route53recoverycontrolconfig
import terrascript.aws.route53recoveryreadiness as route53recoveryreadiness
import terrascript.aws.rum as rum
import terrascript.aws.s3 as s3
import terrascript.aws.s3control as s3control
import terrascript.aws.s3outposts as s3outposts
import terrascript.aws.sagemaker as sagemaker
import terrascript.aws.schemas as schemas
import terrascript.aws.sdb as sdb
import terrascript.aws.secretsmanager as secretsmanager
import terrascript.aws.securityhub as securityhub
import terrascript.aws.serverlessapplicationrepository as serverlessapplicationrepository
import terrascript.aws.servicecatalog as servicecatalog
import terrascript.aws.servicequotas as servicequotas
import terrascript.aws.ses as ses
import terrascript.aws.sfn as sfn
import terrascript.aws.shield as shield
import terrascript.aws.signer as signer
import terrascript.aws.sns as sns
import terrascript.aws.sqs as sqs
import terrascript.aws.ssm as ssm
import terrascript.aws.ssoadmin as ssoadmin
import terrascript.aws.storagegateway as storagegateway
import terrascript.aws.sts as sts
import terrascript.aws.swf as swf
import terrascript.aws.synthetics as synthetics
import terrascript.aws.timestreamwrite as timestreamwrite
import terrascript.aws.transcribe as transcribe
import terrascript.aws.transfer as transfer
import terrascript.aws.transit_gateway as transit_gateway
import terrascript.aws.vpc as vpc
import terrascript.aws.vpc_ipam as vpc_ipam
import terrascript.aws.vpn as vpn
import terrascript.aws.waf as waf
import terrascript.aws.wafregional as wafregional
import terrascript.aws.wavelength as wavelength
import terrascript.aws.worklink as worklink
import terrascript.aws.workspaces as workspaces
import terrascript.aws.x_ray as x_ray
