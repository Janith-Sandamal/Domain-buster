import subprocess
import json

def run_amass(domain):
    """Run Amass for domain enumeration."""
    try:
        result = subprocess.run(['amass', 'enum', '-d', domain, '-json'], capture_output=True, text=True, check=True)
        return json.loads(result.stdout)  # Return the parsed JSON output
    except subprocess.CalledProcessError as e:
        print(f"Error running Amass: {e}")
        return []
