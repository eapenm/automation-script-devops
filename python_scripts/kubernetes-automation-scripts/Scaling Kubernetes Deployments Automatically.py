from kubernetes import client, config 

def scale_deployment(namespace, deployment_name, replicas):
    config.load_kube_config()
    apps_v1 = client.AppsV1Api()

    body = {"spec": {"replicas": replicas}}
    apps_v1.patch_namespaced_deployment_scale(deployment_name, namespace, body)
    print(f"Scaled {deployment_name} to {replicas} replicas in {namespace} namespace.")

if __name__ == "__main__":
    scale_deployment("default", "my-deployment", 5)
