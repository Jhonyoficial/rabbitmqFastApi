 
* celery -A controller worker --loglevel=info
usado para rodar o CELERY e enviar os trabalhos para o rabbitmq
* docker run -it --rm --name rabbitmq -p 5672:5672 -p 15672:15672 rabbitmq:4.0-management
executar rabbitmq no docker