import boto3
import Code.ResourceType.aws_request_resource_type as resource_type

athena_client = boto3.client('athena')

def rawDataRequest(athenaResourceType):
    if athenaResourceType is resource_type.AWS_Request_Resource_Type.athenaGetDataCatalog:
        return athenaGetDataCatalog()
    elif athenaResourceType is resource_type.AWS_Request_Resource_Type.athenaGetDatabase:
        return athenaGetDatabase()
    elif athenaResourceType is resource_type.AWS_Request_Resource_Type.athenaGetNamedQuery:
        return athenaGetNamedQuery()    
    elif athenaResourceType is resource_type.AWS_Request_Resource_Type.athenaGetTableMetadata:
        return athenaGetTableMetadata()

    return 'dosen\'t not match request'

# Athena 의 DataCatalog 정보 조회
def athenaGetDataCatalog():
    response = athena_client.get_data_catalog(
       Name = 'AwsDataCatalog'
    )
    return response

# Athena 의 Database 정보 조회
def athenaGetDatabase():
    response = athena_client.get_database(
       CatalogName = 'AwsDataCatalog',
       DatabaseName = 'upbit-krwbtc-minute-data-database'
    )
    return response

# Athena 에 저장한 Query 정보 조회 (QueryID는 list_named_queries 호출로 획득)
def athenaGetNamedQuery():
    response = athena_client.get_named_query(
        NamedQueryId='73d58720-0eee-4be5-9ebb-72ae4b369efa'
    )
    return response

 # Athena 의 Table Metadata 조회
def athenaGetTableMetadata():
    response = athena_client.get_table_metadata(
       CatalogName = 'AwsDataCatalog',
       DatabaseName = 'upbit-krwbtc-minute-data-database',
       TableName = 'kwangjin_data_lake'
    )
    return response   