/*************************************
 * BACKEND DE API PARA APLICAÇÃO
 * UTILIZANDO MÓDULO HTTP PRIMITIVO
 * Criado em: 27/09/2022
 * Desenvolvedores:
 * ·Luiz Paulo 		https://github.com/LPLA-br
 * ·José Edson 		https://github.com/Edson-Silva-22
 * ·Jasiel Oliveira	https://github.com/Jasielsouza7
 *
 *************************************/

import http from 'node:http';
import { Respostas } from './classes/respostas';
import { Log } from './classes/log';
import { parametros } from './config/config';

const resposta = new Respostas( {} );
const log = new Log();

const server = http.createServer( ( req, res )=>
{
	switch( req.url )
	{
		case '/':
			if ( req.method == 'GET' )
			{
				let stat: number = 200;
				resposta.altResp = { stat: stat, msg: 'backend primitivo Versão 0.0.1' };

				res.writeHead( stat, { 'Content-Type': 'application/json' });
				res.write( resposta.getResp );

				log.setLinha = { url: req.url, metodo: req.method.toString(), cliente: req.socket.remoteAddress, status: stat.toString() };
				console.log( log.getLinha );
			}
			else
			{
				let stat: number = 405;
				resposta.altResp = { status: stat, msg: 'Método não permitido para esta rota' };

				res.writeHead( stat, { 'Content-Type': 'application/json' });
				res.write( resposta.getResp );

				log.setLinha = { url: req.url, metodo: req.method?.toString(), cliente: req.socket.remoteAddress, status: stat.toString() };
				console.log( log.getLinha );
			}
			res.end();
			break;
		default:
			resposta.altResp = { status: 404, msg: 'Recurso solicitado não foi encontrado' };

			res.writeHead( 404, { 'Content-Type': 'application/json' });
			res.write( resposta.getResp );

			log.setLinha = { url: 'Erro', metodo: req.method?.toString(), cliente: req.socket.remoteAddress, status: '404' };
			console.log( log.getLinha );
			break;
	}
	res.end();
});


server.listen( parametros.porta, ()=>{ console.log( `ouvindo porta ${parametros.porta}` ) } );
