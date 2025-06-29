.PHONY: up-tf down-tf rm-tf

up-tf:
	terraform apply -var-file="terraform.tfvars"

down-tf:
	terraform destroy -var-file="terraform.tfvars"

rm-tf:
	sudo rm -r .terraform/*
	sudo rm -f .terraform.lock.hcl
	sudo rm -f terraform.tfstate
	sudo rm -f terraform.tfstate.backup 