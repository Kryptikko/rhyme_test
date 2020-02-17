requires python 3.7
```
python3 -m venv ./env
source env/bin/active
pip install -r requirments.txt
python ./main.py <machine_count> <order_json_file>
```

example:
```bash
python ./main.py --help

python ./main.py 1 ./order.json
```
