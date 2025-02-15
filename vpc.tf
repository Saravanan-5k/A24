resource "aws_vpc" "vpc" {
  cidr_block = "10.0.0.0/16"
  tags = {
    Name = "my-vpc"
  }
}

resource "aws_subnet" "public" {
  vpc_id                  = aws_vpc.vpc.id  
  cidr_block              = "10.0.1.0/24"
  map_public_ip_on_launch = true
  availability_zone       = "us-east-1a"
  tags = {
    Name = "PublicSubnet"
  }
}

resource "aws_internet_gateway" "gw" {
  vpc_id = aws_vpc.vpc.id  
  tags = {
    Name = "InternetGateway"
  }
}

resource "aws_route_table" "public_rt" {
  vpc_id = aws_vpc.vpc.id  
  tags = {
    Name = "PublicRouteTable"
  }
}

resource "aws_route" "internet_access" {
  route_table_id         = aws_route_table.public_rt.id  
  destination_cidr_block = "0.0.0.0/0"
  gateway_id             = aws_internet_gateway.gw.id  
}

resource "aws_route_table_association" "public_association" {
  subnet_id      = aws_subnet.public.id  
  route_table_id = aws_route_table.public_rt.id  
}
