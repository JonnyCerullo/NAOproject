if [ $# -eq 2 ]
then
	cd choreography_generator
	python3 choreography_planner.py

	cd ../choreography_player
	python2.7 choreography_player.py $1 $2
else
  echo 'parameter not valid'
fi