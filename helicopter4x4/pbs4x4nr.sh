#PBS -N evaluation_regions_44
cd ~/idf-py-eval/evaluation_scripts
python3 eval4x4_noregions.py --outfile regions_data_nr_4x4.csv --nruns=100 --lr 0.01 --rmsize 100000 --steps 50 --playouts 5000 --train-size 5000 --epochs 20 --batch-size 32

