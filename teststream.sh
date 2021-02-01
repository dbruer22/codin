ffmpeg \
-f alsa -i plughw:CARD=U0x46d0x825,DEV=0 \
-f v4l2 -i /dev/video0 \
-c:v libx264 -pix_fmt yuv420p -preset ultrafast -g 10 -b:v 1200 \
-bufsize 512k \
-acodec libmp3lame -ar 44100 \
-threads 2 -qscale 3 \
-b:a 128K \
-r 5 \
-s 640x480 \
-f flv rtmp://a.rtmp.youtube.com/live2/uy16-g4ze-j95j-qtjm-2733


ffmpeg -f v4l2 -i /dev/video -bsf dump_extra -an -r 20 -codec:v h264_omx -profile:v baseline -f rtp rtp://0.0.0.0:8004?pkt_size=1300
