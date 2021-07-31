# terraform init
# terraform apply -var "digitalocean_token=${DO_PAT}" -var-file django_sample.tfvars
# terraform destroy -var "digitalocean_token=${DO_PAT}" -var-file django_sample.tfvars

variable "project_name" {}
variable "digitalocean_token" {}
variable "project_public_key_name" {}

# providers
terraform {
  required_providers {
    digitalocean = {
      source = "digitalocean/digitalocean"
      version = "~> 2.0"
    }
  }
}

provider "digitalocean" {
  token = var.digitalocean_token
}

data "digitalocean_ssh_key" "terraform" {
  name = var.project_public_key_name
}

# project
resource "digitalocean_project" "project" {
  name        = var.project_name
  purpose     = "Web Application"
  resources   = [
    digitalocean_droplet.rancher-controller.urn
  ]
}

data "template_file" "cloud-init-yaml" {
  template = file("${path.module}/files/cloud-init.yaml")
}

resource "digitalocean_droplet" "rancher-controller" {
  image       = "rancheros"
  name        = "${var.project_name}"
  region      = "fra1"
  size        = "s-1vcpu-2gb"
  ssh_keys    = [
    data.digitalocean_ssh_key.terraform.id
  ]
  user_data = data.template_file.cloud-init-yaml.rendered
}

output "login" {
  value = "ssh rancher@${digitalocean_droplet.rancher-controller.ipv4_address}"
}