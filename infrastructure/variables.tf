variable "tags" {
  type = map(string)
  default = {
    Environment = "dev"
    Proj = "todo_web_app3"
    Owner       = "I_am"
    terraform   = "True"
  }
}

variable "region" {
  description = "Please Enter AWS Region to deploy Server"
  type        = string
  default     = "eu-north-1"
}

variable "instance_type" {
  description = "Enter Instance Type"
  type        = string
  default     = "t3.nano"
}

variable "allow_ports" {
  description = "List of Ports to open for server"
  type        = list
  default     = ["80", "443", "22"]
}

variable "busket_name" {
  description = "Enter busket_name"
  type        = string
  default     = "bucketname123s1"
}

variable "key_name" {
  default = "KeyFromLinuxAWS-Frankfurt"
}