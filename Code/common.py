import Code.ec2 as ec2
import Code.elb as elb
import Code.eks as eks
import Code.lambda_function as lambda_function
import Code.route53 as route53
import Code.s3 as s3
import Code.efs as efs
import Code.rds as rds
import Code.elasticache as elasticache
import Code.dynamodb as dynamodb
import Code.kinesis_datastream as kinesis_datastream
import Code.kinesis_firehose as kinesis_firehose
import Code.athena as athena
import Code.iam as iam

def rawDataRequest(resourceType):
    
    if 'EC2' in resourceType:
        return ec2.rawDataRequest(resourceType)
    elif 'EKS' in resourceType:
        return eks.rawDataRequest(resourceType)   
    elif 'ELB' in resourceType:
        return elb.rawDataRequest(resourceType)
    elif 'LAMBDA' in resourceType:
        return lambda_function.rawDataRequest(resourceType) 
    elif 'ROUTE53' in resourceType:
        return route53.rawDataRequest(resourceType) 
    elif 'S3' in resourceType:
        return s3.rawDataRequest(resourceType)
    elif 'EFS' in resourceType:
        return efs.rawDataRequest(resourceType)
    elif 'RDS' in resourceType:
        return rds.rawDataRequest(resourceType)   
    elif 'ELASTICACHE' in resourceType:
        return elasticache.rawDataRequest(resourceType)    
    elif 'DYNAMODB' in resourceType:
        return dynamodb.rawDataRequest(resourceType)    
    elif 'KINESIS-DATASTREAM' in resourceType:
        return kinesis_datastream.rawDataRequest(resourceType)
    elif 'KINESIS-FIREHOSE' in resourceType:
        return kinesis_firehose.rawDataRequest(resourceType)  
    elif 'ATHENA' in resourceType:
        return athena.rawDataRequest(resourceType)      
    elif 'IAM' in resourceType:
        return iam.rawDataRequest(resourceType)    

    return 'dosen\'t not match request - FROM COMMON.PY'          
