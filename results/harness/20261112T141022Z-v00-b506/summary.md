# Harness run 20261112T141022Z-v00-b506

- Task: refresh
- Variant: v00-baseline
- Data tag: data-1m-v1
- Targets: F2
- Expected commit: b1660a09614e780473f21788f5ae8523db531ca7
- Notebook run: e982d438-809a-4118-9da7-30598c6d37bd
- Refresh parallelism requested: 6

**Stopped before finishing:**

```
unexpected error: TimeoutError: Operation 'v1/workspaces/58b05b2a-00d2-45df-9034-0a044bb3d162/git/updateFromGit' timed out after 600s (limit: 600s). The backend operation (id=8865feef-83de-4306-99e7-b74c243338e3) may still be running. Query its status at: v1/operations/8865feef-83de-4306-99e7-b74c243338e3
To allow more time, pass a larger 'max_wait_seconds' value (e.g. lro_config={'max_wait_seconds': 1200}).

Traceback (most recent call last):
  File "/tmp/ipykernel_6118/1735656195.py", line 23, in <module>
    head = sync_workspace(cap)
  File "/tmp/ipykernel_6118/211429148.py", line 43, in sync_workspace
    ok(fab.post(f"v1/workspaces/{ws}/git/updateFromGit", json=body, lro_wait=True), f"{cap}: update from Git")
       ~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/trusted-service-user/cluster-env/trident_env/lib/python3.13/site-packages/sempy/fabric/_client/_rest_client.py", line 296, in post
    return self.request("POST", path_or_url, *args, **kwargs)
           ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/trusted-service-user/cluster-env/trident_env/lib/python3.13/site-packages/sempy/fabric/_client/_rest_client.py", line 648, in request
    return self._wait_for_operation(name, OperationStart(response), lro_config=lro_config)
           ~~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/trusted-service-user/cluster-env/trident_env/lib/python3.13/site-packages/sempy/fabric/_client/_rest_client.py", line 728, in _wait_for_operation
    raise TimeoutError(
    ...<4 lines>...
        f"(e.g. lro_config={{'max_wait_seconds': {int(max_wait_seconds * 2)}}}).")
TimeoutError: Operation 'v1/workspaces/58b05b2a-00d2-45df-9034-0a044bb3d162/git/updateFromGit' timed out after 600s (limit: 600s). The backend operation (id=8865feef-83de-4306-99e7-b74c243338e3) may still be running. Query its status at: v1/operations/8865feef-83de-4306-99e7-b74c243338e3
To allow more time, pass a larger 'max_wait_seconds' value (e.g. lro_config={'max_wait_seconds': 1200}).

```

## Log

```
2026-11-12T14:13:12Z run 20261112T141022Z-v00-b506: variant=v00-baseline data_tag=data-1m-v1 targets=['F2'] expected_commit=b1660a09614e780473f21788f5ae8523db531ca7
2026-11-12T14:13:23Z F2: update from Git 6bbfb2927c8f84faaa5079ff221dbf194f7def02 -> b1660a09614e780473f21788f5ae8523db531ca7
2026-11-12T14:23:27Z STOPPED: TimeoutError: Operation 'v1/workspaces/58b05b2a-00d2-45df-9034-0a044bb3d162/git/updateFromGit' timed out after 600s (limit: 600s). The backend operation (id=8865feef-83de-4306-99e7-b74c243338e3) may still be running. Query its status at: v1/operations/8865feef-83de-4306-99e7-b74c243338e3
To allow more time, pass a larger 'max_wait_seconds' value (e.g. lro_config={'max_wait_seconds': 1200}).
```
