#git updator 6000

from flask import Flask, request
import subprocess

app = Flask(__name__)

@app.route("/CS_1", methods=["POST"])
def send_data_CS1():
    data = ""
    data_new = request.get_json()
    print (data_new)
    formatted_string = "{}".format(data_new.get("data", "not found"))
    if formatted_string == "not found":
        raise ValueError('invalid value')
    print(formatted_string)
    data = formatted_string
    print (data)
    file_path = 'D:/source control/year-8-assesment/test.txt'  # Replace with the path to your file
    with open(file_path, 'w') as f:
        f.write(data)
        print(f)
    branch_name = 'main'  # Replace with the name of the branch you want to commit to
    commit_message = 'Update ipad'  # Replace with your own commit message
    # Push the commit
    subprocess.run(['git', 'config', '--global', 'user.email', 'alexanderjw9@icloud.com'])
    subprocess.run(['git', 'config', '--global', 'user.name', 'Ikeue4'])
    subprocess.run(['git', 'add', '-A'])
    subprocess.run(['git', 'commit', '-m', commit_message])
    subprocess.run(['git', 'push', 'origin', branch_name])
    return data

if __name__ == "__main__":
    app.run(host="192.168.1.102")
