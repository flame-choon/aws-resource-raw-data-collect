import boto3
import Code.ResourceType.aws_request_resource_type as resource_type

elasticache_client = boto3.client('elasticache')

def rawDataRequest(elasticacheResourceType):
    if elasticacheResourceType is resource_type.AWS_Request_Resource_Type.elasticacheDescribeReplicationGroups:
        return elasticacheDescribeReplicationGroups()

    return 'dosen\'t not match request'

# ELASTICACHE 의 Replication Group 정보 조회
def elasticacheDescribeReplicationGroups():
    response = elasticache_client.describe_replication_groups(
       ReplicationGroupId='test-redis'
    )
    return response