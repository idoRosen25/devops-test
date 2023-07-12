# **Devops**

this project is a simple single page react apllication for a guess the number game<br/>
Project includes fully automated deployment. Ansible to init AWS server, create and upload IMAGE to Dockerhub and pull on server.<br/>
On commit to branch `main`, execute GithubActions that run tests using Selenium and re-deploy application if all tests pass.<br/><br/>

***
# Requirements

Add in the root directory `group_vers/env` containing the following data:
```
vpc_name: <vpc-name-in-aws>
network: 10.10.0.0/16
aws_region: <your-region>
subnet_cidr: 10.10.0.0/24
subnet: <region-az>
server_type: t2.micro
keypair: <keypair-in-aws>
server_volume_size: 10
server_name: <my-server-name>
env: prod
aws_centos_ami: <centos-ami> 

```
`aws_centos_ami` can be any AMI name. AMIs can be found in AWS marketplace or anu AMI you want.

***
# Client
Clone repository, run `npm i` and then `npm start`
App wll run on `http://localhost:3000`

***
