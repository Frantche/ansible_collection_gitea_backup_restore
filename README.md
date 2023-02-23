# Ansible Collection - frantchenco.gitea

Documentation for the collection.

### Modules


Name | Description
--- | ---
frantchenco.gitea.backup|Create a backup of your gitea installation
frantchenco.gitea.restore|Restore your gitea installation

## Installation and Usage

### Installing the Collection from Ansible Galaxy

create a file name "requirements.yml"
```yaml
---
collections:
- name: community.general
  version: 5.7.0
- name: ansible.posix
  version: 1.4.0
- name: kubernetes.core
  version: 2.3.2
- name: community.docker
  version: 3.3.2
- name: amazon.aws
  version: 5.2.0
- name: git+https://github.com/Frantche/ansible_collection_gitea_backup_restore.git,master
```

Before using the collection, you need to install it with the Ansible Galaxy CLI:

    ansible-galaxy install -r ./requirements.yml

### Examples

### Backup

If you would like to perform a backup of your gitea installation. You will need to prepare the following variables:

If you wish to backup kubernetes
```
gitea_installation: kubernetes
gitea_k8s_container_app_namespace: tobedefined
gitea_k8s_container_app_pod: tobedefined
gitea_k8s_container_db_namespace: tobedefined
gitea_k8s_container_db_pod: tobedefined
```

If you wish to backup docker
```
gitea_installation: docker
gitea_docker_container_app: tobedefined
gitea_docker_container_db: tobedefined
```

The variable to push to backup to S3
```
gitea_backup_s3_access_key: tobedefined
gitea_backup_s3_secret_key: tobedefined
gitea_backup_s3_bucket: tobedefined
gitea_backup_s3_endpoint: tobedefined
gitea_backup_s3_encrypt: tobedefined
```


```yaml
---

- hosts: gitea
  gather_facts: yes
  become: yes
  roles:
  - role: frantchenco.gitea.backup
```

### Restore

If you would like to perform a restore of your gitea installation. You will need to prepare the following variables:

If you wish to backup kubernetes
```
gitea_installation: kubernetes
gitea_k8s_container_app_namespace: tobedefined
gitea_k8s_container_app_pod: tobedefined
gitea_k8s_container_db_namespace: tobedefined
gitea_k8s_container_db_pod: tobedefined
```

If you wish to backup docker
```
gitea_installation: docker
gitea_docker_container_app: tobedefined
gitea_docker_container_db: tobedefined
```

The variable to download the backup file from S3
```
gitea_backup_s3_access_key: tobedefined
gitea_backup_s3_secret_key: tobedefined
gitea_backup_s3_bucket: tobedefined
gitea_backup_s3_endpoint: tobedefined
gitea_backup_s3_encrypt: tobedefined
gitea_backup_s3_filename: tobedefined
```


```yaml
---

- hosts: gitea
  gather_facts: yes
  become: yes
  roles:
  - role: frantchenco.gitea.restore
```