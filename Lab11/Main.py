import re

if __name__ == "__main__":

    result = re.findall("\d+/.+/\d\d\d\d:0[3-6]:[0-5][0-6].+(png|PNG)", open('access_log', ).read())
    print(f"png: {len(result)}")

    result = re.findall("\d+/.+/\d\d\d\d:0[3-6]:[0-5][0-6].+(jpg|JPG)", open('access_log', ).read())
    print(f"jpg: {len(result)}")

    result = re.findall("\d+/.+/\d\d\d\d:0[3-6]:[0-5][0-6].+(jpeg|JPEG)", open('access_log', ).read())
    print(f"jpeg: {len(result)}")

    result = re.findall("\d+/.+/\d\d\d\d:0[3-6]:[0-5][0-6].+(gif|GIF)", open('access_log', ).read())
    print(f"gif: {len(result)}")

