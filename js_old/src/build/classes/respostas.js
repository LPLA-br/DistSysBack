"use strict";
/**************************
 * DEFINIÇÃO DE RESPOSTAS
 * Aumentando o nível de
 * abstração da aplicação
 **************************/
Object.defineProperty(exports, "__esModule", { value: true });
exports.Respostas = void 0;
/**	Classe para construção de respostas
* 	JSON às requisições HTTP
*	@class
* */
class Respostas {
    /**	Construtor da resposta.
    *	@constructor
    *	@param {object} - objeto que será stringficado
    * */
    constructor(obj) {
        this.resposta = JSON.stringify(obj);
    }
    /**	Getter fornecedor de string JSON de um objeto.
    * 	@method
    * */
    get getResp() {
        return this.resposta;
    }
    /**	Altera a string JSON a ser retornada.
    * 	@method
    * 	@param {object} - objeto que alterará a string
    * */
    set altResp(nobj) {
        this.resposta = JSON.stringify(nobj);
    }
}
exports.Respostas = Respostas;
;
