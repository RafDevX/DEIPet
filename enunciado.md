# DEIPet
Após muita dificuldade em determinar as melhores pessoas para manter uma reunião no Zoom interessante, o CP decidiu que cada departamento tem de manter um registo de todos os animais de estimação dos seus alunos e professores. Como departamento de informática não vamos desperdiçar a oportunidade de disponibilizar mais gatos na internet, e por isso desenvolverá a aplicação *DEIPet* que ajuda na gestão da lista de animais de estimação (já com centenas de entradas!).

Por preocupações relacionadas com a proteção de dados, a DSI achou por bem limitar a sua API[1], que alimentará o *DEIPet*, para mostrar apenas dados dos animais de estimação.

O objectivo deste exercício é desenvolver a aplicação **DEIPet** usando a framework **Django**[2][3] (versão 3.1.x).

A aplicação DEIPet vai interagir com a API Petstore[1]. Deve testar os exemplos dados para cada operação de modo a perceber as características dos pedidos à API.

A aplicação DEIPet deve implementar as seguintes funcionalidades:
- Uma página que lista todos¹ os *pets* devolvidos pela API numa tabela. A cada entrada da tabela está associada um *pet* e as colunas devem corresponder ao id, nome e à primeira imagem devolvida pela Petstore.
- A página pessoal de cada *pet* que deve conter o nome, id e todas as imagens do *pet*.
- Uma página com um formulário capaz de adicionar novos *pets* através da API fornecida.

Deve realizar o exercício de forma modular: assim que os advogados metediços saírem do nosso caminho, podemos readicionar as associações entre *pets* e donos.
Serão valorizadas qualidade e estética do código e da interface web apresentada.

Deve submeter num arquivo comprimido por email a sua solução e um ficheiro README, que descreva o procedimento para iniciar um servidor local de testes.
Prazo máximo de entrega: domingo, 11 de abril de 2021, 23:59

Recursos potencialmente úteis:
- https://tailwindcss.com/
- https://getbootstrap.com/

Boa Sorte!

Nota: Durante os testes da adição de novos *pets* pedimos que seja responsável nos nomes e imagens utilizadas.

[1]: https://example.com/swagger-ui
[2]: https://www.djangoproject.com/
[3]: https://docs.djangoproject.com/en/3.1/intro/tutorial01/
