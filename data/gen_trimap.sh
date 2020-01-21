
ROOT=./
DIRECTORY="$ROOT"trimap
if [ ! -d "$DIRECTORY" ]; then
	mkdir trimap	  
fi
python3 gen_trimap.py \
	--mskDir=./mask \
	--saveDir=./trimap \
	--list=./mask.txt --size=10	
