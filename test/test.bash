#!/bin/bash
# SPDX-FileCopyrightText: 2024 Shizen Kotake
# SPDX-License-Identifier: BSD-3-Clause

res=0
dir=~
[ "$1" != "" ] && dir="$1" 

cd $dir/ros2_ws
colcon build
source $dir/.bashrc
timeout 20 ros2 launch mypkg talk_listen.launch.py &> /tmp/test.log

cat /tmp/test.log | grep 'タバコを3本吸いました'
if [ $? = 0 ]; then
    echo FIRST_OK
else
    echo FIRST_NG
    res=1
fi

cat /tmp/test.log | grep '寿命が18分減りました'
if [ $? = 0 ]; then
    echo SECOND_OK
else
    echo SECOND_NG
    res=1
fi

exit $res
