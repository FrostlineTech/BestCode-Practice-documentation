# EXAMPLE SERVICE CONFIGURATION - NOT ACTUAL DEPLOYMENT SCRIPT
# Demonstrates Windows service setup best practices for Django

# 1. SERVICE PARAMETERS EXAMPLE
$serviceName = '{{ ... }}' # Use descriptive service name
$projectRoot = '{{ ... }}' # Path to application root

# 2. ENVIRONMENT CONFIG EXAMPLE
# Always store secrets in secure vaults, never in scripts
# Example using placeholder values:
$env:DB_PASSWORD = '{{ ... }}' # Retrieve from secure storage

# 3. SERVICE REGISTRATION EXAMPLE
# Using NSSM with recommended settings:
# nssm install $serviceName python.exe
# nssm set $serviceName AppParameters runserver
# Note: Actual deployment would use production WSGI server

# 4. LOGGING CONFIG EXAMPLE
# Centralized logging configuration here
# Recommend using application-insights or similar

# SECURITY BEST PRACTICES:
# - Use managed service accounts
# - Enable audit logging
# - Regular credential rotation
