#!/bin/bash

usage ()
{
	echo ""
	echo "pingscan ver.0.1"
	echo "Script para escanear un rango de IPs con ping"
	echo ""
	echo "Uso:"
	echo "pingscan -r <red> -i <inicio> -f <fin> -o|-d (ocupadas)|(desocupadas)"
	echo ""
	echo "pingscan -h (Este menu)"
	echo ""
	echo "Ejemplo: Revisar las IPs desocupadas en el rango 172.17.102.65 - 172.17.102.127"
	echo "pingscan -r 172.17.102 -i 65 -f 127 -o d"
	echo ""
	exit 1

}
oc=0
u=7
while getopts ":r:i:f:odh" opt; do
  case $opt in
    r)
      red=$OPTARG >&2
      ;;
    i)
	  ip_inicio=$OPTARG >&2
	  ;;
	f)
	  ip_fin=$OPTARG >&2
	  ;;
	o) oc=o >&2
	;;
	d) oc=d >&2
	;;
	h) usage
		exit 1
	;;
    \?)
      echo "Opcion invalida: -$OPTARG" >&2
      exit 1
      ;;
    :)
      echo "La opcion -$OPTARG requiere un argumento." >&2
      exit 1
      ;;
  esac
done
if [ $OPTIND -lt 7 ]; then
	usage
fi

#echo $red $ip_inicio $ip_fin
case "$oc" in 
o) 	echo "Listado de IPs ocupadas"
	for ((i=$ip_inicio ; i<=ip_fin ; i++))
  	do
     	ping -q -c 1  $red.$i  &>/dev/null
     	rc=$?
     	#echo $rc
     	if [ $rc -eq 0 ]; then
     		echo  $red.$i
     	fi 
 	done
;;
d)	echo "Listado de IPs desocupadas"
	for ((i=$ip_inicio ; i<=ip_fin ; i++))
  	do
     	ping -q -c 1  $red.$i  &>/dev/null
     	rc=$?
     	#echo $rc
     	if [ $rc -ne 0 ]; then
     		echo  $red.$i
     	fi 
 	done
 ;;
 *) echo "Listado de IPs ocupadas"
	for ((i=$ip_inicio ; i<=ip_fin ; i++))
  	do
     	ping -q -c 1  $red.$i  &>/dev/null
     	rc=$?
     	#echo $rc
     	if [ $rc -eq 0 ]; then
     		echo  $red.$i
     	fi 
 	done
 ;;	
esac