/**************************
 * DEFINIÇÃO DE RESPOSTAS
 * Aumentando o nível de
 * abstração da aplicação
 **************************/

/**	Classe para construção de respostas
* 	JSON às requisições HTTP
*	@class
* */
class Respostas
{

	protected resposta: string;

	/**	Construtor da resposta.
	*	@constructor
	*	@param {object} - objeto que será stringficado
	* */
	constructor( obj: object  )
	{
		this.resposta = JSON.stringify( obj );
	}

	/**	Getter fornecedor de string JSON de um objeto.
	* 	@method
	* */
	public get getResp()
	{
		return this.resposta;
	}

	/**	Altera a string JSON a ser retornada.
	* 	@method
	* 	@param {object} - objeto que alterará a string
	* */
	public set altResp( nobj: object )
	{
		this.resposta = JSON.stringify( nobj );
	}
};

export { Respostas };
