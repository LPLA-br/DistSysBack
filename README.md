# SIMPLES SERVIDOR HTTP/1.0

Construido utilizando o módulo http
para a primeira dinâmica da disciplina
de sistemas distribuidos.

Descontinuado devido a caracteristicas
embutidas no nodejs que não possibilitam
uma visão mais básica dos conceitos da
disciplina de sistemas distribuidos.

<ul>
    <li> Docker </li>
    <li> Typescript </li>
</ul>

```
1. Compile do typescript ao javascript
   para um diretório build dentro de src.

2. Execute o script inico.sh uma vez para:
   criar a imagem docker e executar o container
   ou ...

3. Execute
   $ docker build -t 'sysdistr/back:1.0' .
   no diretório do Dockerfile Seguido de
   $ docker compose up back
   no diretório yml que contém o .yml
```


# SERVIDOR & CLIENTES - PYTHON ---------------------------

<p>
    Servidor e clientes
    implementação simplificada
    para disciplina de
    sistemas distribuidos.
</p>

## REQUISITOS FUNCIONAIS

<ol>
    <li> Formar conexões tcp com o agente-usuário do cliente </li>
    <li> Definir funcionalidade a ser servida para o cliente </li>
    <li> Implementar tratamento de erros para operações falhas no cliente e servidor </li>
    <li> Implementar log para stdout do terminal do servidor </li>
    <li> Utilizar threads para permitir o tratamento simultâneo de N requisições </li>
    <li> Empregar fila de controle para requisições sensíveis que não podem ocorrer simultâneamente </li>
    <li> Empregar controle por pid do processo requisitor </li>
</ol>

## INTEGRANTES DO TRIO

<ol>
    <li> Luiz Paulo de Lima Araújo </li>
    <li> José Edson da Silva Galdino </li>
    <li> Jasiel Oliveira Nascimento Souza </li>
</ol>

## Mestre: Denys Alexandre Barboza da Silva

