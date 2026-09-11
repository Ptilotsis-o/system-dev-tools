#!/usr/bin/env bash
trap 'echo "USR1 received" >> usr1.log' SIGUSR1
echo "PID: 3976" > usr1.log
while true; do sleep 2; done
