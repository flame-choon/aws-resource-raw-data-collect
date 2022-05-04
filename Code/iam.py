import boto3
import Code.ResourceType.aws_request_resource_type as resource_type

iam_client = boto3.client('iam')


def rawDataRequest(iamResourceType):
    if iamResourceType is resource_type.AWS_Request_Resource_Type.iamGetUser:
        return iamGetUser()
    elif iamResourceType is resource_type.AWS_Request_Resource_Type.iamGetUserGroup:
        return iamGetUserGroup()  
    elif iamResourceType is resource_type.AWS_Request_Resource_Type.iamGetRole:
        return iamGetRole()      
    elif iamResourceType is resource_type.AWS_Request_Resource_Type.iamGetPolicy:
        return iamGetPolicy()    

    return 'dosen\'t not match request'

# IAM 의 유저 정보 조회
def iamGetUser():
    response = iam_client.get_user(
        UserName='kwangjin.hwang@bespinglobal.com'
    )
    return response

# IAM 의 사용자 그룹 정보 조회
def iamGetUserGroup():
    response = iam_client.get_group(
        GroupName='admin'
    )
    return response

# IAM 의 역할 정보 조회
def iamGetRole():
    response = iam_client.get_role(
        RoleName='AmazonRedshift-CommandsAccessRole-20220405T160628'
    )
    return response    

# IAM 의 정책 정보 조회
def iamGetPolicy():
    response = iam_client.get_policy(
        PolicyArn='arn:aws:iam::767404772322:policy/service-role/AmazonRedshift-CommandsAccessPolicy-20220405T160628'
    )
    return response    