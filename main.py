import json
import datetime
import Code.common as common
import Code.ResourceType.aws_request_resource_type as resource_type

response = common.rawDataRequest(resource_type.AWS_Request_Resource_Type.ec2DescribeSnapshots)

def datetimeConverter(o):
    if isinstance(o, datetime.datetime):
        return o.__str__()

json_result = json.dumps(response, default = datetimeConverter, indent = 3)

print(json_result)


