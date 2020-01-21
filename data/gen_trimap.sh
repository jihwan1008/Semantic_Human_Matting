
ROOT=./

python3 gen_trimap.py \
	--mskDir=$ROOT/mask \
	--saveDir=$ROOT/trimap \
	--list=./mask.txt --size=10	
