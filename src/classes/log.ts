/********************************
* EMISSOR DE LINHAS DE LOG PARA
* STDOUT DO SERVIDOR PRIMITIVO
*********************************/

/**	Definição de uma linha de log para requisições
*	@param {string} url - url do recurso solicitado pelo cliente
*	@param {string | undefined} metodo - método de requisição http usado pelo cliente
*	@param {string | undefined} status - status de resposta http
*	@param {string | undefined} timestamp - unix timestamp inicializável como string vazia
*	@param {string | undefined} cliente - ip do requisitante 
* */
type linha =
{
	url: string;
	metodo?: string | undefined;
	status?: string | undefined;
	timestamp?: string | undefined;
	cliente?: string | undefined;
};


/** Emissor de linhas de log padronizadas
*   para stdout do servidor
*   @class
* */
class Log
{

	protected ln?: linha;

	/** Contrutor para log das requisições
	*   @constructor
	*   @param {linha | undefined} infos - dados para linha de log
	* */
	constructor( infos?: linha )
	{
		if ( typeof infos != "undefined" )
		{
			infos.timestamp = Date.now().toString();
			this.ln = infos;
		}
	}

	/**	Getter retornador de um objeto de linha de log
	* */
	public get getLinha()
	{
		return this.ln;
	}

	/**	Setter alterador de um objeto de linha de log
	* */
	public set setLinha( infos: linha )
	{
		this.ln = infos;
	}
};

export { Log, linha };
