import boto3
import Code.ResourceType.aws_request_resource_type as resource_type

lambda_client = boto3.client('lambda')

def rawDataRequest(lambdaResourceType):
    if lambdaResourceType is resource_type.AWS_Request_Resource_Type.lambdaGetFunction:
        return lambdaGetFunction()

    return 'dosen\'t not match request'

# Lambda의 Function 정보 조회
def lambdaGetFunction():
    response = lambda_client.get_function(
        FunctionName = 'ec2_start_8_50am'
    )
    return response