import boto3
import Code.ResourceType.aws_request_resource_type as resource_type

rds_client = boto3.client('rds')

def rawDataRequest(rdsResourceType):
    if rdsResourceType is resource_type.AWS_Request_Resource_Type.rdsDescribeDBCluster:
        return rdsDescribeDBCluster()

    return 'dosen\'t not match request'

# RDS 의 db 클러스터 정보 조회
def rdsDescribeDBCluster():
    response = rds_client.describe_db_clusters(
        DBClusterIdentifier = 'database-1'
    )
    return response
