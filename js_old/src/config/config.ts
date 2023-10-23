/*******************************
* PARÂMETROS DE CONFIGURAÇÃO 
* DO SERVIDOR
********************************/

/**	Definição do objeto com configuração
*	@type
*	@param {string} porta
*	@param {string} versão
*
* */
type confCorpo =
{
	porta: 	number;
	versao: string;
};

const parametros: confCorpo =
{
	porta: 8080,
	versao: '1.0',
};

export { parametros };
