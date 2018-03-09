#!/usr/bin/sh

function save() {
	brightnessctl -s
}

function dim() {
	local step=$1
	# Use $1 to define step, otherwise fallback to 3%
	if [ -z "$1" ] then
		step=3
	fi
	brightnessctl set step%-
	sleep 0.100 # 100ms of sleep
}


