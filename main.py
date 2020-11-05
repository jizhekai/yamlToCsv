import yaml
import csv

def readYaml(howTo):
    file_path  = './data/data.yaml'
    excel_path = './data/data.xlsx'
    with open(file_path,'r',encoding='utf-8') as f:
        data = yaml.load(f,yaml.FullLoader)
        with open('./data/data.csv','a+') as csv_f:
            for caseList in data["data"]:
                csv_f.write('\n')
                csv_f.writelines([caseList[item] for item in caseList])
    f.close()

if __name__ == '__main__':
    readYaml('new')
