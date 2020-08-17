# ubuntu_mirror = 'http://mirror.its.sfu.ca/mirror/ubuntu/'
ubuntu_mirror = 'http://mirror.csclub.uwaterloo.ca/ubuntu/'
ubuntu_release = 'bionic'
ubuntu_version = '18.04'
username = 'vagrant'
user_home = '/home/' + username
project_home = user_home + '/project/' # you may need to change the working directory to match your project
project_go_location = project_home + 'tldrusstock/tldr/stockData/goGetStockData' # location of go code


python3_packages = '/usr/local/lib/python3.6/dist-packages'
ruby_gems = '/var/lib/gems/2.5.0/gems/'


# Get Ubuntu sources set up and packages up to date.

template '/etc/apt/sources.list' do
  variables(
    :mirror => ubuntu_mirror,
    :release => ubuntu_release
  )
  notifies :run, 'execute[apt-get update]', :immediately
end
execute 'apt-get update' do
  action :nothing
end
execute 'apt-get upgrade' do
  command 'apt-get dist-upgrade -y'
  only_if 'apt list --upgradeable | grep -q upgradable'
end
directory '/opt'
directory '/opt/installers'


# Basic packages many of us probably want. Includes gcc C and C++ compilers.
package ['build-essential']


# Other core language tools you might want

package ['python','python3','python3-pip','python3-distutils']  # Python
package 'golang-go'  # Go


# NodeJS (more modern than Ubuntu nodejs package) and NPM
remote_file '/opt/installers/node-setup.sh' do
  source 'https://deb.nodesource.com/setup_14.x'
  mode '0755'
end
execute '/opt/installers/node-setup.sh' do
  creates '/etc/apt/sources.list.d/nodesource.list'
  notifies :run, 'execute[apt-get update]', :immediately
end
package ['nodejs']


# Go (more modern than Ubuntu golang-go package)
execute 'snap install --classic go' do
end

# RabbitMQ-related things
# pika is included in pipenv
package ['rabbitmq-server']

# Go amqp, go-finance,  library
execute 'go get github.com/streadway/amqp' do
  cwd project_go_location
  user username
  environment 'HOME' => user_home
  creates project_go_location + '/src/github.com/streadway/amqp/README.md'
end

execute 'go get github.com/piquette/finance-go' do
  cwd project_go_location
  user username
  environment 'HOME' => user_home
  creates project_go_location + '/src/github.com/piquette/finance-go/README.md'
end

# install pipenv
# execute 'pip3 install pipenv' do
# end

# install dependencies for react
execute 'npm install --no-bin-links' do
	cwd project_home
end

# install dependencies for django
execute 'pip3 install -r requirements.txt' do
  cwd project_home
end

# execute 'sed -i -e \'s/\r$//\' .\/startserver.sh' do
#   cwd project_home
# end

# execute 'pipenv --python 3.6' do
#   cwd project_home
# end

# execute 'pipenv install --system' do
#   cwd project_home
# end
