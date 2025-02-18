#!/usr/bin/env python3
"""
Basic Python script to fetch posts from JSONPlaceholder using requests.get()
"""
import requests
import csv


def fetch_and_print_posts():
    """
    Function that fetches posts from JSONPlaceholder
    and save to posts.csv with columns: id, title, and body.
    """
    response = requests.get('https://jsonplaceholder.typicode.com/posts')
    print("Status Code: {}".format(response.status_code))
    if response.status_code == 200:
        posts = response.json()
        for post in posts:
            print(post["title"])


def fetch_and_save_posts():
    """
    Function that fetches all post from JSONPlaceholder.
    """
    response = requests.get('https://jsonplaceholder.typicode.com/posts')
    if response.status_code == 200:
        posts = response.json()
        formatted_posts = [
            {"id": post["id"], "title": post["title"], "body": post["body"]}
            for post in posts
        ]

        with open('posts.csv', 'w', newline='') as csvfile:
            fieldnames = ['id', 'title', 'body']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            for post in formatted_posts:
                writer.writerow(post)


if __name__ == "__main__":
    fetch_and_print_posts()
    fetch_and_save_posts()
