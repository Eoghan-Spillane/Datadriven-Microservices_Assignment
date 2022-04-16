# How to deploy probably

* mkdir ~/.kube
* echo "export KUBE_CONFIG=~/.kube/config" >> ~/.bashrc
* source ~/.bashrc


**Tagging:**
* docker tag datadriven-microservices-assignment_pokemon-client eoghanspillane/pokemonclient:latest
* docker tag datadriven-microservices-assignment_pokemon-server eoghanspillane/pokemonserver:latest
* docker tag datadriven-microservices-assignment_pokemon-website eoghanspillane/pokemonwebsite:latest

**Pushing**
* docker push eoghanspillane/pokemonclient:latest
* or docker Desktop

**Deploying:**
* kubectl create -f pokemon-server-deploy.yml
* kubectl create -f pokemon-server-svc.yml
* kubectl create -f pokemon-redis-deploy.yml
* kubectl create -f pokemon-redis-svc.yml
* kubectl create -f pokemon-website-deploy.yml
* kubectl create -f pokemon-website-svc.yml
* kubectl create -f pokemon-client-deploy.yml
* http://127.0.0.1:30000 

**BusyBox**
* kubectl create -f busybox-test.yml
* kubectl exec -ti busybox -- nslookup redis

**Check whats running**
* kubectl get pods
* kubectl get svc
* kubectl get nodes

* docker ps -a
* kubectl get po

**KIND**
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