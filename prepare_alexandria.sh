#!/bin/bash
#
# (c) Copyright 2016-2017 Hewlett Packard Enterprise Development LP
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.
#
tar -xvf alexandria.tar.gz

hlm_packager_dir=`find /opt/hlm_packager/ -name hos-4.* -type d`/hlinux_venv/
sudo cp third-party/alexandria/alexandria-*.tgz $hlm_packager_dir
sudo /opt/stack/service/packager/venv/bin/create_index --dir $hlm_packager_dir

cd /home/stack/helion/hos/ansible/
ansible-playbook -i hosts/localhost third-party-import.yml
