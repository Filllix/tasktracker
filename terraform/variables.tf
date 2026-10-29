variable "cluster_name" {
  type    = string
  default = "tasktracker"
}

variable "namespace" {
  type    = string
  default = "tasktracker"
}

variable "postgres_user" {
  type    = string
  default = "app"
}

variable "postgres_db" {
  type    = string
  default = "appdb"
}

variable "postgres_password" {
  type      = string
  sensitive = true

  validation {
    condition     = can(regex("^[A-Za-z0-9]{8,}$", var.postgres_password))
    error_message = "Password minimal 8 karakter, hanya huruf dan angka (karakter lain merusak DATABASE_URL)."
  }
}