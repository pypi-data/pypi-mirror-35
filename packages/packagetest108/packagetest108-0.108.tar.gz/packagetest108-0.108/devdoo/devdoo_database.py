#!/usr/bin/env python
# -*- coding: utf-8 -*-

import zmq, json
from service_db import ServiceDB
from service import Service
from yml import Yml
from status import Status
from pymongo import MongoClient

# Conecta ao banco de dados
db_host = 'database.unicoode.com'
db_username = 'devdoo'
db_password = 'mudar123'
db_database = 'admin'
db_port = 27017
mongo_server = MongoClient(
    db_host,
    username=db_username,
    password=db_password,
    authSource=db_database,
    authMechanism='SCRAM-SHA-1',
    port=db_port)
#mongo_server = MongoClient(db_host, db_port)

# TODO:: Enviar para o servidor console a informação de falha de configuração
class DevdooDatabase(object):

    # --------------------------------
    # Error
    # --------------------------------
    # TODO:: Remover classe de error
    class Error(Exception):
        pass

    # --------------------------------
    # __init__
    # --------------------------------
    def __init__(self):
        super(DevdooDatabase, self).__init__()

        # Variaveis default
        self.id = None
        self.service = None
        self.serviceDB = None
        self.zmq_socket_broker = None

        # Variaveis inicializadas
        self.status = Status()

        # Verifica se o arquivo de configuração foi inicalizado corretamente
        if self.__has_config():
            self.__init()
        else:
            self.status.error("INVALID_SERVICE", None, ["FALHA NA INICIALIZACAO DO SERVICO", "DEVDOO-DATABASE"])
            self.status.to_print()

    # --------------------------------
    # __has_config
    # --------------------------------
    '''
    Obtem configurações do servico

    :return: boolean
    '''
    def __has_config(self):
        # Recupera o identificador do servico
        yml = Yml(self.status)
        self.id = yml.id()

        # Verifica se existe um identificador do servico
        if self.status.ready() and self.id:
            self.service = Service(self.id, self.status, True)

        # Retorna o status do serviço de banco
        return self.status.ready() and self.service and self.service.ready()

    # --------------------------------
    # __init
    # --------------------------------
    '''
    Inicializa o serviço

    :return: void
    '''
    def __init(self):
        # Cria contexto ZMQ
        context = zmq.Context()

        # Adaptador de conexão com o broker
        self.zmq_socket_broker = context.socket(zmq.REP)

        # Conecta ao broker secundário
        self.zmq_socket_broker.connect(self.service.broker_connect_backend())

        # Executa o loop da operação
        self.run()

    # --------------------------------
    # operation
    # --------------------------------
    # Executa a ação do Serviço
    #
    # TODO:: Implementar controle ready antes de seguir adiante
    def operation(self):
        # Recebe a mensagem do broker secundário
                 #self.zmq_socket_broker.recv()
        message = self.zmq_socket_broker.recv_multipart()
        self.serviceDB = ServiceDB(message, mongo_server)

        print "RECEBEU DO REST------->>>>", type(message), message
        # print "\nRECEBEU DO REST BBBB------->>>>", type(self.serviceDB.send_result()), self.serviceDB.send_result()

        # Envia mensagem de retorno para o cliente
        self.zmq_socket_broker.send_multipart(self.serviceDB.send_result())

    # --------------------------------
    # operation
    # --------------------------------
    # Executa a ação do Serviço
    #
    def operationXXX(self):
        # self.serviceDB = ServiceDB(self.zmq_socket_broker.recv(), self.config)
        print "self.service =========>>> ", self.service

        # Recebe a mensagem do broker secundário
        message = self.zmq_socket_broker.recv_multipart()
        # print "\nRECEBEU DO REST------->>>>", type(message), message

        # Converte a mensagem em um JSON válido
        valid_json = json.dumps(message[0])
        # print "\nCONVERTED ---->>>>", type(valid_json), valid_json

        # Converte o JSON em dicionário
        message_json = json.loads(json.loads(valid_json))
        # print "\nMESSAGE JSON ---->>>>", type(message_json), message_json

        # Processa a operacao
        # self.zmq_socket_broker.send(self.serviceDB.send())

        # Preenche o campo data (exemplo)
        message_json["body"]["data"] = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"

        # Gera lista de retorno e adiciona a mensagem
        message = list()
        message.append(json.dumps(message_json))
        print "\nRETURN MESSAGE =====>", type(message), message

        # Envia mensagem de retorno para o cliente
        self.zmq_socket_broker.send_multipart(message)
        # print "ENVIA DE VOLTA AO REST<<<<<-------------------", message

    # --------------------------------
    # run
    # --------------------------------
    # Executa a operação em um loop infinito
    #
    # TODO:: Implementar ping de verificação de disponibilidade do serviço
    def run(self):
        while True:
            try:
                self.operation()
            except DevdooDatabase.Error:
                # except Exception as inst:
                #    print "API_DB::RUN::ERROR", inst.args
                self.status.error("SERVICE_FAILURE", None, ["FALHA NA EXECUCAO DO SERVICO", "DEVDOO-DATABASE"])
                self.status.to_print()
