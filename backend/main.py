import argparse

from services.converter import run_converter


def main():
    url = ""  # Default URL
    
    parser = argparse.ArgumentParser(description='Convert Youtube videos to MP3')
    parser.add_argument('url', nargs='?', help='Youtube URL to convert')
    
    args = parser.parse_args()
    
    # Use provided URL or default to the variable
    convert_url = args.url if args.url else url

    print(f"Converting: {convert_url}")
    success = run_converter(convert_url)

    if success:
        print("MP3 Downloaded")
    else:
        print("Failed")

if __name__ == "__main__":
    main()