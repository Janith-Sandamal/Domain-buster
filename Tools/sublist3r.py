import subprocess

def run_sublist3r(domain):
    """Run Sublist3r for domain enumeration."""
    try:
        result = subprocess.run(['sublist3r', '-d', domain], capture_output=True, text=True, check=True)
        return result.stdout.splitlines()  # Return a list of subdomains
    except subprocess.CalledProcessError as e:
        print(f"Error running Sublist3r: {e}")
        return []
