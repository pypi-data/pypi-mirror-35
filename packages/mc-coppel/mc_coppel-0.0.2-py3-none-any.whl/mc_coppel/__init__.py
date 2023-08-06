#coding: utf-8
import sys,os
import pprint
import threading
import time
import json
import datetime
from kafka import KafkaConsumer
from kafka import KafkaProducer
from pymongo import MongoClient
import inspect 
import base64
import json
from colorama import init, Fore, Back, Style
from aiokafka import AIOKafkaProducer,AIOKafkaConsumer
import asyncio


loop = asyncio.get_event_loop()
class db():
    __conexion = None
    __mongoUri = ""
    def __obtenerIpMongo(self):
        miSecreto = ""
        try:
            miSecreto = os.environ["MONGO_CONFIG"]
        except:
            try:
                with open("/run/secrets/MONGO_CONFIG", 'r') as secret_file:
                    miSecreto = secret_file.read()
                    miSecreto = miSecreto.rstrip('\n')
            except:
                print("No se encontro la URI de conexion a mongoDB en variable de entorno (MONGO_CONFIG) ó Secrets Docker (MONGO_CONFIG)")
                print("mongodb://{ip}:{puerto}/")
                sys.exit(0)

        return miSecreto
    
    def __init__(self,mongoUri = ""):
        if mongoUri != "":
            self.__mongoUri = mongoUri
        else:
            self.__mongoUri = self.__obtenerIpMongo()
        
        self.__conexion = None
        
    def conexion(self):
        try:        
            self.__conexion = MongoClient(self.__mongoUri)
            return self.__conexion
        except:
            return None

class microservicio(db):

    db = db
    """
        Clase para conectar el microservicio
        Arguments:
             app (str) -  nombre de la app para la cual es el servicio
             servicio (str) -  nombre del microservicio
    """

    __registrarErroresFlag = False
    __registrarErrores = False
    __registrarErroresParams = {}
    __registrarDependenciasFlag = False
    __registrarDependencias = False
    __registrarDependenciasParams = {}
    __registrarConfig = False
    __app = ""
    __bdConfig = ""
    __errores = {}
    __producer = None
    __producer2 = None
    __consumer = None
    __consumer2 = None
    __objErroTmp = {}
    __esWorker = False
    __registrarService = False
    __inicializaciones = dict(
        mongoUri="", 
        topicName="", 
        configuraciones={}
    )
    __functionWorkerCambiarData = None

    def __verificarExisteAppService(self,tipo):
        if tipo == 1:
            print("Verificado si existe la app ("+self.__app+") ")
        else:
            print("Verificado si existe el servicio ("+self.__inicializaciones["topicName"]+") ")
            
        ret = False
        cnxMongo = self.db().conexion()
        if cnxMongo != None:
            if self.__bdConfig in cnxMongo.database_names():
                db = cnxMongo[self.__bdConfig]
                collection = db["configuraciones"]
                if tipo == 1:
                    info_gen = collection.find_one({"_id":"general"})
                    if info_gen != None:
                        ret = True
                elif tipo == 2:
                    info_serv = collection.find_one({"_id":self.__inicializaciones["topicName"]})
                    if info_serv != None:
                        ret = True
            else:
                print("la app ("+self.__inicializaciones["topicName"]+") no esta registrada")
        else:
            print("No se pudo abrir conexion al mongo de configuracion")

        if ret == True:
            print(Fore.GREEN+"Si existe"+Fore.WHITE)
        else:
            print(Fore.RED+"No existe"+Fore.WHITE)
        
        return ret
    
    def __registrarServicio(self,isBif):
        print(Fore.GREEN+"Registrar servicio : "+self.__inicializaciones["topicName"]+Fore.WHITE)
        try:
            cnxMongo = self.db().conexion()
            db = cnxMongo[self.__bdConfig]
            collection = db["configuraciones"]
            collection.insert({
                    "_id" : self.__inicializaciones["topicName"],
                    "endpoint" : isBif,
                    "configuracion" : {
                    },
                    "errores" : {
                        "-1" : "Error de conexion COLA DE MENSAJERIA. MODI",
                        "-2" : "Parametros Incorrectos.",
                        "-3" : "Error de conexion MONGO.",
                        "-4" : "Error de conexion REDIS.",
                        "-5" : "Timeout.",
                        "-6" : "Token Invalido.",
                        "-99" : "No ha respondido el servicio"
                    }
                })
        except:
            print("")
        

    def __init__(self,app = "",servicio = ""):
        print("\033[2J\033[1;1f") # Borrar pantalla y situar cursor
        print(Fore.WHITE+"*****************************************************************************"+Fore.WHITE)
        self.__app = app
        self.__inicializaciones["topicName"] = servicio

        if self.__app == "appcoppel":
            self.__bdConfig = "configuraciones_appcom"
        else:
            self.__bdConfig = "configuraciones_"+self.__app

        if self.__app != "":
            #TODO Verificar si existen configuraciones para la app
            if self.__verificarExisteAppService(1):
                if self.__verificarExisteAppService(2) == False:
                    self.__registrarService = True
            else:
                print("No existe esta app : ("+self.__app+")")
                sys.exit(0)
        else:
            print("No existe esta app : ("+self.__app+")")
            sys.exit(0)
        
    def __json_to_b64(self,json_in):
        return base64.b64encode(str.encode(json.dumps(json_in)))

    def __b64_to_json(self,encoded):
        decoded = base64.b64decode(encoded)
        return json.loads(decoded.decode('utf-8'))
        
    def __modificarFlujo(self):
        flujoMod = []
        contador = 0

        auxFlujo = []
        auxFlujo.append(self.__inicializaciones["topicName"])
        for item in self.__inicializaciones["flujo"]:
            auxFlujo.append(item)
        
        objetos = len(auxFlujo)
        count = 0
        for element in auxFlujo:
            objeto = {}
            objeto["owner_conf"] = element
            if (count + 1) < objetos:
                objeto["worker_conf"] = auxFlujo[count+1]
            else:
                 objeto["worker_conf"] = ""
            contador = contador + 1
            if contador == 1:
                objeto["grabar_metadata"] = True

            if contador < objetos :
                objeto["end"] = False
            else:
                objeto["end"] = True

            flujoMod.append(objeto)

            count = count + 1
        
        self.__inicializaciones["flujo"] = flujoMod

    def __obtenerErrores(self):
        ret = {}
        try:    
            cnxMongo = self.db(self.__inicializaciones["mongoUri"]).conexion()
            db = cnxMongo[self.__bdConfig]
            collection = db["configuraciones"]
            cursor = collection.find_one({"_id":self.__inicializaciones["topicName"]})
            if  cursor != None:
                ret = cursor["errores"]
            cnxMongo.close()
        except :
            print("")
        return ret

    def __verificarSiExisteErrorEnBD(self,key,valor):
        #print("__verificarSiExisteErrorEnBD : "+ str(key))
        cnxMongo = self.db(self.__inicializaciones["mongoUri"]).conexion()
        db = cnxMongo[self.__bdConfig]
        collection = db["configuraciones"]
        try:
            cursor = collection.find_one({"_id":self.__inicializaciones["topicName"]})
            if cursor != None:
                if "errores" in cursor:
                    actu = cursor["errores"]
                    actu[str(key)] = str(valor)
                    collection.update({"_id":self.__inicializaciones["topicName"]},{"$set":{"errores":actu}},upsert=True)
            cnxMongo.close()
        except Exception as e:
            print("")

    def __dependencias_f(self,obj = {}):
        objTemp = {}
        if obj != {} and "development" not in obj or "production" not in obj:
            print("No se recibieron las dependencias del servicio de ests forma {'development':{},'production':{}}")
            sys.exit(0)
        else:
            if "ENV" in os.environ and (os.environ["ENV"] == "Production" or os.environ["ENV"] == "Prod"):
                print("resgistrar en bd configuracion "+Fore.GREEN+"obj.production"+Fore.WHITE)
                objTemp = obj["production"]
            else:
                print("resgistrar en bd configuracion "+Fore.RED+"obj.development"+Fore.WHITE)
                objTemp = obj["development"]
            
        cnxMongo = self.db(self.__inicializaciones["mongoUri"]).conexion()
        db = cnxMongo[self.__bdConfig]
        collection = db["configuraciones"]
        collection.update({"_id":self.__inicializaciones["topicName"]},{"$set":{"configuracion":objTemp}})
        #print("inserto ó actualizo el configuraciones :")
        #print(objTemp)
        cnxMongo.close()

    def dependencias(self,obj = {}):
        self.__registrarDependenciasFlag = True
        self.__registrarDependencias,self.__registrarDependenciasParams = self.__dependencias_f,obj

    def __errores_f(self,obj):
        self.__objErroTmp = obj
        
        if "-1" in obj or "-2" in obj or "-3" in obj or "-4" in obj  or "-6" in obj or "-99" in obj:
            print("los siguientes codigos no se pueden usar ( -1, -2, -3, -4, -5, -6, -99 )")
            sys.exit(0)
        else:
            for item in obj:
                self.__verificarSiExisteErrorEnBD(item,obj[item])

            #print("inserto ó actualizo los errores :")
            #print(obj)
        self.__errores = self.__obtenerErrores()

    def errores(self,obj):
        self.__registrarErroresFlag = True
        self.__registrarErrores,self.__registrarErroresParams = self.__errores_f,obj
        
    def __inicializa(self,tipo):
        if tipo == 1:
            self.__esWorker = True
            if self.__obtererConfiguraciones():
                self.__streamMessageQueue(self.__functionWorkerCambiarData)
        elif tipo == 2:
            self.__modificarFlujo()
            if self.__obtererConfiguraciones():
                self.__streamMessageQueue(self.__functionBifurcacion)

    def startWorker(self,function = object):

        self.__functionWorkerCambiarData = function

        if self.__registrarService == True:
            self.__registrarServicio(False)
        
        if self.__registrarErroresFlag == True:
            self.__registrarErrores(self.__registrarErroresParams)

        if self.__registrarDependenciasFlag == True:
            self.__registrarDependencias(self.__registrarDependenciasParams)

        if len(inspect.getargspec(self.__functionWorkerCambiarData).args) == 0:
            print("")
            print("")
            print("La funcion (startWorker) recibe un objeto funcion")# debera recibir 2 argumentos no : "+str(countArgs))
            print("*****************************************************************************")
        else:
            
            try:
                ret = inspect.getsource(self.__functionWorkerCambiarData).index("return")
                countArgs = len(inspect.getargspec(self.__functionWorkerCambiarData).args)
                if countArgs != 2:
                    print("*****************************************************************************")
                    print("la funcion de entrada debera recibir 2 argumentos no : "+str(countArgs))
                    print("Argumentos:")
                    print("    1 argumento  = para recibir los datos de configuracion del microservicio")
                    print("    2 argumento  = para recibir los datos de entrada al servicio")
                    print("*****************************************************************************")
                else:
                    """Si se ejecuta este metodo es para que el microservicio funcione como un worker"""
                    self.__inicializa(1)
            except:
                print("la funcion debe retornar una tupla ejm.: return (0,{})")

    def startBifurcacion(self,arreglo = [],function = object):        
        """
            descripcion: flujo de la bifurcacion
            ejemplo: 
            [
                "llavesInicioSesion",
                "consultaPerfilEcommerce"
            ]
        """
        self.__functionWorkerCambiarData = function
        
        if self.__registrarService:
            self.__registrarServicio(True)
            self.errores(self.__objErroTmp)

        if len(inspect.getargspec(self.__functionWorkerCambiarData).args) == 0:
            print("")
            print("")
            print("La funcion (startBifurcacion) recibe un objeto funcion")# debera recibir 2 argumentos no : "+str(countArgs))
            print("*****************************************************************************")
        else:
            countArgs = len(inspect.getargspec(self.__functionWorkerCambiarData).args)
            if countArgs != 5:
                print("*****************************************************************************")
                print("la funcion de entrada debera recibir 5 argumentos no : "+str(countArgs))
                print("funcionalidad de la funcion : modificar la data de entrada del siguiente worker")
                print("Argumentos:")
                print("    1 argumento  = para recibir Nombre del worker que respondio")
                print("    2 argumento  = para recibir Id_transaction")
                print("    3 argumento  = para recibir Configuracion general del Microservicio")
                print("    4 argumento  = para recibir Data inicial de la transaccion")
                print("    5 argumento  = para recibir Respuesta del Worker anterior")
                print("*****************************************************************************")
            else:
                if len(arreglo) == 0:
                    print("****************************************")
                    print("No se recibio el flujo del a bifurcacion")
                    print("****************************************")
                else:
                    self.__inicializaciones["flujo"] = arreglo
                    self.__inicializa(2)
    
    def __obtererConfiguraciones(self):
        bRetorno = True

        cg,cs,err = self.__configuracionGeneralServicios()
        cg["configService"] = cs
        x = cg
        self.__errores = err    
        self.__inicializaciones["configuraciones"] = x

        return bRetorno

    def __buscar(self,microservicio):
        ret = {}
        for item in self.__inicializaciones["flujo"]:
            if item["owner_conf"] == microservicio:
                ret = item
                break
        return ret

    def __guardarMetadata(self,col,obj):
        #print("Guardar metadata en BD")
        try:
            cnxMongo = self.db(self.__inicializaciones["mongoUri"]).conexion()
            db = cnxMongo[self.__inicializaciones["topicName"]]
            collection = None
            if col not in db.collection_names():
                collection = db[col]
                collection.create_index("fecha_alta",expireAfterSeconds=28800)
            else:
                collection = db[col]
            obj["fecha_alta"] = datetime.datetime.now()
            collection.insert(obj)
            cnxMongo.close()
        except Exception as e:
            print("error :"+str(e))

    def __grabarRespuestaMicroservicio(self,respuesta):
        #print("Grabar respuesta_microservicio_granular")
        try:
            cnxMongo = self.db(self.__inicializaciones["mongoUri"]).conexion()
            db = cnxMongo[self.__inicializaciones["topicName"]]
            collection = None
            
            if "respuesta_microservicio_granular" not in db.collection_names():
                collection = db["respuesta_microservicio_granular"]
                collection.create_index("fecha_alta",expireAfterSeconds=28800)
            else:
                collection = db["respuesta_microservicio_granular"]
            respuesta["fecha_alta"] = datetime.datetime.now()
            collection.insert(respuesta)
            cnxMongo.close()
        except Exception as e:
            print("error :"+str(e))
    
    def __obtenerMetadataInicial(self,id):
        #print("Obtener Metadata Inicial")
        meta = {}
        data = {}
        try:
            cnxMongo = self.db(self.__inicializaciones["mongoUri"]).conexion()
            db = cnxMongo[self.__inicializaciones["topicName"]]
            collection = db["metadata_"+self.__inicializaciones["topicName"]]
            cursor = collection.find({"_id":id})
            for item in cursor:
                data = item["data"]
                meta = item["metadata"]
                meta["mtype"] = "output"
            cnxMongo.close()
        except Exception as e:
            print("error :"+str(e))

        return data,meta
    
    def __configuracionGeneralServicios(self):
        try:
            cnxMongo = self.db().conexion()
            db = cnxMongo[self.__bdConfig]
            collection = db["configuraciones"]
            info_gen = collection.find({"_id":"general"})
            info_ser = collection.find({"_id":self.__inicializaciones["topicName"]})
            count = info_ser.count()
            if(count > 0):
                conf_gen = info_gen[0]["configuracion"]
                conf_serv = info_ser[0]["configuracion"]
                errores = info_ser[0]["errores"]

                if "flask_server" in conf_serv :
                    conf_gen["flask_server"] = conf_serv["flask_server"]
                    conf_gen["flask_port"] = conf_serv["flask_port"]

                if "kafka_server" in conf_serv :
                    conf_gen["kafka_server"] = conf_serv["kafka_server"]
                    conf_gen["kafka_port"] = conf_serv["kafka_port"]

                if "mongo_server" in conf_serv :
                    conf_gen["mongo_server"] = conf_serv["mongo_server"]
                    conf_gen["mongo_port"] = conf_serv["mongo_port"]

                if "redis_server" in conf_serv :
                    conf_gen["redis_server"] = conf_serv["redis_server"]
                    conf_gen["redis_port"] = conf_serv["redis_port"]
                    conf_gen["redis_db_id"] = conf_serv["redis_db_id"]

                if "timeout" in conf_serv :
                    conf_gen["timeout"] = conf_serv["timeout"]

                if "reconexion" in conf_serv :
                    conf_gen["reconexion"] = conf_serv["reconexion"]

                if "timeout_internos" in conf_serv :
                    conf_gen["timeout_internos"] = conf_serv["timeout_internos"]

                if "tiempo_revision" in conf_serv:
                    conf_gen["tiempo_revision"] = conf_serv["tiempo_revision"]
                
                cnxMongo.close()
                return conf_gen,conf_serv,errores
            else:
                cnxMongo.close()
                print("No se ha Registrado la configuracion del servicio en Mongo")
                sys.exit(0)
            
        except Exception as e:
            print("error :"+str(e))

    def __functionBifurcacion(self,configService,jsonArguments):
        log = print
        """Retorna topico a responder y json a escribir"""
        metadata = jsonArguments["metadata"]
        data = jsonArguments["data"]
        headers = jsonArguments["headers"]
        msjX = {}
        OWNER = metadata["owner"]
        ID_TRANSACCION = metadata["id_transaction"]
        TOPICO_RESPUESTA = ""
        try:
            log(ID_TRANSACCION + " - call - ["+metadata["owner"]+"]" + str(headers) + str(data) )
            metadata["mtype"] = "input"
            metadata["time"] = str(datetime.datetime.now())
            metadata["bifurcacion"] = True
            
            cursor_conf = self.__buscar(metadata["owner"])
            if "grabar_metadata" in cursor_conf:
                self.__guardarMetadata("metadata_"+metadata["owner"],{"_id":jsonArguments["metadata"]["id_transaction"],"metadata":jsonArguments["metadata"],"data":jsonArguments["data"]})
                uWorker_async = metadata["uworker"]
                string = str(time.time()).replace('.', '')
                jsonArguments["metadata"]["id_operacion"] = int(string)
                jsonArguments["metadata"]["uowner"] = uWorker_async
                jsonArguments["metadata"]["worker"] = cursor_conf["worker_conf"]
                jsonArguments["metadata"]["uworker"] = metadata["worker"]+"_"+str(metadata["id_operacion"])
                jsonArguments["metadata"]["owner"] = self.__inicializaciones["topicName"]
                data_mod = self.__functionWorkerCambiarData(OWNER,ID_TRANSACCION,self.__inicializaciones["configuraciones"],jsonArguments["data"],jsonArguments["data"])
                if data_mod != {}:
                    jsonArguments["data"] = data_mod
                jsonArguments["response"] = {}
                return jsonArguments["metadata"]["worker"],jsonArguments
            else:
                
                self.__grabarRespuestaMicroservicio({"servicio":metadata["owner"],"id_transaccion":jsonArguments["metadata"]["id_transaction"],"response":jsonArguments["response"]})
                data_inicial,metadata_inicial = self.__obtenerMetadataInicial(metadata["id_transaction"])
                success =True
                #Reviso la respuesta del servicio entrante
                if "response" in jsonArguments and jsonArguments["response"]["meta"]["status"] == "ERROR":
                    success = False
                
                # si success y  servicio es fin y  envio al servicio que sigue
                if success == True:
                    log(ID_TRANSACCION +" - "+metadata["owner"] +" SUCCESS")
                    if cursor_conf["end"] == False:
                        log(ID_TRANSACCION +" - "+metadata["owner"] +" NO ES SERVICIO FINAL")
                        uWorker_async = metadata["uworker"]
                        string = str(time.time()).replace('.', '')
                        jsonArguments["metadata"]["id_operacion"] = int(string)
                        jsonArguments["metadata"]["uowner"] = uWorker_async
                        jsonArguments["metadata"]["worker"] = cursor_conf["worker_conf"]
                        jsonArguments["metadata"]["uworker"] = metadata["worker"]+"_"+str(metadata["id_operacion"])
                        jsonArguments["metadata"]["owner"] = self.__inicializaciones["topicName"]
                        data_mod = self.__functionWorkerCambiarData(OWNER,ID_TRANSACCION,self.__inicializaciones["configuraciones"],data_inicial,jsonArguments["response"])
                        if data_mod != {}:
                            jsonArguments["data"] = data_mod
                        jsonArguments["response"] = {}
                        return jsonArguments["metadata"]["worker"],jsonArguments
                    else:
                        log(ID_TRANSACCION +" - "+metadata["owner"] +" ES SERVICIO FINAL")
                        JSON_RESPUESTA_FIN = {}
                        if JSON_RESPUESTA_FIN == {}:
                            JSON_RESPUESTA_FIN = jsonArguments["response"]

                        msj = {"_id":metadata["id_transaction"],"response":JSON_RESPUESTA_FIN,"metadata":metadata_inicial}
                        return "respuesta_"+metadata["callback"],msj
                else:
                    log(ID_TRANSACCION +" - "+metadata["owner"] +" ERROR")
                    msj = {"_id":metadata["id_transaction"],"response":jsonArguments["response"],"metadata":metadata_inicial}
                    return "respuesta_"+metadata["callback"],msj
        except Exception as e:            
            error = {"_id":jsonArguments["metadata"]["id_transaction"],"servicio":self.__inicializaciones["topicName"],"error":str(e)}
            self.__escribirColaMensajeria("Errores_criticos",error,jsonArguments["metadata"]["id_transaction"])

        return self.__inicializaciones["topicName"],{}
    
    def __buscarMensaje(self,id):
        res = ""
        if str(id) in self.__errores:
            res = self.__errores[str(id)]
        else:
            res = "Error No Definido"
        return res

    def __response(self,code,data = None,metadata = None):
        response = {}
        response["meta"] = {}
        response["data"] = {}

        response["meta"]["id_transaction"] = metadata["id_transaction"]
        
        if code == 0:
            response["meta"]["status"] = "SUCCESS"    
            response["data"]["response"] = data
        else:
            response["meta"]["status"] = "ERROR"
            response["data"]["response"] = {
                "errorCode":str(code),
                "userMessage":self.__buscarMensaje(str(code))
            }
        return response
        
    async def escribir(self,topico,respuesta,idTransaction):
        msj = self.__json_to_b64(respuesta)
        self.__producer.send(topico,key=str.encode(str(idTransaction)),value=msj)
        self.__producer.flush()
        print(idTransaction+" - responde en topico ["+topico+"]"+" : "+str(respuesta))

    def __escribirColaMensajeria(self,topico,respuesta,idTransaction = ""):
        #loop.create_task(self.send_one(topico,respuesta))
        loop.create_task(self.escribir(topico,respuesta,idTransaction))
        
    async def __functionBridge(self,function,*args):

        if "smoketest" in args[1]["data"]:
            metadata = args[1]["metadata"]
            data = args[1]["data"]
            headers = args[1]["headers"]
            respuesta = {}
            respuesta["meta"] = {}
            respuesta["data"] = {}
            respuesta["meta"]["id_transaction"] = ""
            respuesta["meta"]["status"] = "SUCCESS"
            respuesta["data"]["response"] = {
                "errorCode":"0",
                "userMessage":"smoketest ok"
            }

            respuestax = {}                                                                                                                                                                                                                                                              																																																														
            respuestax["metadata"] = metadata                                                                                                                                                                                                                                            
            respuestax["headers"] = headers                                                                                                                                                                                                                                              
            respuestax["data"] = data                                                                                                                                                                                                                                              
            respuestax["response"] = respuesta                                                                                                                                                                                                                                      
            respuestax["metadata"]["time"] = str(datetime.datetime.now())                                                                                                                                                                                                                
            respuestax["metadata"]["worker"]  = respuestax["metadata"]["owner"]                                                                                                                                                                                                           
            respuestax["metadata"]["owner"]  = self.__inicializaciones["topicName"]
            respuestax["metadata"]["mtype"] = "output"                                                                                                                                                                                                                                   
            if("uowner" in respuestax["metadata"]):                                                                                                                                                                                                                                      
                uowner = respuestax["metadata"]["uowner"]                                                                                                                                                                                                                            
                                                                                                                                                                                                                                                                                        
            if("uworker" in respuestax["metadata"]):                                                                                                                                                                                                                                     
                uworker = respuestax["metadata"]["uworker"]                                                                                                                                                                                                                          
                                                                                                                                                                                                                                                                                        
            respuestax["metadata"]["uworker"] = uowner                                                                                                                                                                                                                                   
            respuestax["metadata"]["uowner"] = uworker 


            if(metadata["bifurcacion"] == True):                                                                                                                                                                                                                                        
                metadata["bifurcacion"] = False                                                                                                                                                                                                                                     
                TOPICO = respuestax["metadata"]["callback"]
                self.__escribirColaMensajeria(TOPICO,respuestax,metadata["id_transaction"])
            else:
                TOPICO = "respuesta_"+metadata["owner"]
                respuesta2 = {"_id":respuestax["metadata"]["id_transaction"],"response":respuestax["response"],"metadata":respuestax["metadata"]}
                self.__escribirColaMensajeria(TOPICO,respuesta2,metadata["id_transaction"])
        else:                
            if self.__esWorker == True:
                #guarda metadata
                msj2 = {}
                msj2["data"] =  args[1]["data"]
                msj2["headers"] =  args[1]["headers"]
                #self.__guardarMetadata("metadata_"+self.__inicializaciones["topicName"],{"_id":args[1]["metadata"]["id_transaction"],"metadata":args[1]["metadata"]})
                code = 0
                datax = {}
                try:
                    code,datax = function(args[0],msj2) 
                except Exception as e:
                    code,datax  = -99,{}
                    error = {"_id":args[1]["metadata"]["id_transaction"],"servicio":self.__inicializaciones["topicName"],"error":str(e)}
                    self.__escribirColaMensajeria("Errores_criticos",error,args[1]["metadata"]["id_transaction"])
                
                metadata = args[1]["metadata"]
                data = args[1]["data"]
                headers = args[1]["headers"]

                if "metadata" not in args[1] or "data" not in args[1] or "headers" not in args[1]:
                    print("No contiene datos correctos")
                else:
                    respuesta = self.__response(code,datax,metadata)
                    respuestax = {}                                                                                                                                                                                                                                                              																																																														
                    respuestax["metadata"] = metadata                                                                                                                                                                                                                                            
                    respuestax["headers"] = headers                                                                                                                                                                                                                                              
                    respuestax["data"] = data                                                                                                                                                                                                                                              
                    respuestax["response"] = respuesta                                                                                                                                                                                                                                      
                    respuestax["metadata"]["time"] = str(datetime.datetime.now())                                                                                                                                                                                                                
                    respuestax["metadata"]["worker"]  = respuestax["metadata"]["owner"]                                                                                                                                                                                                           
                    respuestax["metadata"]["owner"]  = self.__inicializaciones["topicName"]
                    respuestax["metadata"]["mtype"] = "output"                                                                                                                                                                                                                                   
                    if("uowner" in respuestax["metadata"]):                                                                                                                                                                                                                                      
                        uowner = respuestax["metadata"]["uowner"]                                                                                                                                                                                                                            
                                                                                                                                                                                                                                                                                                
                    if("uworker" in respuestax["metadata"]):                                                                                                                                                                                                                                     
                        uworker = respuestax["metadata"]["uworker"]                                                                                                                                                                                                                          
                                                                                                                                                                                                                                                                                                
                    respuestax["metadata"]["uworker"] = uowner                                                                                                                                                                                                                                   
                    respuestax["metadata"]["uowner"] = uworker    

                    if(metadata["bifurcacion"] == True):                                                                                                                                                                                                                                        
                        metadata["bifurcacion"] = False                                                                                                                                                                                                                                     
                        TOPICO = respuestax["metadata"]["callback"]
                        self.__escribirColaMensajeria(TOPICO,respuestax,respuestax["metadata"]["id_transaction"])
                    else:
                        TOPICO = "respuesta_"+metadata["owner"]                                                                                                                                                                                                                             
                        respuesta2 = {"_id":respuestax["metadata"]["id_transaction"],"response":respuestax["response"],"metadata":respuestax["metadata"]}                                                                                                                                                                                                                                                                                                                             
                        self.__escribirColaMensajeria(TOPICO,respuesta2,respuestax["metadata"]["id_transaction"])
            else:
                TOPICO,respuesta = function(args[0],args[1])
                self.__escribirColaMensajeria(TOPICO,respuesta,args[1]["metadata"]["id_transaction"])

    def __conecctMQ(self):
        ret = False
        try:
            self.__producer = KafkaProducer(bootstrap_servers=self.__inicializaciones["configuraciones"]["kafka_servers"])
            #self.__consumer = KafkaConsumer(self.__inicializaciones["topicName"],bootstrap_servers=self.__inicializaciones["configuraciones"]["kafka_servers"],group_id=str(self.__inicializaciones["topicName"]))
            #self.__producer2 = AIOKafkaProducer(loop=loop, bootstrap_servers=self.__inicializaciones["configuraciones"]["kafka_servers"])
            self.__consumer2 = AIOKafkaConsumer(self.__inicializaciones["topicName"],loop=loop, bootstrap_servers=self.__inicializaciones["configuraciones"]["kafka_servers"],group_id=str(self.__inicializaciones["topicName"]))
            ret = True
        except:
            ret = False
        return ret

    async def __consume(self,function,configService):
        print(Fore.CYAN+" * Running Daemon on : " + str(self.__inicializaciones["configuraciones"]["kafka_servers"]) + " topic: " + self.__inicializaciones["topicName"]+Fore.WHITE)
        #await self.__producer2.start()
        await self.__consumer2.start()
        try:
            async for msg in self.__consumer2:
                try:
                    msj = self.__b64_to_json(msg.value)
                    loop.create_task(self.__functionBridge(function,configService,msj))   
                except:
                    pass
        finally:
            await self.__consumer2.stop()
            #await self.__producer2.stop()
            print("se desconecto la cola de mensajeria (reconectar)")
            self.__conecctMQ()
            if self.__esWorker == True:
                self.__streamMessageQueue(self.__functionWorkerCambiarData)
            else:
                self.__streamMessageQueue(self.__functionBifurcacion)
            
    def __streamMessageQueue(self,function):

        proxy = "proxy" in self.__inicializaciones["configuraciones"] ? self.__inicializaciones["configuraciones"]["proxy"] : {}
        configService = {
            "configGral":{
                "proxy":proxy,
                "timeoutInternos":self.__inicializaciones["configuraciones"]["timeout_internos"],
                "mongoUri" : self.__inicializaciones["configuraciones"]["mongo_uri"]},
            "configService":self.__inicializaciones["configuraciones"]["configService"]
        }
        self.__inicializaciones["mongoUri"] = configService["configGral"]["mongoUri"]

        if self.__conecctMQ() ==True:
            loop.run_until_complete(self.__consume(function,configService))
        else:
	        print("Error:\n############################\nNo esta activo el Message Queue\n############################\n")
