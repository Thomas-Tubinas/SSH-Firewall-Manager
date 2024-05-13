#!/bin/bash

# Create "Attack info" directory if it doesn't exist
mkdir -p "Attack info"

# Function to execute whois command and save output
execute_whois() {
    ip="$1"
    output_file="Attack info/${ip}_whois.txt"
    whois "$ip" > "$output_file"
    echo "Whois information for $ip saved to $output_file"
}

# Read lines from input file
input_file="activity_log.txt"

if [ ! -f "$input_file" ]; then
    echo "Error: Input file '$input_file' not found."
    exit 1
fi

# Process each line from the input file
while IFS= read -r line || [ -n "$line" ]; do
    # Check if the line contains "whois" command
    if [[ "$line" == *"whois "* ]]; then
        # Extract IP address from the line
        ip=$(echo "$line" | awk '{print $2}')
        
        # Execute whois command for the IP address
        execute_whois "$ip"
    fi
done < "$input_file"
