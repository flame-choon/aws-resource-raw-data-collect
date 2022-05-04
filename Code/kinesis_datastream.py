import boto3
import Code.ResourceType.aws_request_resource_type as resource_type

kinesis_client = boto3.client('kinesis')

def rawDataRequest(kinesisResourceType):
    if kinesisResourceType is resource_type.AWS_Request_Resource_Type.kinesisDescribeStream:
        return kinesisDescribeStream()

    return 'dosen\'t not match request'


# Kinesis의 DataStream 정보 조회
def kinesisDescribeStream():
    response = kinesis_client.describe_stream(
        StreamName='kinesis-data-stream'
    )
    return response