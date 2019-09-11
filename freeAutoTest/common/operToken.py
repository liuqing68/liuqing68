# coding=utf-8 

from getRootPath import root_dir
import os

token_file = os.path.join(root_dir, "conf", "tokens")


def write_file(token):
	with open(token_file, "w") as fp:
		fp.write(token)


def read_token():
	with open(token_file) as fp:
		return eval((fp.readlines()[0]))


if __name__ == "__main__":
	token = "12345"
	write_file(token)
	print(read_token()["assertToken"])
	print(read_token()["centerToken"])
	print(read_token()["fundToken"])
