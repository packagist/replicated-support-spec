collect:
  v1:
    - docker.container-cp:
        description: Background worker logs
        container: packagist-worker
        src_path: /var/log/supervisor/workers.log
        output_dir: /worker/
        include_empty: true

