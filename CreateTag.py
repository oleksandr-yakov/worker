import requests
import sys
import re


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
    repository_name = "oleksandr-yakov/core"
    token = sys.argv[1]
    max_tag = find_max_tag(repository_name, token)
    print(max_tag)
