#!/bin/sh

ALVO=$1
PORTA=$2

if [[ $ALVO == '' || $PORTA == '' ]]; then
  echo 'comando ALVO PORTA';
fi

# DISPARA N CLIENTES SIMULTÂNEAMENTE

./cliente.py $ALVO $PORTA 1 1  1 &
./cliente.py $ALVO $PORTA 1 1  1 &
./cliente.py $ALVO $PORTA 1 2  2 &
./cliente.py $ALVO $PORTA 1 2  2 &
./cliente.py $ALVO $PORTA 1 3  3 &
./cliente.py $ALVO $PORTA 1 3  3 &

