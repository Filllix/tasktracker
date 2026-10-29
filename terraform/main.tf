resource "kind_cluster" "this" {
  name            = var.cluster_name
  kubeconfig_path = "${path.module}/kubeconfig"
  wait_for_ready  = true
}

resource "kubernetes_namespace_v1" "app" {
  metadata {
    name = var.namespace
    labels = {
      "app.kubernetes.io/part-of" = "tasktracker"
    }
  }
}

resource "kubernetes_secret_v1" "db" {
  metadata {
    name      = "tasktracker-db"
    namespace = kubernetes_namespace_v1.app.metadata[0].name
  }

  data = {
    POSTGRES_USER     = var.postgres_user
    POSTGRES_PASSWORD = var.postgres_password
    POSTGRES_DB       = var.postgres_db
    DATABASE_URL      = "postgresql://${var.postgres_user}:${var.postgres_password}@db:5432/${var.postgres_db}"
  }
}