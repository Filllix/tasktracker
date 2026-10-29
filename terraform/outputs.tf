output "kubeconfig_path" {
  value = kind_cluster.this.kubeconfig_path
}

output "namespace" {
  value = kubernetes_namespace_v1.app.metadata[0].name
}