
# PYNC
### Python Network Companion

![Debian](https://img.shields.io/badge/Debian-13-A81D33?style=for-the-badge&logo=debian&logoColor=white)
![Linux](https://img.shields.io/badge/Linux-000000?style=for-the-badge&logo=linux&logoColor=FCC624)
![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=FFD43B)
![i3wm](https://img.shields.io/badge/i3wm-088CCB?style=for-the-badge&logo=i3&logoColor=white)

PYNC (Python Network Companion) é um projeto de estudos desenvolvido durante o curso **Python para Pentesters**, ministrado por Messias Eric.

O objetivo é construir, de forma incremental, uma ferramenta inspirada no Netcat, utilizando apenas Python e os conceitos apresentados ao longo do curso. Cada nova aula poderá resultar em melhorias, novas funcionalidades e refatorações, fazendo deste repositório um registro da evolução do aprendizado.

> Este projeto possui finalidade exclusivamente educacional.

---

## Objetivos

- Estudar programação em Python aplicada à Segurança da Informação.
- Praticar Programação Orientada a Objetos.
- Desenvolver uma arquitetura reutilizável para ferramentas de rede.
- Implementar recursos semelhantes aos encontrados no Netcat.
- Evoluir o código conforme o avanço no curso.

---

## Estado atual

Atualmente o projeto está nas etapas iniciais.

As primeiras implementações contemplam:

- Estrutura inicial do projeto;
- Organização em classes;
- Métodos para comunicação TCP e UDP;
- Separação da lógica em módulos.

---

## Funcionalidades planejadas

- [x] Estrutura baseada em classes
- [x] Cliente TCP
- [x] Servidor TCP
- [x] Cliente UDP
- [x] Servidor UDP
- [x] Interface por linha de comando (CLI)
- [ ] Transferência de arquivos
- [ ] Shell remoto (ambiente controlado de laboratório)
- [ ] Múltiplos clientes
- [ ] Criptografia das comunicações
- [ ] Logs

---

## Estrutura do projeto

```text
.
├── main.py
├── src
│   ├── engine.py
│   └── flow.py
└── README.md
````

---

## Como executar

Clone o repositório:

```bash
git clone https://github.com/Theus-Vieira/tool-pync-python.git
```

Entre na pasta:

```bash
cd tool-pync-python
```

Execute:

```bash
python3 main.py --help
```

---

## Tecnologias

* Python 3
* Programação Orientada a Objetos
* Sockets TCP/UDP
* Linux

---

## Aviso

Este projeto foi desenvolvido para fins de estudo e treinamento em redes de computadores e Segurança da Informação.

Não utilize este software em ambientes ou sistemas sem autorização.

---

## Créditos

Este projeto foi inspirado no desafio proposto durante o curso **Python para Pentesters**, ministrado por **Messias Eric**, e representa uma implementação própria desenvolvida como exercício de aprendizado.

