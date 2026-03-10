# OpenStack Authentication
application_credential_id     = "19f2c50127f74650a6c0f9eaefef32e2"
application_credential_secret = "ItocYp2VRJGU5-lvLFOHS8CiYemmGdcndC1ZYHgmHKZrtDxcA9uqRgteNCuUkxJA1jEDNQjjBNZVINjMuvdt2w"

# SSH Configuration
ssh_public_key       = "ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIFMeWM0P4IQmhjKheGHNZIn7ig8/9HMy7IiC8XLNWLsn lisa.rebecca.schmidt@fau.de"
ssh_private_key_path = "~/.ssh/fau_openstack_key"

# VM Configuration
vm_name      = "hpc-knowledge-database"
flavor_name  = "SCS-4V-16-100s"  # 4 vCPU, 16GB RAM, 100GB disk
image_name   = "Ubuntu 22.04"

# Network Configuration
network_name = "hpc_kb_net"
subnet_name  = "hpc_kb_sub"
subnet_cidr  = "10.240.60.0/24"
gateway_ip   = "10.240.60.1"
vm_fixed_ip  = "10.240.60.10"

# Security - IMPORTANT: Will restrict these after getting OpenWebUI IP
ssh_allowed_cidr = "0.0.0.0/0"  # TODO: Restrict to FAU network after deployment
api_allowed_cidr = "0.0.0.0/0"  # TODO: Restrict to OpenWebUI IP after deployment

# Storage
elasticsearch_volume_size = 100  # GB

# Docker Images
docker_registry = "lisarebecca"
dr_api_tag      = "latest"
indexer_tag     = "latest"

# LLM Configuration
llm_base_url = "http://lme49.cs.fau.de:30000/v1"
llm_model    = "openai/gpt-oss-120b"

# External Network Configuration (FAU-specific)
external_network_id = "eff4eaad-c424-49ba-b17c-050a8f422935"
floating_ip_pool    = "FAU-Intern"
