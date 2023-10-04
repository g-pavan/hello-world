import functions_framework

@functions_framework.cloud_event
def helloGET(cloud_event):
    print('Hello pavan function')