import boto3
import Code.ResourceType.aws_request_resource_type as resource_type

elb_client = boto3.client('elbv2')

def rawDataRequest(elbResourceType):
    if elbResourceType is resource_type.AWS_Request_Resource_Type.elbDescribeLoadBalancers:
        return elbDescribeLoadBalancers()

    return 'dosen\'t not match request'

# ELB 의 정보 조회
def elbDescribeLoadBalancers():
    response = elb_client.describe_load_balancers(
    Names = [
        'msa-harbor-alb'
        ]
    )
    return response