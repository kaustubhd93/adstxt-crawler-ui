import os

def handle_uploaded_file(fileObj):
    home_dir = os.environ["HOME"]
    write_uploaded_file = home_dir + "/adstxtwebapp/" + fileObj._name
    with open(write_uploaded_file, "wb+") as destination:
        for chunk in fileObj.chunks():
            destination.write(chunk)
