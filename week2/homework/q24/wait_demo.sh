#!/bin/bash
sleep 5 &
wait
echo "Done" > wait.log
