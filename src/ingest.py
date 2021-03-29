import dvc.api
import os

fullpath = os.path.join("data", "data.xml")
with dvc.api.open(
        'get-started/data.xml',
        repo='https://github.com/iterative/dataset-registry'
        ) as fd:
    with open(fullpath,"w") as fw :
        fw.writelines(fd.readlines())
