"use strict";
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
var __importDefault = (this && this.__importDefault) || function (mod) {
    return (mod && mod.__esModule) ? mod : { "default": mod };
};
Object.defineProperty(exports, "__esModule", { value: true });
const node_http_1 = __importDefault(require("node:http"));
const respostas_1 = require("./classes/respostas");
const log_1 = require("./classes/log");
const config_1 = require("./config/config");
const resposta = new respostas_1.Respostas({});
const log = new log_1.Log();
const server = node_http_1.default.createServer((req, res) => {
    var _a, _b;
    switch (req.url) {
        case '/':
            if (req.method == 'GET') {
                let stat = 200;
                resposta.altResp = { stat: stat, msg: 'backend primitivo Versão 0.0.1' };
                res.writeHead(stat, { 'Content-Type': 'application/json' });
                res.write(resposta.getResp);
                log.setLinha = { url: req.url, metodo: req.method.toString(), cliente: req.socket.remoteAddress, status: stat.toString() };
                console.log(log.getLinha);
            }
            else {
                let stat = 405;
                resposta.altResp = { status: stat, msg: 'Método não permitido para esta rota' };
                res.writeHead(stat, { 'Content-Type': 'application/json' });
                res.write(resposta.getResp);
                log.setLinha = { url: req.url, metodo: (_a = req.method) === null || _a === void 0 ? void 0 : _a.toString(), cliente: req.socket.remoteAddress, status: stat.toString() };
                console.log(log.getLinha);
            }
            res.end();
            break;
        default:
            resposta.altResp = { status: 404, msg: 'Recurso solicitado não foi encontrado' };
            res.writeHead(404, { 'Content-Type': 'application/json' });
            res.write(resposta.getResp);
            log.setLinha = { url: 'Erro', metodo: (_b = req.method) === null || _b === void 0 ? void 0 : _b.toString(), cliente: req.socket.remoteAddress, status: '404' };
            console.log(log.getLinha);
            break;
    }
    res.end();
});
server.listen(config_1.parametros.porta, () => { console.log(`ouvindo porta ${config_1.parametros.porta}`); });
