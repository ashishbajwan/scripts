import requests

print("========================================================")
file_path = 'ip.txt'
try:
    with open(file_path, 'r') as file:
        for line in file:
            url = """http://""" + str(line.strip()) + """/"""""
            print(url)
            x = requests.get(url)
            data = x.text
            if data is not None and "<title>IIS Windows Server</title>" in data:
                print("IIS Page found")
                print
                file1 = open("IIS.txt", "a")
                file1.write(url + "\n")
                file1.close()
                print("========================================================")
            else :
                print("========================================================")
                continue
except FileNotFoundError:
    print(f"File '{file_path}' not found.")
except Exception as e:
    print("An error occurred")
