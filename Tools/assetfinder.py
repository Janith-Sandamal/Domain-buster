import subprocess

def run_assetfinder(domain):
    """Run Assetfinder for domain enumeration."""
    try:
        result = subprocess.run(['assetfinder', '--subs', domain], capture_output=True, text=True, check=True)
        return result.stdout.splitlines()  # Return a list of subdomains
    except subprocess.CalledProcessError as e:
        print(f"Error running Assetfinder: {e}")
        return []
