# Redirect checkpoints to /tmp, away from project directories
c.FileContentsManager.checkpoints_kwargs = {"root_dir": "/tmp"}
