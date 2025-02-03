#!/bin/bash

cont=1
term=30

while [ $term -ge $cont ]
do
    echo "Run: $cont"
    python3 tuning_node_de.py $cont
    let cont=$cont+1
done