# Find best square

## Requirement

This script have been tested under Python 3.8.5.

## How to

### Generate maps

With values for x: columns, y: rows and d: density:

```bash
for i in {1..10}
do
    python3 map_gen.py x y d > map$i.txt
done
```

### Resolve maps

```bash
python3 find_square.py map1.txt map2.txt *.txt
```