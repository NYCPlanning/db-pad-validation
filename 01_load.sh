# Create dir
mkdir -p data

# Download from Bytes
curl -O https://www1.nyc.gov/assets/planning/download/zip/data-maps/open-data/pad19a.zip

# Unzip
unzip pad19a.zip -d data/tmp

# Remove .zip
rm *.zip