# postdeployment.sh file
currentTime=$(date +"%Y-%m-%d %H:%M:%S")
filePath="/home/site/wwwroot/postdeploymentfile.txt"
echo $currentTime > $filePath
