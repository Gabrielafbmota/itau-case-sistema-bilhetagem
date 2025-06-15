service=$1


cd ~/workspace/itau-case/itau-case-sistema-bilhetagem/services

ls | grep $service || mkdir $service

cd $service

# Copiar todos os arquivos de dentro de /home/gabriela/workspace/itau-case/itau-case-sistema-bilhetagem/services/user-service para a pasta atual

cp -r ~/workspace/itau-case/itau-case-sistema-bilhetagem/services/user-service/* .



