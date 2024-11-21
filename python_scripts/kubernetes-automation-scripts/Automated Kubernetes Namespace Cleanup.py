from kubernetes import client, config 

def delete_unused_namespaces():
    config.load_kube_config()
    v1 = client.CoreV1Api()
    
    namespaces = v1.list_namespace()
    for ns in namespaces.items:
        if ns.status.phase == "Terminating":  # Example condition for unused namespace
            print(f"Deleting namespace: {ns.metadata.name}")
            v1.delete_namespace(ns.metadata.name)

if __name__ == "__main__":
    delete_unused_namespaces()