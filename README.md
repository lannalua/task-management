# 📝 - Task Management:
- API de Gerenciamento de Tarefas

## ✅ - Vantagens do Flask:

- Simplicidade: Uma das vantagens do Flask é a sua simplicidade e sua facilidade no aprendizado. Seu código é legivel e intuitivo, tornando-o uma escolha popular para iniciantes e desenvolvedores experientes;
- Escalabilidade: o Flask pode ser estendido com várias extensões e bibliotecas para adicionar funcionalidades conforme necessário. Isso permite escalabilidade à medida que os projetos crescem;
- Flexibilidade: O Flask permite aos desenvolvedores escolherem suas próprias ferramentas e bibliotecas para construir aplicações personalizadas. Ele não impõe estruturas rígidas, permitindo uma abordagem mais flexível para o desenvolvimento.

## ✏️ - Funcionalidades: 

- CREATE;
- READ;
- UPDATE;
- DELETE;

## ⚙️ - Ferramentas/Tecnologias:

- Python;
- Flask;
- Pytest;

Guia de Workflow do Projeto de Gerenciamento de TarefasEste guia detalha os passos para configurar, executar e testar a aplicação de gerenciamento de tarefas.
## 1. Configuração Inicial
Para começar, clone o repositório do projeto e configure o ambiente virtual.# Clona o repositório
git clone https://github.com/lannalua/task-management

## Instala o venv (se necessário)
sudo apt install python3-venv

## Entra no diretório do projeto
cd task-management

## Cria e ativa o ambiente virtual
python -m venv venv
source venv/bin/activate

## Instala as dependências do projeto
pip install -r requirements.txt
## 2. Instalação e Execução de TestesInstale as bibliotecas necessárias para testes e cobertura de código.# Instala as bibliotecas de teste
pip install coverage
pip install pytest
Observação: A biblioteca python-cov não é necessária, pois a coverage já cobre essa funcionalidade quando usada com pytest.Para rodar o aplicativo e gerar os dados de cobertura, use o comando:# Roda o aplicativo e coleta dados de cobertura
coverage run --parallel-mode app.py
Dica: Para evitar o erro "no data results", certifique-se de que os arquivos de teste estão usando o client em vez da biblioteca requests para fazer as requisições. Você pode precisar mover ou renomear o arquivo tests.py para test_app.py para que o pytest o encontre automaticamente.
## 3. Executando os Testes e Analisando a Cobertura

Depois de preparar o ambiente, você pode executar os testes e gerar relatórios de cobertura.# Renomeia o arquivo de teste para seguir a convenção do pytest
mv tests.py test_app.py

# Executa os testes com verbosidade
pytest -vv test_app.py
Relatórios de CoberturaPara ver a cobertura diretamente no terminal:pytest -vv --cov=app --cov-report=term-missing
Para gerar um relatório HTML detalhado:pytest -vv test_app.py --cov=app --cov-report=html --cov-report=term-missing
O relatório HTML será gerado na pasta htmlcov. Abra o arquivo index.html no seu navegador para visualizá-lo.
## 4. Testes de Mutação com MutMutUse mutmut para encontrar pontos fracos nos seus testes.Primeiro, crie o arquivo setup.cfg no diretório raiz do projeto e adicione o seguinte conteúdo:
[mutmut]
paths_to_mutate=app.py
runner=pytest -x --tb=short --disable-warnings
tests_dir=.

Agora você pode rodar os testes de mutação e ver os resultados.# Executa os testes de mutação
mutmut run

# Exibe os resultados
mutmut results
