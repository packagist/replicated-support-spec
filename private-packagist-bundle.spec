specs:

- os.read-file:
    filepath: /etc/application.conf
    output_dir: /files/some/path/


- docker.container-inspect:
    output_dir: /replicated/replicated/inspect
    container_list_options:
      All: true
      Filters:
        name:
          - "replicated"
          - "retraced"
          - "premkit"

- docker.logs:
    output_dir: /replicated/replicated/logs
    container_list_options:
      All: true
      Filters:
        name:
          - "replicated"
          - "retraced"
          - "premkit"


- os.loadavg:
    output_dir: /os/loadavg
- os.hostname:
    output_dir: /os/hostname
- os.uptime:
    output_dir: /os/uptime
- os.run-command:
    output_dir: /os/df
    name: df
    args:
      - -h
      - --total
- os.run-command:
    output_dir: /os/proc/meminfo
    name: cat
    args:
      - /proc/meminfo
- os.run-command:
    output_dir: /os/proc/cpuinfo
    name: cat
    args:
      - /proc/cpuinfo
- os.run-command:
    output_dir: /os/ps
    name: ps
    args:
      - auwwf
- os.read-file:
    filepath: /etc/os-release
    output_dir: /os/etc/os-release
- os.read-file:
    filepath: /usr/lib/os-release
    output_dir: /os/usr/lib/os-release
- os.read-file:
    filepath: /etc/centos-release
    output_dir: /os/etc/centos-release


- docker.info:
    output_dir: /docker/info
- docker.ps:
    output_dir: /docker/ps
- docker.container-inspect:
    output_dir: /docker/my-container
    container_list_options:
      All: true
      Filters:
        name:
          - "my-sweet-container"


- os.run-command:
    output_dir: /commands/df/
    name: df
    args:
      - -h
      - --total
