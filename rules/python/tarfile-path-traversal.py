import tarfile

tf = tarfile.open(f)

# ruleid: tarfile-path-traversal
tf.extract(i)

# ruleid: tarfile-path-traversal
tf.extractall(i)

# ruleid: tarfile-path-traversal
tf = tarfile.open(f).extract(i)

# ruleid: tarfile-path-traversal
tf = tarfile.open(f).extractall(i)

with tarfile.open(f) as tf:
    # ruleid: tarfile-path-traversal
    tf.extract(i)

    # ruleid: tarfile-path-traversal
    tf.extractall(i)
