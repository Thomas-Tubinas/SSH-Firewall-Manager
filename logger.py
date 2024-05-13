import re
import sys

def parse_log(file_path):
    close_pattern = re.compile(r'Connection closed by authenticating user (\w+) (\d+\.\d+\.\d+\.\d+) port (\d+) \[preauth\]')
    accept_pattern = re.compile(r'Accepted publickey for (\w+) from (\d+\.\d+\.\d+\.\d+) port (\d+)')
    invalid_user_pattern = re.compile(r'Invalid user (\w+) from (\d+\.\d+\.\d+\.\d+) port (\d+)')
    close_dict = {}
    accept_dict = {}
    invalid_user_dict = {}

    try:
        with open(file_path, 'r') as file:
            for line in file:
                close_match = close_pattern.search(line)
                accept_match = accept_pattern.search(line)
                invalid_user_match = invalid_user_pattern.search(line)

                if close_match:
                    user, ip, port = close_match.groups()
                    if ip not in close_dict:
                        close_dict[ip] = {'user': user, 'ports': set()}
                    close_dict[ip]['ports'].add(port)

                if accept_match:
                    user, ip, port = accept_match.groups()
                    if ip not in accept_dict:
                        accept_dict[ip] = {'user': user, 'ports': set()}
                    accept_dict[ip]['ports'].add(port)

                if invalid_user_match:
                    user, ip, port = invalid_user_match.groups()
                    if ip not in invalid_user_dict:
                        invalid_user_dict[ip] = {'user': user, 'ports': set()}
                    invalid_user_dict[ip]['ports'].add(port)

    except FileNotFoundError:
        print(f"Error: The file {file_path} does not exist.")
        sys.exit(1)
    except Exception as e:
        print(f"An error occurred: {e}")
        sys.exit(1)

    return close_dict, accept_dict, invalid_user_dict

def display_results(close_dict, accept_dict, invalid_user_dict):
    print("Closed Connections:")
    for ip, info in close_dict.items():
        print(f"whois {ip}")

    print("\nInvalid User Attempts:")
    for ip, info in invalid_user_dict.items():
        print(f"whois {ip}")

def main():
    file_path = #Replace with path to file
    close_dict, accept_dict, invalid_user_dict = parse_log(file_path)
    display_results(close_dict, accept_dict, invalid_user_dict)

if __name__ == "__main__":
    main()
