# Harness run 20261110T161824Z-v99-6981

- Task: refresh
- Variant: v99-kitchen-sink
- Data tag: data-1m-v1
- Targets: PPU
- Expected commit: eccd5b6aa5a7e6d1e9f310741db0fd25d01812a7
- Notebook run: cb630abc-4c4a-4582-93ca-e4d840dbebe8
- Refresh parallelism requested: 6

**Stopped before finishing:**

```
unexpected error: OperationException: The event Id=136 does not contain the column Id=2. Please refer to product documentation for a list of available event columns.

Technical Details:
RootActivityId: 4888c04d-2ff2-41c2-ab68-c03e7c9dd9a5
Date (UTC): 11/10/2026 4:19:33 PM

   at Microsoft.AnalysisServices.Core.AnalysisServicesClient.SendExecuteAndReadResponse(ImpactDetailCollection impacts, Boolean expectEmptyResults, Boolean throwIfError)
   at Microsoft.AnalysisServices.Core.AnalysisServicesClient.Create(IMajorObject parent, IMajorObject obj, ObjectExpansion expansion, ImpactDetailCollection impact, Boolean allowOverwrite, XmlaWarningCollection warnings, JaXmlSerializer serializer)
   at Microsoft.AnalysisServices.Core.Server.Update(IMajorObject obj, UpdateOptions options, UpdateMode mode, XmlaWarningCollection warnings, ImpactDetailCollection impactResult)
   at Microsoft.AnalysisServices.Core.Server.SendUpdate(IMajorObject obj, UpdateOptions options, UpdateMode mode, XmlaWarningCollection warnings, ImpactDetailCollection impactResult)
   at Microsoft.AnalysisServices.MajorObject.Update(UpdateOptions options, UpdateMode mode, XmlaWarningCollection warnings)
   at Microsoft.AnalysisServices.MajorObject.Update(UpdateOptions options, UpdateMode mode)
   at Microsoft.Fabric.SemanticLink.TraceCollector.Start(Int32 delayInSeconds)
   at System.RuntimeMethodHandle.InvokeMethod(Object target, Void** arguments, Signature sig, Boolean isConstructor)
   at System.Reflection.MethodBaseInvoker.InvokeDirectByRefWithFewArgs(Object obj, Span`1 copyOfArgs, BindingFlags invokeAttr)

Traceback (most recent call last):
  File "/tmp/ipykernel_6382/2443177563.py", line 41, in <module>
    ref, logs = traced_refresh(cap, dataset_id)
                ~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^
  File "/tmp/ipykernel_6382/1460445152.py", line 169, in traced_refresh
    trace.start()
    ~~~~~~~~~~~^^
  File "/home/trusted-service-user/cluster-env/trident_env/lib/python3.13/site-packages/sempy/fabric/_trace/_trace.py", line 144, in start
    self._trace_collector.Start(delay)
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^
Microsoft.AnalysisServices.OperationException: The event Id=136 does not contain the column Id=2. Please refer to product documentation for a list of available event columns.

Technical Details:
RootActivityId: 4888c04d-2ff2-41c2-ab68-c03e7c9dd9a5
Date (UTC): 11/10/2026 4:19:33 PM

   at Microsoft.AnalysisServices.Core.AnalysisServicesClient.SendExecuteAndReadResponse(ImpactDetailCollection impacts, Boolean expectEmptyResults, Boolean throwIfError)
   at Microsoft.AnalysisServices.Core.AnalysisServicesClient.Create(IMajorObject parent, IMajorObject obj, ObjectExpansion expansion, ImpactDetailCollection impact, Boolean allowOverwrite, XmlaWarningCollection warnings, JaXmlSerializer serializer)
   at Microsoft.AnalysisServices.Core.Server.Update(IMajorObject obj, UpdateOptions options, UpdateMode mode, XmlaWarningCollection warnings, ImpactDetailCollection impactResult)
   at Microsoft.AnalysisServices.Core.Server.SendUpdate(IMajorObject obj, UpdateOptions options, UpdateMode mode, XmlaWarningCollection warnings, ImpactDetailCollection impactResult)
   at Microsoft.AnalysisServices.MajorObject.Update(UpdateOptions options, UpdateMode mode, XmlaWarningCollection warnings)
   at Microsoft.AnalysisServices.MajorObject.Update(UpdateOptions options, UpdateMode mode)
   at Microsoft.Fabric.SemanticLink.TraceCollector.Start(Int32 delayInSeconds)
   at System.RuntimeMethodHandle.InvokeMethod(Object target, Void** arguments, Signature sig, Boolean isConstructor)
   at System.Reflection.MethodBaseInvoker.InvokeDirectByRefWithFewArgs(Object obj, Span`1 copyOfArgs, BindingFlags invokeAttr)

```

## Log

```
2026-11-10T16:19:17Z run 20261110T161824Z-v99-6981: variant=v99-kitchen-sink data_tag=data-1m-v1 targets=['PPU'] expected_commit=eccd5b6aa5a7e6d1e9f310741db0fd25d01812a7
2026-11-10T16:19:20Z PPU: not connected to Git; the model there is the one published by hand
2026-11-10T16:19:21Z PPU: v99-kitchen-sink is c30a54fc-597b-4dda-b406-9efe7e320643, DataTag reads back data-1m-v1
2026-11-10T16:19:33Z PPU: trace event ProgressReportEnd: not listed
2026-11-10T16:19:33Z PPU: trace event CommandEnd: not listed
2026-11-10T16:19:33Z PPU: trace event Error: not listed
2026-11-10T16:19:33Z PPU: trace event ExecutionMetrics: not listed
2026-11-10T16:19:33Z STOPPED: OperationException: The event Id=136 does not contain the column Id=2. Please refer to product documentation for a list of available event columns.

Technical Details:
RootActivityId: 4888c04d-2ff2-41c2-ab68-c03e7c9dd9a5
Date (UTC): 11/10/2026 4:19:33 PM

   at Microsoft.AnalysisServices.Core.AnalysisServicesClient.SendExecuteAndReadResponse(ImpactDetailCollection impacts, Boolean expectEmptyResults, Boolean throwIfError)
   at Microsoft.AnalysisServices.Core.AnalysisServicesClient.Create(IMajorObject parent, IMajo
```
