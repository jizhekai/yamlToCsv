import yaml

def readYaml():
    file_path  = './data/data.yaml'
    with open(file_path,'r',encoding='utf-8') as f:
        data = yaml.load(f,yaml.FullLoader)
        print(data)
    f.close()

if __name__ == '__main__':
    readYaml()
