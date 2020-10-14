# find-squre


## requirements

this script have been tested under Python 3.8.5

## how to

### generate maps

With x: columns, y: rows, d: density beeing set

```bash
for i in {1..10}
do
    python3 map_gen.py x y d > map$i.txt
done
```

### resolve maps

```bash
python3 find-square map1.txt map2.txt *.txt
```