if [ ! -d output/$1 ]
then
    mkdir output/$1
fi

python src/fingerprinting.py input/$1/$1.html output/$1/fingerprinting.json
python src/pixel_track.py input/$1/$1.har output/$1/pixel_track.json
python src/cookie_sync.py input/$1/$1.har output/$1/cookie_sync.json
python src/cookies.py input/$1/$1.har output/$1/cookies.json