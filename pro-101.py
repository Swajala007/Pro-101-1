import os
import dropbox
from dropbox.files import WriteMode



class Transferdata:
    def __init__(self,accesstoken):
        self.accesstoken = accesstoken

    def uploadFiles(self,filefrom,fileto):
        dbx = dropbox.Dropbox(self.accesstoken)

        for root,dirs,files in os.walk(filefrom):

            for fileName in files:
                local_path = os.path.join(root,fileName)
                relative_path = os.path.relpath(local_path,filefrom)
                dropbox_path = os.path.join(fileto,relative_path)

        with open(local_path,"rb") as f:
            dbx.files_upload(f.read(),dropbox_path, mode= WriteMode('overwrite'))


def main():
    accesstoken="sl.BNF9IAMtnZnKU1j-VTq4dhHpTtjH_0dldx_U8O-w_xk6PmnhkDWGUwnz_uq5QIZxAPGKzVs61n4Ao934CLBWKz3qDO71fckW8-SW34RAIDx9HcMLMyAh9RmIGNqdqk-_byOmG2mj0nf-"
    transferdata = Transferdata(accesstoken)

    filefrom = str(input("Enter the folder path to transfer:-"))
    fileto = input("enter the full path to upload to dropbox:-")
    transferdata.uploadFiles(filefrom,fileto)
    print("filesuploaded")

main()    