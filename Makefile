ENV_FILE=environment.yml

## Functions
environment:
	conda env create -f $(ENV_FILE)