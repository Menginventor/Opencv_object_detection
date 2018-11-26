import yaml
import yamlordereddictloader

with open("data.yml") as f:
    yaml_data = yaml.load(f, Loader=yamlordereddictloader.Loader)
print(yaml_data['B']['C'])