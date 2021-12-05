# django-docker-compose-deploy


This repo was created by following the tutorial of London App Developer on YouTube (https://www.youtube.com/watch?v=mScd-Pc_pX0&ab_channel=LondonAppDeveloper)

For issues about permissions try the following in Ubuntu:

sudo chmod -R a+rwx ./data
or
sudo chown -R $USER: $HOME

# Deploy on AWS

## Set up the EC2 Instance:

- Create a Free instance with low resources (free tier)
- Connect/log in to the server via SSH by:
    - PuTTy client on windows (e.g. solarputty)
    - Ubuntu terminal:
        ssh Public IPv4 DNS
        (e.g ssh ec2-user@ec2-00-00-00-00.eu-west-1.compute.amazonaws.com)

- Once connected download the two requirements for deploying the app:
    - Install git: sudo yum install git -y
    - Install docker: sudo amazon-linux-extras install docker -y

- Once installed enable docker so it starts with reboot.
    - sudo systemctl enable docker.service

- Start it without needing to reboot by running:
    - sudo systemctl start docker.service

- Add our user to the docker group so the user has the permission to run applications user docker. This user will be granted the permissions needed to run docker containers.
    - sudo usermod -aG docker ec2-user

- Install docker-compose:
    In https://docs.docker.com/compose/install/ there instrucctions. 
    
    We will be using this link to download the executable:
        sudo curl -L "https://github.com/docker/compose/releases/download/1.29.2/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
    Then we make it executable by:
        hmod +x /usr/local/bin/docker-compose

- Log out the machine and log in back so the group permissions are applied. Run "exit" and log in back as in the first step.

## Clone the app repo to the Instance

### Set up a deploy key in Github:

- From the EC2 Instance type (generate ssh on the actual server to authenticate with github):. Leave the location by default and set a passphrase if you thing it is necessary.
    - ssh-keygen -t ed25519 -b 4096

- Copy the public key by typing:
    - cat ~/.ssh/id_ed25519.pub

-  Within the repo page go to Settings > Deploy keys > Add new Key and paste the public key (Do not need to "Allow write access")

### Clon and run the service

- Go to repo page > Clone by SSH
- Go to EC2 Instance terminal (login if you are not) and git clone the repol.
- Switch to the repo directory 
- Add the configuration.You can copy the .env.sample into .env by  "cp .env.sample .env" and then edit .env with a text editor (e.g. vi .env)

DB_NAME=app   
DB_USER=approotuser
DB_PASS=supersecurepassword123
SECRET_KEY=ajdfhadslfhajdhfasljfhaldsf
ALLOWED_HOSTS=ec2-52-31-93-53.eu-west-1.compute.amazonaws.com

- Run the docker-compose to pull down the dependencies and run the application. It will download and build the container.

docker-compose -f docker-compose-deply.yml up -d

## Test all is running good

Once app is running you can access through the Public IPv4 DNS directly from a brower:

http://ec2-52-31-93-53.eu-west-1.compute.amazonaws.com/admin/login/?next=/admin/

Create the new user by:
docker-compose -f docker-compose-deploy.yml run -rm app sh -c "python manage.py createsuperuser"

You are good to go!!

you can run logs by:
docker-compose -f docker-compose-deploy.yml logs

## Update the code

To update the code you can make changes in your local environment, commit the changes and push them to the git repository. Then you pull down to the EC2 Instance and run the build of the given services, as in:

docker-compose -f docker-compose-deply.yml build app

This will replace the container app.

## Further Development

This repo does not considering continuous integration processes. Look for other resources to know how to deploy on a production grade enviorment, where we would define all the infrastructure as code, set up automation and set up other things like automated workflows so when you push your code to git or your push it to your gitlab instance it automatically builds it and deploys it to an environment.