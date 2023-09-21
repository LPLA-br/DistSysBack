"use strict";
/********************************
* EMISSOR DE LINHAS DE LOG PARA
* STDOUT DO SERVIDOR PRIMITIVO
*********************************/
Object.defineProperty(exports, "__esModule", { value: true });
exports.Log = void 0;
/** Emissor de linhas de log padronizadas
*   para stdout do servidor
*   @class
* */
class Log {
    /** Contrutor para log das requisições
    *   @constructor
    *   @param {linha | undefined} infos - dados para linha de log
    * */
    constructor(infos) {
        if (typeof infos != "undefined") {
            infos.timestamp = Date.now().toString();
            this.ln = infos;
        }
    }
    /**	Getter retornador de um objeto de linha de log
    * */
    get getLinha() {
        return this.ln;
    }
    /**	Setter alterador de um objeto de linha de log
    * */
    set setLinha(infos) {
        this.ln = infos;
    }
}
exports.Log = Log;
;
