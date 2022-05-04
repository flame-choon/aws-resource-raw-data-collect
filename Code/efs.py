import boto3
import Code.ResourceType.aws_request_resource_type as resource_type

efs_client = boto3.client('efs')

def rawDataRequest(efsResourceType):
    if efsResourceType is resource_type.AWS_Request_Resource_Type.efsDescribeFileSystem:
        return efsDescribeFileSystem()

    return 'dosen\'t not match request'


# EFS의 File System 정보 조회
def efsDescribeFileSystem():
    response = efs_client.describe_file_systems(
        FileSystemId='fs-0d6d805f0b9a8be6d'
    )
    return response