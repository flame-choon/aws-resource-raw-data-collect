import boto3
import Code.ResourceType.aws_request_resource_type as resource_type

ec2_client = boto3.client('ec2')

def rawDataRequest(ec2ResourceType):

    if ec2ResourceType is resource_type.AWS_Request_Resource_Type.ec2DescribeInstance:
        return ec2DescribeInstance()
    elif ec2ResourceType is resource_type.AWS_Request_Resource_Type.ec2DescribeVolumes:
        return ec2DescribeVolumes()
    elif ec2ResourceType is resource_type.AWS_Request_Resource_Type.ec2DescribeKeyPairs:
        return ec2DescribeKeyPairs()
    elif ec2ResourceType is resource_type.AWS_Request_Resource_Type.ec2DescribeSnapshots:
        return ec2DescribeSnapshots() 
    elif ec2ResourceType is resource_type.AWS_Request_Resource_Type.ec2DescribeImages:
        return ec2DescribeImages()    
    elif ec2ResourceType is resource_type.AWS_Request_Resource_Type.ec2DescribeRouteTables:
        return ec2DescribeRouteTables()   
    elif ec2ResourceType is resource_type.AWS_Request_Resource_Type.ec2DescribeVpcs:
        return ec2DescribeVpcs()    
    elif ec2ResourceType is resource_type.AWS_Request_Resource_Type.ec2DescribeSubnets:
        return ec2DescribeSubnets()    
    elif ec2ResourceType is resource_type.AWS_Request_Resource_Type.ec2DescribeInternetGateways:
        return ec2DescribeInternetGateways()    
    elif ec2ResourceType is resource_type.AWS_Request_Resource_Type.ec2DescribeEIPAddress:
        return ec2DescribeEIPAddress()    
    elif ec2ResourceType is resource_type.AWS_Request_Resource_Type.ec2DescribeNATGateways:
        return ec2DescribeNATGateways()    
    elif ec2ResourceType is resource_type.AWS_Request_Resource_Type.ec2DescribeVPCPeeringConnections:
        return ec2DescribeVPCPeeringConnections() 
    elif ec2ResourceType is resource_type.AWS_Request_Resource_Type.ec2DescribeNetworkACLs:
        return ec2DescribeNetworkACLs()     
    elif ec2ResourceType is resource_type.AWS_Request_Resource_Type.ec2DescribeSecurityGroups:
        return ec2DescribeSecurityGroups()
    elif ec2ResourceType is resource_type.AWS_Request_Resource_Type.ec2DescribeVpcEndpoints:
        return ec2DescribeVpcEndpoints()    
      
    return 'dosen\'t not match request'

# EC2 의 Instance 정보 조회
def ec2DescribeInstance():
    response = ec2_client.describe_instances(
    InstanceIds = [
        'i-000082730bdd2ec33'
        ]
    )
    return response

# EC2 의 Volume 정보 조회
def ec2DescribeVolumes():
    response = ec2_client.describe_volumes(
    VolumeIds = [
        'vol-0a648b3da7ba1290d'
        ]
    )
    return response

# EC2 의 KeyPair 정보 조회
def ec2DescribeKeyPairs():
    response = ec2_client.describe_key_pairs(
    KeyPairIds = [
        'key-067a1e2da92416c2e'
        ]
    )
    return response

# EC2의 Snapshot 정보 조회
def ec2DescribeSnapshots():
    response = ec2_client.describe_snapshots(
    SnapshotIds = [
        'snap-050dcc44b388532b6'
        ]
    )
    return response

# EC2 의 Image 정보 조회
def ec2DescribeImages():
    response = ec2_client.describe_images(
    ImageIds = [
        'ami-04876f29fd3a5e8ba'
        ]
    )
    return response

# EC2 의 RouteTable 정보 조회
def ec2DescribeRouteTables():
    response = ec2_client.describe_route_tables(
    RouteTableIds = [
        'rtb-0ead2f0b6b380abf8'
        ]
    )
    return response

# EC2 의 VPC 정보 조회
def ec2DescribeVpcs():
    response = ec2_client.describe_vpcs(
    VpcIds = [
        'vpc-07c41a395ef34a994'
        ]
    )
    return response

# EC2 의 Subnet 정보 조회
def ec2DescribeSubnets():
    response = ec2_client.describe_subnets(
    SubnetIds = [
        'subnet-0cba48789535597d6'
        ]
    )
    return response

# EC2 의 Internet GW 정보 조회
def ec2DescribeInternetGateways():
    response = ec2_client.describe_internet_gateways (
    InternetGatewayIds = [
        'igw-06ba57ec5520e6baf'
        ]
    )
    return response

# EC2의 EIP 정보 조회
def ec2DescribeEIPAddress():
    response = ec2_client.describe_addresses(
    PublicIps = [
        '13.124.223.34'
        ]
    )
    return response

# EC2의 NAT Gateway 정보 조회
def ec2DescribeNATGateways():
    response = ec2_client.describe_nat_gateways(
    NatGatewayIds=[
        'nat-08d7df1898dad5a0d'
        ]
    )
    return response

# EC2의 VPC Peering Connections 정보 조회
def ec2DescribeVPCPeeringConnections():
    response = ec2_client.describe_vpc_peering_connections(
    VpcPeeringConnectionIds = [
        'pcx-0de84d51e09e872e1'
        ]
    )

# EC2의 Network ACLs 정보 조회
def ec2DescribeNetworkACLs():
    response = ec2_client.describe_network_acls(
    NetworkAclIds=[
        'acl-0b93b4271b091e56e'
        ]
    )
    return response

# EC2의 Security Groups 정보 조회
def ec2DescribeSecurityGroups():
    response = ec2_client.describe_security_groups(
    GroupIds=[
        'sg-04bd4502261b34826'
        ]
    )
    return response

# EC2의 EndPoints 정보 조회
def ec2DescribeVpcEndpoints():
    response = ec2_client.describe_vpc_endpoints(
    VpcEndpointIds=[
        'vpce-0c7a3b74bf9b1aeb9'
        ]
    )
    return response