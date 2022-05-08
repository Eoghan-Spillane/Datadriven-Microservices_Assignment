# How to deploy probably

* mkdir ~/.kube
* echo "export KUBE_CONFIG=~/.kube/config" >> ~/.bashrc
* source ~/.bashrc

**Tagging:**
docker tag datadriven-microservices-assignment_pokemon-client eoghanspillane/pokemon-client:newest
docker tag datadriven-microservices-assignment_pokemon-server eoghanspillane/pokemon-server:newest
docker tag datadriven-microservices-assignment_pokemon-website eoghanspillane/pokemon-website:newest
docker tag datadriven-microservices-assignment_digimon-client eoghanspillane/digimon-client:newest

docker tag datadriven-microservices-assignment_digimon-server eoghanspillane/digimon-server:newest
docker tag datadriven-microservices-assignment_pokemon-server eoghanspillane/pokemon-server:newest

**Pushing**
* docker push eoghanspillane/pokemonclient:latest
* or docker Desktop

**Deploying:**
kubectl create -f pokemon-server-svc.yml
kubectl create -f digimon-server-svc.yml
kubectl create -f pokemon-redis-svc.yml
kubectl create -f pokemon-website-svc.yml

kubectl create -f digimon-server-deploy.yml
kubectl create -f pokemon-redis-deploy.yml
kubectl create -f pokemon-website-deploy.yml
kubectl create -f pokemon-client-deploy.yml
kubectl create -f digimon-client-deploy.yml

http://127.0.0.1:30000 

**Deleting:**
kubectl delete deployments.apps pokemon-server-deploy
kubectl delete deployments.apps redis-deploy
kubectl delete deployments.apps pokemon-client-deploy
kubectl delete deployments.apps pokemon-website-deploy
kubectl delete service  pokemon-server
kubectl delete service  pokemon-website
kubectl delete service  redis
kubectl delete deployments.apps busybox-test
kubectl delete -f busybox-test.yml


**BusyBox:**
* kubectl create -f busybox-test.yml
* kubectl exec -ti busybox -- nslookup redis

**Check whats running:**
* kubectl get pods
* kubectl get svc
* kubectl get nodes

* docker ps -a
* kubectl get po

**KIND:**
* curl -Lo ./kind https://github.com/kubernetes-sigs/kind/releases/download/v0.7.0/kind-linux-amd64
* chmod +x ./kind
* sudo mv ./kind /usr/local/bin/

* echo $KUBECONFIG
* ls $HOME/.kube
* kind create cluster --name wslkind
* ls $HOME/.kube

* kubectl apply -f https://raw.githubusercontent.com/kubernetes/dashboard/v2.0.0-rc6/aio/deploy/recommended.yaml
* kubectl get all -n kubernetes-dashboard
* kubectl proxy

kubectl get events --sort-by=.metadata.creationTimestamp

kubectl get deployments
kubectl apply -f Deployment/
k6 run Deployment/Testing/script.js

kubectl autoscale deployment pokemon-website-deploy  --cpu-percent=50 --min=2 --max=20
kubectl get hpa


02df94c5711780249dafd5dc1f3458532df21053
