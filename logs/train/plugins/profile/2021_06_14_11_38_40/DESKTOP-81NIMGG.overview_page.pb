?	??j+???@??j+???@!??j+???@	??/??c0@??/??c0@!??/??c0@"e
=type.googleapis.com/tensorflow.profiler.PerGenericStepDetails$??j+???@?ǘ?????Ao???T?@Y^K?=?X@*	gfffN9?@2?
JIterator::Model::MaxIntraOpParallelism::Map::BatchV2::Shuffle::Zip[0]::Mapu??U@!?;?D0V@)??H.??U@1?ρV@:Preprocessing2k
4Iterator::Model::MaxIntraOpParallelism::Map::BatchV2L?
F%?W@!????X@)?Y??ڊ@1:???:?@:Preprocessing2b
+Iterator::Model::MaxIntraOpParallelism::Map??N@?X@!A?????X@)??H??@1뮚\<@:Preprocessing2y
BIterator::Model::MaxIntraOpParallelism::Map::BatchV2::Shuffle::Zip??H?V@!>|
2V@)*??D???1?L??5
??:Preprocessing2?
RIterator::Model::MaxIntraOpParallelism::Map::BatchV2::Shuffle::Zip[1]::TensorSlice ?~?:p??!?.??U???) ?~?:p??1?.??U???:Preprocessing2?
WIterator::Model::MaxIntraOpParallelism::Map::BatchV2::Shuffle::Zip[0]::Map::TensorSlice?3??7??!??6NX??)?3??7??1??6NX??:Preprocessing2t
=Iterator::Model::MaxIntraOpParallelism::Map::BatchV2::Shuffle?Pk?wV@!????8V@)?z?G???12_S"P??:Preprocessing2]
&Iterator::Model::MaxIntraOpParallelism?=yX??X@!?>?'??X@)?&S???1?O??{Ȃ?:Preprocessing2F
Iterator::Model???9#?X@!      Y@)???Q?~?19H_p?~?:Preprocessing:?
]Enqueuing data: you may want to combine small input data chunks into fewer but larger chunks.
?Data preprocessing: you may increase num_parallel_calls in <a href="https://www.tensorflow.org/api_docs/python/tf/data/Dataset#map" target="_blank">Dataset map()</a> or preprocess the data OFFLINE.
?Reading data from files in advance: you may tune parameters in the following tf.data API (<a href="https://www.tensorflow.org/api_docs/python/tf/data/Dataset#prefetch" target="_blank">prefetch size</a>, <a href="https://www.tensorflow.org/api_docs/python/tf/data/Dataset#interleave" target="_blank">interleave cycle_length</a>, <a href="https://www.tensorflow.org/api_docs/python/tf/data/TFRecordDataset#class_tfrecorddataset" target="_blank">reader buffer_size</a>)
?Reading data from files on demand: you should read data IN ADVANCE using the following tf.data API (<a href="https://www.tensorflow.org/api_docs/python/tf/data/Dataset#prefetch" target="_blank">prefetch</a>, <a href="https://www.tensorflow.org/api_docs/python/tf/data/Dataset#interleave" target="_blank">interleave</a>, <a href="https://www.tensorflow.org/api_docs/python/tf/data/TFRecordDataset#class_tfrecorddataset" target="_blank">reader buffer</a>)
?Other data reading or processing: you may consider using the <a href="https://www.tensorflow.org/programmers_guide/datasets" target="_blank">tf.data API</a> (if you are not using it now)?
:type.googleapis.com/tensorflow.profiler.BottleneckAnalysis?
both?Your program is MODERATELY input-bound because 16.4% of the total step time sampled is waiting for input. Therefore, you would need to reduce both the input time and other time.no*no9??/??c0@I??]?T@Zno>Look at Section 3 for the breakdown of input time on the host.B?
@type.googleapis.com/tensorflow.profiler.GenericStepTimeBreakdown?
	?ǘ??????ǘ?????!?ǘ?????      ??!       "      ??!       *      ??!       2	o???T?@o???T?@!o???T?@:      ??!       B      ??!       J	^K?=?X@^K?=?X@!^K?=?X@R      ??!       Z	^K?=?X@^K?=?X@!^K?=?X@b      ??!       JCPU_ONLYY??/??c0@b q??]?T@Y      Y@q?C o	??"?
both?Your program is MODERATELY input-bound because 16.4% of the total step time sampled is waiting for input. Therefore, you would need to reduce both the input time and other time.b
`input_pipeline_analyzer (especially Section 3 for the breakdown of input operations on the Host)Q
Otf_data_bottleneck_analysis (find the bottleneck in the tf.data input pipeline)m
ktrace_viewer (look at the activities on the timeline of each Host Thread near the bottom of the trace view)"T
Rtensorflow_stats (identify the time-consuming operations executed on the CPU_ONLY)"Z
Xtrace_viewer (look at the activities on the timeline of each CPU_ONLY in the trace view)*?
?<a href="https://www.tensorflow.org/guide/data_performance_analysis" target="_blank">Analyze tf.data performance with the TF Profiler</a>*y
w<a href="https://www.tensorflow.org/guide/data_performance" target="_blank">Better performance with the tf.data API</a>2M
=type.googleapis.com/tensorflow.profiler.GenericRecommendation
nono2no:
Refer to the TF2 Profiler FAQ2"CPU: B 