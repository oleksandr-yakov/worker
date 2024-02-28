import requests
import sys
import re

def check_tag(tag):
    pattern = r'^v\d+\.\d+\.\d+$'
    return bool(re.match(pattern, tag))

def find_max_tag(repository_name, token):
    headers = {"Authorization": f"token {token}"}
    url = f"https://api.github.com/repos/{repository_name}/tags"

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()

        tags = [tag["name"] for tag in response.json()]

        def tag_to_tuple(tag):
            return tuple(map(int, re.findall(r'\d+', tag)))

        max_tag = max(tags, key=tag_to_tuple)
        return max_tag

    except requests.exceptions.RequestException as e:
        print("An error occurred:", e)
        return None


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print(False)

    option = sys.argv[1]
    argument = sys.argv[2]

    if option == "--check_tag":
        is_valid = check_tag(argument)
        print(is_valid)
    elif option == "--get_max_tag":
        repository_name = "oleksandr-yakov/core"
        max_tag = find_max_tag(repository_name, argument)
        print(max_tag)
    else:
        print("Invalid option")
        sys.exit(1)
