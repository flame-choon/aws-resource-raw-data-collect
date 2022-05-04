import boto3
import Code.ResourceType.aws_request_resource_type as resource_type

eks_client = boto3.client('eks')

def rawDataRequest(eksResourceType):
    if eksResourceType is resource_type.AWS_Request_Resource_Type.eksDescribeCluster:
        return eksDescribeCluster()

    return 'dosen\'t not match request'


# EKS의 Cluster 정보 조회
def eksDescribeCluster():
    response = eks_client.describe_cluster(
        name='secho-gran-xi-cluster'
    )
    return response