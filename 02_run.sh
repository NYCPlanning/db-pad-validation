# create dir
mkdir -p output/high
mkdir -p output/low

# generate report for high house numbers 
docker run --rm \
    -v `pwd`:/db-pad-validation\
    -w /db-pad-validation\
    sptkl/docker-geosupport:19a python3 geocode_high.py

# generate report for low house numbers
docker run --rm \
    -v `pwd`:/db-pad-validation\
    -w /db-pad-validation\
    sptkl/docker-geosupport:19a python3 geocode_low.py