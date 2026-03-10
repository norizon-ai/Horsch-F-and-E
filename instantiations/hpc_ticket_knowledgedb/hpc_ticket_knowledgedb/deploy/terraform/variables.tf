# OpenStack Provider Variables
variable "auth_url" {
  description = "OpenStack authentication URL"
  type        = string
  default     = "https://api.cc.rrze.de:5000"
}

variable "region" {
  description = "OpenStack region"
  type        = string
  default     = "DE-ERL"
}

variable "tenant_name" {
  description = "OpenStack project/tenant name"
  type        = string
  default     = "Pro_Norizon"
}

variable "domain_name" {
  description = "OpenStack domain name"
  type        = string
  default     = "fau"
}

variable "application_credential_id" {
  description = "OpenStack application credential ID"
  type        = string
  sensitive   = true
}

variable "application_credential_secret" {
  description = "OpenStack application credential secret"
  type        = string
  sensitive   = true
}

# VM Configuration
variable "vm_name" {
  description = "Name of the VM instance"
  type        = string
  default     = "hpc-knowledge-database"
}

variable "flavor_name" {
  description = "OpenStack flavor for the VM (4 vCPU, 16GB RAM recommended for Elasticsearch)"
  type        = string
  default     = "SCS-4V-16-100"
}

variable "image_name" {
  description = "OS image name"
  type        = string
  default     = "Ubuntu 22.04"
}

variable "keypair_name" {
  description = "Name for the SSH keypair"
  type        = string
  default     = "hpc-kb-key"
}

variable "ssh_public_key" {
  description = "SSH public key content"
  type        = string
}

variable "ssh_private_key_path" {
  description = "Path to SSH private key for output command"
  type        = string
  default     = "~/.ssh/fau_openstack_key"
}

# Network Configuration
variable "network_name" {
  description = "Name of the network"
  type        = string
  default     = "hpc_kb_net"
}

variable "subnet_name" {
  description = "Name of the subnet"
  type        = string
  default     = "hpc_kb_sub"
}

variable "subnet_cidr" {
  description = "CIDR block for the subnet"
  type        = string
  default     = "10.240.60.0/24"
}

variable "gateway_ip" {
  description = "Gateway IP for the subnet"
  type        = string
  default     = "10.240.60.1"
}

variable "vm_fixed_ip" {
  description = "Fixed IP for the VM within the subnet"
  type        = string
  default     = "10.240.60.10"
}

variable "dns_nameservers" {
  description = "DNS nameservers"
  type        = list(string)
  default     = ["131.188.4.30", "131.188.19.10"]
}

variable "router_name" {
  description = "Name of the router"
  type        = string
  default     = "hpc_kb_router"
}

variable "external_network_id" {
  description = "ID of the external network"
  type        = string
  default     = "f0dd6c0f-9629-45e8-9cdc-d7c9c4d92d48"
}

variable "floating_ip_pool" {
  description = "Floating IP pool name"
  type        = string
  default     = "belwue"
}

# Security Group Configuration
variable "secgroup_name" {
  description = "Name of the security group"
  type        = string
  default     = "hpc_kb_secgroup"
}

variable "ssh_allowed_cidr" {
  description = "CIDR block allowed for SSH access"
  type        = string
  default     = "0.0.0.0/0"  # Restrict this in production!
}

variable "api_allowed_cidr" {
  description = "CIDR block allowed for API access"
  type        = string
  default     = "0.0.0.0/0"  # Restrict this to your OpenWebUI IP in production!
}

variable "internal_network_cidr" {
  description = "CIDR block for internal network services"
  type        = string
  default     = "10.240.60.0/24"
}

# Storage Configuration
variable "elasticsearch_volume_size" {
  description = "Size of the Elasticsearch data volume in GB"
  type        = number
  default     = 100
}

# Application Configuration
variable "docker_registry" {
  description = "Docker registry for images"
  type        = string
  default     = "lisarebecca"
}

variable "dr_api_tag" {
  description = "Docker image tag for DR API"
  type        = string
  default     = "latest"
}

variable "indexer_tag" {
  description = "Docker image tag for indexer"
  type        = string
  default     = "latest"
}

variable "llm_base_url" {
  description = "LLM API base URL (NHR Hub Gateway)"
  type        = string
  default     = "https://hub.nhr.fau.de/api/llmgw/v1"
}

variable "llm_api_key" {
  description = "LLM API key for NHR Hub"
  type        = string
  sensitive   = true
  default     = "sk-a9uOWS13GwXfELWArWcnAA"
}

variable "llm_model" {
  description = "LLM model name"
  type        = string
  default     = "gpt-oss-120b"
}
