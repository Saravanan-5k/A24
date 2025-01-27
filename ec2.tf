provider "aws" {
  region = "us-east-1" 
}

resource "aws_instance" "ec2_instance" {
  ami           = "ami-01816d07b1128cd2d" 
  instance_type = "t2.micro"

  tags = {
    Name = "MyEC2Instance"
  }
}
