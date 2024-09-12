#Monitoring VM Instances and Sending Alerts
from google.cloud import compute, pubsub_v1
project_id = 'my-project-id'

#create compute and pub/sub clients
compute_client = compute.Client(project=project_id)
publisher = pubsub_V1.PublisherClient()

#Get VM Insatnces
instances = compute_client.instances.list(project=project_id, zone='us-east-1')
#Monitor CPU utilization
for instance in instances:
    cpu_utilization = instance.metadata['instance/cpu/utilization']
    if int(cpu_utilization) > 80:
        #Publish a message to Cloud Pub/Sub
        topic_name = 'my-topic'
        publisher.publish(topic_name,data=f'High CPU utilization on instance:{instance.name}')
         