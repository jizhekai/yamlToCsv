import yaml
import csv
import os

def readYaml():
    file_path  = './data/data.yaml'
    with open(file_path,'r',encoding='utf-8-sig') as f:
        data = yaml.load(f,yaml.FullLoader)['data']
        lines = []
        for case in data:
            line = []
            for item in case:
                if isinstance(case[item],list):
                    case[item] = '\n'.join(['【'+ str(case[item].index(line)+1) +'】'+ line for line in case[item]])
                line.append(case[item])
            lines.append(line)
    f.close()
            
    fcsv = open('./data/data.csv','a+',encoding='utf-8-sig',newline="")
    f_csv = csv.writer(fcsv)
    for line in lines:
        f_csv.writerow(line)

if __name__ == '__main__':
    readYaml()