region                     = "eu-central-1"
instance_type              = "t3.nano"


allow_ports = ["80","443","22","8000","8001"]


tags = {
  Environment = "prod"
  Project = "Todo_web_app4"
  Owner = "You_are"
  Terraform = "True"
}


key_name = "KeyFromLinuxAWS-Frankfurt"