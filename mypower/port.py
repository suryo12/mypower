import os

from .count_nout import count_nout

def port(path_in,path_out):
    for dirpath, _, files in os.walk(path_in):
        for f in files:
            if f[-2:] == '.m':
                print(os.path.join(dirpath,f))
                nout = count_nout(os.path.join(dirpath,f))
                current_folder = os.path.join(path_out,dirpath.replace(path_in,''))
                if not os.path.isdir(current_folder):
                    os.makedirs(current_folder)
                if not os.path.isfile(os.path.join(current_folder,'__init__.py')):
                    with open(os.path.join(current_folder,'__init__.py'),'w') as fout:
                        pass
                with open(os.path.join(current_folder,f[:-2]+'.py'),'w') as fout:
                    fout.write(f'def {f[:-2]}(*args,nout={nout},oc=None):\n')
                    fout.write('\tif oc == None:\n')
                    fout.write('\t\tfrom ..oc_matpower import oc_matpower\n')
                    fout.write('\toc = oc_matpower()\n')
                    fout.write(f'\treturn oc.{f[:-2]}(*args,nout=nout)\n')