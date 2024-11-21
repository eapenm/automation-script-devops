from kubernetes import client, config 

def monitor_pods_status():
    config.load_kube_config()
    v1 = client.CoreV1Api()

    namespaces = v1.list_namespace()
    for ns in namespaces.items:
        print(f"\nNamespace: {ns.metadata.name}")
        pods = v1.list_namespaced_pod(ns.metadata.name)
        for pod in pods.items:
            print(f"Pod: {pod.metadata.name}, Status: {pod.status.phase}")

if __name__ == "__main__":
    monitor_pods_status()