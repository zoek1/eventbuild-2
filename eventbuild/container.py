import os

def build(client, dockfile, *args, **kwargs):
    return client.build(path=dockfile, *args, **kwargs)

def run(client, image, output, *args, **kwargs):
    output_path = os.path.abspath(output)
    id_container = client.create_container(image=image, volumes=['/package'], 
                                 host_config=client.create_host_config(binds={
                                     output_path: {
                                         'bind': '/package',
                                         'mode': 'rw',
                                     }
                                 }))
    client.start(id_container)
    return client.logs(container=id_container, stream=True)
  
