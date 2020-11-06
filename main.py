import yaml
import csv
import sys
import os

def readYaml():
    dirname = './data/'+ sys.argv[1]
    if not os.path.exists(dirname):
        os.mkdir(dirname)
    file_path  = './data/'+ sys.argv[1] +'/' + sys.argv[1] +'.yaml'
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
            
    fcsv = open('./data/'+ sys.argv[1] +'/' + sys.argv[1] +'.csv','w+',encoding='utf-8-sig',newline="")
    f_csv = csv.writer(fcsv)
    f_csv.writerow(['tc.title','tc.group','tc.executor','tc.precondition','tc.step.desc','tc.step.expected','tc.caseType','tc.priority'])
    f_csv.writerow('\n')
    for line in lines:
        f_csv.writerow(line)

if __name__ == '__main__':
    readYaml()