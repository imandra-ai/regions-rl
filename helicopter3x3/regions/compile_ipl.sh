#!/bin/sh

if [ -z "$1" ]; then
    echo "Specify a python file."
    exit
fi

PROG="import sys;import ast2json;import json; print(json.dumps(ast2json.str2json(sys.stdin.read())))"

echo "Uploading python ast json. "
HASH=$(cat $1 |  python3 -c "$PROG" | curl -X POST -d @- "http://localhost:8000")
echo "Got response: $HASH"

GETURL="http://localhost:8000/$HASH/ipl"
echo "Getting IPL from $GETURL"
curl $GETURL > $1.ipl

echo "Done. Curl command to get regions python:"
echo "cat regions.json | curl -X PUT -d @- http://localhost:8000/$HASH/ite_regions > regions_tree.py"
