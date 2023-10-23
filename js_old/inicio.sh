#!/bin/bash

# Script para primeira execução
# CRIADO POR: LUIZ PAULO
# 21/09/2023

if [[ $(docker image ls -a | grep 'sysdistr/back' | wc -l ) == "1" ]]; then
	echo "abortado: imagem já existe";
	exit;
else
	docker build -t 'sysdistr/back:1.0' . ;
fi

cd ./yml;
docker compose up back;

