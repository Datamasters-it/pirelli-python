import argparse

def main(urls):
    for idx, url in enumerate(urls):
        file_name = f"file{idx + 1}.txt"
        print(f"URL: {url}, File Name: {file_name}")

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('urls', nargs='+', help='URLs of the files to download')
    args = parser.parse_args()
    print(args.urls)