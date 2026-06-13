# Redirect checkpoints to /tmp, away from project directories
c.FileContentsManager.checkpoints_kwargs = {"root_dir": "/tmp"}

# Disable .Trash folder
c.FileContentsManager.delete_to_trash = False

# IPC transport is faster than TCP, but only works on the same machine
c.KernelManager.transport = "ipc"
