from kubernetes import client, config

def rolling_update(namespace, deployment_name, image):
    config.load_kube_config()
    apps_v1 = client.AppsV1Api() 

    body = {"spec": {"template": {"spec": {"containers": [{"name": deployment_name, "image": image}]}}}}
    apps_v1.patch_namespaced_deployment(deployment_name, namespace, body)
    print(f"Rolling update initiated for {deployment_name} with new image {image}.")

if __name__ == "__main__":
    rolling_update("default", "my-deployment", "my-image:latest")
