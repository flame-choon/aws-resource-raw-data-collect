
class AWS_Request_Resource_Type:

    # EC2
    ec2DescribeInstance = 'EC2_DESCRIBE_INSTANCES'                                 # EC2 인스턴스 정보 조회
    ec2DescribeVolumes = 'EC2_DESCRIBE_VOLUMES'                                    # EC2 의 Volume 정보 조회
    ec2DescribeKeyPairs = 'EC2_DESCRIBE_KEY_PAIRS'                                 # EC2 의 KeyPair 정보 조회
    ec2DescribeSnapshots = 'EC2_DESCRIBE_SNAPSHOTS'                                # EC2의 Snapshot 정보 조회
    ec2DescribeImages = 'EC2_DESCRIBE_IMAGES'                                      # EC2 의 Image 정보 조회
    ec2DescribeRouteTables = 'EC2_DESCRIBE_ROUTE_TABLES'                           # EC2 의 RouteTable 정보 조회
    ec2DescribeVpcs = 'EC2_DESCRIBE_VPCS'                                          # EC2 의 VPC 정보 조회    
    ec2DescribeSubnets = 'EC2_DESCRIBE_SUBNETS'                                    # EC2 의 Subnet 정보 조회
    ec2DescribeInternetGateways = 'EC2_DESCRIBE_INTERNET_GATEWAYS'                 # EC2 의 Internet GW 정보 조회
    ec2DescribeEIPAddress = 'EC2_DESCRIBE_EIP_Address'                             # EC2의 EIP 정보 조회
    ec2DescribeNATGateways = 'EC2_DESCRIBE_NAT_GATEWAYS'                           # EC2의 NAT Gateway 정보 조회
    ec2DescribeVPCPeeringConnections = 'EC2_DESCRIBE_VPC_PEERING_CONNECTIONS'      # EC2의 VPC Peering Connections 정보 조회
    ec2DescribeNetworkACLs = 'EC2_DESCRIBE_NETWORK_ACLS'                           # EC2의 Network ACLs 정보 조회
    ec2DescribeSecurityGroups = 'EC2_DESCRIBE_SECURITY_GROUPS'                     # EC2의 Security Groups 정보 조회
    ec2DescribeVpcEndpoints = 'EC2_DESCRIBE_VPC_ENDPOINTS'                         # EC2의 EndPoints 정보 조회

    # Lambda
    lambdaGetFunction = 'LAMBDA_GET_FUNCTION'                                      # Lambda의 Function 정보 조회

    # ELB
    elbDescribeLoadBalancers = 'ELB_DESCRIBE_LOAD_BALANCERS'                       # ELB 의 정보 조회

    # EKS 
    eksDescribeCluster = 'EKS_DESCRIBE_CLUSTER'   
    
    # ROUTE 53
    route53GetHostedZone = 'ROUTE53_GET_HOSTED_ZONE'
    
    # S3
    s3GetListBuckets = 'S3_GET_LIST_BUCKETS' 
    s3GetBucketAccelerateConfiguration = 'S3_GET_BUCKET_ACCELERATE_CONFIGURATION'
    s3GetBucketAcl = 'S3_GET_BUCKET_ACL'   
    s3GetBucketAnalyticsConfiguration = 'S3_GET_BUCKET_ANALYTICS_CONFIGURATION'   


    # EFS
    efsDescribeFileSystem = 'EFS_DESCRIBE_FILE_SYSTEM'
    
    # RDS
    rdsDescribeDBCluster = 'RDS_DESCRIBE_DB_CLUSTER'

    # ELASTICACHE
    elasticacheDescribeReplicationGroups = 'ELASTICACHE_DESCRIBE_REPLICATION_GROUPS'

    # DynamoDB
    dynamodbDescribeTable = 'DYNAMODB_DESCRIBE_TABLE'

    # Kinesis - DataStream
    kinesisDescribeStream = 'KINESIS-DATASTREAM_DESCRIBE_STREAM'

    # Kinesis - Firehose
    kinesisFirehoseStream = 'KINESIS-FIREHOSE_DESCRIBE_DELIVERY_STREAM'

    # GLUE

    # ATHENA
    athenaGetDataCatalog = 'ATHENA_GET_DATA_CATALOG'
    athenaGetDatabase = 'ATHENA_GET_DATABASE'
    athenaGetNamedQuery = 'ATHENA_GET_NAMED_QUERY'
    athenaGetTableMetadata = 'ATHENA_GET_TABLE_METADATA'


    # IAM
    iamGetUser = 'IAM_GET_USER'
    iamGetUserGroup = 'IAM_GET_USER_GROUP'
    iamGetRole = 'IAM_GET_ROLE'
    iamGetPolicy = 'IAM_GET_POLICY'