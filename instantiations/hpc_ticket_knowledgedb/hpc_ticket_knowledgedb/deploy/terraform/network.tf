# Network Configuration for HPC Knowledge Database

# Create network
resource "openstack_networking_network_v2" "hpc_kb_net" {
  name           = var.network_name
  admin_state_up = "true"
}

# Create subnet
resource "openstack_networking_subnet_v2" "hpc_kb_sub" {
  name            = var.subnet_name
  network_id      = openstack_networking_network_v2.hpc_kb_net.id
  cidr            = var.subnet_cidr
  ip_version      = 4
  enable_dhcp     = true
  gateway_ip      = var.gateway_ip
  dns_nameservers = var.dns_nameservers
}

# Create router
resource "openstack_networking_router_v2" "hpc_kb_router" {
  name                = var.router_name
  admin_state_up      = true
  external_network_id = var.external_network_id
}

# Connect subnet to router
resource "openstack_networking_router_interface_v2" "hpc_kb_router_interface" {
  router_id = openstack_networking_router_v2.hpc_kb_router.id
  subnet_id = openstack_networking_subnet_v2.hpc_kb_sub.id
}

# Security Group
resource "openstack_compute_secgroup_v2" "hpc_kb_secgroup" {
  name        = var.secgroup_name
  description = "Security group for HPC Knowledge Database VM"

  # SSH access
  rule {
    from_port   = 22
    to_port     = 22
    ip_protocol = "tcp"
    cidr        = var.ssh_allowed_cidr
  }

  # DR API (8001)
  rule {
    from_port   = 8001
    to_port     = 8001
    ip_protocol = "tcp"
    cidr        = var.api_allowed_cidr
  }

  # Elasticsearch (9200) - internal only
  rule {
    from_port   = 9200
    to_port     = 9200
    ip_protocol = "tcp"
    cidr        = var.internal_network_cidr
  }

  # ICMP (ping)
  rule {
    from_port   = -1
    to_port     = -1
    ip_protocol = "icmp"
    cidr        = "0.0.0.0/0"
  }

  # HTTP/HTTPS for updates and Docker pulls
  rule {
    from_port   = 80
    to_port     = 80
    ip_protocol = "tcp"
    cidr        = "0.0.0.0/0"
  }

  rule {
    from_port   = 443
    to_port     = 443
    ip_protocol = "tcp"
    cidr        = "0.0.0.0/0"
  }

  # Egress - allow all outbound
  rule {
    from_port   = 1
    to_port     = 65535
    ip_protocol = "tcp"
    cidr        = "0.0.0.0/0"
  }

  rule {
    from_port   = 1
    to_port     = 65535
    ip_protocol = "udp"
    cidr        = "0.0.0.0/0"
  }
}
