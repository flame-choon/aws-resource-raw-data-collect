import boto3
import Code.ResourceType.aws_request_resource_type as resource_type

s3_client = boto3.client('s3')
s3_resource = boto3.resource('s3')

def rawDataRequest(s3ResourceType):
    if s3ResourceType is resource_type.AWS_Request_Resource_Type.s3GetListBuckets:
        return s3GetListBuckets()
    elif s3ResourceType is resource_type.AWS_Request_Resource_Type.s3GetBucketAccelerateConfiguration:
        return s3GetBucketAccelerateConfiguration()
    elif s3ResourceType is resource_type.AWS_Request_Resource_Type.s3GetBucketAcl:
        return s3GetBucketAcl()
    elif s3ResourceType is resource_type.AWS_Request_Resource_Type.s3GetBucketAnalyticsConfiguration:
        return s3GetBucketAnalyticsConfiguration()

    return 'dosen\'t not match request'

# s3 의 버켓 목록 조회
def s3GetListBuckets():
    # response = s3_client.get_hosted_zone(
    #     Id = 'Z0712647MZDIF6Y6JZ34'
    # )
    return s3_client.list_buckets()

# S3 의 버켓 전송 가속화 설정 조회
def s3GetBucketAccelerateConfiguration():
    response = s3_client.get_bucket_accelerate_configuration(
        Bucket='kwangjin-glue-script-bucket'
    )
    return response    

# S3 의 버켓 ACL 설정 조회
def s3GetBucketAcl():
    response = s3_client.get_bucket_acl(
        Bucket='kwangjin-glue-script-bucket'
    )
    return response

# S3 의 버켓 스토리지 클래스 분석 설정 조회
def s3GetBucketAnalyticsConfiguration():
    response = s3_client.get_bucket_analytics_configuration(
        Bucket='kwangjin-glue-script-bucket',
        Id='test-configuration'
    )
    return response    

# get_bucket_cors()
# get_bucket_encryption()
# get_bucket_intelligent_tiering_configuration()
# get_bucket_inventory_configuration()
# get_bucket_lifecycle()
# get_bucket_lifecycle_configuration()
# get_bucket_location()
# get_bucket_logging()
# get_bucket_metrics_configuration()
# get_bucket_notification()
# get_bucket_notification_configuration()
# get_bucket_ownership_controls()
# get_bucket_policy()
# get_bucket_policy_status()
# get_bucket_replication()
# get_bucket_request_payment()
# get_bucket_tagging()
# get_bucket_versioning()
# get_bucket_website()
# get_public_access_block()