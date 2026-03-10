terraform {
  required_version = ">= 0.14.0"
  required_providers {
    openstack = {
      source  = "terraform-provider-openstack/openstack"
      version = "~> 1.53.0"
    }
    local = {
      source  = "hashicorp/local"
      version = "2.5.2"
    }
  }
}

provider "openstack" {
  auth_url                      = var.auth_url
  region                        = var.region
  tenant_name                   = var.tenant_name
  domain_name                   = var.domain_name
  application_credential_id     = var.application_credential_id
  application_credential_secret = var.application_credential_secret
}

# SSH Key Pair
resource "openstack_compute_keypair_v2" "hpc_kb_key" {
  name       = var.keypair_name
  public_key = var.ssh_public_key
}

# Compute Instance for HPC Knowledge Database
resource "openstack_compute_instance_v2" "hpc_kb_vm" {
  name            = var.vm_name
  flavor_name     = var.flavor_name
  image_name      = var.image_name
  key_pair        = openstack_compute_keypair_v2.hpc_kb_key.name
  security_groups = [openstack_compute_secgroup_v2.hpc_kb_secgroup.name]

  network {
    name        = openstack_networking_network_v2.hpc_kb_net.name
    fixed_ip_v4 = var.vm_fixed_ip
  }

  # User data script to initialize the VM
  user_data = templatefile("${path.module}/user_data.sh", {
    docker_registry = var.docker_registry
    dr_api_tag     = var.dr_api_tag
    indexer_tag    = var.indexer_tag
    llm_base_url   = var.llm_base_url
    llm_model      = var.llm_model
  })

  depends_on = [
    openstack_compute_secgroup_v2.hpc_kb_secgroup,
    openstack_networking_subnet_v2.hpc_kb_sub,
    openstack_networking_router_v2.hpc_kb_router
  ]
}

# Volume for Elasticsearch data persistence
resource "openstack_blockstorage_volume_v3" "hpc_kb_es_volume" {
  name = "${var.vm_name}-elasticsearch-data"
  size = var.elasticsearch_volume_size
}

# Attach volume to VM
resource "openstack_compute_volume_attach_v2" "hpc_kb_es_attach" {
  instance_id = openstack_compute_instance_v2.hpc_kb_vm.id
  volume_id   = openstack_blockstorage_volume_v3.hpc_kb_es_volume.id
}

# Floating IP
resource "openstack_networking_floatingip_v2" "hpc_kb_floating_ip" {
  pool = var.floating_ip_pool
}

# Associate Floating IP with VM
resource "openstack_compute_floatingip_associate_v2" "hpc_kb_floating_ip_assoc" {
  floating_ip = openstack_networking_floatingip_v2.hpc_kb_floating_ip.address
  instance_id = openstack_compute_instance_v2.hpc_kb_vm.id
}

# Outputs
output "floating_ip" {
  value       = openstack_networking_floatingip_v2.hpc_kb_floating_ip.address
  description = "Floating IP address of the HPC KB VM"
}

output "vm_name" {
  value       = openstack_compute_instance_v2.hpc_kb_vm.name
  description = "Name of the HPC KB VM"
}

output "fixed_ip" {
  value       = openstack_compute_instance_v2.hpc_kb_vm.network[0].fixed_ip_v4
  description = "Fixed internal IP of the VM"
}

output "ssh_command" {
  value       = "ssh -i ${var.ssh_private_key_path} ubuntu@${openstack_networking_floatingip_v2.hpc_kb_floating_ip.address}"
  description = "SSH command to connect to the VM"
}

output "dr_api_url" {
  value       = "http://${openstack_networking_floatingip_v2.hpc_kb_floating_ip.address}:8001"
  description = "URL for the DR API service"
}

output "elasticsearch_url" {
  value       = "http://${openstack_networking_floatingip_v2.hpc_kb_floating_ip.address}:9200"
  description = "URL for Elasticsearch (internal access only)"
}
