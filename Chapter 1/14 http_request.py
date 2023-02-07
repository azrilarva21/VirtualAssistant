from urllib.request import urlopen
import json


def main():
    url = "https://jsonplaceholder.typicode.com/todos/1"
    with urlopen(url) as response:
        body = response.read()

    todo_item = json.loads(body)
    print(todo_item)


if __name__ == '__main__':main()