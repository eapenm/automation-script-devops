from kubernetes import client, config

def get_pod_logs(namespace):
    config.load_kube_config() 
    v1 = client.CoreV1Api()

    pods = v1.list_namespaced_pod(namespace)
    for pod in pods.items:
        logs = v1.read_namespaced_pod_log(pod.metadata.name, namespace)
        print(f"Logs from {pod.metadata.name}:\n{logs}")

if __name__ == "__main__":
    get_pod_logs("default")
