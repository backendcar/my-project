
file_name1 = "index.kljsf.lgk.html"
file_name2 = "application.py"

allowed_format = {"txt" , "py" , "html" , "css"}
def checkFileformat(fileName):
    formatt = fileName.split(".")[-1]
    return "." in fileName and formatt in allowed_format

