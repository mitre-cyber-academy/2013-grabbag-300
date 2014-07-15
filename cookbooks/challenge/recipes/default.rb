cookbook_file "/etc/init.d/challenge" do
  source "python_server_init_d"
  mode 0755
end

# This path is hardcoded into the web challenge-server.py...sorry
remote_directory "/opt/challenge" do
  source "web"
  owner "root"
  group "root"
  mode 0755
end

file "/opt/challenge/challenge_server.py" do
  mode "755"
end

python_pip "bottle" do
  action :install
end

service "challenge" do
  supports :start => true, :stop => true, :restart => true
  action [:start, :enable]
end