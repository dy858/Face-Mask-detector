	w-!t+?@w-!t+?@!w-!t+?@	?_gA]?'@?_gA]?'@!?_gA]?'@"e
=type.googleapis.com/tensorflow.profiler.PerGenericStepDetails$w-!t+?@?<,Ԛ???A??\??@Y??<,??S@*	ffff?o?@2?
JIterator::Model::MaxIntraOpParallelism::Map::BatchV2::Shuffle::Zip[0]::Map??h o?Q@!??d??U@)??|г}Q@1?U?<?U@:Preprocessing2k
4Iterator::Model::MaxIntraOpParallelism::Map::BatchV2????x?R@!ڻ?E?W@)?7??dj@1??޷?'@:Preprocessing2b
+Iterator::Model::MaxIntraOpParallelism::MapQ?|a?S@!r?b|??X@)[Ӽ?@1si??H@:Preprocessing2y
BIterator::Model::MaxIntraOpParallelism::Map::BatchV2::Shuffle::ZipX?2ı?Q@!??晚V@)?&?W??1?'K?	??:Preprocessing2?
RIterator::Model::MaxIntraOpParallelism::Map::BatchV2::Shuffle::Zip[1]::TensorSlicevq?-??!%okR??)vq?-??1%okR??:Preprocessing2t
=Iterator::Model::MaxIntraOpParallelism::Map::BatchV2::Shuffle;pΈҖQ@!?Ѓ??V@)P??n???1?#tn???:Preprocessing2?
WIterator::Model::MaxIntraOpParallelism::Map::BatchV2::Shuffle::Zip[0]::Map::TensorSlice}??b٭?!?EH???)}??b٭?1?EH???:Preprocessing2]
&Iterator::Model::MaxIntraOpParallelism??"???S@!?LSߐ?X@)Έ?????1?F^???:Preprocessing2F
Iterator::Modele?`TR?S@!      Y@)??_vOv?1???,+?{?:Preprocessing:?
]Enqueuing data: you may want to combine small input data chunks into fewer but larger chunks.
?Data preprocessing: you may increase num_parallel_calls in <a href="https://www.tensorflow.org/api_docs/python/tf/data/Dataset#map" target="_blank">Dataset map()</a> or preprocess the data OFFLINE.
?Reading data from files in advance: you may tune parameters in the following tf.data API (<a href="https://www.tensorflow.org/api_docs/python/tf/data/Dataset#prefetch" target="_blank">prefetch size</a>, <a href="https://www.tensorflow.org/api_docs/python/tf/data/Dataset#interleave" target="_blank">interleave cycle_length</a>, <a href="https://www.tensorflow.org/api_docs/python/tf/data/TFRecordDataset#class_tfrecorddataset" target="_blank">reader buffer_size</a>)
?Reading data from files on demand: you should read data IN ADVANCE using the following tf.data API (<a href="https://www.tensorflow.org/api_docs/python/tf/data/Dataset#prefetch" target="_blank">prefetch</a>, <a href="https://www.tensorflow.org/api_docs/python/tf/data/Dataset#interleave" target="_blank">interleave</a>, <a href="https://www.tensorflow.org/api_docs/python/tf/data/TFRecordDataset#class_tfrecorddataset" target="_blank">reader buffer</a>)
?Other data reading or processing: you may consider using the <a href="https://www.tensorflow.org/programmers_guide/datasets" target="_blank">tf.data API</a> (if you are not using it now)?
:type.googleapis.com/tensorflow.profiler.BottleneckAnalysis?
both?Your program is MODERATELY input-bound because 11.8% of the total step time sampled is waiting for input. Therefore, you would need to reduce both the input time and other time.no*no9?_gA]?'@I?WTV@Zno>Look at Section 3 for the breakdown of input time on the host.B?
@type.googleapis.com/tensorflow.profiler.GenericStepTimeBreakdown?
	?<,Ԛ????<,Ԛ???!?<,Ԛ???      ??!       "      ??!       *      ??!       2	??\??@??\??@!??\??@:      ??!       B      ??!       J	??<,??S@??<,??S@!??<,??S@R      ??!       Z	??<,??S@??<,??S@!??<,??S@b      ??!       JCPU_ONLYY?_gA]?'@b q?WTV@