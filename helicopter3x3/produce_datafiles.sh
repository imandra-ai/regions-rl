python3 eval3x3.py --outfile regions_data.csv    --regions=True  --nruns=10 --lr 0.01 --rmsize 1000 --steps 50 --playouts 100 --train-size 100 --epochs 20 --batch-size 5
python3 eval3x3.py --outfile regions_data_nr.csv --regions=False --nruns=10 --lr 0.01 --rmsize 1000 --steps 50 --playouts 100 --train-size 100 --epochs 20 --batch-size 5
