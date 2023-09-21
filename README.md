# SIMPLES SERVIDOR HTTP/1.0

construido utilizando o módulo http
do nodejs para as dinâmicas exigências
das aulas de sistemas distribuidos.

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


