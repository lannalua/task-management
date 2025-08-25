# 📝 - Task Management:
- API de Gerenciamento de Tarefas

##Objetivo do projeto:
Avaliar a cobertura dos casos de teste do repositório original com a utilização da técnica de Testes de Mutação com o mutmut. 

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

# Guia de Workflow do Projeto de Gerenciamento de Tarefas

Este guia detalha os passos para configurar, executar e testar a aplicação de gerenciamento de tarefas.

## 1. Configuração Inicial

Para começar, clone o repositório do projeto e configure o ambiente virtual.

```sh 
git clone https://github.com/lannalua/task-management
sudo apt install python3-venv
cd task-management
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## 2. Servidor Flask

Para executar os testes é necessário inicializar o servidor em um terminal a parte:
```coverage run --parallel-mode app.py```

## 3. Executando os Testes e Analisando a Cobertura

Renomeia o arquivo de teste para seguir a convenção do mutmut
```mv tests.py test_app.py```

---Executa os testes com verbosidade
```pytest -vv test_app.py```

--- Relatórios de Cobertura
Para ver a cobertura diretamente no terminal:
```pytest -vv --cov=app --cov-report=term-missing```
Para gerar um relatório HTML detalhado:
```pytest -vv test_app.py --cov=app --cov-report=html --cov-report=term-missing```

O relatório HTML será gerado na pasta htmlcov. Abra o arquivo index.html no seu navegador para visualizá-lo.

## 4. Testes de Mutação com MutMut

Use mutmut para encontrar pontos fracos nos seus testes.Primeiro, crie o arquivo ```setup.cfg``` no diretório raiz do projeto e adicione o seguinte conteúdo:
```sh
touch setup.cfg
nano setup.sfg
```

```sh
[mutmut]
paths_to_mutate=app.py
runner=pytest -x --tb=short --disable-warnings
tests_dir=.
```

Agora você pode rodar os testes de mutação e ver os resultados.
### Executa os testes de mutação
```mutmut run```

### Exibe os resultados
```mutmut results```
