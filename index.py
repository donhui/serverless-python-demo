import json
import app
import uuid

def main_handler(event, context):
    print("event: " + json.dumps(event, indent = 2)) 
    url = event["queryString"]["url"]

    name = str(uuid.uuid1())
    ext = get_ext(url)

    file = app.download(url,'/tmp/', name + "."+ ext)
    res = app.ppt_to_text(file)
    
    return {
        "result": res  
    }


def get_ext(path):
    suffix = path.split(".")[1]
    return suffix;

if __name__=='__main__':
    url = 'http://localhost/test.pptx'

    name = str(uuid.uuid1())
    ext = get_ext(url)
    
    file = app.download(url,'/tmp/', name + "."+ ext)
    res = app.ppt_to_text(file)
    
    print(res)
