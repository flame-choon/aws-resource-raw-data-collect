import boto3
import Code.ResourceType.aws_request_resource_type as resource_type

route53_client = boto3.client('route53')

def rawDataRequest(route53ResourceType):
    if route53ResourceType is resource_type.AWS_Request_Resource_Type.route53GetHostedZone:
        return route53GetHostedZone()

    return 'dosen\'t not match request'

# Route53 의 정보 조회
def route53GetHostedZone():
    response = route53_client.get_hosted_zone(
        Id = 'Z0712647MZDIF6Y6JZ34'
    )
    return response
