from kubernetes import client, config

def monitor_pod_resources(namespace):
    config.load_kube_config() 
    metrics_client = client.CustomObjectsApi()

    pod_metrics = metrics_client.list_namespaced_custom_object(
        "metrics.k8s.io", "v1beta1", namespace, "pods"
    )
    for pod in pod_metrics['items']:
        pod_name = pod['metadata']['name']
        containers = pod['containers']
        for container in containers:
            print(f"Pod: {pod_name}, Container: {container['name']}, "
                  f"CPU: {container['usage']['cpu']}, Memory: {container['usage']['memory']}")

if __name__ == "__main__":
    monitor_pod_resources("default")
