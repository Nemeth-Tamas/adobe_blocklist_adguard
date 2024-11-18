# get fresh list at https://a.dove.isdumb.one/list.txt
# convert list from hostfile format to adguard home dns format

import requests


def get_hostfile(url):
    r = requests.get(url)
    return r.text


def convert_hosts_to_adguard_blocklist_from_url(url, output_file):
    """
    Converts a Windows hosts file from a URL to an AdGuard Home blocklist format.

    Args:
        url (str): URL to the hosts file.
        output_file (str): Path to the output AdGuard blocklist file.
    """
    try:
        hosts_content = get_hostfile(url)
        with open(output_file, 'w') as outfile:
            for line in hosts_content.splitlines():
                # Strip any leading/trailing whitespace from the line
                line = line.strip()

                # Ignore comments and empty lines
                if line.startswith('#') or not line:
                    continue

                # Split the line into parts (space-separated), and take the domain (second part)
                parts = line.split()
                if len(parts) > 1:
                    domain = parts[1]
                    # Write in AdGuard blocklist format
                    outfile.write(f"||{domain}^\n")

        print(f"Blocklist successfully created at {output_file}")
    except Exception as e:
        print(f"An error occurred: {e}")


# Example usage
# Replace with your desired output file path
output_file_path = "adguard_blocklist.txt"
convert_hosts_to_adguard_blocklist_from_url(
    "https://a.dove.isdumb.one/list.txt", output_file_path)
