#!/bin/bash
# Load credentials
source .env

echo "--- Lab Session: $(date) ---"

# 1. ORCID Authentication
echo "Authenticating ORCID iD: 0009-0004-2154-7555..."
TOKEN_RESPONSE=$(curl -s -X POST https://orcid.org/oauth/token \
  -H "Accept: application/json" \
  -d "client_id=$ORCID_CLIENT_ID" \
  -d "client_secret=$ORCID_CLIENT_SECRET" \
  -d "grant_type=client_credentials" \
  -d "scope=/read-public")

ORCID_ACCESS_TOKEN=$(echo $TOKEN_RESPONSE | grep -oP '(?<="access_token":")[^"]*')

if [ -z "$ORCID_ACCESS_TOKEN" ]; then
    echo "ORCID Auth Failed."
else
    echo "Identity Verified. Token Secured."
fi

# 2. Run Nasdaq Analysis
echo "Fetching Nasdaq 100 Level..."
PRICE=$(python3 nasdaq_engine.py)
echo "Current Market Pulse: \$ $PRICE"
echo "--------------------------------------"
