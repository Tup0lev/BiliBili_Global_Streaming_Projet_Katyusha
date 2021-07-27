#INFO

PROXY=""
echo $PROXY
SRC=""
echo $SRC
RTMP_ADDR=""
echo $RTMP_ADDR
RTMP_KEY=""
echo $RTMP_KEY

#LOOP

until false

do

POLL_INTERVAL=$(( $RANDOM % 15 + 5 ))

T=$(date +"%H_%M")

echo "Title = $T"

#CHECK STREAM
if
curl --proxy $PROXY -A "User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36" $SRC --silent | grep -o -m 1 -q "$T" ;
then

echo "STREAM ACTIVE, WILL START FFMPEG"
streamlink --http-proxy "$PROXY" $SRC best -o - | ffmpeg -i - -acodec copy -vcodec copy -f flv "$RTMP_ADDR$RTMP_KEY"

else
echo "STREAM INACTIVE, QUITTING"

echo INT=$POLL_INTERVAL

sleep $POLL_INTERVAL
fi

done