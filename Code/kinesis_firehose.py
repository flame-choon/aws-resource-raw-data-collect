import boto3
import Code.ResourceType.aws_request_resource_type as resource_type

firehose_client = boto3.client('firehose')

def rawDataRequest(firehoseResourceType):
    if firehoseResourceType is resource_type.AWS_Request_Resource_Type.kinesisFirehoseStream:
        return kinesisFirehoseStream()

    return 'dosen\'t not match request'


# Kinesis의 FireHose 정보 조회
def kinesisFirehoseStream():
    response = firehose_client.describe_delivery_stream(
        DeliveryStreamName='KDS-S3-ZyoFY'
    )
    return response