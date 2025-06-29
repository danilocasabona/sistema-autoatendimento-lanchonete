terraform {
  required_providers {
    docker = {
      source  = "kreuzwerker/docker"
      version = "~> 3.0.2"
    }
  }
}
# Variáveis
variable "app_port" {}
variable "postgres_port" {}
variable "postgres_user" {}
variable "postgres_pass" {}
variable "postgres_db" {}
variable "database_url" {}

# Volume do banco
resource "docker_volume" "pgdata" {
  name = "pgdata"
}

# Imagem e container do banco de dados
resource "docker_image" "db_image" {
  name = "lanchonete_db:latest"
  build {
    context    = "../.docker/bin/postgresql"
    dockerfile = "Dockerfile"
  }
}

resource "docker_container" "db" {
  name  = "lanchonete_db"
  image = docker_image.db_image.name

  env = [
    "POSTGRES_USER=${var.postgres_user}",
    "POSTGRES_PASSWORD=${var.postgres_pass}",
    "POSTGRES_DB=${var.postgres_db}",
    "PGDATA=/var/lib/postgresql/data/pgdata"
  ]

  ports {
    internal = 5432
    external = var.postgres_port
  }

  volumes {
    volume_name    = docker_volume.pgdata.name
    container_path = "/var/lib/postgresql/data"
  }
}

# Imagem e container do app
resource "docker_image" "app_image" {
  name = "lanchonete_app:latest"
  build {
    context    = "../.docker/bin/webserver"
    dockerfile = "Dockerfile"
  }
}

resource "docker_container" "app" {
  name  = "lanchonete_app"
  image = docker_image.app_image.name

  depends_on = [docker_container.db]

  env = [
    "POSTGRES_USER=${var.postgres_user}",
    "POSTGRES_PASSWORD=${var.postgres_pass}",
    "POSTGRES_DB=${var.postgres_db}"
  ]

  ports {
    internal = 8000
    external = var.app_port
  }

  # Montar volume com o código-fonte
  mounts {
    type        = "bind"
    source      = "${abspath("${path.module}/..")}"
    target      = "/app"
    read_only   = false
  }

  command = [
    "uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"
  ]
}