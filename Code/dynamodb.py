import boto3
import Code.ResourceType.aws_request_resource_type as resource_type

dynamodb_client = boto3.client('dynamodb')

def rawDataRequest(dynamodbResourceType):
    if dynamodbResourceType is resource_type.AWS_Request_Resource_Type.dynamodbDescribeTable:
        return dynamodbDescribeTable()

    return 'dosen\'t not match request'


# Dynamo DB의 Table 정보 조회
def dynamodbDescribeTable():
    response = dynamodb_client.describe_table(
        TableName='dynamodb-table'
    )
    return response