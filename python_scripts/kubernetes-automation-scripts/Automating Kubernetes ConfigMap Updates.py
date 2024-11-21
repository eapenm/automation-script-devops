from kubernetes import client, config 

def update_configmap(namespace, configmap_name, key, value):
    config.load_kube_config()
    v1 = client.CoreV1Api()

    configmap = v1.read_namespaced_config_map(configmap_name, namespace)
    configmap.data[key] = value

    v1.patch_namespaced_config_map(configmap_name, namespace, configmap)
    print(f"Updated {configmap_name} with {key}: {value} in {namespace} namespace.")

if __name__ == "__main__":
    update_configmap("default", "my-configmap", "config_key", "new_value")
